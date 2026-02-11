---
name: fe-review-partial
description: "Runs the frontend partial review pipeline based on SSOT commit logs."
user-invocable: true
disable-model-invocation: true
context: fork
agent: fe-review-partial-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If `.claude/reports/review/fe/partial/active/` exists, move it to `.claude/reports/review/fe/partial/archive/<timestamp>/`.
2. Ensure `.claude/reports/review/fe/partial/active/` exists (create as needed).
3. Follow the fe-review-partial-master instructions exactly.
4. Use Bash to read the latest SSOT submodule commit from `../docs` and validate the partial commit convention.
5. If the commit scope is unclear or missing domains, stop and request user confirmation.
6. Call only the domain review skills required by the confirmed scope.
7. Ensure each domain report is written to `.claude/reports/review/fe/partial/active/<domain>_raw.md`.
8. Verify all expected report files exist before proceeding.
9. Produce `MASTER_PLAN.md` and `TASKS/TASK-XXX.md` in `.claude/reports/review/fe/partial/active/` and request approval.
