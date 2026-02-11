---
name: commit-plan
description: "Plans a commit based on git status/diff, requests approval, commits, and optionally pushes."
user-invocable: true
disable-model-invocation: false
context: fork
agent: commit-agent
allowed-tools: Bash, Read, Write, Glob
---
Workflow (Required)
1. Run `git status --porcelain`.
   - If no changes, report to the user and stop.
2. Run `git diff --stat` and `git diff --name-only` for an overview.
3. If staged changes exist, also run `git diff --cached --stat`.
4. Check `.claude/reports/` for recent review/dev summaries and use them to draft a commit plan.
5. Present a concise change summary and propose 1-3 commit message candidates (Korean).
6. Ask the user to approve committing. If approved, confirm the final commit message.
   - If the message contains `Co-authored-by` or similar, remove it and confirm the sanitized message.
7. Ask whether to commit all changes or a specified subset of files.
8. Stage files using `git add` (all or selected).
9. Run `git commit -m "<message>"`.
10. Ask whether to push.
    - If approved, run `git push`.
    - If not approved, stop.
