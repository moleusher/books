# IDAES Unit Model Configurator

Configure, customize, and extend IDAES unit models.

## Knowledge Base Paths
- **KB root**: `numericalMethod/IDAES/`
- **Custom model dev**: `repo/docs/how_to_guides/custom_models/general_model_development.rst`
- **Unit model class**: `repo/docs/reference_guides/core/unit_model_block.rst`
- **Control volume 0D**: `repo/docs/reference_guides/core/control_volume_0d.rst`
- **Control volume 1D**: `repo/docs/reference_guides/core/control_volume_1d.rst`
- **Generic unit refs**: `repo/docs/reference_guides/model_libraries/generic/unit_models/`
- **Unit model examples**: `examples/idaes_examples/notebooks/docs/unit_models/`
- **Custom unit example**: `examples/idaes_examples/notebooks/docs/unit_models/custom_unit_models/`
- **HDA example**: `examples/idaes_examples/notebooks/docs/tut/core/hda_flowsheet.ipynb`

## Standard Unit Model Configuration (Real API)

### Common Arguments
```python
m.fs.unit = UnitModelType(
    property_package=m.fs.thermo_params,  # REQUIRED — always first
    # Optional common arguments:
    has_holdup=False,           # Dynamic holdup
    has_heat_transfer=False,    # Heat exchange with environment
    has_pressure_change=False,  # dP calculations
    has_phase_equilibrium=True, # Phase split in unit
    # Dynamic:
    dynamic=False,
)
```

### Reactors
```python
from idaes.models.unit_models import (CSTR, EquilibriumReactor,
                                       GibbsReactor, PFR,
                                       StoichiometricReactor)

# CSTR
m.fs.r101 = CSTR(property_package=m.fs.thermo_params,
                 reaction_package=m.fs.reaction_params,
                 has_heat_transfer=True)

# Stoichiometric (yield-based)
m.fs.r101 = StoichiometricReactor(
    property_package=m.fs.thermo_params,
    reaction_package=m.fs.reaction_params)

# Fix conversion manually:
m.fs.r101.conversion = Var(initialize=0.75, bounds=(0, 1))
m.fs.r101.conv_constraint = Constraint(
    expr=m.fs.r101.conversion * flow_in == flow_in - flow_out)
m.fs.r101.conversion.fix(0.75)
```

### Heat Transfer
```python
from idaes.models.unit_models import Heater, HeatExchanger

m.fs.h101 = Heater(property_package=m.fs.thermo_params,
                   has_pressure_change=True,
                   has_phase_equilibrium=True)

# Fix one of:
m.fs.h101.heat_duty.fix(0)              # or
m.fs.h101.outlet.temperature.fix(600)   # via control_volume.properties_out[0].temperature
```

### Fluid Handling
```python
from idaes.models.unit_models import Pump, Compressor, Turbine, Valve, PressureChanger
from idaes.models.unit_models.pressure_changer import ThermodynamicAssumption

m.fs.c101 = PressureChanger(
    property_package=m.fs.thermo_params,
    compressor=True,
    thermodynamic_assumption=ThermodynamicAssumption.isentropic)

m.fs.p101 = Pump(property_package=m.fs.thermo_params)
```

### Separation
```python
from idaes.models.unit_models import Flash, Separator

# Flash: 2 DOF (heat duty + dP, or T + P)
m.fs.f101 = Flash(property_package=m.fs.thermo_params)
m.fs.f101.heat_duty.fix(0)        # adiabatic
m.fs.f101.deltaP.fix(0)           # isobaric

# Outlet ports: .vap_outlet, .liq_outlet
```

### Flow Routing
```python
from idaes.models.unit_models import Feed, Product, Mixer, StateJunction

m.fs.feed = Feed(property_package=m.fs.thermo_params)
m.fs.m101 = Mixer(property_package=m.fs.thermo_params, num_inlets=3)
m.fs.prod = Product(property_package=m.fs.thermo_params)
```

## Degrees of Freedom per Unit Type

| Unit | Typical DOF | Common Specs |
|------|-------------|--------------|
| Heater | 1 | Heat duty OR outlet T |
| Flash | 2 | Heat duty + dP (or T + P) |
| Pump/Compressor | 1 | dP OR work |
| Mixer | 0 | (determined by inlets) |
| Feed | N_comp + 2 | Total flow, N_comp-1 fractions, T, P |
| Product | 0 | (determined by inlet) |
| CSTR | 2+ | Volume + heat duty (or conversion + T) |
| PFR | 2+ | Length + heat duty |
| Valve | 1 | dP OR Cv |
| Separator | N_out-1 | Split fractions |

## Building Custom Unit Models

### Template from Skeleton Unit
See: `repo/idaes/models/unit_models/skeleton_unit.py`

### Required Pattern
```python
from idaes.core import (declare_process_block_class,
                         UnitModelBlockData)
from pyomo.common.config import ConfigValue

@declare_process_block_class("MyUnit")
class MyUnitData(UnitModelBlockData):
    CONFIG = UnitModelBlockData.CONFIG()
    CONFIG.declare("my_arg", ConfigValue(
        default=None,
        domain=int,
        description="My custom argument"))

    def build(self):
        super().build()
        # 1. Create control volume(s)
        # 2. Add ports (inlet, outlet)
        # 3. Add constraints (mass/energy balance, design eqns)
        # 4. Optionally add performance methods

    def initialize(self, state_args=None, solver_options=None, **kwargs):
        # Sequential initialization: fix inlets → solve CV → fix outlets
        # Fallback pattern:
        from idaes.core.util.exceptions import InitializationError
        from idaes.core.solvers import get_solver
        try:
            initializer = self.default_initializer(solver_options=solver_options)
            initializer.initialize(self, output_level=idaeslog.INFO_LOW)
        except InitializationError:
            get_solver(solver_options=solver_options).solve(self)
```

### Key Base Classes
| Base Class | Location | Use For |
|------------|----------|---------|
| `UnitModelBlockData` | `idaes.core` | All unit models |
| `ControlVolume0DBlockData` | `idaes.core` | Well-mixed volumes |
| `ControlVolume1DBlockData` | `idaes.core` | Plug flow, axial dispersion |
| `PhysicalParameterBlock` | `idaes.core` | Custom property packages |
| `StateBlockData` | `idaes.core` | Custom state definitions |

### Common Config Arguments (from UnitModelBlockData)
- `dynamic` (bool): steady-state vs dynamic
- `has_holdup` (bool): material/energy accumulation
- `property_package` (PhysicalParameterBlock): thermo
- `property_package_args` (dict): passed to state blocks

## Initialization Patterns

### Default Initializer
```python
initializer = unit.default_initializer(solver_options=optarg)
initializer.initialize(unit, output_level=idaeslog.INFO_LOW)
```

### Custom Initialization Sequence (sequential modular)
```python
def init_flowsheet(m):
    # Fix inlet states
    m.fs.feed.initialize()

    # Propagate: solve each unit in flow order
    for unit in [m.fs.heater, m.fs.flash, m.fs.product]:
        unit.initialize()

    # Unfix outlet if needed, then solve full flowsheet
```

## Related Skills
- `idaes-flowsheet-builder` — connect unit models into flowsheets
- `idaes-property-selector` — ensure compatible property package
- `idaes-model-debugger` — debug unit model issues
