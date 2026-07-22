"""
HDA (Hydrodealkylation) Reactor + Recycle Flowsheet

Reaction: C6H5CH3 + H2 -> C6H6 + CH4

Flowsheet topology:
  I101 (toluene feed)  \
                         -> M101 (Mixer) -> R101 (Reactor) -> F101 (Flash) -> S101 (Splitter)
  I102 (H2 feed)       /                    |                                            |
                                            |                                            -> P102 (purge, 20%)
                                            -> C101 (Compressor) <-- recycle (80%) ----+
                                            |
                                            -> P101 (benzene product from flash liq)

Tear stream: s03 (M101.outlet -> R101.inlet)
Initialization: manual tear-stream propagation with sequential unit initialization.

References:
  - Thermo: idaes_examples/mod/hda/hda_ideal_VLE_modular.py  (FpTPxpc state def)
  - Reaction: idaes_examples/mod/hda/hda_reaction_modular.py
  - Init pattern: idaes_examples/mod/hda/hda_flowsheet_extras.py
"""

from pyomo.environ import (
    ConcreteModel,
    Var,
    Constraint,
    TransformationFactory,
    value,
    TerminationCondition,
)
from pyomo.network import Arc

from idaes.core import FlowsheetBlock
from idaes.core.solvers import get_solver
from idaes.core.util.model_statistics import degrees_of_freedom
from idaes.core.util.initialization import propagate_state
import idaes.logger as idaeslog

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

from idaes.models.properties.modular_properties.base.generic_property import (
    GenericParameterBlock,
)
from idaes.models.properties.modular_properties.base.generic_reaction import (
    GenericReactionParameterBlock,
)

# HDA-specific thermo and reaction configurations
from idaes_examples.mod.hda.hda_ideal_VLE_modular import thermo_config
from idaes_examples.mod.hda.hda_reaction_modular import reaction_config


# =============================================================================
# 1. Build the Model and Attach Property Packages
# =============================================================================
m = ConcreteModel()
m.fs = FlowsheetBlock(dynamic=False)

m.fs.thermo_params = GenericParameterBlock(**thermo_config)
m.fs.reaction_params = GenericReactionParameterBlock(
    property_package=m.fs.thermo_params, **reaction_config
)

print("=" * 72)
print("HDA FLOWSHEET: TOLUENE + H2 -> BENZENE + CH4")
print("=" * 72)

# =============================================================================
# 2. Add Unit Models
# =============================================================================
# Feeds
m.fs.I101 = Feed(property_package=m.fs.thermo_params)  # Toluene feed
m.fs.I102 = Feed(property_package=m.fs.thermo_params)  # Hydrogen feed

# Mixer (3 inlets: toluene feed, H2 feed, recycle stream)
m.fs.M101 = Mixer(
    property_package=m.fs.thermo_params,
    num_inlets=3,
)

# Stoichiometric reactor (yield-based, not kinetic)
m.fs.R101 = StoichiometricReactor(
    property_package=m.fs.thermo_params,
    reaction_package=m.fs.reaction_params,
    has_heat_of_reaction=True,
    has_heat_transfer=True,
    has_pressure_change=False,
)

# Flash for vapor-liquid separation
m.fs.F101 = Flash(
    property_package=m.fs.thermo_params,
    has_heat_transfer=True,
    has_pressure_change=True,
)

# Splitter: purge / recycle
m.fs.S101 = Splitter(
    property_package=m.fs.thermo_params,
    ideal_separation=False,
    outlet_list=["purge", "recycle"],
)

# Compressor for recycle stream
m.fs.C101 = PressureChanger(
    property_package=m.fs.thermo_params,
    compressor=True,
    thermodynamic_assumption=ThermodynamicAssumption.isothermal,
)

# Products
m.fs.P101 = Product(property_package=m.fs.thermo_params)  # Benzene product (liquid)
m.fs.P102 = Product(property_package=m.fs.thermo_params)  # Purge (vapor)

print("Unit models created.")

# =============================================================================
# 3. Connect Unit Models with Arcs
# =============================================================================
m.fs.s01 = Arc(source=m.fs.I101.outlet, destination=m.fs.M101.inlet_1)
m.fs.s02 = Arc(source=m.fs.I102.outlet, destination=m.fs.M101.inlet_2)
m.fs.s03 = Arc(
    source=m.fs.M101.outlet, destination=m.fs.R101.inlet
)  # <-- TEAR STREAM
m.fs.s04 = Arc(source=m.fs.R101.outlet, destination=m.fs.F101.inlet)
m.fs.s05 = Arc(source=m.fs.F101.vap_outlet, destination=m.fs.S101.inlet)
m.fs.s06 = Arc(
    source=m.fs.F101.liq_outlet, destination=m.fs.P101.inlet
)  # Benzene product
m.fs.s07 = Arc(source=m.fs.S101.purge, destination=m.fs.P102.inlet)  # Purge
m.fs.s08 = Arc(source=m.fs.S101.recycle, destination=m.fs.C101.inlet)
m.fs.s09 = Arc(source=m.fs.C101.outlet, destination=m.fs.M101.inlet_3)

# Convert arcs to equality constraints
TransformationFactory("network.expand_arcs").apply_to(m)

initial_dof = degrees_of_freedom(m)
print(f"Arcs expanded. Initial DOF: {initial_dof}")

# =============================================================================
# 4. Fix Feed Conditions
# =============================================================================
# Small epsilon to keep mole fractions away from singularities
eps = 1e-5

# --- Feed I101: Toluene at 0.3 mol/s, 350 K, 5 atm (506625 Pa) ---
# Toluene is liquid-dominant at these conditions.
m.fs.I101.flow_mol_phase[0, "Liq"].fix(0.3 - 2 * eps)
m.fs.I101.flow_mol_phase[0, "Vap"].fix(2 * eps)

# Liquid phase: benzene and toluene only (H2 and CH4 are vapor-only)
m.fs.I101.mole_frac_phase_comp[0, "Liq", "benzene"].fix(eps)
m.fs.I101.mole_frac_phase_comp[0, "Liq", "toluene"].fix(1.0 - eps)

# Vapor phase: all four components (trace amounts)
m.fs.I101.mole_frac_phase_comp[0, "Vap", "benzene"].fix(0.25)
m.fs.I101.mole_frac_phase_comp[0, "Vap", "toluene"].fix(0.25)
m.fs.I101.mole_frac_phase_comp[0, "Vap", "hydrogen"].fix(0.25)
m.fs.I101.mole_frac_phase_comp[0, "Vap", "methane"].fix(0.25)

m.fs.I101.temperature.fix(350)
m.fs.I101.pressure.fix(506625)

# --- Feed I102: Hydrogen at 0.3 mol/s, 350 K, 5 atm (506625 Pa) ---
# Hydrogen is vapor-only.
m.fs.I102.flow_mol_phase[0, "Liq"].fix(eps)
m.fs.I102.flow_mol_phase[0, "Vap"].fix(0.3 - eps)

# Liquid phase: only benzene and toluene (tiny amounts for stability)
m.fs.I102.mole_frac_phase_comp[0, "Liq", "benzene"].fix(0.5)
m.fs.I102.mole_frac_phase_comp[0, "Liq", "toluene"].fix(0.5)

# Vapor phase: mostly hydrogen
m.fs.I102.mole_frac_phase_comp[0, "Vap", "benzene"].fix(eps)
m.fs.I102.mole_frac_phase_comp[0, "Vap", "toluene"].fix(eps)
m.fs.I102.mole_frac_phase_comp[0, "Vap", "hydrogen"].fix(1.0 - 3 * eps)
m.fs.I102.mole_frac_phase_comp[0, "Vap", "methane"].fix(eps)

m.fs.I102.temperature.fix(350)
m.fs.I102.pressure.fix(506625)

print(f"Feed conditions fixed. DOF: {degrees_of_freedom(m)}")

# =============================================================================
# 5. Fix Unit Model Specifications
# =============================================================================

# --- Stoichiometric Reactor ---
# Conversion variable: fraction of toluene converted
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
m.fs.R101.heat_duty.fix(0)  # Adiabatic operation

# --- Flash F101 ---
m.fs.F101.vap_outlet.temperature.fix(325)  # K
m.fs.F101.deltaP.fix(0)  # No pressure drop

# --- Splitter S101 ---
m.fs.S101.split_fraction[0, "purge"].fix(0.2)  # 20% purge, 80% recycle

# --- Compressor C101 ---
m.fs.C101.outlet.pressure.fix(506625)  # 5 atm

print(f"Unit specifications fixed. DOF: {degrees_of_freedom(m)}")

# Verify square system
dof = degrees_of_freedom(m)
if dof != 0:
    raise RuntimeError(
        f"Expected DOF = 0 before initialization, got {dof}. "
        "Check that all feed conditions and unit specs are fixed."
    )
print("DOF = 0 -- Square system ready for initialization.")

# =============================================================================
# 6. Initialize -- Manual Tear Stream Method
# =============================================================================

def initialize_unit(unit, optarg=None):
    """
    Initialize a unit model using its default initializer.
    Falls back to direct solve if the initializer fails.
    """
    from idaes.core.util.exceptions import InitializationError

    if optarg is None:
        optarg = {
            "nlp_scaling_method": "user-scaling",
            "OF_ma57_automatic_scaling": "yes",
            "max_iter": 1000,
            "tol": 1e-8,
        }
    try:
        init = unit.default_initializer(solver_options=optarg)
        init.initialize(unit, output_level=idaeslog.INFO_LOW)
    except InitializationError:
        solver = get_solver(solver_options=optarg)
        solver.solve(unit)


print("\n" + "-" * 72)
print("INITIALIZATION -- Manual Tear Stream Propagation")
print("-" * 72)

# Tear stream: s03 = M101.outlet -> R101.inlet
# Provide reasonable guesses for the mixer outlet (combined feeds + recycle)
tear_guesses = {
    "flow_mol_phase": {
        (0, "Liq"): 0.3,
        (0, "Vap"): 0.6,
    },
    "mole_frac_phase_comp": {
        (0, "Liq", "benzene"): 0.01,
        (0, "Liq", "toluene"): 0.99,
        (0, "Vap", "benzene"): 0.02,
        (0, "Vap", "toluene"): 0.02,
        (0, "Vap", "hydrogen"): 0.60,
        (0, "Vap", "methane"): 0.36,
    },
    "temperature": {0: 350},
    "pressure": {0: 506625},
}

# Step 1: Deactivate the tear stream equality constraint
m.fs.s03_expanded.deactivate()
print(f"DOF after tear deactivation: {degrees_of_freedom(m)}")

# Step 2: Fix the tear guesses on the destination of the torn stream
# (R101.inlet is the destination of s03)
for var_name, idx_val_map in tear_guesses.items():
    for idx, val in idx_val_map.items():
        getattr(m.fs.s03.destination, var_name)[idx].fix(val)

print(f"DOF after fixing tear guesses: {degrees_of_freedom(m)}")

# Solver options for initialization
optarg_init = {
    "nlp_scaling_method": "user-scaling",
    "OF_ma57_automatic_scaling": "yes",
    "max_iter": 300,
}
init_solver = get_solver(solver_options=optarg_init)

# Step 3: Sequential initialization in flow order
# Start from the unit AFTER the tear (R101) and go around the loop.
print("Sequential initialization started...")

initialize_unit(m.fs.R101)  # Reactor (inlet fixed by tear guesses)
print("  R101 initialized.")

propagate_state(m.fs.s04)  # R101.outlet -> F101.inlet
initialize_unit(m.fs.F101)  # Flash
print("  F101 initialized.")

propagate_state(m.fs.s05)  # F101.vap_outlet -> S101.inlet
initialize_unit(m.fs.S101)  # Splitter
print("  S101 initialized.")

propagate_state(m.fs.s08)  # S101.recycle -> C101.inlet
initialize_unit(m.fs.C101)  # Compressor
print("  C101 initialized.")

propagate_state(m.fs.s09)  # C101.outlet -> M101.inlet_3

# Now initialize the upstream side (feeds and mixer)
initialize_unit(m.fs.I101)  # Toluene feed
print("  I101 initialized.")
propagate_state(m.fs.s01)  # I101.outlet -> M101.inlet_1

initialize_unit(m.fs.I102)  # Hydrogen feed
print("  I102 initialized.")
propagate_state(m.fs.s02)  # I102.outlet -> M101.inlet_2

initialize_unit(m.fs.M101)  # Mixer
print("  M101 initialized.")

# Propagate through the tear to close the loop
propagate_state(m.fs.s03)  # M101.outlet -> R101.inlet (overwrites tear guesses)

# Solve the partially-torn flowsheet
init_solver.solve(m, tee=False)
print("  Tear-fixed flowsheet solved.")

# Step 4: Unfix tear variables and reactivate the constraint
for var_name, idx_val_map in tear_guesses.items():
    for idx in idx_val_map:
        getattr(m.fs.s03.destination, var_name)[idx].unfix()

m.fs.s03_expanded.activate()

dof = degrees_of_freedom(m)
print(f"DOF after restoring tear stream: {dof}")
if dof != 0:
    raise RuntimeError(f"DOF should be 0 after restoring tear, got {dof}")

print("Initialization complete.")

# =============================================================================
# 7. Solve the Full Flowsheet
# =============================================================================
print("\n" + "-" * 72)
print("FULL FLOWSHEET SOLVE")
print("-" * 72)

optarg_full = {
    "nlp_scaling_method": "user-scaling",
    "OF_ma57_automatic_scaling": "yes",
    "max_iter": 1000,
    "tol": 1e-8,
}
solver = get_solver(solver_options=optarg_full)
results = solver.solve(m, tee=True)

print()
if results.solver.termination_condition == TerminationCondition.optimal:
    print("*** Solver terminated: OPTIMAL ***")
else:
    print(f"*** Solver terminated: {results.solver.termination_condition} ***")

# =============================================================================
# 8. Report Results
# =============================================================================
print("\n" + "=" * 72)
print("FLOWSHEET RESULTS")
print("=" * 72)

m.fs.report()

print("\n" + "=" * 72)
print("KEY STREAM AND UNIT SUMMARIES")
print("=" * 72)

# --- Fresh Feeds ---
print("\n--- Fresh Feeds ---")
for feed_name, feed_block in [("I101 (Toluene)", m.fs.I101), ("I102 (H2)", m.fs.I102)]:
    t = value(feed_block.outlet.temperature[0])
    p = value(feed_block.outlet.pressure[0])
    f_vap = value(feed_block.outlet.flow_mol_phase[0, "Vap"])
    f_liq = value(feed_block.outlet.flow_mol_phase[0, "Liq"])
    print(f"  {feed_name:20s}  T={t:.1f} K  P={p:.0f} Pa  "
          f"Vap={f_vap:.4f} mol/s  Liq={f_liq:.4f} mol/s")

# --- Reactor ---
print("\n--- Stoichiometric Reactor R101 ---")
t_in = value(m.fs.R101.inlet.temperature[0])
t_out = value(m.fs.R101.outlet.temperature[0])
p_out = value(m.fs.R101.outlet.pressure[0])
conv = value(m.fs.R101.conversion)
q_rx = value(m.fs.R101.heat_duty[0])
print(f"  Inlet temperature:          {t_in:.1f} K")
print(f"  Outlet temperature:         {t_out:.1f} K")
print(f"  Outlet pressure:            {p_out:.0f} Pa")
print(f"  Toluene conversion:         {conv:.1%}")
print(f"  Heat duty:                  {q_rx:.1f} W (0 = adiabatic)")

# --- Flash ---
print("\n--- Flash F101 ---")
t_flash = value(m.fs.F101.vap_outlet.temperature[0])
p_flash = value(m.fs.F101.vap_outlet.pressure[0])
q_flash = value(m.fs.F101.heat_duty[0])
f_vap = value(m.fs.F101.vap_outlet.flow_mol_phase[0, "Vap"])
f_liq = value(m.fs.F101.liq_outlet.flow_mol_phase[0, "Liq"])

benzene_vap = value(
    m.fs.F101.control_volume.properties_out[0].flow_mol_phase_comp["Vap", "benzene"]
)
toluene_vap = value(
    m.fs.F101.control_volume.properties_out[0].flow_mol_phase_comp["Vap", "toluene"]
)
h2_vap = value(
    m.fs.F101.control_volume.properties_out[0].flow_mol_phase_comp["Vap", "hydrogen"]
)
ch4_vap = value(
    m.fs.F101.control_volume.properties_out[0].flow_mol_phase_comp["Vap", "methane"]
)

print(f"  Temperature:                {t_flash:.1f} K")
print(f"  Pressure:                   {p_flash:.0f} Pa")
print(f"  Heat duty:                  {q_flash:.1f} W")
print(f"  Vapor outlet flow:          {f_vap:.4f} mol/s")
print(f"    - benzene:                {benzene_vap:.6f} mol/s")
print(f"    - toluene:                {toluene_vap:.6f} mol/s")
print(f"    - hydrogen:               {h2_vap:.6f} mol/s")
print(f"    - methane:                {ch4_vap:.6f} mol/s")
print(f"  Liquid outlet flow:         {f_liq:.4f} mol/s")

# --- Benzene Product (Flash Liquid) ---
liq_benzene_mf = value(
    m.fs.F101.liq_outlet.mole_frac_phase_comp[0, "Liq", "benzene"]
)
liq_toluene_mf = value(
    m.fs.F101.liq_outlet.mole_frac_phase_comp[0, "Liq", "toluene"]
)
benzene_prod_rate = f_liq * liq_benzene_mf
toluene_prod_rate = f_liq * liq_toluene_mf

print("\n--- Benzene Product (F101 Liquid Outlet -> P101) ---")
print(f"  Total liquid flow:          {f_liq:.4f} mol/s")
print(f"  Benzene mole fraction:      {liq_benzene_mf:.4f}  "
      f"({liq_benzene_mf:.1%})")
print(f"  Toluene mole fraction:      {liq_toluene_mf:.4f}")
print(f"  Benzene production rate:    {benzene_prod_rate:.6f} mol/s")
print(f"  Toluene in product:         {toluene_prod_rate:.6f} mol/s")

# --- Splitter ---
print("\n--- Splitter S101 ---")
recycle_flow = value(m.fs.S101.recycle.flow_mol_phase[0, "Vap"])
purge_flow = value(m.fs.S101.purge.flow_mol_phase[0, "Vap"])
print(f"  Purge split fraction:       0.20")
print(f"  Vapor to recycle (80%):     {recycle_flow:.4f} mol/s")
print(f"  Vapor to purge (20%):       {purge_flow:.4f} mol/s")

# --- Compressor ---
print("\n--- Compressor C101 ---")
c_in_t = value(m.fs.C101.inlet.temperature[0])
c_out_t = value(m.fs.C101.outlet.temperature[0])
c_out_p = value(m.fs.C101.outlet.pressure[0])
print(f"  Inlet temperature:           {c_in_t:.1f} K")
print(f"  Outlet temperature:          {c_out_t:.1f} K  (isothermal)")
print(f"  Outlet pressure:             {c_out_p:.0f} Pa")

# --- Overall Conversion and Yield ---
print("\n--- Overall Performance ---")
total_benzene_produced = benzene_prod_rate  # mol/s
toluene_fresh = value(m.fs.I101.outlet.flow_mol_phase[0, "Liq"])
h2_fresh = value(m.fs.I102.outlet.flow_mol_phase[0, "Vap"]) * value(
    m.fs.I102.outlet.mole_frac_phase_comp[0, "Vap", "hydrogen"]
)
print(f"  Fresh toluene fed:           {toluene_fresh:.4f} mol/s")
print(f"  Fresh hydrogen fed:          {h2_fresh:.4f} mol/s")
print(f"  Benzene produced:            {total_benzene_produced:.6f} mol/s")
print(f"  Benzene yield (vs. toluene): "
      f"{total_benzene_produced / toluene_fresh:.2%}")

print("\n" + "=" * 72)
print("SIMULATION COMPLETE")
print("=" * 72)
