---
name: fe-dev
description: "Runs the frontend dev pipeline based on review task cards."
user-invocable: true
disable-model-invocation: false
context: fork
agent: fe-dev-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If `.claude/reports/dev/fe/full/active/` exists, move it to `.claude/reports/dev/fe/full/archive/<timestamp>/`.
2. Ensure `.claude/reports/dev/fe/full/active/` exists (create as needed).
3. Ensure `.claude/reports/dev/fe/full/active/RESULTS/` exists (create as needed).
4. Verify `.claude/reports/review/fe/full/active/MASTER_PLAN.md` and `.claude/reports/review/fe/full/active/TASKS/` exist.
5. For each task card, select the appropriate dev skill by DOMAIN.
6. Call the dev skill via SlashCommand, passing one task card at a time.
7. After all tasks, write `.claude/reports/dev/fe/full/active/DEV_SUMMARY.md` in English.
