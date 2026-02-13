---
name: be-review-room-lobby-ssot
description: "Backend Room/Lobby SSOT review skill. Produces one SSOT report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: be-review-room-lobby-ssot
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Review only SSOT compliance for domain 'room_lobby'.
- Ensure a report file is created at the required output path.
- If the file is not created, report failure to the master.
