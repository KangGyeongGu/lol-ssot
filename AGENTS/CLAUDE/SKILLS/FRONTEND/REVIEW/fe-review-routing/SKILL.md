---
name: fe-review-routing
description: "Frontend domain review skill. Produces a report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: fe-review-routing
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Write the report in English to `.claude/reports/review/fe/routing_raw.md`.
- If the file is not created, report failure to the master.
