---
name: fe-review-partial
description: "Runs the frontend partial review pipeline (SSOT + QUALITY split) based on SSOT commit logs."
user-invocable: true
disable-model-invocation: true
context: fork
agent: fe-review-partial-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If .claude/reports/review/fe/partial/active/ exists, move it to .claude/reports/review/fe/partial/archive/<timestamp>/.
2. Ensure .claude/reports/review/fe/partial/active/ exists (create as needed).
3. Follow fe-review-partial-master instructions exactly.
4. Use Bash to read latest SSOT submodule commit from ../docs and validate partial commit convention.
5. If commit scope is unclear or domains are missing, stop and request user confirmation.
6. For each confirmed domain, call both domain review skills (SSOT + QUALITY).
7. Ensure each domain writes two reports:
   - .claude/reports/review/fe/partial/active/<domain>_ssot_raw.md
   - .claude/reports/review/fe/partial/active/<domain>_quality_raw.md
8. Verify all expected report files exist before proceeding.
9. Produce MASTER_PLAN.md and TASKS/TASK-XXX.md in .claude/reports/review/fe/partial/active/ and request approval.
