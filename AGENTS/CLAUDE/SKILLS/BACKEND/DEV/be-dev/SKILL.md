---
name: be-dev
description: "Runs the backend dev pipeline based on review task cards."
user-invocable: true
disable-model-invocation: true
context: fork
agent: be-dev-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. Delete and recreate `.claude/reports/dev/be/`.
2. Verify `.claude/reports/review/be/MASTER_PLAN.md` and `.claude/reports/review/be/TASKS/` exist.
3. For each task card, select the appropriate dev skill by DOMAIN.
4. Call the dev skill via SlashCommand, passing one task card at a time.
5. After all tasks, write `.claude/reports/dev/be/DEV_SUMMARY.md` in English.
