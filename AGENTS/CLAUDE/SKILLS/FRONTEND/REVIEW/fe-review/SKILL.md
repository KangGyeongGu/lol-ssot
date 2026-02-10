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
1. Delete and recreate `.claude/reports/review/fe/`.
2. Call all frontend review skills via SlashCommand:
   - /fe-review-api
   - /fe-review-state
   - /fe-review-routing
   - /fe-review-realtime
   - /fe-review-quality
3. Verify all required report files exist.
4. If any are missing, rerun the missing skills and stop.
5. Read only report files and consolidate per the master agent instructions.
