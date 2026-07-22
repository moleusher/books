# IDAES Initialization Guide

Initialize IDAES models — single units to full recycle flowsheets. Without proper initialization,
nonlinear solvers (IPOPT) will almost certainly fail to converge.

## Knowledge Base Paths
- **KB root**: `numericalMethod/IDAES/`
- **Initialization docs**: `repo/docs/reference_guides/initialization/index.rst`
- **BT Initializer**: `repo/docs/reference_guides/initialization/bt_initializer.rst`
- **Single CV Initializer**: `repo/docs/reference_guides/initialization/single_cv_initializer.rst`
- **Developing initializers**: `repo/docs/reference_guides/initialization/developing_initializers.rst`
- **Source**: `repo/idaes/core/initialization/`
- **propagate_state**: `repo/idaes/core/util/initialization.py` (line 136)
- **Full HDA init example**: `examples/idaes_examples/notebooks/docs/tut/core/hda_flowsheet.ipynb`
- **Tear stream extras**: `examples/idaes_examples/mod/hda/hda_flowsheet_extras.py`
- **Model diagnostics**: `repo/docs/explanations/model_diagnostics/index.rst`

## The Golden Rule

> **Always initialize unit-by-unit in flow order before solving the full flowsheet.**

Solving the entire flowsheet at once with no initial values → almost guaranteed failure.
Sequential initialization → gives IPOPT a feasible starting point.

## Level 1: Single Unit (No Recycle)

### Pattern A: default_initializer (preferred)
```python
import idaes.logger as idaeslog

optarg = {
    "nlp_scaling_method": "user-scaling",
    "OF_ma57_automatic_scaling": "yes",
    "max_iter": 1000,
    "tol": 1e-8,
}

initializer = unit.default_initializer(solver_options=optarg)
initializer.initialize(unit, output_level=idaeslog.INFO_LOW)
```

### Pattern B: Error Fallback (robust)
```python
from idaes.core.util.exceptions import InitializationError
from idaes.core.solvers import get_solver

def initialize_unit(unit, optarg=None):
    if optarg is None:
        optarg = {
            "nlp_scaling_method": "user-scaling",
            "OF_ma57_automatic_scaling": "yes",
            "max_iter": 300,
        }
    try:
        initializer = unit.default_initializer(solver_options=optarg)
        initializer.initialize(unit, output_level=idaeslog.INFO_LOW)
    except InitializationError:
        # Fallback: solve the unit directly
        solver = get_solver(solver_options=optarg)
        results = solver.solve(unit)
        if not check_optimal_termination(results):
            raise RuntimeError(f"Failed to initialize {unit.name}")
```

**Use Pattern B when**: the unit has tight bounds, complex equilibrium, or the default initializer is known to be fragile.

### Single Unit Order (forward flow)
```
Feed → Heater → Flash → Product
  1       2        3        4
```
Initialize in numerical order. After each unit, propagete state to the next:
```python
from idaes.core.util.initialization import propagate_state

initialize_unit(m.fs.feed)
propagate_state(m.fs.s01)    # feed → heater
initialize_unit(m.fs.heater)
propagate_state(m.fs.s02)    # heater → flash
initialize_unit(m.fs.flash)
```

## Level 2: Flowsheet with Recycle (Tear Stream)

A recycle loop creates a cyclic dependency: downstream unit output → upstream unit input.

```
Feed → Mixer → Heater → Reactor → Flash → Splitter → Product
         ↑                                    │
         │         Compressor ←───────────────┘ (recycle)
         └────────────────────────────────────┘
```

### Concept: Tear Stream

"Tear" (cut) one stream in the recycle loop, turning the cyclic graph into an acyclic one. Assign a guess to the torn stream. After solving the acyclic flowsheet, compare the calculated tear stream against the guess. Iterate until converged.

### Method A: SequentialDecomposition (Pyomo Built-in)

```python
from pyomo.network import SequentialDecomposition

def init_with_sd(m, tear_guesses):
    seq = SequentialDecomposition()
    seq.options.select_tear_method = "heuristic"
    seq.options.tear_method = "Wegstein"     # or "Direct"
    seq.options.iterLim = 5                  # only 5 iterations for warm-start

    G = seq.create_graph(m)
    heuristic_tear_set = seq.tear_set_arcs(G, method="heuristic")
    order = seq.calculation_order(G)

    # Feed tear guesses to the torn stream destination
    seq.set_guesses_for(heuristic_tear_set[0].destination, tear_guesses)

    print(f"Tear stream: {heuristic_tear_set[0].destination.name}")
    print(f"Solve order: {[o[0].name for o in order]}")

    # Run: each unit in order with tear iteration
    seq.run(m, initialize_unit)
```

**When to use**: simpler, less code. Good first attempt.
**Limitations**: less control over individual unit failures, harder to debug.

### Method B: Manual Propagation (Full Control)

Deactivate tear constraint → fix tear values → solve downstream → unfix → reactivate.

```python
from idaes.core.util.initialization import propagate_state

def manual_tear_init(m, tear_arc, tear_guesses):
    """
    tear_arc: the Arc to tear (e.g., m.fs.s03)
    tear_guesses: dict of {var_name: {index: value}} for the torn destination
    """
    optarg = {
        "nlp_scaling_method": "user-scaling",
        "OF_ma57_automatic_scaling": "yes",
        "max_iter": 300,
    }

    # Step 1: Deactivate tear stream constraint
    tear_constraint_name = tear_arc.name + "_expanded"
    getattr(m.fs, tear_constraint_name).deactivate()
    print(f"DOF after tear deactivation: {degrees_of_freedom(m)}")

    # Step 2: Fix tear stream destination to guesses
    for var_group, vars_dict in tear_guesses.items():
        for idx, val in vars_dict.items():
            getattr(tear_arc.destination, var_group)[idx].fix(val)
    print(f"DOF after fixing tear: {degrees_of_freedom(m)}")

    solver = get_solver(solver_options=optarg)

    # Step 3: Sequential initialization in flow order
    # IMPORTANT: Start from the unit AFTER the tear, go around the loop
    initialize_unit(m.fs.heater)
    propagate_state(arc=m.fs.arc_heater_to_reactor)
    initialize_unit(m.fs.reactor)
    propagate_state(arc=m.fs.arc_reactor_to_flash)
    initialize_unit(m.fs.flash)
    propagate_state(arc=m.fs.arc_flash_to_splitter)
    initialize_unit(m.fs.splitter)
    propagate_state(arc=m.fs.arc_splitter_to_compressor)
    initialize_unit(m.fs.compressor)
    propagate_state(arc=m.fs.arc_compressor_to_mixer)

    # Step 4: Initialize feed + mixer (upstream of tear)
    initialize_unit(m.fs.feed)
    propagate_state(arc=m.fs.arc_feed_to_mixer)
    initialize_unit(m.fs.mixer)

    # Step 5: Propagate through tear to close the loop
    propagate_state(arc=tear_arc)

    # Step 6: Solve full flowsheet with tear fixed
    results = solver.solve(m, tee=False)
    print(f"Initial solve: {results.solver.termination_condition}")

    # Step 7: Unfix tear and reactivate constraint
    for var_group, vars_dict in tear_guesses.items():
        for idx in vars_dict:
            getattr(tear_arc.destination, var_group)[idx].unfix()
    getattr(m.fs, tear_constraint_name).activate()
    print(f"DOF after restoring tear: {degrees_of_freedom(m)}")
```

**When to use**: complex flowsheets, debugging initialization failures, needing precise control.
**Limitations**: requires knowing the tear stream and guesses, more code.

### How to Generate Tear Guesses

Tear guesses come from the tear stream's SOURCE port values BEFORE tearing:

```python
def get_tear_guesses(tear_arc):
    """Extract current values from tear source as guesses."""
    source = tear_arc.source
    guesses = {}
    for v in source.vars:
        guesses[v.name] = value(v)
    return guesses
```

Or, more practically, from the inlet feed conditions:
```python
# Feed conditions at Mixer inlet = reasonable tear guess
tear_guesses = {
    "flow_mol_phase_comp": {
        (0, "Vap", "benzene"): 0.001,
        (0, "Vap", "toluene"): 0.001,
        (0, "Vap", "hydrogen"): 0.1,
        (0, "Vap", "methane"): 0.05,
    },
    "temperature": {0: 350},
    "pressure": {0: 350000},
}
```

### Choosing the Tear Stream

Rule: tear the stream that minimizes the number of variables to guess.
- **Vapor-only streams**: fewer phase variables
- **Post-mixer stream**: combines all feeds → good place to tear before unit ops
- **Heuristic**: `SequentialDecomposition` with `"heuristic"` method does this automatically

## Level 3: After Initialization — Full Solve

```python
optarg_full = {
    "nlp_scaling_method": "user-scaling",
    "OF_ma57_automatic_scaling": "yes",
    "max_iter": 1000,
    "tol": 1e-8,
}

solver = get_solver(solver_options=optarg_full)
results = solver.solve(m, tee=True)

from pyomo.environ import check_optimal_termination
if not check_optimal_termination(results):
    # Initialization was insufficient — consider:
    # 1. Relax bounds temporarily
    # 2. Use manual propagation with intermediate solves
    # 3. Try Wegstein iteration for tear convergence
    raise RuntimeError(
        f"Solver failed after initialization: {results.solver.termination_condition}"
    )
```

## Common Initialization Failures

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `InitializationError` on first unit | Bad feed values | Check T, P within property valid range; check mole fractions sum to 1 |
| Unit initializes but next unit fails | propagate_state skipped | Always call `propagate_state(arc=...)` between units |
| Tear won't converge | Bad tear guess | Use source port values as initial guess, or solve a simpler version first |
| Wegstein diverges | Tear iteration unstable | Switch to `"Direct"` method or manual propagation |
| DOF wrong after tear | Constraint activate/deactivate mismatch | Double-check `_expanded` suffix on tear constraint name |
| Solver says "optimal" but wrong answers | Poor tear convergence | Increase `iterLim`, switch to manual with intermediate full solves |
| `Restoration failed` | Infeasible intermediate state | Relax bounds during initialization, then tighten for final solve |
| `IndexError` on tear_guesses | Wrong variable name or index structure | Inspect `tear_arc.destination.vars` to get exact names and indices |

## Initialization Checklist

1. ✓ `degrees_of_freedom(m)` = 0 before starting initialization
2. ✓ Feed boundary conditions are physically reasonable
3. ✓ Tear stream identified (for recycle flowsheets)
4. ✓ Tear guesses are reasonable (not zero flow/temperature)
5. ✓ Unit order follows flow direction (feed → products)
6. ✓ `propagate_state()` called between every unit pair
7. ✓ Each unit initialized successfully before moving to next
8. ✓ DOF returns to 0 after restoring tear constraint
9. ✓ `check_optimal_termination(results)` is True
10. ✓ Mass/energy balance verified post-solve

## Quick Reference: Initialization API

```python
# Core initializer
unit.default_initializer(solver_options={...}).initialize(unit, output_level=...)

# State propagation
propagate_state(source=port1, destination=port2)
propagate_state(arc=my_arc)  # auto-detects direction

# Tear tools
from pyomo.network import SequentialDecomposition  # automatic tear detection

# Error handling
from idaes.core.util.exceptions import InitializationError  # catch init failures

# Utility
from idaes.core.util.model_statistics import degrees_of_freedom  # check DOF
from pyomo.environ import check_optimal_termination             # verify solve
```

## Related Skills
- `idaes-flowsheet-builder` — build the flowsheet before initializing
- `idaes-model-debugger` — diagnose failures during or after initialization
- `idaes-unit-configurator` — understand per-unit initialization requirements
