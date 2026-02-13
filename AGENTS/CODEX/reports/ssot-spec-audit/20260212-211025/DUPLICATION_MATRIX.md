# Duplication Matrix

| Task | Target | Agent | Status | Max Severity | Findings | Summary |
|---|---|---|---|---|---:|---|
| DUP-NORMATIVE | NORMATIVE_DUPLICATION | duplication-auditor | FAIL | high | 3 | Detected duplicated/conflicting normative rules across SSOT areas, including one high-severity conflict on UI message SSOT ownership/keyspace that creates mutually incompatible implementation guidance. |
| DUP-OWNERSHIP | OWNERSHIP_VIOLATION | duplication-auditor | FAIL | critical | 2 | Found 2 ownership violations in scope. A critical SSOT breach exists where Frontend docs redefine Product-owned UI copy SSOT, and additional cross-area ownership drift statements assign copy ownership to Frontend from Design/Frontend docs. |
| DUP-TERMINOLOGY | TERM_CONFLICT | duplication-auditor | FAIL | high | 2 | Detected 2 terminology issues in scope: 1 high-severity `PageRoute` definition conflict and 1 medium-severity route/state alias ambiguity (`ROOM_LIST`). |
