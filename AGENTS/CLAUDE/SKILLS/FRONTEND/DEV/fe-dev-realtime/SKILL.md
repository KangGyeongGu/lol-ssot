---
name: fe-dev-realtime
description: "Frontend dev skill. Implements a single task."
user-invocable: false
disable-model-invocation: false
context: fork
agent: fe-dev-realtime
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Write the report in English to `.claude/reports/dev/fe/RESULTS/<TASK_ID>.md`.
- If the file is not created, report failure to the master.
