"""
===============================================================================
 IDAES Flash Simulation  --  Benzene-Toluene (50/50 mol%) Adiabatic Isobaric
===============================================================================

 Feed:  1 mol/s, 350 K, 1 atm (101325 Pa), equimolar benzene / toluene
 Flash: adiabatic (heat_duty = 0), isobaric (deltaP = 0)

 This version builds the thermodynamic property package from scratch using
 IDAES's GenericParameterBlock with the modular property framework, rather
 than relying on a pre-built property package (BTXParameterBlock).

 Property package: Ideal Raoult's law VLE for benzene-toluene
   - Vapor phase:  Ideal gas  (EoS = Ideal)
   - Liquid phase: Ideal liquid (EoS = Ideal)
   - Vapor pressure: RPP4 (4-parameter corresponding-states correlation)
   - Heat capacity:  RPP4 (ideal gas), Perrys (liquid)
   - Phase equilibrium: SmoothVLE with fugacity form

 Solves for the equilibrium flash temperature and the vapor/liquid
 phase compositions and flow rates.

 Sources for thermodynamic data:
   [1] The Properties of Gases and Liquids (1987), 4th ed., Reid
   [2] Perry's Chemical Engineers' Handbook, 7th ed.
   [3] Engineering Toolbox, https://www.engineeringtoolbox.com (Dec 2019)

===============================================================================
"""

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #
from pyomo.environ import (
    ConcreteModel,
    TransformationFactory,
    value,
    units as pyunits,
)
from pyomo.network import Arc

from idaes.core import FlowsheetBlock, LiquidPhase, VaporPhase, Component
from idaes.core.solvers import get_solver
from idaes.core.util.initialization import propagate_state
from idaes.core.util.model_statistics import degrees_of_freedom

from idaes.models.unit_models import Feed, Flash, Product

from idaes.models.properties.modular_properties import GenericParameterBlock
from idaes.models.properties.modular_properties.state_definitions import FTPx
from idaes.models.properties.modular_properties.eos.ideal import Ideal
from idaes.models.properties.modular_properties.phase_equil import SmoothVLE
from idaes.models.properties.modular_properties.phase_equil.bubble_dew import (
    IdealBubbleDew,
)
from idaes.models.properties.modular_properties.phase_equil.forms import fugacity
from idaes.models.properties.modular_properties.pure import Perrys, RPP4

import idaes.logger as idaeslog


# --------------------------------------------------------------------------- #
# Property package configuration
# --------------------------------------------------------------------------- #
# This dictionary is passed to GenericParameterBlock to build the complete
# set of thermodynamic property correlations from scratch.
# Every method (Perrys, RPP4, fugacity, SmoothVLE, etc.) is a pre-built IDAES
# library component — no custom coding required, but the user must assemble
# the configuration manually.

THERMO_CONFIG = {
    # =========================================================================
    # Component definitions
    # =========================================================================
    "components": {
        "benzene": {
            "type": Component,
            "elemental_composition": {"C": 6, "H": 6},
            # Property methods (each is a class from modular_properties.pure)
            "dens_mol_liq_comp": Perrys,
            "enth_mol_liq_comp": Perrys,
            "enth_mol_ig_comp": RPP4,
            "pressure_sat_comp": RPP4,
            # Phase equilibrium uses the fugacity form (Raoult's law for ideal)
            "phase_equilibrium_form": {("Vap", "Liq"): fugacity},
            # Numerical parameter values
            "parameter_data": {
                "mw": (78.1136e-3, pyunits.kg / pyunits.mol),          # [1]
                "pressure_crit": (48.9e5, pyunits.Pa),                 # [1]
                "temperature_crit": (562.2, pyunits.K),                 # [1]
                # Liquid molar density  (Perrys method coefficients)
                "dens_mol_liq_comp_coeff": {
                    "eqn_type": 1,
                    "1": (1.0162, pyunits.kmol * pyunits.m**-3),       # [2] pg 2-98
                    "2": (0.2655, None),
                    "3": (562.16, pyunits.K),
                    "4": (0.28212, None),
                },
                # Ideal gas heat capacity coefficients  (RPP4 — 4th order poly)
                "cp_mol_ig_comp_coeff": {
                    "A": (-3.392e1, pyunits.J / pyunits.mol / pyunits.K),      # [1]
                    "B": (4.739e-1, pyunits.J / pyunits.mol / pyunits.K**2),
                    "C": (-3.017e-4, pyunits.J / pyunits.mol / pyunits.K**3),
                    "D": (7.130e-8, pyunits.J / pyunits.mol / pyunits.K**4),
                },
                # Liquid heat capacity coefficients  (Perrys — 5th order poly)
                "cp_mol_liq_comp_coeff": {
                    "1": (1.29e2, pyunits.J / pyunits.kmol / pyunits.K),       # [2]
                    "2": (-1.7e-1, pyunits.J / pyunits.kmol / pyunits.K**2),
                    "3": (6.48e-4, pyunits.J / pyunits.kmol / pyunits.K**3),
                    "4": (0, pyunits.J / pyunits.kmol / pyunits.K**4),
                    "5": (0, pyunits.J / pyunits.kmol / pyunits.K**5),
                },
                # Standard enthalpies of formation  [3]
                "enth_mol_form_liq_comp_ref": (49.0e3, pyunits.J / pyunits.mol),
                "enth_mol_form_vap_comp_ref": (82.9e3, pyunits.J / pyunits.mol),
                # Vapor pressure correlation coefficients (RPP4)
                "pressure_sat_comp_coeff": {
                    "A": (-6.98273, None),  # [1]
                    "B": (1.33213, None),
                    "C": (-2.62863, None),
                    "D": (-3.33399, None),
                },
            },
        },
        "toluene": {
            "type": Component,
            "elemental_composition": {"C": 7, "H": 8},
            "dens_mol_liq_comp": Perrys,
            "enth_mol_liq_comp": Perrys,
            "enth_mol_ig_comp": RPP4,
            "pressure_sat_comp": RPP4,
            "phase_equilibrium_form": {("Vap", "Liq"): fugacity},
            "parameter_data": {
                "mw": (92.1405e-3, pyunits.kg / pyunits.mol),          # [1]
                "pressure_crit": (41e5, pyunits.Pa),                   # [1]
                "temperature_crit": (591.8, pyunits.K),                 # [1]
                "dens_mol_liq_comp_coeff": {
                    "eqn_type": 1,
                    "1": (0.8488, pyunits.kmol * pyunits.m**-3),       # [2] pg 2-98
                    "2": (0.26655, None),
                    "3": (591.8, pyunits.K),
                    "4": (0.2878, None),
                },
                "cp_mol_ig_comp_coeff": {
                    "A": (-2.435e1, pyunits.J / pyunits.mol / pyunits.K),      # [1]
                    "B": (5.125e-1, pyunits.J / pyunits.mol / pyunits.K**2),
                    "C": (-2.765e-4, pyunits.J / pyunits.mol / pyunits.K**3),
                    "D": (4.911e-8, pyunits.J / pyunits.mol / pyunits.K**4),
                },
                "cp_mol_liq_comp_coeff": {
                    "1": (1.40e2, pyunits.J / pyunits.kmol / pyunits.K),       # [2]
                    "2": (-1.52e-1, pyunits.J / pyunits.kmol / pyunits.K**2),
                    "3": (6.95e-4, pyunits.J / pyunits.kmol / pyunits.K**3),
                    "4": (0, pyunits.J / pyunits.kmol / pyunits.K**4),
                    "5": (0, pyunits.J / pyunits.kmol / pyunits.K**5),
                },
                "enth_mol_form_liq_comp_ref": (12.0e3, pyunits.J / pyunits.mol),  # [3]
                "enth_mol_form_vap_comp_ref": (50.1e3, pyunits.J / pyunits.mol),  # [3]
                "pressure_sat_comp_coeff": {
                    "A": (-7.28607, None),  # [1]
                    "B": (1.38091, None),
                    "C": (-2.83433, None),
                    "D": (-2.79168, None),
                },
            },
        },
    },
    # =========================================================================
    # Phase definitions
    # =========================================================================
    "phases": {
        "Liq": {"type": LiquidPhase, "equation_of_state": Ideal},
        "Vap": {"type": VaporPhase, "equation_of_state": Ideal},
    },
    # =========================================================================
    # Base units of measurement
    # =========================================================================
    "base_units": {
        "time": pyunits.s,
        "length": pyunits.m,
        "mass": pyunits.kg,
        "amount": pyunits.mol,
        "temperature": pyunits.K,
    },
    # =========================================================================
    # State definition
    # =========================================================================
    "state_definition": FTPx,
    "state_bounds": {
        "flow_mol": (0, 100, 1000, pyunits.mol / pyunits.s),
        "temperature": (273.15, 300, 450, pyunits.K),
        "pressure": (5e4, 1e5, 1e6, pyunits.Pa),
    },
    "pressure_ref": (1e5, pyunits.Pa),
    "temperature_ref": (300, pyunits.K),
    # =========================================================================
    # Phase equilibrium
    # =========================================================================
    "phases_in_equilibrium": [("Vap", "Liq")],
    "phase_equilibrium_state": {("Vap", "Liq"): SmoothVLE},
    "bubble_dew_method": IdealBubbleDew,
}


# --------------------------------------------------------------------------- #
# 1.  Build the flowsheet
# --------------------------------------------------------------------------- #
def build_flowsheet():
    """Construct the flowsheet topology: Feed -> Flash -> Vap/liq Products."""
    m = ConcreteModel()
    m.fs = FlowsheetBlock(dynamic=False)

    # Property package  --  built from the configuration dictionary above
    m.fs.properties = GenericParameterBlock(**THERMO_CONFIG)

    # --- Unit models ------------------------------------------------------- #
    # Feed (source)
    m.fs.feed = Feed(property_package=m.fs.properties)

    # Flash drum (adiabatic, isobaric)
    m.fs.flash = Flash(
        property_package=m.fs.properties,
        has_heat_transfer=True,
        has_pressure_change=True,
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
    # 1 mol/s of equimolar benzene/toluene at 350 K, 1 atm
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
# 3.  Initialize the flowsheet (sequential, upstream -> downstream)
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
# 4.  Solve
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
# 5.  Report
# --------------------------------------------------------------------------- #
def report_results(m):
    """Print key results to stdout."""
    print()
    print("=" * 70)
    print("  IDAES FLASH SIMULATION  --  RESULTS")
    print("  (GenericParameterBlock — manual property configuration)")
    print("=" * 70)

    # --- Feed -------------------------------------------------------------- #
    print("\n  FEED STREAM")
    print("  " + "-" * 66)
    print(f"       Flow rate : {value(m.fs.feed.flow_mol[0]):>10.4f}  mol/s")
    print(f"      Temperature : {value(m.fs.feed.temperature[0]):>10.2f}  K"
          f"  ({value(m.fs.feed.temperature[0]) - 273.15:.2f} degC)")
    print(f"         Pressure : {value(m.fs.feed.pressure[0]) / 101325:>10.4f}  atm")
    print(f"  Benzene (frac) : {value(m.fs.feed.mole_frac_comp[0, 'benzene']):>10.4f}")
    print(f"  Toluene  (frac) : {value(m.fs.feed.mole_frac_comp[0, 'toluene']):>10.4f}")

    # --- Flash ------------------------------------------------------------- #
    print("\n  FLASH DRUM")
    print("  " + "-" * 66)
    print(f"           Heat duty : {value(m.fs.flash.heat_duty[0]):>10.2f}  W")
    print(f"        Pressure drop : {value(m.fs.flash.deltaP[0]):>10.2f}  Pa")

    # Equilibrium temperature from the flash outlet property block
    props_out = m.fs.flash.control_volume.properties_out[0]
    T_flash = value(props_out.temperature)
    print(f"  Flash temperature   : {T_flash:>10.2f}  K"
          f"  ({T_flash - 273.15:.2f} degC)")

    # --- Vapor product ---------------------------------------------------- #
    print("\n  VAPOR OUTLET")
    print("  " + "-" * 66)
    v_flow = value(m.fs.flash.vap_outlet.flow_mol[0])
    v_yb = value(m.fs.flash.vap_outlet.mole_frac_comp[0, "benzene"])
    v_yt = value(m.fs.flash.vap_outlet.mole_frac_comp[0, "toluene"])
    print(f"       Flow rate : {v_flow:>10.4f}  mol/s  ({v_flow*100:.2f}% of feed)")
    print(f"      Temperature : {value(m.fs.flash.vap_outlet.temperature[0]):>10.2f}  K")
    print(f"  Benzene (y)    : {v_yb:>10.4f}")
    print(f"  Toluene  (y)   : {v_yt:>10.4f}")

    # --- Liquid product --------------------------------------------------- #
    print("\n  LIQUID OUTLET")
    print("  " + "-" * 66)
    l_flow = value(m.fs.flash.liq_outlet.flow_mol[0])
    l_xb = value(m.fs.flash.liq_outlet.mole_frac_comp[0, "benzene"])
    l_xt = value(m.fs.flash.liq_outlet.mole_frac_comp[0, "toluene"])
    print(f"       Flow rate : {l_flow:>10.4f}  mol/s  ({l_flow*100:.2f}% of feed)")
    print(f"      Temperature : {value(m.fs.flash.liq_outlet.temperature[0]):>10.2f}  K")
    print(f"  Benzene (x)    : {l_xb:>10.4f}")
    print(f"  Toluene  (x)   : {l_xt:>10.4f}")

    # --- Phase fraction and equilibrium data ------------------------------ #
    total_in = value(m.fs.feed.flow_mol[0])
    vf = v_flow / total_in if total_in > 0 else 0
    print(f"\n  PHASE FRACTION")
    print(f"    Vapor fraction (V/F) : {vf:>10.4f}  ({vf*100:.2f}%)")
    print(f"    Liquid fraction (L/F): {l_flow/total_in:>10.4f}"
          f"  ({l_flow/total_in*100:.2f}%)")

    if v_flow > 1e-8 and l_flow > 1e-8:
        K_b = v_yb / l_xb if l_xb > 0 else float("inf")
        K_t = v_yt / l_xt if l_xt > 0 else float("inf")
        alpha = K_b / K_t if K_t > 0 else float("inf")
        print(f"\n  EQUILIBRIUM (K-values)")
        print(f"    K_benzene (y/x)  : {K_b:>10.4f}")
        print(f"    K_toluene  (y/x) : {K_t:>10.4f}")
        print(f"    Rel. volatility  : {alpha:>10.4f}")

    # --- Overall molar balance -------------------------------------------- #
    total_out = v_flow + l_flow
    print("\n  OVERALL MOLAR BALANCE")
    print("  " + "-" * 66)
    print(f"          Total in : {total_in:>10.4f}  mol/s")
    print(f"         Total out : {total_out:>10.4f}  mol/s")
    print(f"           Balance : {total_in - total_out:>+10.2e}  mol/s")

    # Component balances
    z_b = value(m.fs.feed.mole_frac_comp[0, "benzene"])
    bal_b = v_flow * v_yb + l_flow * l_xb - total_in * z_b
    z_t = value(m.fs.feed.mole_frac_comp[0, "toluene"])
    bal_t = v_flow * v_yt + l_flow * l_xt - total_in * z_t
    print(f"     Benzene balance : {bal_b:>+10.2e}  mol/s")
    print(f"     Toluene balance : {bal_t:>+10.2e}  mol/s")

    # --- Context ----------------------------------------------------------- #
    print("\n  NOTE")
    print("  At 350 K and 1 atm, the mixture is a subcooled liquid (below the")
    print("  bubble point of ~365 K). With adiabatic operation (Q=0), no heat")
    print("  is available to drive vaporization, so the outlet remains entirely")
    print("  liquid at 350 K with the same composition as the feed.")
    print("  To observe partial vaporization, increase the feed temperature")
    print("  above the bubble point or reduce the flash pressure.")

    print("\n" + "=" * 70)
    print("  Simulation completed successfully.")
    print("=" * 70)
    print()


# --------------------------------------------------------------------------- #
# 6.  Main
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

    # Initialize
    initialize_flowsheet(model)

    # Solve
    solve_flowsheet(model)

    # Report
    report_results(model)

    # Also use the built-in IDAES flash report method
    print("IDAES built-in flash report:")
    model.fs.flash.report()
