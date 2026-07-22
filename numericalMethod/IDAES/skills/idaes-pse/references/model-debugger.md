# IDAES Model Debugger

Diagnose and fix common IDAES issues: initialization failure, solver non-convergence,
numerical scaling problems, structural singularity, and degree-of-freedom errors.

## Knowledge Base Paths
- **KB root**: `numericalMethod/IDAES/`
- **Diagnostics workflow**: `repo/docs/explanations/model_diagnostics/index.rst`
- **Degeneracy hunter**: `repo/docs/explanations/model_diagnostics/degeneracy_hunter.rst`
- **SVD analysis**: `repo/docs/explanations/model_diagnostics/svd_analysis.rst`
- **Scaling diagnostics**: `repo/docs/explanations/scaling_toolbox/diagnosing_scaling_issues.rst`
- **Scaling workflow**: `repo/docs/explanations/scaling_toolbox/scaling_workflow.rst`
- **Initialization ref**: `repo/docs/reference_guides/initialization/index.rst`
- **Solver ref**: `repo/docs/reference_guides/core/solvers.rst`
- **Diagnostics examples**: `examples/idaes_examples/notebooks/docs/diagnostics/`
- **Configuration**: `repo/docs/reference_guides/configuration.rst`

## Diagnostic Protocol (Real API)

### Phase 1: Structural Check
```python
from idaes.core.util.model_statistics import degrees_of_freedom

dof = degrees_of_freedom(m)
print(f"DOF = {dof}")  # MUST be 0

# List fixed vs unfixed variables if DOF != 0
from idaes.core.util.model_statistics import (large_residuals_set,
                                               variables_near_bounds,
                                               variables_in_activated_constraints)
```

### Phase 2: Scaling Check
```python
from idaes.core.util.scaling import (badly_scaled_var_generator,
                                      unscaled_variables_generator,
                                      calculate_scaling_factors)

# Auto-calculate scaling factors
calculate_scaling_factors(m)

# Check for problems
for v in badly_scaled_var_generator(m):
    print(f"Badly scaled: {v.name} = {v.value}, scale={v.scaling_factor}")
for v in unscaled_variables_generator(m):
    print(f"Unscaled: {v.name}")
```

Common scaling:
- Flow rates: scale to ~1 (factor = 1/typical_flow)
- Pressure (Pa): scale factor ~1e-5 (→ bar) or ~1e-6 (→ MPa)
- Enthalpy (J/mol): scale factor ~1e-6 to 1e-7
- Compositions: usually fine (0–1 range)

### Phase 3: Initialization
```python
import idaes.logger as idaeslog
from idaes.core.util.exceptions import InitializationError
from idaes.core.solvers import get_solver

optarg = {
    "nlp_scaling_method": "user-scaling",
    "OF_ma57_automatic_scaling": "yes",
    "max_iter": 1000,
    "tol": 1e-8,
}

# Pattern with error fallback:
def init_unit(unit):
    try:
        initializer = unit.default_initializer(solver_options=optarg)
        initializer.initialize(unit, output_level=idaeslog.INFO_LOW)
    except InitializationError as e:
        print(f"Initialization failed: {e}, falling back to solve...")
        solver = get_solver(solver_options=optarg)
        results = solver.solve(unit)
        print(f"Fallback solve: {results.solver.termination_condition}")

# Initialize in flow order: feed → heater → flash → etc.
for unit in [m.fs.feed, m.fs.heater, m.fs.flash]:
    init_unit(unit)
```

### Phase 4: Solver Diagnostics
```python
solver = get_solver(solver_options=optarg)
results = solver.solve(m, tee=True)

print(f"Termination: {results.solver.termination_condition}")
print(f"Status: {results.solver.status}")

# Check solution quality
from pyomo.environ import check_optimal_termination
if check_optimal_termination(results):
    print("Solution is optimal")
```

### Phase 5: Advanced Diagnostics

**Degeneracy Hunter** (find redundant/dependent constraints):
```python
from idaes.core.util.diagnostics import DiagnosticsToolbox
dt = DiagnosticsToolbox(m)
dt.report_structural_issues()
```

**Check residuals**:
```python
# After solve, check all constraint residuals
for c in m.component_data_objects(Constraint, active=True):
    resid = abs(value(c.body) - value(c.upper if c.upper is not None else c.lower)) if c.equality else 0
    if resid > 1e-6:
        print(f"Large residual: {c.name} = {resid}")
```

## Common Error Patterns & Solutions

| Error | Diagnosis | Fix |
|-------|-----------|-----|
| `DOF != 0` | Wrong # of fixed vars | Count DOF per unit; check each spec |
| `Infeasible` | Contradictory specs | Check T-crossing, P-violations, mass balance |
| `Unbounded` | Missing bound | Add bounds on all free variables |
| `Restoration failed` | IPOPT couldn't restore feasibility | Relax bounds, better initial guess, scale |
| `Numerical difficulty` | Poor scaling | Scale flows to ~1, P to bar, H to MJ |
| `Initialization fails` | Bad initial guess or range | Check T,P within property method valid range |
| `Division by zero` | Zero flow/size | Add small epsilon or fix to non-zero |
| `Constraint residual large` | Dependent or contradictory | Use Degeneracy Hunter |

### IPOPT-Specific Options Tuning
```python
optarg = {
    "max_iter": 1000,
    "tol": 1e-8,
    "constr_viol_tol": 1e-8,
    "acceptable_tol": 1e-6,
    "acceptable_constr_viol_tol": 1e-6,
    "nlp_scaling_method": "user-scaling",  # or "gradient-based"
    "OF_ma57_automatic_scaling": "yes",
    "halt_on_ampl_error": "yes",
}
```

### When to Use HSL Solvers
IDAES ships with MA57 (HSL). For harder problems, install MA27/MA86:
```bash
idaes get-extensions --extra ma27 ma86
```

## Post-Solution Validation
1. **Mass balance**: Σ(in) ≈ Σ(out) within 1e-6
2. **Energy balance**: Energy in ≈ Energy out within 1e-6
3. **Phase check**: Vapor fraction 0–1 for VLE units
4. **Temperature cross**: No internal temperature cross-over in heat exchangers
5. **Engineering sense**: Flow rates, temperatures, pressures in expected ranges

## Related Skills
- `idaes-flowsheet-builder` — build correctly from the start
- `idaes-property-selector` — ensure property package is compatible
- `idaes-unit-configurator` — debug individual unit configuration
