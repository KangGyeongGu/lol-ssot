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
1. Delete and recreate `.claude/reports/review/be/`.
2. Call all backend review skills via SlashCommand:
   - /be-review-auth-user
   - /be-review-room-lobby
   - /be-review-game-lifecycle
   - /be-review-ban-pick-shop
   - /be-review-realtime
   - /be-review-redis
   - /be-review-jpa-db
   - /be-review-core-infra
3. Verify all required report files exist.
4. If any are missing, rerun the missing skills and stop.
5. Read only report files and consolidate per the master agent instructions.
