---
name: fe-review
description: "Runs the frontend full review pipeline (SSOT + QUALITY split) and validates all report files."
user-invocable: true
disable-model-invocation: true
context: fork
agent: fe-review-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If .claude/reports/review/fe/full/active/ exists, move it to .claude/reports/review/fe/full/archive/<timestamp>/.
2. Ensure .claude/reports/review/fe/full/active/ exists (create as needed).
3. Call all frontend split review skills via SlashCommand:
   - /fe-review-api-ssot
   - /fe-review-api-quality
   - /fe-review-state-ssot
   - /fe-review-state-quality
   - /fe-review-routing-ssot
   - /fe-review-routing-quality
   - /fe-review-realtime-ssot
   - /fe-review-realtime-quality
   - /fe-review-quality-ssot
   - /fe-review-quality-quality
4. Verify all required report files exist in .claude/reports/review/fe/full/active/.
5. If any report is missing, rerun only the missing skills and stop.
6. Read only report files and consolidate per fe-review-master instructions.
