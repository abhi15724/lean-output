# lean-output

*He reads the draft, says nothing, and hands it back half as long. Nothing true was lost.*

The editor for your AI agent. Highest quality in the fewest tokens, on both sides: what the agent **writes** and what it **reads**.



## How it works

Before writing or reading, the agent stops at the first rung that holds:

```
1. Needs saying or doing at all?  -> no: skip it
2. Already in context?            -> refer, don't repeat
3. A tool can do it?              -> run it, don't read/narrate
4. Belongs in a file or diff?     -> file; one line in chat
5. One sentence?                  -> one sentence
6. Only then: the minimum that is complete
```

Lean, not negligent. Never cut: correctness, safety warnings, edge cases that change what you do, requested depth, understanding the problem.

## Install (Claude Code)

```
/plugin marketplace add abhi15724/lean-output
```
```
/plugin install lean-output@lean-output
```
(Send as two separate prompts.) Needs `node` on PATH for the two hooks; without it the skill still works.

Local test: `claude --plugin-dir ./lean-output` and `claude plugin validate ./lean-output`.

## Modes and commands

| Command | What it does |
|---|---|
| `/lean [lite\|standard\|ultra\|off]` | Set mode; no argument turns it on at the default level |
| `/lean-review [file]` | Delete-list of token waste in a reply, draft or file |
| `/lean-audit` | Token cost of always-loaded context (CLAUDE.md, rules, descriptions) |
| `/lean-compress <file>` | Trim a prompt/skill/doc to `*.lean.*`, with a loss check |
| `/lean-gain` | Real usage from your Claude Code transcripts |
| `/lean-help` | Quick reference |

Default mode: `LEAN_DEFAULT_MODE` env var or `defaultMode` in `~/.config/lean-output/config.json` (`%APPDATA%\lean-output\config.json` on Windows). Default is `standard`. Say "full detail" to override for one turn.

## Cost of the plugin itself

Full ruleset once per session (about 400 tokens), then a one-line reminder per prompt (about 30 tokens). The audit script is a heuristic estimate, not a tokenizer.

## Honest numbers

None published. See [benchmarks/](benchmarks/) for an A/B method with a quality gate. `/lean-gain` reads actual `usage` fields from your transcripts.

## Other agents

`AGENTS.md`, `.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.github/copilot-instructions.md` carry the ruleset (instruction-only, no modes/hooks). Generated from `rules/core.md`: `node scripts/sync-rules.js` (`--check` in CI).

## Uninstall

Run `node scripts/uninstall.js` first (removes the mode flag and config), then `/plugin remove lean-output`.

## Development

```
node scripts/sync-rules.js && node tests/run.js
```

MIT.
"# lean-output" 
