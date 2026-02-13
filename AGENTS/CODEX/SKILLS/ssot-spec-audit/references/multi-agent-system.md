# Multi-Agent System Design

## Agent Inventory

| agent_id | target kind | fan-out |
|---|---|---:|
| area-auditor | area | 6 |
| relation-auditor | relation | 7 |
| duplication-auditor | duplication | 3 |
| agent-spec-auditor | agent_spec | 2 |
| traceability-auditor | traceability | 1 |
| aggregator (orchestrator internal) | all | 1 |
| gatekeeper (orchestrator internal) | all | 1 |

## Execution Sequence

```mermaid
flowchart TD
  U[User] --> O[orchestrate_multi_agent_audit.py]
  O --> Q[Build task queue]
  Q --> A1[area-auditor workers x6]
  Q --> A2[relation-auditor workers x7]
  Q --> A3[duplication-auditor workers x3]
  Q --> A4[agent-spec-auditor workers x2]
  Q --> A5[traceability-auditor worker x1]
  A1 --> R[worker_results/*.json]
  A2 --> R
  A3 --> R
  A4 --> R
  A5 --> R
  R --> G[Aggregator]
  G --> M[Matrix files + final_report.json]
  M --> K[Gatekeeper fail_on]
  K --> S[SUMMARY.md]
```

## Contracts

- worker request schema: `schemas/worker_request.schema.json`
- worker result schema: `schemas/worker_result.schema.json`
- final report schema: `schemas/final_report.schema.json`

## Notes

- Worker context isolation is process-level isolation via parallel `codex exec` calls.
- The orchestrator writes prompts and request payloads for reproducibility.
- Partial mode reduces fan-out based on changed file path hints.
