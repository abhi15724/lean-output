---
description: Audit always-loaded context (CLAUDE.md, rules, skill descriptions, commands) for token cost
allowed-tools: Read, Bash, Glob, Grep
---

Audit what loads on every session in this project and globally: `CLAUDE.md` (project and `~/.claude/`), `AGENTS.md`, `.claude/rules/`, skill and command descriptions, agent descriptions.

1. List each file with size: `wc -c`.
2. Run `python ${CLAUDE_PLUGIN_ROOT}/skills/lean-output/scripts/token_audit.py <file>` on the largest ones.
3. Report a ranked table: file, ~tokens, biggest waste (duplicate rules, filler, long examples, content that belongs in an on-demand file).
4. Recommend at most 5 changes, highest saving first. Do not edit anything.
