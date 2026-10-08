---
description: Quick reference for lean-output commands, modes, and configuration
---

| Command | Purpose |
|---|---|
| `/lean` | Enable the configured default mode. |
| `/lean lite` | Remove filler/repetition. |
| `/lean standard` | Concise, complete default behavior. |
| `/lean ultra` | Maximum brevity while preserving correctness. |
| `/lean fast-build` | Enable fast-build workflow. |
| `/lean off` | Disable lean-output. |
| `/lean-fast-build <idea>` | Start a fast software build. |
| `/lean-audit` | Audit always-loaded context. |
| `/lean-compress <file>` | Safely compress a file. |
| `/lean-review [file]` | Find removable verbosity. |
| `/lean-gain [--last N]` | Report measured local transcript usage. |

Default mode: `LEAN_DEFAULT_MODE`, then `~/.config/lean-output/config.json`, otherwise `standard`.

Say `full detail` or `step by step` to override brevity for one turn.
