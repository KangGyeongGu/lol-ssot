---
name: be-review
description: "Runs the backend full review pipeline (SSOT + QUALITY split) and validates all report files."
user-invocable: true
disable-model-invocation: true
context: fork
agent: be-review-master
allowed-tools: SlashCommand, Read, Write, Glob, Bash
---
Workflow (Required)
1. If .claude/reports/review/be/full/active/ exists, move it to .claude/reports/review/be/full/archive/<timestamp>/.
2. Ensure .claude/reports/review/be/full/active/ exists (create as needed).
3. Call all backend split review skills via SlashCommand:
   - /be-review-auth-user-ssot
   - /be-review-auth-user-quality
   - /be-review-room-lobby-ssot
   - /be-review-room-lobby-quality
   - /be-review-game-lifecycle-ssot
   - /be-review-game-lifecycle-quality
   - /be-review-ban-pick-shop-ssot
   - /be-review-ban-pick-shop-quality
   - /be-review-realtime-ssot
   - /be-review-realtime-quality
   - /be-review-redis-ssot
   - /be-review-redis-quality
   - /be-review-jpa-db-ssot
   - /be-review-jpa-db-quality
   - /be-review-core-infra-ssot
   - /be-review-core-infra-quality
4. Verify all required report files exist in .claude/reports/review/be/full/active/.
5. If any report is missing, rerun only the missing skills and stop.
6. Read only report files and consolidate per be-review-master instructions.
