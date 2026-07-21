# IDAES Configuration Reference (parsed from readthedocs)

Access via `idaes.cfg` after importing idaes. Load order: internal defaults → global config file → local working directory config file. JSON format.

## Configuration Options

### warning_to_exception
- **Default**: `False`
- **Requires reconfig()**: Yes
- **Description**: Convert warnings to RuntimeError exceptions. Useful for ensuring clean models.

### deprecation_to_exception
- **Default**: `False`
- **Requires reconfig()**: Yes
- **Description**: Convert deprecation warnings to RuntimeError. Ensures no deprecated APIs are used.

### use_idaes_solvers
- **Default**: `True`
- **Requires reconfig()**: Yes
- **Description**: When False, prefers user-installed solvers over `idaes get-extensions` solvers.

### logger_capture_solver
- **Default**: `True`
- **Requires reconfig()**: No
- **Description**: Route solver output to logger (True) or screen (False).

### logger_tags
- **Default**: `["framework", "model", "flowsheet", "unit", "control_volume", "properties", "reactions"]`
- **Requires reconfig()**: No
- **Description**: Tags whose log messages are recorded. Must be subset of `valid_log_tags`.

### valid_log_tags
- **Default**: `["framework", "model", "flowsheet", "unit", "control_volume", "properties", "reactions", "ui"]`
- **Requires reconfig()**: No
- **Description**: Allowed log tags (whitelist for validation).

### ipopt.options
- **Default**: `{"nlp_scaling_method": "gradient-based"}`
- **Requires reconfig()**: No
- **Description**: Default IPOPT solver options. Passes through to AMPL executable.

### ipopt.options.nlp_scaling_method
- Options: `"gradient-based"` | `"user-scaling"` | `"none"`
- Set via: `idaes.cfg["ipopt"]["options"]["nlp_scaling_method"] = "user-scaling"`

## Commands

| Command | Purpose |
|---------|---------|
| `idaes config-write --file idaes.conf --default` | Write default config template |
| `idaes data-directory` | Find global config file location |
| `idaes.read_config(path)` | Load config file at runtime |
| `idaes.reconfig()` | Apply changes to options requiring it |
