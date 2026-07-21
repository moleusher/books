---
name: idaes-pse
description: >
  IDAES process systems engineering — build flowsheets, configure property packages,
  add unit models, initialize and solve process simulations. Use this skill whenever
  the user mentions IDAES, process simulation, flowsheet, chemical process modeling,
  Pyomo-based optimization, reactor design, distillation, flash calculation, heat
  exchanger modeling, property packages (NRTL, Peng-Robinson, cubic EoS),
  thermodynamic configuration, or any kind of chemical engineering simulation task.
  Even if the user doesn't say "IDAES" explicitly, if they ask about building a
  process model with unit operations, this is the skill to use.
---

# IDAES Process Modeling

Route to the right reference based on task. KB root: `numericalMethod/IDAES/`

## Router

| User says | Read this reference |
|-----------|-------------------|
| "build/create flowsheet", "set up model", "process simulation", "connect unit models" | `references/flowsheet-builder.md` |
| "property package", "thermo", "NRTL", "Peng-Robinson", "EoS", "state definition", "config dict" | `references/property-selector.md` |
| "add/configure [unit]", "reactor", "heat exchanger", "flash", "CSTR", "PFR", "custom unit" | `references/unit-configurator.md` |
| "not converging", "solver failed", "debug", "scaling", "infeasible", "DOF" | `references/model-debugger.md` |
| "initialize", "tear stream", "recycle", "SequentialDecomposition", "propagate" | `references/initialization-guide.md` |

## Decision Tree

```
User wants to →
├── Build a NEW flowsheet?
│   Read in order: flowsheet-builder → property-selector → unit-configurator → initialization-guide
│
├── Pick thermodynamic methods?
│   Read: property-selector + docs/component-parameter-database.md
│
├── Add/configure a specific unit?
│   Read: unit-configurator
│
├── Debug a failing model?
│   Read: model-debugger
│
└── Initialize a recycle flowsheet?
    Read: initialization-guide
```

## Quick Start — Flash Simulation

Minimal flash unit with benzene-toluene using pre-built BTX package:

```python
from pyomo.environ import ConcreteModel, TransformationFactory, value
from pyomo.network import Arc
from idaes.core import FlowsheetBlock
from idaes.models.unit_models import Flash, Feed, Product
from idaes.models.properties.activity_coeff_models import BTXParameterBlock
from idaes.core.solvers import get_solver
from idaes.core.util.initialization import propagate_state
import idaes.logger as idaeslog

# 1. Model + flowsheet
m = ConcreteModel()
m.fs = FlowsheetBlock(dynamic=False)

# 2. Property package (pre-built BTX: benzene + toluene, ideal VLE)
m.fs.properties = BTXParameterBlock(valid_phase=('Liq', 'Vap'))

# 3. Unit models
m.fs.feed = Feed(property_package=m.fs.properties)
m.fs.flash = Flash(property_package=m.fs.properties,
                   has_heat_transfer=True, has_pressure_change=True)
m.fs.vap = Product(property_package=m.fs.properties)
m.fs.liq = Product(property_package=m.fs.properties)

# 4. Connect
m.fs.s01 = Arc(source=m.fs.feed.outlet, destination=m.fs.flash.inlet)
m.fs.s02 = Arc(source=m.fs.flash.vap_outlet, destination=m.fs.vap.inlet)
m.fs.s03 = Arc(source=m.fs.flash.liq_outlet, destination=m.fs.liq.inlet)
TransformationFactory("network.expand_arcs").apply_to(m)

# 5. Fix feed: 1 mol/s, equimolar benzene/toluene, 350K, 1 atm
m.fs.feed.flow_mol.fix(1.0)
m.fs.feed.temperature.fix(350)
m.fs.feed.pressure.fix(101325)
m.fs.feed.mole_frac_comp["benzene"].fix(0.5)
m.fs.feed.mole_frac_comp["toluene"].fix(0.5)

# 6. Fix flash specs: adiabatic + isobaric
m.fs.flash.heat_duty.fix(0)
m.fs.flash.deltaP.fix(0)

# 7. Initialize
optarg = {"nlp_scaling_method": "user-scaling",
          "OF_ma57_automatic_scaling": "yes", "max_iter": 1000}
initialize_unit(m.fs.feed, optarg)
propagate_state(arc=m.fs.s01)
initialize_unit(m.fs.flash, optarg)

# 8. Solve
solver = get_solver(solver_options=optarg)
results = solver.solve(m, tee=True)

# 9. Report
m.fs.flash.report()
```

## Shared Imports

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

## Key KB Paths

- Index: `numericalMethod/IDAES/README.md`
- Component database: `numericalMethod/IDAES/docs/component-parameter-database.md`
- Source code: `numericalMethod/IDAES/repo/idaes/`
- RST docs: `numericalMethod/IDAES/repo/docs/`
- Examples: `numericalMethod/IDAES/examples/idaes_examples/notebooks/docs/`
