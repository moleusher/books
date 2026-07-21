# IDAES Property Method Selector

Select and configure thermodynamic property packages for IDAES simulations.

## Knowledge Base Paths
- **KB root**: `numericalMethod/IDAES/`
- **Property framework**: `repo/docs/explanations/components/property_package/general/index.rst`
- **Modular props doc**: `repo/docs/explanations/components/property_package/general/generic_definition.rst`
- **State definitions**: `repo/docs/explanations/components/property_package/general/state_definition.rst`
- **EoS details**: `repo/docs/explanations/components/property_package/general/eos/`
- **Phase equilibrium**: `repo/docs/explanations/components/property_package/general/phase_equilibrium.rst`
- **Transport props**: `repo/docs/explanations/components/property_package/general/transport_properties/`
- **Reaction packages**: `repo/docs/explanations/components/property_package/general_reactions/`
- **Config examples**: `examples/idaes_examples/mod/hda/hda_ideal_VLE_modular.py`
- **BTX VLE example**: `examples/idaes_examples/notebooks/docs/properties/dictionary_txy_diagrams.ipynb`
- **Source**: `repo/idaes/models/properties/modular_properties/`
- **Component parameter DB**: `docs/component-parameter-database.md` ← COPY-PASTE FROM HERE

## Two Approaches

### Approach A: Modular Framework (recommended — most flexible)

Use `GenericParameterBlock` with a configuration dictionary.

```python
from idaes.models.properties.modular_properties import GenericParameterBlock
from idaes.models.properties.modular_properties.state_definitions import FTPx
from idaes.models.properties.modular_properties.eos.ideal import Ideal
from idaes.models.properties.modular_properties.eos.ceos import Cubic
from idaes.models.properties.modular_properties.phase_equil import SmoothVLE
from idaes.models.properties.modular_properties.phase_equil.forms import fugacity
from idaes.models.properties.modular_properties.pure import Perrys, RPP4, RPP5, NIST
from idaes.core import LiquidPhase, VaporPhase, Component

configuration = { ... }  # Build config dict (see below)
m.fs.properties = GenericParameterBlock(**configuration)
```

### Approach B: Pre-Built Parameter Blocks

Import a ready-made class (less flexible but simpler):
```python
from idaes.models.properties.activity_coeff_models import BTXParameterBlock
m.fs.properties = BTXParameterBlock(valid_phase=('Liq', 'Vap'))
```

Available pre-built packages in `repo/idaes/models/properties/`:
- `activity_coeff_models/` — BTX, methane combustion, generic activity coefficient
- `general_helmholtz/` — Helmholtz EoS
- `iapws95.py` — IAPWS-95 water/steam
- `swco2.py` — sCO2 properties

## Decision Tree

```
Is the system aqueous/electrolyte?
├── YES → Custom electrolyte package needed
│   - See repo/idaes/core/base/electrolyte_property_set.py
│   - Use modular framework with ElectrolytePropertySet
└── NO → What phases?
    ├── Gas-phase only (combustion, gasification)
    │   → ideal.py EoS + NIST/Perry's data
    │   - repo/idaes/models/properties/modular_properties/eos/ideal.py
    ├── Vapor-Liquid Equilibrium (distillation, flash, etc.)
    │   ├── Non-polar (hydrocarbons, N2, O2, CO2)
    │   │   → Cubic EoS (Peng-Robinson / SRK)
    │   │   - repo/idaes/models/properties/modular_properties/eos/ceos.py
    │   │   - See examples/.../docs/properties/parameter_estimation_pr.ipynb
    │   └── Polar (water, alcohols, acids, amines)
    │       → Activity coefficient via SmoothVLE or fugacity forms
    │       - repo/idaes/models/properties/modular_properties/phase_equil/forms.py
    │       - See examples/.../docs/properties/dictionary_txy_diagrams.ipynb
    └── Refrigeration / power cycles → Helmholtz EoS
```

## Building a Configuration Dictionary

### Minimal template:
```python
from pyomo.environ import units as pyunits

configuration = {
    "components": {
        "comp_name": {
            "type": Component,
            "parameter_data": {
                "mw": (0.07811, pyunits.kg / pyunits.mol),
                "pressure_crit": (4.89e6, pyunits.Pa),
                "temperature_crit": (562.2, pyunits.K),
                # Add: cp_mol_ig_comp_coeff, dens_mol_liq_comp_coeff,
                #      enth_mol_form_liq_comp_ref, pressure_sat_comp_coeff
            },
            "dens_mol_liq_comp": Perrys,
            "enth_mol_liq_comp": Perrys,
            "enth_mol_ig_comp": RPP4,
            "pressure_sat_comp": RPP4,
            "phase_equilibrium_form": {("Vap", "Liq"): fugacity},
        },
    },
    "phases": {
        "Liq": {"type": LiquidPhase, "equation_of_state": Ideal},
        "Vap": {"type": VaporPhase, "equation_of_state": Ideal},
    },
    "state_definition": FTPx,
    "base_units": {
        "time": pyunits.s,
        "length": pyunits.m,
        "mass": pyunits.kg,
        "amount": pyunits.mol,
        "temperature": pyunits.K,
    },
    "phases_in_equilibrium": [("Vap", "Liq")],
    "phase_equilibrium_state": {("Vap", "Liq"): SmoothVLE},
    "pressure_ref": (101325, pyunits.Pa),
    "temperature_ref": (298.15, pyunits.K),
}
```

### State Definition Choices
| Module | State Variables | Best For |
|--------|----------------|----------|
| `FTPx` | Flow, T, P, mole frac | General-purpose VLE |
| `FcTP` | Flow comp, T, P | Fixed component set |
| `FcPh` | Flow comp, P, H | Energy balance dominant |
| `FpcTP` | Flow-phase-comp, T, P | Multi-phase tracking |
| `FTPx` | Flow, T, P, mole frac | Flash calculations |

### EoS Modules (repo/idaes/models/properties/modular_properties/eos/)
| Module | Use |
|--------|-----|
| `ideal.py` | Ideal gas, ideal liquid |
| `ceos.py` | Cubic EoS (Peng-Robinson, SRK) |
| `enrtl.py` | Electrolyte NRTL |
| `eos_base.py` | Base class for custom EoS |

### Pure Component Data Sources
| Module | Source |
|--------|--------|
| `Perrys` | Perry's Handbook |
| `RPP4`, `RPP5` | Reid, Prausnitz & Poling 4th/5th ed. |
| `NIST` | NIST webbook |
| `ConstantProperties` | User-specified constants |

### Phase Equilibrium Methods
| Module | Method |
|--------|--------|
| `SmoothVLE` | Smooth VLE formulation |
| `forms.py` (fugacity) | Fugacity equality |
| `bubble_dew.py` (IdealBubbleDew) | Ideal bubble/dew point |

### Transport Properties (when needed)
| Module | Method |
|--------|--------|
| `chapman_enskog` | Gas viscosity |
| `chung_pure` | Pure component |
| `viscosity_wilke` | Gas mixture viscosity |
| `thermal_conductivity_wms` | Gas thermal conductivity |

Import from `idaes.models.properties.modular_properties.transport_properties`.

## Reaction Packages
```python
from idaes.models.properties.modular_properties.base.generic_reaction import (
    GenericReactionParameterBlock)
m.fs.reaction_params = GenericReactionParameterBlock(
    property_package=m.fs.thermo_params, **reaction_config)
```

Reaction config includes: reaction rate forms, equilibrium constants, heat of reaction forms.

## Quick Validation
1. Does the config cover ALL components with parameter_data?
2. Are binary interaction parameters set for all pairs? (NRTL: `tau`, Cubic EoS: `kappa`)
3. Is T/P range within the property method's validity?
4. Does state_definition match what unit models expect?
5. Can you reproduce known saturation pressure or VLE data?

## Related Skills
- `idaes-flowsheet-builder` — build flowsheet after property setup
- `idaes-model-debugger` — debug property-related convergence issues
