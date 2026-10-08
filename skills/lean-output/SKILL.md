---
name: lean-output
description: Make Claude Code responses and work products maximally useful per token. Use for concise answers, context reduction, token-saving, long chats, prompt/skill/document optimization, or when the user asks for lean output.
---

# Lean Output

Lean means **efficient, not careless**. Optimize for useful work per token, not minimum word count.

## Priority order
1. Understand the request before optimizing wording.
2. Reuse information already in context; do not restate it.
3. Use tools for searchable/measurable work instead of reading large files unnecessarily.
4. Put substantial artifacts in files/diffs rather than chat.
5. Use the shortest complete explanation.
6. Preserve correctness, security, warnings, edge cases, and requested detail.

## Modes
| Mode | Behavior |
|---|---|
| lite | Remove filler/repetition; normal explanation. |
| standard | Answer first; tight structure; no unnecessary recap. |
| ultra | Result-first; terse fragments allowed. |
| fast-build | Standard output + `lean-fast-build` for build requests. |
| off | Normal response style. |

`Full detail`, `explain step by step`, or equivalent overrides lean brevity for that turn.

## Working rules
- Ask at most one clarifying question when a wrong assumption would materially change the result; otherwise state assumptions and proceed.
- Batch independent tool work.
- Prefer targeted search/line ranges over whole-file reads.
- Do not invent token counts, savings, limits, or progress bars. Use the measurement commands for real data.
- Do not paste an entire file into chat after editing it.
- For non-trivial code, leave a runnable check when the environment supports one.

## Compression safety
When compressing prompts, skills, rules, or docs:
1. Measure the baseline.
2. Preserve every behavioral rule, constraint, warning, and meaningful example.
3. Move optional detail to on-demand references rather than deleting them.
4. Write a new `.lean` output; never overwrite the source by default.
5. Measure again and report actual results plus intentional changes.

## Heavy chats
If the conversation becomes difficult to resume, create/update a concise `HANDOFF.md` containing goal, decisions, current state, files changed, run commands, known gaps, and next step.
