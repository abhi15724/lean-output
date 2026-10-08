---
description: Audit always-loaded Claude Code context and identify the highest-value token reductions.
allowed-tools: Read, Bash, Glob, Grep
---

# Lean Audit

Audit project/global always-loaded context: `CLAUDE.md`, `AGENTS.md`, `.claude/rules/`, command/skill descriptions, and agent descriptions.

1. Inventory candidate files and measure bytes.
2. Run `python ${CLAUDE_PLUGIN_ROOT}/skills/lean-output/scripts/token_audit.py <file>` on the largest candidates.
3. Rank waste by likely savings: duplicated rules, filler, repeated examples, stale content, and detail that belongs on demand.
4. Recommend at most 5 changes, highest value first.
5. Do not edit files unless the user explicitly asks for remediation.

Never call a heuristic estimate an exact token count.
