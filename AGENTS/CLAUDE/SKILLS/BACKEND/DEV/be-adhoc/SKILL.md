---
name: be-adhoc
description: "Runs a backend ad-hoc fix based on a user prompt."
user-invocable: true
disable-model-invocation: false
context: fork
agent: be-dev-adhoc
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If `.claude/reports/dev/be/adhoc/active/` exists, move it to `.claude/reports/dev/be/adhoc/archive/<timestamp>/`.
2. Ensure `.claude/reports/dev/be/adhoc/active/` exists (create as needed).
3. Follow the be-dev-adhoc instructions exactly.
4. Ensure `.claude/reports/dev/be/adhoc/active/RESULTS/` exists.
5. Determine the target domain from the user prompt. Ask for clarification if unclear.
6. Create a single TASK_ID and call the mapped dev skill.
7. Provide the output path `.claude/reports/dev/be/adhoc/active/RESULTS/<TASK_ID>.md` to the dev skill.
8. Write `.claude/reports/dev/be/adhoc/active/DEV_SUMMARY.md` in English.
