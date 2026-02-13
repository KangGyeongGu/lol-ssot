---
name: ssot-spec-audit
description: Run a multi-agent SSOT consistency audit by orchestrating multiple Codex worker contexts in parallel. Use when you need area-level validation, cross-area relation checks, duplication/conflict detection, agent-skill wiring checks, and consolidated severity-gated reports.
---

# SSOT Spec Audit

## Overview

Run one command that fans out into multiple Codex worker executions (`codex exec`) and aggregates results.

Worker groups:
- Area auditors (`01_PRODUCT` to `06_BACKEND`)
- Relation auditors (area-to-area required relationships)
- Duplication auditors (duplicate/conflicting norms and ownership violations)
- Agent-spec auditors (agent/skill role, mapping, reference completeness)
- Traceability auditor (end-to-end requirement traceability)

## Run

Default (recommended):

```bash
python3 AGENTS/CODEX/SKILLS/ssot-spec-audit/scripts/run_ssot_audit.py
```

Options:

```bash
# full mode (default)
python3 AGENTS/CODEX/SKILLS/ssot-spec-audit/scripts/run_ssot_audit.py -- --mode full

# partial mode using changed files list
python3 AGENTS/CODEX/SKILLS/ssot-spec-audit/scripts/run_ssot_audit.py -- \
  --mode partial \
  --changed-files-list .tmp/changed_files.txt

# strict gate (fail on medium+)
python3 AGENTS/CODEX/SKILLS/ssot-spec-audit/scripts/run_ssot_audit.py -- --fail-on medium

# smoke test without codex workers
python3 AGENTS/CODEX/SKILLS/ssot-spec-audit/scripts/run_ssot_audit.py -- --dry-run

# keep legacy summary/matrix files (optional)
python3 AGENTS/CODEX/SKILLS/ssot-spec-audit/scripts/run_ssot_audit.py --keep-aux-files -- --mode full
```

## Outputs

Default output directory:

```text
AGENTS/CODEX/reports/ssot-spec-audit/<timestamp>/
```

Primary human-readable output:
- `REPORT.md`: consolidated report with per-finding
  - 원인
  - 원인이라고 판단한 이유
  - 구체적인 수정 제안

Machine/audit artifacts kept:
- `RUN_CONTEXT.json`: run metadata and plan summary
- `requests/*.request.json`: worker input payloads
- `prompts/*.prompt.md`: rendered worker prompts
- `worker_results/*.json`: worker output payloads
- `logs/*.stdout.log`, `logs/*.stderr.log`: worker execution logs
- `final_report.json`: aggregated machine-readable report

By default, legacy human-check files are removed after `REPORT.md` is generated:
- `SUMMARY.md`, `TOP_FINDINGS.md`, `*_MATRIX.md`, `*_MATRIX.csv`

Use `--keep-aux-files` to retain them.

## Interpretation Rules

Use these severity buckets:
- `critical`: mandatory SSOT relation/reference failure
- `high`: wiring/mapping inconsistency or blocking spec conflict
- `medium`: relation drift, traceability gap, ambiguous ownership
- `low`: minor quality/documentation weakness

Default gate exits non-zero when findings meet/exceed `--fail-on` (`high` by default).

## References

Read these before changing orchestration or policy:
- `references/audit-rules.md`
- `references/multi-agent-system.md`
- `schemas/worker_request.schema.json`
- `schemas/worker_result.schema.json`
- `schemas/final_report.schema.json`
