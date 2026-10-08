# lean-output

**A disciplined efficiency toolkit for Claude Code.**

Lean Output reduces unnecessary context and verbosity while protecting correctness, security, accessibility, and required detail. It also includes a fast-build workflow for shipping maintainable software in fewer turns.

## What it does

- **Lean modes:** `lite`, `standard`, `ultra`, `fast-build`, `off`
- **Fast builds:** vertical-slice delivery, smoke checks, and resumable handoffs
- **Context audit:** identify expensive always-loaded instructions
- **Compression:** reduce prompts/skills/docs without silently dropping rules
- **Review:** find removable verbosity
- **Usage report:** inspect locally stored transcript volume
- **Persistent mode:** lightweight `UserPromptSubmit` hook
- **Configurable defaults:** environment variable or JSON config

## Commands

| Command | Purpose |
|---|---|
| `/lean` | Enable configured default mode |
| `/lean standard` | Concise, complete responses |
| `/lean ultra` | Very terse output |
| `/lean fast-build` | Fast software delivery workflow |
| `/lean off` | Disable the plugin's brevity guidance |
| `/lean-fast-build <idea>` | Build using the fast-build protocol |
| `/lean-audit` | Audit always-loaded context |
| `/lean-compress <file>` | Compress a file safely |
| `/lean-review [file]` | Review for verbosity |
| `/lean-gain [--last N]` | Show measured local usage |
| `/lean-help` | Command reference |

## Configuration

The default mode is resolved in this order:

1. `LEAN_DEFAULT_MODE` environment variable
2. `~/.config/lean-output/config.json` → `defaultMode`
3. `standard`

Example:

```json
{
  "defaultMode": "standard",
  "language": "auto",
  "maxClarifyingQuestions": 1,
  "showUsageEstimates": false,
  "fastBuild": {
    "writeHandoff": true,
    "runSmokeCheck": true
  }
}
```

## Design principles

### Efficient, not careless
Token reduction never justifies dropping a security warning, constraint, edge case, validation step, or user-requested depth.

### Measure instead of guessing
`token_audit.py` gives a heuristic estimate. It is explicitly **not** a tokenizer-exact count. `usage_report.py` reports locally discoverable transcript volume and also uses a heuristic conversion.

### Speed without rework
Fast-build starts with the smallest runnable vertical slice, batches independent changes, verifies the result, and records a handoff when work may continue later.

## Project layout

```text
.claude-plugin/plugin.json  Plugin metadata
commands/                    User-facing slash commands
config/                      Safe editable defaults
hooks/                       Persistent mode handling
skills/                      Lean workflows
  lean-output/               Core rules, references, measurement scripts
  lean-fast-build/           Fast software delivery
  lean-audit/                Context audit
  lean-compress/             Safe compression
  lean-review/               Verbosity review
  lean-gain/                 Usage reporting
tests/                      Local regression checks
```

## Development

Run the regression tests from the plugin root:

```bash
python3 -m unittest discover -s tests -v
```

Run a token audit:

```bash
python3 skills/lean-output/scripts/token_audit.py README.md
```

## Philosophy

**Less noise. More useful work. No shortcuts on quality.**