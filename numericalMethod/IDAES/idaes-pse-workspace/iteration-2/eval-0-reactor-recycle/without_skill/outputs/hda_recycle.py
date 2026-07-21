"""
HDA (Hydrodealkylation) Flowsheet with Recycle
================================================
C6H5CH3 + H2  ->  C6H6 + CH4
 (toluene) (hydrogen) (benzene) (methane)

Flowsheet topology:
  I101 (toluene: 0.3 mol/s, 350 K, 5 atm)  --\
                                                M101 --+--> R101 --> F101 --+-- vap --> S101 --+-- recycle --> C101 --+
  I102 (hydrogen: 0.3 mol/s, 350 K, 5 atm) -/                                                        .             |
                                                                   (benzene product)                  .             |
                                                                                                       +-- purge --> P102
                                                                                                       +--> back to M101

Known good values (after convergence, for verification):
    Reactor outlet T:   ~941 K
    Flash heat duty:    ~-0.059 MW  (condenser)
    Benzene product:    ~0.20 mol/s (Liq phase)
    Purge H2:           ~0.06 mol/s
"""

# -----------------------------------------------------------------------------
# 1. Imports
# -----------------------------------------------------------------------------
from pyomo.environ import (
    ConcreteModel,
    Var,
    Constraint,
    Expression,
    value,
    units as pyunits,
    TransformationFactory,
    TerminationCondition,
)
from pyomo.network import Arc

from idaes.core import FlowsheetBlock
from idaes.models.unit_models import (
    Feed,
    Product,
    Mixer,
    StoichiometricReactor,
    Flash,
    Separator as Splitter,
    PressureChanger,
)
from idaes.models.unit_models.pressure_changer import ThermodynamicAssumption
from idaes.core.util.model_statistics import degrees_of_freedom
from idaes.core.util.exceptions import InitializationError
from idaes.core.solvers import get_solver
from idaes.core.util.initialization import propagate_state
from idaes.models.properties.modular_properties.base.generic_property import (
    GenericParameterBlock,
)
from idaes.models.properties.modular_properties.base.generic_reaction import (
    GenericReactionParameterBlock,
)
import idaes.logger as idaeslog

from idaes_examples.mod.hda.hda_ideal_VLE_modular import thermo_config
from idaes_examples.mod.hda.hda_reaction_modular import reaction_config


# -----------------------------------------------------------------------------
# 2. Initialization helper
# -----------------------------------------------------------------------------
def _init_unit(unit):
    """Initialize a single unit model using its default initializer, with a
    direct-solve fallback if the initializer raises InitializationError."""
    optarg = {
        "nlp_scaling_method": "user-scaling",
        "OF_ma57_automatic_scaling": "yes",
        "max_iter": 1000,
        "tol": 1e-8,
    }
    try:
        initializer = unit.default_initializer(solver_options=optarg)
        initializer.initialize(unit, output_level=idaeslog.INFO_LOW)
    except InitializationError:
        solver = get_solver(solver_options=optarg)
        solver.solve(unit, tee=False)


# -----------------------------------------------------------------------------
# 3. Main simulation
# -----------------------------------------------------------------------------
def main():
    # =========================================================================
    # 3a.  Flowsheet model & property packages
    # =========================================================================
    m = ConcreteModel()
    m.fs = FlowsheetBlock(dynamic=False)

    m.fs.thermo_params = GenericParameterBlock(**thermo_config)
    m.fs.reaction_params = GenericReactionParameterBlock(
        property_package=m.fs.thermo_params, **reaction_config
    )

    # =========================================================================
    # 3b.  Unit models
    # =========================================================================
    # -- Feeds --
    m.fs.I101 = Feed(property_package=m.fs.thermo_params)  # toluene
    m.fs.I102 = Feed(property_package=m.fs.thermo_params)  # hydrogen

    # -- Mixer (3 inlets: toluene, hydrogen, recycle) --
    m.fs.M101 = Mixer(
        property_package=m.fs.thermo_params,
        num_inlets=3,
    )

    # -- Stoichiometric reactor (adiabatic, 75 % conversion) --
    m.fs.R101 = StoichiometricReactor(
        property_package=m.fs.thermo_params,
        reaction_package=m.fs.reaction_params,
        has_heat_of_reaction=True,
        has_heat_transfer=True,
        has_pressure_change=False,
    )

    # -- Flash tank (325 K, deltaP = 0) --
    m.fs.F101 = Flash(
        property_package=m.fs.thermo_params,
        has_heat_transfer=True,
        has_pressure_change=True,
    )

    # -- Splitter (20 % purge / 80 % recycle) --
    m.fs.S101 = Splitter(
        property_package=m.fs.thermo_params,
        ideal_separation=False,
        outlet_list=["purge", "recycle"],
    )

    # -- Compressor on recycle (isothermal, outlet = 5 atm) --
    m.fs.C101 = PressureChanger(
        property_package=m.fs.thermo_params,
        compressor=True,
        thermodynamic_assumption=ThermodynamicAssumption.isothermal,
    )

    # -- Products --
    m.fs.P101 = Product(property_package=m.fs.thermo_params)  # benzene (liq)
    m.fs.P102 = Product(property_package=m.fs.thermo_params)  # purge (vap)

    # =========================================================================
    # 3c.  Connections (Arcs)
    # =========================================================================
    m.fs.s01 = Arc(source=m.fs.I101.outlet, destination=m.fs.M101.inlet_1)
    m.fs.s02 = Arc(source=m.fs.I102.outlet, destination=m.fs.M101.inlet_2)
    # Tear: recycle loop ends at mixer; s03 is the tear stream
    m.fs.s03 = Arc(source=m.fs.M101.outlet, destination=m.fs.R101.inlet)
    m.fs.s04 = Arc(source=m.fs.R101.outlet, destination=m.fs.F101.inlet)
    m.fs.s05 = Arc(source=m.fs.F101.vap_outlet, destination=m.fs.S101.inlet)
    m.fs.s06 = Arc(source=m.fs.S101.recycle, destination=m.fs.C101.inlet)
    m.fs.s07 = Arc(source=m.fs.C101.outlet, destination=m.fs.M101.inlet_3)
    m.fs.s08 = Arc(source=m.fs.F101.liq_outlet, destination=m.fs.P101.inlet)
    m.fs.s09 = Arc(source=m.fs.S101.purge, destination=m.fs.P102.inlet)

    TransformationFactory("network.expand_arcs").apply_to(m)

    # =========================================================================
    # 3d.  Feed specifications
    # =========================================================================
    #
    # The state definition (FpTPxpc) uses flow_mol_phase_comp[t, p, c] as the
    # core state variable.  Components valid only in Vap (hydrogen, methane)
    # have no Liq index; the reverse is true by default for benzene / toluene
    # which appear in both phases.
    #
    # Small non-zero values (1e-8) are used for absent components to help the
    # solver avoid singular Jacobians.

    # -- I101 : toluene feed  (0.3 mol/s, 350 K, 5 atm) --
    m.fs.I101.outlet.flow_mol_phase_comp[0, "Liq", "toluene"].fix(0.3)
    m.fs.I101.outlet.flow_mol_phase_comp[0, "Liq", "benzene"].fix(1e-8)
    m.fs.I101.outlet.flow_mol_phase_comp[0, "Vap", "toluene"].fix(1e-8)
    m.fs.I101.outlet.flow_mol_phase_comp[0, "Vap", "benzene"].fix(1e-8)
    m.fs.I101.outlet.flow_mol_phase_comp[0, "Vap", "hydrogen"].fix(1e-8)
    m.fs.I101.outlet.flow_mol_phase_comp[0, "Vap", "methane"].fix(1e-8)
    m.fs.I101.outlet.temperature.fix(350)
    m.fs.I101.outlet.pressure.fix(506625)

    # -- I102 : hydrogen feed  (0.3 mol/s, 350 K, 5 atm) --
    #     Hydrogen and methane are vapour-only; (Liq, H2) / (Liq, CH4) do not
    #     exist.  We still fix the Liq entries for benzene/toluene to small
    #     non-zero values.
    m.fs.I102.outlet.flow_mol_phase_comp[0, "Vap", "hydrogen"].fix(0.3)
    m.fs.I102.outlet.flow_mol_phase_comp[0, "Vap", "benzene"].fix(1e-8)
    m.fs.I102.outlet.flow_mol_phase_comp[0, "Vap", "toluene"].fix(1e-8)
    m.fs.I102.outlet.flow_mol_phase_comp[0, "Vap", "methane"].fix(1e-8)
    m.fs.I102.outlet.flow_mol_phase_comp[0, "Liq", "benzene"].fix(1e-8)
    m.fs.I102.outlet.flow_mol_phase_comp[0, "Liq", "toluene"].fix(1e-8)
    m.fs.I102.outlet.temperature.fix(350)
    m.fs.I102.outlet.pressure.fix(506625)

    # =========================================================================
    # 3e.  Unit model specifications
    # =========================================================================

    # -- Stoichiometric reactor: 75 % conversion of toluene, adiabatic --
    m.fs.R101.conversion = Var(initialize=0.75, bounds=(0, 1))
    m.fs.R101.conv_constraint = Constraint(
        expr=m.fs.R101.conversion
        * m.fs.R101.control_volume.properties_in[0].flow_mol_phase_comp[
            "Vap", "toluene"
        ]
        == (
            m.fs.R101.control_volume.properties_in[0].flow_mol_phase_comp[
                "Vap", "toluene"
            ]
            - m.fs.R101.control_volume.properties_out[0].flow_mol_phase_comp[
                "Vap", "toluene"
            ]
        )
    )
    m.fs.R101.conversion.fix(0.75)
    m.fs.R101.heat_duty.fix(0)  # adiabatic

    # -- Flash: isothermal at 325 K, no pressure drop --
    m.fs.F101.vap_outlet.temperature.fix(325.0)
    m.fs.F101.deltaP.fix(0)

    # -- Splitter: 20 % purge, 80 % recycle (by default) --
    m.fs.S101.split_fraction[0, "purge"].fix(0.2)

    # -- Compressor: outlet pressure = 5 atm = 506625 Pa --
    m.fs.C101.outlet.pressure.fix(506625)

    # =========================================================================
    # 3f.  Degrees-of-freedom check
    # =========================================================================
    print(f"Initial DOF (should be 0): {degrees_of_freedom(m)}")
    assert degrees_of_freedom(m) == 0, (
        f"Expected 0 DOF, got {degrees_of_freedom(m)}"
    )

    # =========================================================================
    # 4.  Initialization  —  manual tear-stream propagation
    # =========================================================================
    #
    # The recycle loop is broken at s03 (mixer outlet → reactor inlet).  We:
    #   1. Deactivate the equality constraint for the tear arc
    #   2. Fix the reactor inlet (tear destination) to initial guesses
    #   3. Initialise all units in process-flow order, propagating state
    #      forward after each initialisation
    #   4. Solve the acyclic system with the tear still fixed
    #   5. Unfix the tear variables and re-activate the arc
    #
    # Tear guesses — the recycle stream is initially unknown, so we start with
    # fresh-feed values.  The sequential propagate-fix loop will converge.

    TEAR_ARC = m.fs.s03
    TEAR_CONSTRAINT = TEAR_ARC.name + "_expanded"

    tear_guesses = {
        "flow_mol_phase_comp": {
            (0, "Liq", "toluene"): 0.3,
            (0, "Liq", "benzene"): 1e-8,
            (0, "Vap", "toluene"): 1e-8,
            (0, "Vap", "benzene"): 1e-8,
            (0, "Vap", "hydrogen"): 0.3,
            (0, "Vap", "methane"): 1e-8,
        },
        "temperature": {0: 350.0},
        "pressure": {0: 506625.0},
    }

    print("\n--- Manual tear-stream initialisation ---")

    # Step 1: deactivate the tear constraint
    getattr(m.fs, TEAR_CONSTRAINT).deactivate()
    print(f"  DOF after tear deactivated: {degrees_of_freedom(m)}")

    # Step 2: fix tear destination to guesses
    for varname, idx_val in tear_guesses.items():
        for idx, val in idx_val.items():
            getattr(TEAR_ARC.destination, varname)[idx].fix(val)
    print(f"  DOF after tear fixed:        {degrees_of_freedom(m)}")

    # Step 3: sequential initialisation around the loop
    #
    # Order: reactor → flash → splitter → compressor → feeds → mixer
    # After each initialise, propagate state across the connecting arc so the
    # next unit has a feasible inlet.

    _init_unit(m.fs.R101)               # inlet fixed to tear guesses
    propagate_state(arc=m.fs.s04)       # R101.outlet → F101.inlet

    _init_unit(m.fs.F101)
    propagate_state(arc=m.fs.s05)       # F101.vap_outlet → S101.inlet
    propagate_state(arc=m.fs.s08)       # F101.liq_outlet → P101.inlet

    _init_unit(m.fs.S101)
    propagate_state(arc=m.fs.s06)       # S101.recycle → C101.inlet
    propagate_state(arc=m.fs.s09)       # S101.purge → P102.inlet

    _init_unit(m.fs.C101)
    propagate_state(arc=m.fs.s07)       # C101.outlet → M101.inlet_3

    _init_unit(m.fs.I101)
    propagate_state(arc=m.fs.s01)       # I101.outlet → M101.inlet_1
    _init_unit(m.fs.I102)
    propagate_state(arc=m.fs.s02)       # I102.outlet → M101.inlet_2

    _init_unit(m.fs.M101)
    propagate_state(arc=m.fs.s03)       # M101.outlet → R101.inlet
                                        #   (overwrites the fixed guesses)

    _init_unit(m.fs.P101)
    _init_unit(m.fs.P102)

    # Step 4: solve the acyclic system (tear still fixed)
    optarg_init = {
        "nlp_scaling_method": "user-scaling",
        "OF_ma57_automatic_scaling": "yes",
        "max_iter": 300,
        "tol": 1e-8,
    }
    solver = get_solver(solver_options=optarg_init)
    solver.solve(m, tee=False)
    print("  Initial (tear-fixed) solve completed.")

    # Step 5: unfix tear variables and re-activate
    for varname, idx_val in tear_guesses.items():
        for idx in idx_val:
            getattr(TEAR_ARC.destination, varname)[idx].unfix()
    getattr(m.fs, TEAR_CONSTRAINT).activate()
    print(f"  DOF after tear restored:     {degrees_of_freedom(m)}")

    # =========================================================================
    # 5.  Solve the full flowsheet
    # =========================================================================
    print("\n--- Solving full flowsheet ---")
    optarg_full = {
        "nlp_scaling_method": "user-scaling",
        "OF_ma57_automatic_scaling": "yes",
        "max_iter": 1000,
        "tol": 1e-8,
    }
    solver = get_solver("ipopt_v2", options=optarg_full)
    results = solver.solve(m, tee=True)

    if results.solver.termination_condition == TerminationCondition.optimal:
        print("\n=== HDA Flowsheet solved successfully ===\n")
    else:
        print(
            f"\nSolver termination: {results.solver.termination_condition}\n"
        )
        return  # skip reporting if solve failed

    # =========================================================================
    # 6.  Results
    # =========================================================================
    m.fs.report()

    # -- Benzene product stream (F101 liquid outlet) --
    ben_liq = value(
        m.fs.F101.control_volume.properties_out[0].flow_mol_phase_comp[
            "Liq", "benzene"
        ]
    )
    tol_liq = value(
        m.fs.F101.control_volume.properties_out[0].flow_mol_phase_comp[
            "Liq", "toluene"
        ]
    )
    ben_liq_mol_frac = ben_liq / (ben_liq + tol_liq + 1e-12)

    print("\n========== Key Results ==========")
    print(f"Reactor outlet temperature:  "
          f"{value(m.fs.R101.control_volume.properties_out[0].temperature):.1f} K")
    print(f"Flash heat duty:             "
          f"{value(m.fs.F101.heat_duty[0]):.2f} W")
    print(f"Benzene product (liq flow):  {ben_liq:.5f} mol/s")
    print(f"Benzene purity in liq prod:  {ben_liq_mol_frac:.4f}")
    purge_h2 = value(
        m.fs.S101.control_volume.properties_out[0].flow_mol_phase_comp[
            "Vap", "hydrogen"
        ]
    )
    print(f"Purge H2 flow:               {purge_h2:.5f} mol/s")
    print("================================")


if __name__ == "__main__":
    main()
