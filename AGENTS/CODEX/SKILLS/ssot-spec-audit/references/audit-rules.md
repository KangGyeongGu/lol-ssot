# Audit Rules

## Multi-Agent Scope

One orchestrator run dispatches multiple worker contexts.

1. `area-auditor`
- targets: `01_PRODUCT`, `02_DESIGN`, `03_API`, `04_DOMAIN`, `05_FRONTEND`, `06_BACKEND`
- checks: required docs, link integrity, area boundary ownership, intra-area consistency

2. `relation-auditor`
- targets: PRODUCT_DESIGN, PRODUCT_API, DESIGN_FRONTEND, API_FRONTEND, API_BACKEND, DOMAIN_API, DOMAIN_BACKEND
- checks: required relationship presence, reference directionality, relation-level duplication/conflict

3. `duplication-auditor`
- targets: NORMATIVE_DUPLICATION, TERM_CONFLICT, OWNERSHIP_VIOLATION
- checks: duplicated/contradictory rules, conflicting glossary terms, SSOT ownership violations

4. `agent-spec-auditor`
- targets: backend and frontend agent/skill trees
- checks: role scope completeness, mapping completeness, reference existence, master/subskill wiring

5. `traceability-auditor`
- target: E2E_TRACEABILITY
- checks: Product -> Design -> API -> Domain -> FE/BE trace chain and orphan spec detection

## Severity Policy

- `critical`
  - mandatory relation/reference absent
  - source-of-truth ownership violated with blocking impact
- `high`
  - mapping/wiring mismatch that breaks orchestration expectations
  - conflicting normative statements requiring immediate reconciliation
- `medium`
  - relation drift, traceability gaps, ambiguous cross-area ownership
- `low`
  - minor document quality issues with low execution risk

## Gate Policy

- final status is `fail` if any finding meets/exceeds `--fail-on`
- final status is `warn` if findings exist below threshold
- final status is `pass` when no findings exist

## Output Contract

Each run must emit:
- `RUN_CONTEXT.json`
- `requests/*.request.json`
- `prompts/*.prompt.md`
- `worker_results/*.json`
- `logs/*.stdout.log`, `logs/*.stderr.log`
- `final_report.json`
- `SUMMARY.md`
- `AREA_MATRIX.md`
- `RELATION_MATRIX.md`
- `DUPLICATION_MATRIX.md`
- `AGENT_SPEC_MATRIX.md`
- `TRACEABILITY_MATRIX.md`
- `TOP_FINDINGS.md`

Default output path:
- `AGENTS/CODEX/reports/ssot-spec-audit/<timestamp>/`
