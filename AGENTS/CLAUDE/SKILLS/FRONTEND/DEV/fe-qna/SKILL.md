---
name: fe-qna
description: "Frontend QnA skill. Answers questions without modifying code."
user-invocable: true
disable-model-invocation: false
context: fork
agent: fe-qna
allowed-tools: Read, Grep, Glob, Write, Bash
---
Workflow (Required)
1. Follow the fe-qna agent instructions exactly.
2. Do not modify code or configuration.
3. Read only the minimum files needed to answer.
