---
name: be-review
description: "Runs the backend review pipeline and validates report files."
user-invocable: true
disable-model-invocation: true
context: fork
agent: be-review-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If `.claude/reports/review/be/full/active/` exists, move it to `.claude/reports/review/be/full/archive/<timestamp>/`.
2. Ensure `.claude/reports/review/be/full/active/` exists (create as needed).
3. Call all backend review skills via SlashCommand:
   - /be-review-auth-user
   - /be-review-room-lobby
   - /be-review-game-lifecycle
   - /be-review-ban-pick-shop
   - /be-review-realtime
   - /be-review-redis
   - /be-review-jpa-db
   - /be-review-core-infra
4. Verify all required report files exist in `.claude/reports/review/be/full/active/`.
5. If any are missing, rerun the missing skills and stop.
6. Read only report files and consolidate per the master agent instructions.
