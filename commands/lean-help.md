---
description: Quick reference for lean-output commands and modes
---

Print this table and nothing else:

| Command | Does |
|---|---|
| `/lean [lite\|standard\|ultra\|off]` | Set mode; no argument = on at default |
| `/lean-review [file]` | Delete-list of token waste |
| `/lean-audit` | Cost of always-loaded context |
| `/lean-compress <file>` | Trim a prompt/skill/doc safely |
| `/lean-gain` | Real usage from your transcripts |

Default mode: `LEAN_DEFAULT_MODE` env var or `defaultMode` in `~/.config/lean-output/config.json`. Say "full detail" to override for one turn.
