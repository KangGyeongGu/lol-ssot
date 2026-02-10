---
name: be-dev-game-lifecycle
description: "Backend dev skill. Implements a single task."
user-invocable: false
disable-model-invocation: false
context: fork
agent: be-dev-game-lifecycle
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Write the report in English to `.claude/reports/dev/be/RESULTS/<TASK_ID>.md`.
- If the file is not created, report failure to the master.
