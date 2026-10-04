---
description: Review text (last reply, a draft, or a file) for token waste and hand back a delete-list
argument-hint: [file path, or blank for the last reply]
allowed-tools: Read, Bash
---

Review for token waste: $ARGUMENTS (if blank, your previous reply).

Output only a delete-list. One line per item: `"quoted fragment" -> cut | merge | shorten to "..."` plus est. tokens saved. End with total saved. Flag anything that looks removable but carries a real warning, edge case or number, and keep it. Produce the tightened version only if the user asks.
