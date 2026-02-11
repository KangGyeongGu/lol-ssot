---
name: fe-dev-partial
description: "Runs the frontend partial dev pipeline based on partial review task cards."
user-invocable: true
disable-model-invocation: false
context: fork
agent: fe-dev-partial-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If `.claude/reports/dev/fe/partial/active/` exists, move it to `.claude/reports/dev/fe/partial/archive/<timestamp>/`.
2. Ensure `.claude/reports/dev/fe/partial/active/` exists (create as needed).
3. Ensure `.claude/reports/dev/fe/partial/active/RESULTS/` exists.
4. Verify `.claude/reports/review/fe/partial/active/MASTER_PLAN.md` and `.claude/reports/review/fe/partial/active/TASKS/` exist.
5. For each task card, select the appropriate dev skill by DOMAIN.
6. Call the dev skill via SlashCommand and provide the output path `.claude/reports/dev/fe/partial/active/RESULTS/<TASK_ID>.md`.
7. After all tasks, write `.claude/reports/dev/fe/partial/active/DEV_SUMMARY.md` in English.
