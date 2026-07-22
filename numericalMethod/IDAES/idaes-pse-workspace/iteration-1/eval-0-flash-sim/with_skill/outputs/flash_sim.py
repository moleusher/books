"""
===============================================================================
 IDAES Flash Simulation
===============================================================================
 Benzene-Toluene (50/50 mol%) Adiabatic Isobaric Flash

 Feed:  1 mol/s, 350 K, 1 atm (101325 Pa), equimolar benzene / toluene
 Flash: adiabatic (heat_duty = 0), isobaric (deltaP = 0)
 Property package: BTX activity-coefficient VLE (ideal Raoult's law)

 Solves for the equilibrium flash temperature and the vapor / liquid
 phase compositions and flow rates.
===============================================================================

References
----------
- IDAES Flash unit model:
  /home/admin/books/numericalMethod/IDAES/repo/idaes/models/unit_models/flash.py
- BTX property package:
  /home/admin/books/numericalMethod/IDAES/repo/idaes/models/properties/
  activity_coeff_models/BTX_activity_coeff_VLE.py
- IDAES demo flowsheet (canonical pattern):
  /home/admin/books/numericalMethod/IDAES/repo/idaes/models/flowsheets/
  demo_flowsheet.py
- Test suite patterns (initialization / solving):
  /home/admin/books/numericalMethod/IDAES/repo/idaes/models/unit_models/
  tests/test_flash.py
"""

from pyomo.environ import ConcreteModel, TransformationFactory, value
from pyomo.network import Arc

from idaes.core import FlowsheetBlock
from idaes.core.solvers import get_solver
from idaes.core.util.initialization import propagate_state
from idaes.core.util.model_statistics import degrees_of_freedom

from idaes.models.unit_models import Feed, Flash, Product
from idaes.models.properties.activity_coeff_models.BTX_activity_coeff_VLE import (
    BTXParameterBlock,
)

import idaes.logger as idaeslog


# --------------------------------------------------------------------------- #
# 1.  Build the flowsheet
# --------------------------------------------------------------------------- #
def build_flowsheet():
    """Construct the flowsheet topology: Feed -> Flash -> Vap/liq Products."""
    m = ConcreteModel()
    m.fs = FlowsheetBlock(dynamic=False)

    # Property package  --  ideal Raoult's law for benzene / toluene
    m.fs.properties = BTXParameterBlock(
        valid_phase=("Liq", "Vap"),
        activity_coeff_model="Ideal",
    )

    # --- Unit models ------------------------------------------------------- #
    # Feed (source)
    m.fs.feed = Feed(property_package=m.fs.properties)

    # Flash drum (adiabatic, isobaric, ideal phase-based separation)
    m.fs.flash = Flash(
        property_package=m.fs.properties,
        has_heat_transfer=True,
        has_pressure_change=True,
        ideal_separation=True,
    )

    # Terminal product blocks
    m.fs.vap_product = Product(property_package=m.fs.properties)
    m.fs.liq_product = Product(property_package=m.fs.properties)

    # --- Stream connections via Pyomo Arcs --------------------------------- #
    m.fs.s01 = Arc(source=m.fs.feed.outlet, destination=m.fs.flash.inlet)
    m.fs.s02 = Arc(
        source=m.fs.flash.vap_outlet, destination=m.fs.vap_product.inlet
    )
    m.fs.s03 = Arc(
        source=m.fs.flash.liq_outlet, destination=m.fs.liq_product.inlet
    )

    # Convert arcs to equality constraints
    TransformationFactory("network.expand_arcs").apply_to(m.fs)

    return m


# --------------------------------------------------------------------------- #
# 2.  Fix specifications (set degrees of freedom to zero)
# --------------------------------------------------------------------------- #
def set_specifications(m):
    """Fix feed conditions and flash operating parameters."""

    # --- Feed specifications ----------------------------------------------- #
    # 1 mol/s of equimolar benzene / toluene at 350 K, 1 atm
    m.fs.feed.flow_mol.fix(1.0)                              # mol/s
    m.fs.feed.temperature.fix(350)                            # K
    m.fs.feed.pressure.fix(101325)                            # Pa  (1 atm)
    m.fs.feed.mole_frac_comp[0, "benzene"].fix(0.5)
    m.fs.feed.mole_frac_comp[0, "toluene"].fix(0.5)

    # --- Flash operating specs --------------------------------------------- #
    # Adiabatic  (no heat transferred)
    m.fs.flash.heat_duty.fix(0.0)                             # W
    # Isobaric   (no pressure drop)
    m.fs.flash.deltaP.fix(0.0)                                # Pa


# --------------------------------------------------------------------------- #
# 3.  Apply variable bounds (robustness for the legacy BTX property package)
# --------------------------------------------------------------------------- #
def set_variable_bounds(m):
    """
    The legacy BTX activity-coefficient property package does not natively
    bound intermediate variables used in the equilibrium calculation,
    which can trigger domain errors during initialization.
    """
    for prop in [
        m.fs.flash.control_volume.properties_in,
        m.fs.flash.control_volume.properties_out,
    ]:
        # Bubble / dew point temperatures  (these are the VLE candidate T)
        prop[0.0].temperature_bubble.setlb(300)
        prop[0.0].temperature_bubble.setub(550)
        prop[0.0].temperature_dew.setlb(300)
        prop[0.0].temperature_dew.setub(550)

        # Internal equilibrium-temperature variable
        prop[0.0]._temperature_equilibrium.setlb(300)
        prop[0.0]._temperature_equilibrium.setub(550)

        # Saturation pressures  (Antoine equation output)
        prop[0.0].pressure_sat_comp.setlb(1e4)
        prop[0.0].pressure_sat_comp.setub(5e6)


# --------------------------------------------------------------------------- #
# 4.  Initialize the flowsheet (sequential, upstream -> downstream)
# --------------------------------------------------------------------------- #
def initialize_flowsheet(m):
    """
    Sequential initialization:
      1. Feed (source)
      2. Propagate state across arc S01  ->  flash.inlet
      3. Flash drum
      4. Propagate state across arcs S02 / S03  ->  products
    """
    # Feed
    m.fs.feed.initialize(outlvl=idaeslog.INFO)

    # Feed outlet -> Flash inlet
    propagate_state(arc=m.fs.s01)

    # Flash (contains the VLE and energy balance)
    m.fs.flash.initialize(outlvl=idaeslog.INFO)

    # Flash outlets -> Products (provides initial guesses)
    propagate_state(arc=m.fs.s02)
    propagate_state(arc=m.fs.s03)


# --------------------------------------------------------------------------- #
# 5.  Solve
# --------------------------------------------------------------------------- #
def solve_flowsheet(m):
    """Solve the flowsheet with IPOPT."""
    solver = get_solver(
        "ipopt_v2",
        solver_options={
            "nlp_scaling_method": "gradient-based",
            "mu_strategy": "adaptive",
            "max_iter": 1000,
            "tol": 1e-8,
        },
    )
    results = solver.solve(m, tee=True)
    return results


# --------------------------------------------------------------------------- #
# 6.  Report
# --------------------------------------------------------------------------- #
def report_results(m):
    """Print key results to stdout."""
    print()
    print("=" * 62)
    print("  IDAES FLASH SIMULATION  --  RESULTS")
    print("=" * 62)

    # --- Feed -------------------------------------------------------------- #
    print("\n  FEED STREAM")
    print("  " + "-" * 58)
    print(f"       Flow rate : {value(m.fs.feed.flow_mol[0]):>10.4f}  mol/s")
    print(f"      Temperature : {value(m.fs.feed.temperature[0]):>10.2f}  K")
    print(f"         Pressure : {value(m.fs.feed.pressure[0]) / 101325:>10.4f}  atm")
    print(f"  Benzene (frac) : {value(m.fs.feed.mole_frac_comp[0, 'benzene']):>10.4f}")
    print(f"  Toluene  (frac) : {value(m.fs.feed.mole_frac_comp[0, 'toluene']):>10.4f}")

    # --- Flash ------------------------------------------------------------- #
    print("\n  FLASH DRUM")
    print("  " + "-" * 58)
    print(f"           Heat duty : {value(m.fs.flash.heat_duty[0]):>10.2f}  W")
    print(f"        Pressure drop : {value(m.fs.flash.deltaP[0]):>10.2f}  Pa")

    # Equilibrium temperature from the flash outlet property block
    T_flash = value(m.fs.flash.control_volume.properties_out[0].temperature)
    print(f"  Flash temperature   : {T_flash:>10.2f}  K")

    # --- Vapor product ---------------------------------------------------- #
    print("\n  VAPOR OUTLET")
    print("  " + "-" * 58)
    print(f"       Flow rate : {value(m.fs.flash.vap_outlet.flow_mol[0]):>10.4f}  mol/s")
    print(f"      Temperature : {value(m.fs.flash.vap_outlet.temperature[0]):>10.2f}  K")
    print(f"  Benzene (y)    : {value(m.fs.flash.vap_outlet.mole_frac_comp[0, 'benzene']):>10.4f}")
    print(f"  Toluene  (y)   : {value(m.fs.flash.vap_outlet.mole_frac_comp[0, 'toluene']):>10.4f}")

    # --- Liquid product --------------------------------------------------- #
    print("\n  LIQUID OUTLET")
    print("  " + "-" * 58)
    print(f"       Flow rate : {value(m.fs.flash.liq_outlet.flow_mol[0]):>10.4f}  mol/s")
    print(f"      Temperature : {value(m.fs.flash.liq_outlet.temperature[0]):>10.2f}  K")
    print(f"  Benzene (x)    : {value(m.fs.flash.liq_outlet.mole_frac_comp[0, 'benzene']):>10.4f}")
    print(f"  Toluene  (x)   : {value(m.fs.flash.liq_outlet.mole_frac_comp[0, 'toluene']):>10.4f}")

    # --- Overall molar balance -------------------------------------------- #
    total_in = value(m.fs.feed.flow_mol[0])
    total_out = value(
        m.fs.flash.vap_outlet.flow_mol[0] + m.fs.flash.liq_outlet.flow_mol[0]
    )
    print("\n  OVERALL MOLAR BALANCE")
    print("  " + "-" * 58)
    print(f"          Total in : {total_in:>10.4f}  mol/s")
    print(f"         Total out : {total_out:>10.4f}  mol/s")
    print(f"           Balance : {total_in - total_out:>+10.2e}  mol/s")
    print("=" * 62)
    print()


# --------------------------------------------------------------------------- #
# 7.  Main
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    # Build
    model = build_flowsheet()

    # Specify
    set_specifications(model)

    # Verify DOF
    dof = degrees_of_freedom(model)
    print(f"\nDegrees of freedom (should be 0): {dof}")
    if dof != 0:
        raise RuntimeError(
            f"Model has {dof} DOF -- expected 0.  Cannot solve."
        )

    # Set robust variable bounds for the legacy BTX package
    set_variable_bounds(model)

    # Initialize
    initialize_flowsheet(model)

    # Solve
    solve_flowsheet(model)

    # Report
    report_results(model)

    # Also use the built-in IDAES flash report method
    print("IDAES built-in flash report:")
    model.fs.flash.report()
