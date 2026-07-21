# IDAES Skills for Claude Code

**Entry point**: `SKILL.md` — routes to the right sub-skill based on task.

## Skill Index

| Skill | File | Purpose | Trigger |
|-------|------|---------|---------|
| **🎯 Router** | `SKILL.md` | Entry point, decision tree → delegates to sub-skills | "IDAES", "process simulation", "flowsheet" |
| **Flowsheet Builder** | `idaes-flowsheet-builder.md` | Build complete process flowsheets end-to-end | "build IDAES flowsheet", "create process model", "set up IDAES simulation" |
| **Property Selector** | `idaes-property-selector.md` | Choose thermodynamic property methods | "select property package", "which EoS", "NRTL vs Peng-Robinson", "thermodynamic method" |
| **Model Debugger** | `idaes-model-debugger.md` | Diagnose solver/convergence/initialization issues | "IDAES not converging", "solver failed", "initialization error", "debug IDAES model" |
| **Unit Configurator** | `idaes-unit-configurator.md` | Configure, customize, build unit models | "add reactor", "configure heat exchanger", "custom unit model", "unit operation" |
| **Initialization Guide** | `idaes-initialization-guide.md` | Initialize flowsheets — single units, tear streams, recycle loops | "initialize flowsheet", "tear stream", "recycle convergence", "SequentialDecomposition" |

## Usage Pattern

Agents should:
1. **Read the skill file** to get the structured workflow and KB paths
2. **Navigate the KB** using the paths listed at the top of each skill
3. **Reference specific files** in `repo/docs/` for detailed information
4. **Study example notebooks** in `examples/idaes_examples/notebooks/docs/` for working code

## Skill Combinatorics

Most tasks require chaining skills:
- **New flowsheet**: Flowsheet Builder → Property Selector → Unit Configurator → Initialization Guide
- **Debugging**: Model Debugger (then Property Selector or Unit Configurator as needed)
- **Recycle flowsheet**: Flowsheet Builder → Initialization Guide (tear stream methods)
- **Adding unit**: Unit Configurator → Flowsheet Builder (for connection)

## Token Efficiency

These skills are designed to minimize token consumption:
- Each skill file is ~100-150 lines, not hundreds
- KB paths are precise file references — no need to grep/search
- Decision trees encode domain knowledge that would take many rounds of trial-and-error
- Common patterns/anti-patterns prevent rookie mistakes

## Installation

To use as Claude Code skills, copy to `.claude/skills/` or register in settings.json.
Currently these live in `numericalMethod/IDAES/skills/` as reference implementations.
