---
name: be-review-game-lifecycle
description: "Backend domain review skill. Produces a report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: be-review-game-lifecycle
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Write the report in English to `.claude/reports/review/be/game_lifecycle_raw.md`.
- If the file is not created, report failure to the master.
