# Relation Matrix

| Task | Target | Agent | Status | Max Severity | Findings | Summary |
|---|---|---|---|---|---:|---|
| REL-API-BACKEND | API_BACKEND | relation-auditor | PASS | low | 0 | Backend API/realtime implementation-rule documents consistently reference `03_API` as contract SSOT, and no API↔backend rule conflicts or relation-level duplication were found within the scoped paths. |
| REL-API-FRONTEND | API_FRONTEND | relation-auditor | FAIL | high | 2 | Frontend routing SSOT drifts from API contract SSOT on PageRoute usage: FE rules currently include non-contract route values as PageRoute and overgeneralize pageRoute-driven transitions. |
| REL-DESIGN-FRONTEND | DESIGN_FRONTEND | relation-auditor | WARN | medium | 2 | Frontend documents correctly reference design token and page-requirement sources, but two medium relation-drift issues remain around ownership and scope clarity between design requirements and frontend consumption rules. |
| REL-DOMAIN-API | DOMAIN_API | relation-auditor | WARN | medium | 2 | Found 2 medium DOMAIN_API consistency issues: one-way cross-area references (DOMAIN->API only) and a stage mapping drift in ROOM_GAME_STARTED. |
| REL-DOMAIN-BACKEND | DOMAIN_BACKEND | relation-auditor | FAIL | high | 1 | Found a high-severity domain-to-backend mapping mismatch: backend write-back timing rule does not preserve the domain SSOT’s per-entity timing requirements. |
| REL-PRODUCT-API | PRODUCT_API | relation-auditor | FAIL | high | 2 | Found 2 PRODUCT_API relation issues: 1 high mapping conflict in lifecycle REST routing and 1 medium requirement-to-contract traceability gap. |
| REL-PRODUCT-DESIGN | PRODUCT_DESIGN | relation-auditor | FAIL | critical | 3 | Detected PRODUCT_DESIGN SSOT relation failures: direct cross-area references are missing, intent-to-design mapping is implicit, and behavioral rules are duplicated across Product and Design without explicit ownership links. |
