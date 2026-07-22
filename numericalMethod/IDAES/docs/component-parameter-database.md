# IDAES Component Parameter Database

Maps chemical species → pre-existing thermodynamic parameter configs in the IDAES knowledge base.
Agents should **copy-paste from these sources** rather than inventing parameter data.

## Quick Lookup by Chemical

| Chemical | EoS Type | Source File |
|----------|----------|-------------|
| **argon** | Peng-Robinson | `repo/idaes/models/properties/modular_properties/examples/ASU_PR.py` |
| **benzene** | Ideal / PR | `repo/.../examples/BT_ideal.py`, `BT_PR.py`, `examples/.../mod/hda/hda_ideal_VLE_modular.py` |
| **bmimPF6** (ionic liquid) | Peng-Robinson | `repo/.../examples/CO2_bmimPF6_PR.py` |
| **carbon_dioxide** (CO₂) | PR / Ideal VLE | `repo/.../examples/CO2_bmimPF6_PR.py`, `CO2_H2O_Ideal_VLE.py` |
| **CH4** (methane) | Ideal / PR | `examples/.../mod/methanol/methanol_ideal_vapor.py`, `HC_PR.py`, `HDA` |
| **CH3OH** (methanol) | Ideal | `examples/.../mod/methanol/methanol_ideal_vapor.py`, `methanol_ideal_VLE.py` |
| **CO** (carbon monoxide) | Ideal | `examples/.../mod/methanol/methanol_ideal_vapor.py`, `methanol_ideal_VLE.py` |
| **ethylene_glycol** | Ideal | `examples/.../notebooks/docs/unit_models/operations/eg_h2o_ideal.py`, `reactors/egprod_ideal.py` |
| **ethylene_oxide** | Ideal | `examples/.../notebooks/docs/unit_models/reactors/egprod_ideal.py` |
| **H2** (hydrogen) | Ideal / PR | `examples/.../mod/methanol/methanol_ideal_vapor.py`, `HC_PR.py`, `HDA` |
| **H2O** (water) | Ideal VLE / ENRTL | `repo/.../examples/CO2_H2O_Ideal_VLE.py`, `enrtl_H2O_NaCl_KCl.py`, `enrtl_NaBr_mixed_solvent.py` |
| **KCl** (electrolyte) | ENRTL | `repo/.../examples/enrtl_H2O_NaCl_KCl.py` |
| **MeOH** (methanol solvent) | ENRTL | `repo/.../examples/enrtl_NaBr_mixed_solvent.py` |
| **NaCl** (electrolyte) | ENRTL | `repo/.../examples/enrtl_H2O_NaCl_KCl.py` |
| **NaBr** (electrolyte) | ENRTL | `repo/.../examples/enrtl_NaBr_mixed_solvent.py` |
| **nitrogen** (N₂) | Peng-Robinson | `repo/.../examples/ASU_PR.py` |
| **oxygen** (O₂) | Peng-Robinson | `repo/.../examples/ASU_PR.py` |
| **toluene** | Ideal / PR | `repo/.../examples/BT_ideal.py`, `BT_PR.py`, `examples/.../mod/hda/hda_ideal_VLE_modular.py` |

## By Chemical System (copy-paste target)

All paths relative to `numericalMethod/IDAES/`.

### 1. Benzene-Toluene (Ideal VLE)
**File**: `repo/idaes/models/properties/modular_properties/examples/BT_ideal.py`
**Type**: Ideal gas + Ideal liquid, Fugacity VLE
**Components**: benzene, toluene
**State definition**: FTPx
**Pure data**: Perrys, RPP4
**Best for**: Simple VLE distillation, flash calculations

### 2. Benzene-Toluene (Peng-Robinson)
**File**: `repo/idaes/models/properties/modular_properties/examples/BT_PR.py`
**Type**: Cubic EoS (PR), Fugacity VLE
**Components**: benzene, toluene
**State definition**: FTPx
**Pure data**: RPP4
**Best for**: High-pressure VLE, non-ideal hydrocarbon mixtures

### 3. Hydrodealkylation (HDA) — Benzene+Toluene+Hydrogen+Methane
**File**: `examples/idaes_examples/mod/hda/hda_ideal_VLE_modular.py`
**Type**: Ideal gas + Ideal liquid, SmoothVLE
**Components**: benzene, toluene, hydrogen, methane
**State definition**: FpcTP (flow + phase + components)
**Reaction package**: `examples/idaes_examples/mod/hda/hda_reaction_modular.py`
**Best for**: Reactive flowsheet with hydrodealkylation: C₆H₅CH₃ + H₂ → C₆H₆ + CH₄

### 4. Methanol Synthesis — Vapor Phase Only
**File**: `examples/idaes_examples/mod/methanol/methanol_ideal_vapor.py`
**Type**: Ideal gas (no liquid phase)
**Components**: CH4, CO, H2, CH3OH
**State definition**: FTPx
**Pure data**: RPP4
**Best for**: Methanol synthesis loop (gas-phase reactor)

### 5. Methanol Synthesis — with VLE
**File**: `examples/idaes_examples/mod/methanol/methanol_ideal_VLE.py`
**Type**: Ideal gas + Ideal liquid, SmoothVLE
**Components**: CH4, CO, H2, CH3OH, H2O
**State definition**: FTPx
**Pure data**: RPP4, NIST (vapor pressure)
**Best for**: Methanol synthesis with condensation/separation

### 6. Hydrogen-Methane (Peng-Robinson, VLE)
**File**: `repo/idaes/models/properties/modular_properties/examples/HC_PR.py`
**Type**: Cubic EoS (PR), Fugacity VLE
**Components**: hydrogen, methane
**State definition**: FTPx
**Best for**: Cryogenic H₂/CH₄ separation

### 7. Hydrogen-Methane (PR, Vapor Only)
**File**: `repo/idaes/models/properties/modular_properties/examples/HC_PR_vap.py`
**Type**: Cubic EoS (PR), vapor phase only
**Components**: hydrogen, methane
**Best for**: Gas-phase only systems

### 8. CO₂ + Ionic Liquid (bmimPF6)
**File**: `repo/idaes/models/properties/modular_properties/examples/CO2_bmimPF6_PR.py`
**Type**: Cubic EoS (PR), Fugacity VLE
**Components**: bmimPF6, carbon_dioxide
**State definition**: FTPx
**Best for**: CO₂ capture with ionic liquids

### 9. CO₂ + H₂O (Ideal VLE)
**File**: `repo/idaes/models/properties/modular_properties/examples/CO2_H2O_Ideal_VLE.py`
**Type**: Ideal gas + Ideal liquid, Fugacity VLE
**Components**: H2O, CO2
**State definition**: FTPx
**Pure data**: Perrys, NIST
**Best for**: CO₂ absorption in water, carbon capture

### 10. Air Separation Unit (N₂-Ar-O₂, Peng-Robinson)
**File**: `repo/idaes/models/properties/modular_properties/examples/ASU_PR.py`
**Type**: Cubic EoS (PR), Fugacity VLE + NIST vapor pressure
**Components**: nitrogen, argon, oxygen
**State definition**: FTPx
**Includes**: Binary interaction parameters (PR_kappa) for all pairs
**Best for**: Cryogenic air separation, distillation columns

### 11. H₂O-NaCl-KCl (Electrolyte NRTL)
**File**: `repo/idaes/models/properties/modular_properties/examples/enrtl_H2O_NaCl_KCl.py`
**Type**: Electrolyte NRTL (symmetric reference state)
**Components**: H2O (solvent), Na⁺, K⁺, Cl⁻ (ions)
**State definition**: FTPx
**Best for**: Brine, desalination, electrolyte thermodynamics

### 12. NaBr in Mixed Solvent (Electrolyte NRTL)
**File**: `repo/idaes/models/properties/modular_properties/examples/enrtl_NaBr_mixed_solvent.py`
**Type**: Electrolyte NRTL
**Components**: H2O, MeOH, EtOH (solvents), Na⁺, Br⁻ (ions)
**State definition**: FTPx
**Best for**: Mixed-solvent electrolyte systems

### 13. Ethylene Glycol + Water
**File**: `examples/idaes_examples/notebooks/docs/unit_models/operations/eg_h2o_ideal.py`
**Type**: Ideal gas + Ideal liquid, Fugacity VLE
**Components**: water, ethylene_glycol
**Best for**: EG-water separation, glycol dehydration

### 14. Ethylene Oxide → Ethylene Glycol (Reactive)
**File**: `examples/idaes_examples/notebooks/docs/unit_models/reactors/egprod_ideal.py`
**Type**: Ideal gas + Ideal liquid, Fugacity VLE
**Components**: ethylene_oxide, water, ethylene_glycol
**Best for**: Reactive system: C₂H₄O + H₂O → C₂H₆O₂

## How to Use (Agent Instructions)

### To build a property package for a NEW system:
1. Find the closest match in the table above
2. Read the config dict from the source file
3. Copy-paste the `configuration = {...}` block as a template
4. Replace component names and parameter data for your chemicals
5. Adjust `state_definition`, `phases`, `phases_in_equilibrium` for your system

### Where to find thermodynamic constants:
- **Cp_ig coefficients**: RPP4, RPP5, NIST modules (or Perry's Handbook, Poling et al.)
- **Critical constants**: RPP4, NIST webbook
- **Vapor pressure**: RPP4, RPP5, NIST
- **Liquid density**: Perrys
- **Binary interaction (PR κ_ij)**: Literature, or set to 0 for initial runs
- **NRTL τ**: Literature or parameter estimation from VLE data

### Pre-built packages (no config dict needed):
```python
from idaes.models.properties.activity_coeff_models import BTXParameterBlock
from idaes.models.properties import iapws95   # IAPWS-95 water/steam
from idaes.models.properties import swco2     # sCO2
```
These are simpler but only available for specific systems.

## Related Reference
- Property selector skill: `skills/idaes-property-selector.md`
- Modular property framework docs: `repo/docs/explanations/components/property_package/general/index.rst`
