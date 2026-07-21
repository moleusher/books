# IDAES Flowsheet Builder

Build complete IDAES process flowsheets — select property packages, configure unit models,
connect streams, solve, and analyze results.

## Knowledge Base Paths
- **KB root**: `numericalMethod/IDAES/`
- **Workflow guide**: `repo/docs/how_to_guides/workflow/index.rst`
- **Property framework**: `repo/docs/explanations/components/property_package/general/index.rst`
- **Unit model refs**: `repo/docs/reference_guides/model_libraries/generic/unit_models/index.rst`
- **Example flowsheets**: `examples/idaes_examples/notebooks/docs/flowsheets/`
- **Tutorial (HDA)**: `examples/idaes_examples/notebooks/docs/tut/core/hda_flowsheet.ipynb`
- **Property config examples**: `examples/idaes_examples/mod/hda/hda_ideal_VLE_modular.py`

## Standard Workflow (Real API)

### Step 1: Imports
```python
# Pyomo
from pyomo.environ import (ConcreteModel, Constraint, Var, Expression,
                            Objective, TransformationFactory, value, units as pyunits)
from pyomo.network import Arc

# IDAES core
from idaes.core import FlowsheetBlock
from idaes.core.solvers import get_solver
from idaes.core.util.model_statistics import degrees_of_freedom
import idaes.logger as idaeslog

# Unit models
from idaes.models.unit_models import (Flash, Heater, Mixer, Pump, Valve,
                                       PressureChanger, Feed, Product,
                                       StoichiometricReactor, Separator)
```

### Step 2: Property Package (Modular Framework — most common)

```python
from idaes.models.properties.modular_properties import GenericParameterBlock
from idaes.models.properties.modular_properties.state_definitions import FTPx
from idaes.models.properties.modular_properties.eos.ideal import Ideal
from idaes.models.properties.modular_properties.phase_equil import SmoothVLE
from idaes.models.properties.modular_properties.pure import Perrys, RPP4
from idaes.core import LiquidPhase, VaporPhase, Component

configuration = {
    "components": {
        "benzene": {
            "type": Component,
            "parameter_data": {
                "mw": (78.11e-3, pyunits.kg / pyunits.mol),
                "pressure_crit": (48.9e5, pyunits.Pa),
                "temperature_crit": (562.2, pyunits.K),
                # ... see full example for all parameters
            },
            # Property method assignments per component
            "dens_mol_liq_comp": Perrys,
            "enth_mol_liq_comp": Perrys,
            "enth_mol_ig_comp": RPP4,
            "pressure_sat_comp": RPP4,
            "phase_equilibrium_form": {("Vap", "Liq"): fugacity},
        },
        # ... add all components
    },
    "phases": {
        "Liq": {"type": LiquidPhase, "equation_of_state": Ideal},
        "Vap": {"type": VaporPhase, "equation_of_state": Ideal},
    },
    "state_definition": FTPx,
    "base_units": {"time": pyunits.s, "length": pyunits.m,
                    "mass": pyunits.kg, "amount": pyunits.mol,
                    "temperature": pyunits.K},
    "phases_in_equilibrium": [("Vap", "Liq")],
    "phase_equilibrium_state": {("Vap", "Liq"): SmoothVLE},
    "pressure_ref": (1e5, pyunits.Pa),
    "temperature_ref": (298.15, pyunits.K),
}
```

**Alternative: Pre-built Property Package** (simpler when available):
```python
from idaes.models.properties.activity_coeff_models import BTXParameterBlock
m.fs.properties = BTXParameterBlock(valid_phase=('Liq', 'Vap'))
```

### Step 3: Create Flowsheet & Attach Properties
```python
m = ConcreteModel()
m.fs = FlowsheetBlock(dynamic=False)
m.fs.thermo_params = GenericParameterBlock(**configuration)

# If reactive system, also add reaction package:
from idaes.models.properties.modular_properties.base.generic_reaction import (
    GenericReactionParameterBlock)
m.fs.reaction_params = GenericReactionParameterBlock(
    property_package=m.fs.thermo_params, **reaction_config)
```

### Step 4: Add Unit Models
```python
m.fs.feed = Feed(property_package=m.fs.thermo_params)
m.fs.heater = Heater(property_package=m.fs.thermo_params,
                     has_pressure_change=True,
                     has_phase_equilibrium=True)
m.fs.flash = Flash(property_package=m.fs.thermo_params)
m.fs.mixer = Mixer(property_package=m.fs.thermo_params,
                   num_inlets=2)
m.fs.product = Product(property_package=m.fs.thermo_params)
```

### Step 5: Connect Streams
```python
m.fs.s01 = Arc(source=m.fs.feed.outlet, destination=m.fs.heater.inlet)
m.fs.s02 = Arc(source=m.fs.heater.outlet, destination=m.fs.flash.inlet)
m.fs.s03 = Arc(source=m.fs.flash.vap_outlet, destination=m.fs.product.inlet)

# Expand arcs to constraints:
TransformationFactory("network.expand_arcs").apply_to(m)
```

### Step 6: Fix Degrees of Freedom
```python
# Feed conditions
m.fs.feed.flow_mol.fix(100)           # mol/s
m.fs.feed.temperature.fix(350)         # K
m.fs.feed.pressure.fix(101325)         # Pa
m.fs.feed.mole_frac_comp["benzene"].fix(0.5)
m.fs.feed.mole_frac_comp["toluene"].fix(0.5)

# Unit specs
m.fs.flash.heat_duty.fix(0)           # adiabatic
m.fs.flash.deltaP.fix(0)              # isobaric
```

### Step 7: Initialize (Sequential, Unit-by-Unit)
```python
optarg = {
    "nlp_scaling_method": "user-scaling",
    "OF_ma57_automatic_scaling": "yes",
    "max_iter": 1000,
    "tol": 1e-8,
}

# Pattern 1: use default_initializer
initializer = m.fs.feed.default_initializer(solver_options=optarg)
initializer.initialize(m.fs.feed, output_level=idaeslog.INFO_LOW)

# Pattern 2: with error fallback
from idaes.core.util.exceptions import InitializationError
try:
    initializer = unit.default_initializer(solver_options=optarg)
    initializer.initialize(unit, output_level=idaeslog.INFO_LOW)
except InitializationError:
    solver = get_solver(solver_options=optarg)
    solver.solve(unit)
```

### Step 8: Solve
```python
solver = get_solver(solver_options=optarg)
results = solver.solve(m, tee=True)
print(results.solver.termination_condition)  # Should be 'optimal'
```

## Common Patterns

### Recycle Loops (Tear Streams)
```python
from pyomo.network import SequentialDecomposition
seq = SequentialDecomposition()
seq.options.select_tear_method = "heuristic"
seq.options.tear_method = "Wegstein"
seq.options.iterLim = 5
seq.run(m, tear_guesses)
```

### Dynamic Simulation
Set `dynamic=True`, configure `time_set` and `ContinuousSet` on the flowsheet.

### Solving with IPOPT Directly
```python
from pyomo.environ import SolverFactory
solver = SolverFactory("ipopt")
results = solver.solve(m, tee=True)
```

## Anti-Patterns
- Don't fix both inlet AND outlet flows (causes over-specification)
- Don't forget `TransformationFactory("network.expand_arcs")` before solving
- Don't mix modular and pre-built property packages on connected units
- Don't fix temperature on an outlet port directly — use `control_volume.properties_out[t].temperature` for Flash units
- Don't skip initialization — IDAES models almost always need sequential initialization before full solve

## Debugging Checklist
1. `degrees_of_freedom(m)` must be 0
2. Check scaling: `idaes.core.util.scaling.badly_scaled_var_generator(m)`
3. Check initialization worked: no exceptions, reasonable values
4. Solver status: `results.solver.termination_condition`
5. See `idaes-model-debugger` skill for detailed diagnostics

## Related Skills
- `idaes-property-selector` — choose thermodynamic methods and build configuration dict
- `idaes-model-debugger` — diagnose initialization/convergence issues
- `idaes-unit-configurator` — configure individual unit models
