---
name: be-dev-room-lobby
description: "Backend dev skill. Implements a single task."
user-invocable: false
disable-model-invocation: false
context: fork
agent: be-dev-room-lobby
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Ensure the result file is created at the output path required by the agent.
- If the file is not created, report failure to the master.
