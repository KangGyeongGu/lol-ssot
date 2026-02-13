---
name: fe-review-api-ssot
description: "Frontend API SSOT review skill. Produces one SSOT report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: fe-review-api-ssot
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Review only SSOT compliance for domain 'api'.
- Ensure a report file is created at the required output path.
- If the file is not created, report failure to the master.
