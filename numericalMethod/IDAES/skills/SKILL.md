# IDAES Process Modeling Skill

Route to the right sub-skill based on the task.

## Router

| Trigger | Sub-Skill |
|---------|-----------|
| "build/create flowsheet", "set up IDAES model", "process simulation", "connect unit models" | → `idaes-flowsheet-builder.md` |
| "property package", "thermodynamic method", "NRTL", "Peng-Robinson", "EoS", "state definition", "configuration dict" | → `idaes-property-selector.md` |
| "add/configure [unit]", "reactor", "heat exchanger", "flash", "custom unit model", "CSTR", "PFR" | → `idaes-unit-configurator.md` |
| "not converging", "solver failed", "initialization error", "debug", "scaling", "infeasible", "degrees of freedom" | → `idaes-model-debugger.md` |
| "initialize flowsheet", "tear stream", "recycle loop", "SequentialDecomposition", "propagate_state", "Wegstein" | → `idaes-initialization-guide.md` |

## Decision Tree

```
User task →
├── Building a NEW flowsheet from scratch?
│   ├── Step 1: idaes-flowsheet-builder    (structure, units, arcs, solve)
│   ├── Step 2: idaes-property-selector    (thermo config dict)
│   ├── Step 3: idaes-unit-configurator    (per-unit specs, DOF)
│   └── Step 4: idaes-initialization-guide (tear streams if recycle)
│
├── Choosing/changing property methods?
│   └── idaes-property-selector + docs/component-parameter-database.md
│
├── Adding a specific unit model?
│   └── idaes-unit-configurator
│
├── Solver won't converge / model broken?
│   └── idaes-model-debugger
│
└── Initializing a flowsheet with recycle?
    └── idaes-initialization-guide
```

## Knowledge Base Root

All sub-skills reference paths relative to: `numericalMethod/IDAES/`

Key entry points:
- KB index: `README.md`
- Component parameters: `docs/component-parameter-database.md`
- Repo (source + RST docs): `repo/`
- Examples (239 notebooks): `examples/idaes_examples/notebooks/docs/`

## Common Imports (used across all sub-skills)

```python
from pyomo.environ import (ConcreteModel, Constraint, Var, Expression,
                            Objective, TransformationFactory, value, units as pyunits)
from pyomo.network import Arc
from idaes.core import FlowsheetBlock
from idaes.core.solvers import get_solver
from idaes.core.util.model_statistics import degrees_of_freedom
from idaes.core.util.initialization import propagate_state
import idaes.logger as idaeslog
```
