---
description: Review a response or file for unnecessary verbosity and return a precise delete/merge/shorten list.
argument-hint: file path, or blank for the previous reply
allowed-tools: Read, Bash
---

Review: $ARGUMENTS

Output only actionable edits, one per line:
`"fragment" -> cut | merge | shorten to "..."`

Keep warnings, constraints, numbers, and edge cases that materially affect the result. Include a savings estimate only when measured; otherwise omit it. Produce a rewritten version only when requested.
