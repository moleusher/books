# IDAES Workflow Guide (parsed from readthedocs)

## General Workflow

The IDAES platform follows a modular workflow for constructing and solving process models.

### Standard Steps

1. **Import IDAES and Pyomo modules**
2. **Create a Pyomo ConcreteModel**
3. **Create a FlowsheetBlock** (steay-state or dynamic)
4. **Select and attach a Property Package** to the flowsheet
5. **Add Unit Models** to the flowsheet
6. **Connect Unit Models** with Arcs
7. **Fix degrees of freedom** (feed conditions, unit specs)
8. **Expand Arcs** to constraints
9. **Scale the model**
10. **Initialize** the model
11. **Solve**

### Key APIs in Workflow Order

```python
# 1-3: Model setup
from pyomo.environ import ConcreteModel
from idaes.core import FlowsheetBlock
m = ConcreteModel()
m.fs = FlowsheetBlock(dynamic=False)

# 4: Property package
from idaes.models.properties import YourPropertyPackage
m.fs.properties = YourPropertyPackage()

# 5: Unit models
from idaes.models.unit_models import Heater, Flash, Mixer
m.fs.heater = Heater(property_package=m.fs.properties)

# 6: Connections
from idaes.core import Arc
m.fs.arc1 = Arc(source=m.fs.unit1.outlet, destination=m.fs.unit2.inlet)

# 7: Fix DOF
m.fs.feed.flow_mol.fix(100)
m.fs.feed.temperature.fix(350)
m.fs.feed.pressure.fix(101325)
m.fs.feed.mole_frac_comp["benzene"].fix(0.5)
m.fs.feed.mole_frac_comp["toluene"].fix(0.5)

# 8: Expand arcs
from pyomo.network import Arc
TransformationFactory("network.expand_arcs").apply_to(m)

# 9: Scale
from idaes.core.util.scaling import calculate_scaling_factors
calculate_scaling_factors(m)

# 10: Initialize
m.fs.unit.initialize()

# 11: Solve
from idaes.core.solvers import get_solver
solver = get_solver()
results = solver.solve(m)
```

## Data Reconciliation & Parameter Estimation

Workflow for fitting models to data:

1. Define model with unknown parameters as Pyomo `Var` (not fixed)
2. Import measurement data
3. Set up objective function (weighted least squares)
4. Solve the parameter estimation problem
