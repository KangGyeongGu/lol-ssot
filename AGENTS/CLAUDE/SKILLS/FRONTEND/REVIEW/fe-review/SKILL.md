---
name: fe-review
description: "Runs the frontend review pipeline and validates report files."
user-invocable: true
disable-model-invocation: true
context: fork
agent: fe-review-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If `.claude/reports/review/fe/full/active/` exists, move it to `.claude/reports/review/fe/full/archive/<timestamp>/`.
2. Ensure `.claude/reports/review/fe/full/active/` exists (create as needed).
3. Call all frontend review skills via SlashCommand:
   - /fe-review-api
   - /fe-review-state
   - /fe-review-routing
   - /fe-review-realtime
   - /fe-review-quality
4. Verify all required report files exist in `.claude/reports/review/fe/full/active/`.
5. If any are missing, rerun the missing skills and stop.
6. Read only report files and consolidate per the master agent instructions.
