---
name: be-review-ban-pick-shop
description: "Backend domain review skill. Produces a report file."
user-invocable: false
disable-model-invocation: false
context: fork
agent: be-review-ban-pick-shop
allowed-tools: Read, Grep, Glob, Write, Bash
---
Instructions
- Follow the assigned agent instructions.
- Write the report in English to `.claude/reports/review/be/ban_pick_shop_raw.md`.
- If the file is not created, report failure to the master.
