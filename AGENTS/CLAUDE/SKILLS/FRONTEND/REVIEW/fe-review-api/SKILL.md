---
name: fe-review-api
description: "Frontend domain review skill. Produces a report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: fe-review-api
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Ensure the report file is created at the output path required by the agent.
- If the file is not created, report failure to the master.
