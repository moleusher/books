# IDAES Knowledge Base

Institute for the Design of Advanced Energy Systems (IDAES) — multi-scale, simulation-based, open-source process systems engineering framework.

## Directory Structure

```
numericalMethod/IDAES/
├── README.md              # This file — knowledge base index
├── repo/                  # idaes-pse.git (shallow clone, main branch)
│   ├── docs/              # Sphinx RST documentation source (313 .rst files)
│   ├── idaes/             # Python package (872 .py files)
│   │   ├── core/          # Framework backbone (flowsheet, control volumes, solvers, etc.)
│   │   ├── models/        # Generic model libraries (properties, unit_models, costing, control)
│   │   ├── models_extra/  # Extended models (power_gen, gas_solid_contactors, column, etc.)
│   │   ├── apps/          # Application modules (grid_integration, etc.)
│   │   ├── commands/      # CLI (idaes get-extensions, etc.)
│   │   └── conftest.py    # Pytest fixtures
│   └── scripts/           # Build scripts
├── examples/              # idaes-examples.git (shallow clone)
│   └── idaes_examples/notebooks/
│       ├── docs/          # 239 tested & documented notebooks (12 categories)
│       └── held/          # 4 unmaintained notebooks
└── skills/                # Claude Code skill definitions for IDAES development
```

## Quick Start Paths for Agents

### 🏗️ Building a Flowsheet (most common task)

1. **Start here**: `repo/docs/how_to_guides/workflow/index.rst` — model setup workflow
2. **Property package**: `repo/docs/explanations/components/property_package/general/index.rst`
3. **Unit models**: `repo/docs/reference_guides/model_libraries/generic/unit_models/index.rst`
4. **Example flowsheets**: `examples/idaes_examples/notebooks/docs/flowsheets/`

### 📚 API Reference (auto-generated from docstrings)

The Python source IS the API reference. Key entry points:
- **Flowsheet**: `repo/idaes/core/base/flowsheet_model.py`
- **Process Block**: `repo/idaes/core/base/process_block.py`
- **Unit Model**: `repo/idaes/core/base/unit_model.py`
- **Control Volume (0D)**: `repo/idaes/core/base/control_volume_0d.py`
- **Control Volume (1D)**: `repo/idaes/core/base/control_volume_1d.py`
- **Property packages**: `repo/idaes/core/base/property_meta.py`
- **Solvers**: `repo/idaes/core/solvers/`
- **Initialization**: `repo/idaes/core/initialization/`
- **Scaling**: `repo/idaes/core/scaling/`

### 🧪 Examples by Category (239 notebooks)

| Category | Path | Key Topics |
|----------|------|------------|
| **Tutorials** | `examples/.../docs/tut/` | Core concepts, UI intro |
| **Unit Models** | `examples/.../docs/unit_models/` | Operations, reactors, custom unit models, liquid extraction |
| **Flowsheets** | `examples/.../docs/flowsheets/` | HDA with costing/distillation, methanol synthesis, TSA |
| **Properties** | `examples/.../docs/properties/` | Txy diagrams, parameter estimation (PR EoS), custom packages |
| **Parameter Estimation** | `examples/.../docs/param_est/` | NRTL using state blocks & unit models |
| **Diagnostics** | `examples/.../docs/diagnostics/` | Degeneracy hunter, structural singularity, diagnostics toolbox |
| **DAE Systems** | `examples/.../docs/dae/` | PETSc for chemistry, PID control |
| **Surrogates** | `examples/.../docs/surrogates/` | ALAMO, PySMO, Keras/OMLT, sCO2 |
| **Scaling** | `examples/.../docs/scaling/` | Scaling workflows |
| **Power Generation** | `examples/.../docs/power_gen/` | NGCC, SOFC, supercritical |

## Documentation Map

### Getting Started
| Topic | RST Source |
|-------|------------|
| Installation (Win/Mac/Linux) | `repo/docs/tutorials/getting_started/` |
| Advanced Install (contributors) | `repo/docs/tutorials/advanced_install/` |
| IDAES Examples | `repo/docs/tutorials/tutorials_examples.rst` |

### How-To Guides
| Topic | RST Source |
|-------|------------|
| Setting up IDAES Models | `repo/docs/how_to_guides/workflow/` |
| Custom Model Development | `repo/docs/how_to_guides/custom_models/` |
| Versioned Installs | `repo/docs/how_to_guides/versioned_idaes_install.rst` |
| FlowsheetRunner Interface | `repo/docs/how_to_guides/structfs/` |
| Optional Dependencies | `repo/docs/how_to_guides/opt_dependencies.rst` |

### Explanations (Deep Dives)
| Topic | RST Source |
|-------|------------|
| Why IDAES | `repo/docs/explanations/why_idaes.rst` |
| Core Concepts | `repo/docs/explanations/concepts.rst` |
| Components (flowsheet/unit/property/ui) | `repo/docs/explanations/components/` |
| Property Package Framework | `repo/docs/explanations/components/property_package/general/` |
| Model Diagnostics | `repo/docs/explanations/model_diagnostics/` |
| Scaling Toolbox | `repo/docs/explanations/scaling_toolbox/` |
| Modeling Extensions | `repo/docs/explanations/modeling_extensions/` |
| Related Packages | `repo/docs/explanations/related_packages/` |

### Reference Guides
| Topic | RST Source |
|-------|------------|
| **Model Libraries** | `repo/docs/reference_guides/model_libraries/` |
| — Generic (properties, units, control, costing) | `.../generic/` |
| — Power Generation | `.../power_generation/` |
| — Gas Solid Contactors | `.../gas_solid_contactors/` |
| — Extra (PHE, TSA, membranes) | `.../models_extra/` |
| **Core API** | `repo/docs/reference_guides/core/` |
| — Process/Flowsheet Block | `.../process_block.rst`, `.../flowsheet_block.rst` |
| — Control Volumes (0D/1D) | `.../control_volume_0d.rst`, `.../control_volume_1d.rst` |
| — Property Classes | `.../physical_property_class.rst`, `.../reaction_property_class.rst` |
| — Unit Model Class | `.../unit_model_block.rst` |
| — Component/Phase classes | `.../comp.rst`, `.../phase.rst` |
| — Solvers | `.../solvers.rst` |
| — Utility Methods | `.../util/` |
| — Costing | `.../costing/` |
| **Scaling** | `repo/docs/reference_guides/scaling/` |
| **Initialization** | `repo/docs/reference_guides/initialization/` |
| **CLI Commands** | `repo/docs/reference_guides/commands/` |
| **Configuration** | `repo/docs/reference_guides/configuration.rst` |
| **Logging** | `repo/docs/reference_guides/logging.rst` |
| **Developer Guide** | `repo/docs/reference_guides/developer/` |
| **Grid Integration** | `repo/docs/reference_guides/apps/grid_integration/` |

## Available Unit Models (28 in Generic Library)

**Reactors**: CSTR, Equilibrium, Gibbs, PFR, Stoichiometric (Yield)
**Heat Transfer**: Heater, HeatExchanger (0D), HeatExchanger (Lumped Capacitance), HeatExchanger (NTU), HeatExchanger (1D), Shell & Tube (1D)
**Fluid Flow**: Compressor, Pump, Turbine, Valve, Pressure Changer
**Separation**: Flash, Separator, Multi-Stream Contactor
**Mixing/Splitting**: Mixer, Feed, Feed+Flash, Product
**Transport**: StateJunction, Translator, Stream Scaler
**Solid-Liquid**: (separate sub-library)
**Other**: Skeleton Unit Model (template for custom)

## Property Packages

**VLE**: Activity Coefficient (NRTL, Wilson, UNIQUAC), Cubic EoS (Peng-Robinson, Soave-Redlich-Kwong), Helmholtz EoS
**Modular Framework**: Composible state definitions, transport property methods, reaction packages
**State Definitions**: FTPx, FcTP, FcPh, FpcTP, FPhx
**Transport**: Chapman-Enskog, Chung (pure), viscosity-Wilke, thermal conductivity-WMS

## Key Architectural Concepts

1. **Flowsheet** = Pyomo ConcreteModel containing unit models connected by Arcs
2. **Unit Model** = ControlVolume(s) + property packages + constraints
3. **Property Package** = thermodynamic/transport property calculations (pluggable)
4. **State Block** = material/energy state at a point (attached to ports)
5. **Port** = connection point for Arcs between unit models
6. **Arc** = equality constraints linking inlet/outlet ports

## Agent Usage Guide

### For Understanding Code
```bash
# Read a specific RST doc
Read repo/docs/reference_guides/model_libraries/generic/unit_models/flash.rst

# Find a specific model implementation
grep -r "class Flash" repo/idaes/models/

# Explore examples
find examples/idaes_examples/notebooks/docs/flowsheets -name "*.ipynb"
```

### For Building New Models
1. Read `repo/docs/how_to_guides/workflow/index.rst` for the standard workflow
2. Study a similar unit model in `repo/idaes/models/unit_models/`
3. Study the property package framework in `repo/docs/explanations/components/property_package/general/`
4. Reference example notebooks in `examples/idaes_examples/notebooks/docs/unit_models/`

### For Property Method Selection
1. Read `repo/docs/explanations/components/property_package/general/index.rst`
2. For VLE: Activity Coefficient (polar) vs Cubic EoS (non-polar)
3. For electrolytes: `repo/idaes/core/base/electrolyte_property_set.py`

## Related Resources
- Online docs: https://idaes-pse.readthedocs.io/en/stable/
- Examples site: https://idaes-examples.readthedocs.io/en/latest/
- GitHub: https://github.com/IDAES/idaes-pse
- IDAES+ platform: https://idaesplus.readthedocs.io/latest/
- UI docs: https://idaes-ui.readthedocs.io/en/latest/
- Citation: Lee et al. (2021), J. Adv. Manuf. Process. 3(3), e10095
