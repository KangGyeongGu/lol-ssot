---
name: fe-review-routing-quality
description: "Frontend Routing quality review skill. Produces one quality report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: fe-review-routing-quality
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Review only code quality for domain 'routing'.
- Do not rely on SSOT raw reports produced by other subagents.
- Ensure a report file is created at the required output path.
- If the file is not created, report failure to the master.
