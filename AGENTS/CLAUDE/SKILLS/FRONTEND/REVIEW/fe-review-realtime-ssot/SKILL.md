---
name: fe-review-realtime-ssot
description: "Frontend Realtime SSOT review skill. Produces one SSOT report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: fe-review-realtime-ssot
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Review only SSOT compliance for domain 'realtime'.
- Ensure a report file is created at the required output path.
- If the file is not created, report failure to the master.
