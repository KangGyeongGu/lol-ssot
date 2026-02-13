# Top Findings

1. [CRITICAL] `REL-PRODUCT-DESIGN` `relation/PRODUCT_DESIGN` REL_MISSING_MANDATORY_CROSS_REF - Mandatory PRODUCT_DESIGN relationship is not explicitly documented: Product core requirements only reference Product docs, while Design requirements reference API docs only and omit Product sources.
- evidence: `01_PRODUCT/REQUIREMENTS.md:5`
- evidence: `01_PRODUCT/REQUIREMENTS.md:6`
- evidence: `02_DESIGN/README.md:28`
2. [CRITICAL] `DUP-OWNERSHIP` `duplication/OWNERSHIP_VIOLATION` source_of_truth_violation.copy_ssot_redefined - `05_FRONTEND/FE_NOTIFICATION_MESSAGES.md` redefines Product-owned UI copy by declaring itself the single document for message keys/Korean text and providing canonical copy mappings, while Product explicitly owns UI copy SSOT in `01_PRODUCT/COPY_TEXT.md`.
- evidence: `01_PRODUCT/README.md:6`
- evidence: `01_PRODUCT/COPY_TEXT.md:2`
- evidence: `05_FRONTEND/FE_NOTIFICATION_MESSAGES.md:2`
3. [CRITICAL] `TRACE-E2E` `traceability/E2E_TRACEABILITY` TRACE_REQ_DESIGN_MANDATORY_LINK_MISSING - The requirement-to-design segment is missing explicit mandatory references: Product requirement sources link only within `01_PRODUCT`, while Design page requirements link directly to API docs, leaving the `requirement -> design -> api` chain non-deterministic.
- evidence: `01_PRODUCT/REQUIREMENTS.md:5`
- evidence: `01_PRODUCT/REQUIREMENTS.md:6`
- evidence: `01_PRODUCT/USER_FLOWS.md:7`
4. [HIGH] `AREA-05_FRONTEND` `area/05_FRONTEND` ROUTING_PAGE_ROUTE_CONTRACT_MISMATCH - Frontend routing rules treat multiple app routes as API `PageRoute` values, but upstream REST conventions restrict `PageRoute` to three values (`WAITING_ROOM`, `BAN_PICK_SHOP`, `IN_GAME`), creating a routing/API contract mismatch.
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:14`
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:16`
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:27`
5. [HIGH] `REL-API-FRONTEND` `relation/API_FRONTEND` PAGE_ROUTE_ENUM_MISMATCH - `05_FRONTEND` routing rules redefine `PageRoute` with values outside the API contract (`WELCOME`, `MAIN`, `RESULT`, `MY_PAGE`), conflicting with API SSOT enum constraints.
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:14`
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:16`
- evidence: `03_API/CONTRACT/REST/CONVENTIONS.md:137`
6. [HIGH] `REL-DOMAIN-BACKEND` `relation/DOMAIN_BACKEND` DOMAIN_BACKEND_WRITE_POLICY_TIMING_MISMATCH - `06_BACKEND/BE_DATA_MODEL_RULES.md` defines write-back persistence timing as a single rule (`GAME_FINISHED` or room/game end), but domain SSOT requires different timing by entity group (ROOM* at `startGame`, GAME* at `GAME_FINISHED`). This can cause backend orchestration/persistence behavior to diverge from domain SSOT.
- evidence: `06_BACKEND/BE_DATA_MODEL_RULES.md:19`
- evidence: `04_DOMAIN/DATA_MODEL.md:58`
- evidence: `04_DOMAIN/DATA_MODEL.md:62`
7. [HIGH] `REL-PRODUCT-API` `relation/PRODUCT_API` LIFECYCLE_BAN_PICK_ENDPOINT_CONFLICT - `03_API/LIFECYCLE.md` has conflicting REST mappings for BAN/PICK/SHOP. Section 3.3 lists distinct endpoints (`/ban`, `/pick`, `/shop/purchase`), but section 5.3 maps BAN/PICK/SHOP to only `/shop/purchase`, which can miswire client orchestration against product flow and page-map contracts.
- evidence: `03_API/LIFECYCLE.md:73`
- evidence: `03_API/LIFECYCLE.md:137`
- evidence: `03_API/PAGE_MAP/BAN_PICK_SHOP.md:23`
8. [HIGH] `DUP-NORMATIVE` `duplication/NORMATIVE_DUPLICATION` NORMATIVE_CONFLICT_UI_MESSAGE_SSOT - UI message source-of-truth rules conflict across PRODUCT and FRONTEND: one rule requires all UI text to come from COPY_TEXT keys, while another defines a separate notification-message SSOT with ERROR/NOTICE keyspace and localized text in FRONTEND docs.
- evidence: `01_PRODUCT/COPY_TEXT.md:2`
- evidence: `05_FRONTEND/FE_CONVENTIONS.md:54`
- evidence: `05_FRONTEND/FE_API_CLIENT.md:34`
9. [HIGH] `DUP-TERMINOLOGY` `duplication/TERM_CONFLICT` TERM_DEFINITION_CONFLICT_PAGEROUTE - `PageRoute` has conflicting definitions across SSOT areas. API contracts define it as a 3-value active-game routing enum, while frontend routing rules redefine/expand it as general app routes (`WELCOME`, `MAIN`, `RESULT`, `MY_PAGE`, etc.) and require route naming to match `PageRoute`.
- evidence: `03_API/CONTRACT/REST/CONVENTIONS.md:137`
- evidence: `03_API/CONTRACT/REST/OPENAPI.yaml.md:131`
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:14`
10. [HIGH] `AGENTSPEC-BACKEND` `agent_spec/BACKEND_AGENT_SKILL` required_reference_existence.partial_review_docs_path_missing - Partial review orchestration requires reading the latest SSOT commit from `../docs`, but that path is absent in this repository environment, creating a blocking wiring dependency for `/be-review-partial`.
- evidence: `AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/BE_REVIEW_PARTIAL_MASTER_AGENT.md:15`
- evidence: `AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-partial/SKILL.md:14`
- evidence: `../docs`
11. [HIGH] `TRACE-E2E` `traceability/E2E_TRACEABILITY` TRACE_API_BAN_PICK_SHOP_MAPPING_CONFLICT - API lifecycle documentation contains conflicting BAN/PICK/SHOP REST mappings, which can miswire requirement/design-driven orchestration.
- evidence: `03_API/LIFECYCLE.md:73`
- evidence: `03_API/LIFECYCLE.md:137`
- evidence: `03_API/PAGE_MAP/BAN_PICK_SHOP.md:23`
12. [HIGH] `TRACE-E2E` `traceability/E2E_TRACEABILITY` TRACE_DOMAIN_BACKEND_WRITE_POLICY_TIMING_MISMATCH - The requirement-to-domain-to-backend chain is inconsistent for write-back timing: backend rule text allows a broad end-of-room/game flush, while domain SSOT requires phase-specific timing by entity group.
- evidence: `06_BACKEND/BE_DATA_MODEL_RULES.md:19`
- evidence: `04_DOMAIN/DATA_MODEL.md:58`
- evidence: `04_DOMAIN/DATA_MODEL.md:62`
13. [HIGH] `TRACE-E2E` `traceability/E2E_TRACEABILITY` TRACE_API_FRONTEND_PAGEROUTE_ENUM_MISMATCH - Frontend routing rules redefine API `PageRoute` scope, breaking API-to-frontend traceability for active-game routing decisions required by product flow.
- evidence: `01_PRODUCT/USER_FLOWS.md:37`
- evidence: `03_API/CONTRACT/REST/CONVENTIONS.md:137`
- evidence: `03_API/CONTRACT/REST/OPENAPI.yaml.md:131`
14. [MEDIUM] `AREA-02_DESIGN` `area/02_DESIGN` SSOT_SCOPE_BOUNDARY_LAYOUT_RULE - WAITING_ROOM page requirements define fixed grid placement rules, which conflicts with 02_DESIGN README scope that explicitly excludes layout/component positioning.
- evidence: `02_DESIGN/README.md:7`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/WAITING_ROOM.md:25`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/WAITING_ROOM.md:28`
15. [MEDIUM] `AREA-02_DESIGN` `area/02_DESIGN` REQUIRED_DOC_OWNERSHIP_AMBIGUITY - 02_DESIGN README lists FE_NOTIFICATION_MESSAGES.md inside the 02_DESIGN file structure, but the document is missing in this area, creating required-doc and ownership ambiguity.
- evidence: `02_DESIGN/README.md:24`
- evidence: `02_DESIGN/FE_NOTIFICATION_MESSAGES.md`
16. [MEDIUM] `AREA-03_API` `area/03_API` API_LIFECYCLE_ENDPOINT_DRIFT - `LIFECYCLE.md` collapses BAN/PICK/SHOP actions into only `/games/{gameId}/shop/purchase`, which drifts from the canonical REST contracts that define separate `/ban` and `/pick` endpoints.
- evidence: `03_API/LIFECYCLE.md:137`
- evidence: `03_API/CONTRACT/REST/API_SUMMARY.md:67`
- evidence: `03_API/CONTRACT/REST/API_SUMMARY.md:68`
17. [MEDIUM] `AREA-03_API` `area/03_API` API_TIME_SYNC_TRACEABILITY_GAP - `TIME_SYNC` on `/user/queue/time` is defined as a basic subscription in realtime contracts, but lifecycle diagrams and page-level subscription maps omit it, creating traceability drift for timing synchronization behavior.
- evidence: `03_API/LIFECYCLE.md:25`
- evidence: `03_API/LIFECYCLE.md:145`
- evidence: `03_API/LIFECYCLE.md:180`
18. [MEDIUM] `AREA-04_DOMAIN` `area/04_DOMAIN` DOMAIN_WRITE_POLICY_DRIFT - Persistent entities are defined with default write-through policy, but the Phase 2 timing table marks DB writes as "필요 시 write-through", creating ambiguous persistence semantics for runtime logs.
- evidence: `04_DOMAIN/DATA_MODEL.md:53`
- evidence: `04_DOMAIN/DB_NOTES.md:104`
- evidence: `04_DOMAIN/REDIS_DB_TIMING.md:27`
19. [MEDIUM] `AREA-05_FRONTEND` `area/05_FRONTEND` COPY_SSOT_OWNERSHIP_DRIFT - Frontend docs conflict on copy ownership: conventions/API client require UI copy keys from `01_PRODUCT/COPY_TEXT.md`, while notification rules define Korean copy text directly in `05_FRONTEND`, weakening SSOT ownership clarity.
- evidence: `05_FRONTEND/FE_CONVENTIONS.md:54`
- evidence: `05_FRONTEND/FE_API_CLIENT.md:34`
- evidence: `05_FRONTEND/README.md:30`
20. [MEDIUM] `AREA-06_BACKEND` `area/06_BACKEND` TEST_RULE_COVERAGE_GAP_WRITE_POLICY - Backend data write-policy SSOT rules (write-through/write-back and GAME_FINISHED/termination flush semantics) are defined but not explicitly reflected in backend test-rule coverage statements, reducing rule-to-test traceability.
- evidence: `06_BACKEND/BE_DATA_MODEL_RULES.md:17`
- evidence: `06_BACKEND/BE_DATA_MODEL_RULES.md:19`
- evidence: `06_BACKEND/BE_TEST_RULES.md:37`
21. [MEDIUM] `REL-API-FRONTEND` `relation/API_FRONTEND` PAGE_ROUTE_SCOPE_OVERGENERALIZATION - Frontend routing rule states transitions are only PageRoute-based/API `pageRoute`-based, but API SSOT defines non-pageRoute transition branches (e.g., login result and signup overlay), creating ambiguous contract usage boundaries.
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:26`
- evidence: `05_FRONTEND/FE_ROUTING_RULES.md:27`
- evidence: `03_API/PAGE_MAP/WELCOME.md:24`
22. [MEDIUM] `REL-DESIGN-FRONTEND` `relation/DESIGN_FRONTEND` SCOPE_OWNERSHIP_DRIFT_WAITING_ROOM_LAYOUT - `WAITING_ROOM` page requirements include fixed player-grid placement rules, but both design and frontend area scopes exclude layout/component positioning. This creates ambiguous ownership for rules frontend is expected to consume.
- evidence: `02_DESIGN/README.md:3`
- evidence: `02_DESIGN/README.md:7`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/WAITING_ROOM.md:25`
23. [MEDIUM] `REL-DESIGN-FRONTEND` `relation/DESIGN_FRONTEND` NOTIFICATION_DOC_OWNERSHIP_DRIFT - Design declares `FE_NOTIFICATION_MESSAGES.md` inside `02_DESIGN/PAGE_REQUIREMENTS`, but the actual notification SSOT lives in `05_FRONTEND`. This creates cross-area ownership drift for page-level notification requirements.
- evidence: `02_DESIGN/README.md:24`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/FE_NOTIFICATION_MESSAGES.md`
- evidence: `05_FRONTEND/FE_NOTIFICATION_MESSAGES.md:2`
24. [MEDIUM] `REL-DOMAIN-API` `relation/DOMAIN_API` REL_REQUIRED_LINK_PRESENCE_GAP - DOMAIN documents reference API contracts, but API contract docs do not reference DOMAIN SSOT docs, leaving DOMAIN_API traceability one-directional.
- evidence: `04_DOMAIN/DATA_MODEL.md:12`
- evidence: `04_DOMAIN/REDIS_DB_TIMING.md:8`
- evidence: `03_API/CONTRACT/REST/OPENAPI.yaml.md:30`
25. [MEDIUM] `REL-DOMAIN-API` `relation/DOMAIN_API` ENTITY_CONTRACT_STAGE_MAPPING_DRIFT - `ROOM_GAME_STARTED` event allows `PICK`/`SHOP` stages, but the domain transition model defines game start as `BAN` (RANKED) or `PLAY` (NORMAL), creating ambiguous Domain<->API stage semantics.
- evidence: `04_DOMAIN/DATA_MODEL.md:674`
- evidence: `04_DOMAIN/DATA_MODEL.md:675`
- evidence: `03_API/CONTRACT/REALTIME/EVENTS.md:187`
26. [MEDIUM] `REL-PRODUCT-API` `relation/PRODUCT_API` PRODUCT_REQUIREMENT_TO_API_LINK_GAP - Product requirement documents reference API conceptually but do not provide explicit links to concrete API contracts, leaving requirement-to-contract traceability weak and audit mapping ambiguous.
- evidence: `01_PRODUCT/USER_FLOWS.md:4`
- evidence: `01_PRODUCT/USER_FLOWS.md:8`
- evidence: `01_PRODUCT/REQUIREMENTS.md:6`
27. [MEDIUM] `REL-PRODUCT-DESIGN` `relation/PRODUCT_DESIGN` REL_INTENT_TO_DESIGN_MAPPING_IMPLICIT - Design page requirements are organized by page but do not map each requirement block to specific Product intent clauses, reducing traceability and making drift detection difficult.
- evidence: `01_PRODUCT/REQUIREMENTS.md:100`
- evidence: `01_PRODUCT/USER_FLOWS.md:15`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/WAITING_ROOM.md:4`
28. [MEDIUM] `REL-PRODUCT-DESIGN` `relation/PRODUCT_DESIGN` REL_DUPLICATED_BEHAVIORAL_RULES - Behavioral norms are duplicated between Product and Design documents without explicit derivation links, creating non-SSOT duplication and future conflict risk.
- evidence: `01_PRODUCT/REQUIREMENTS.md:95`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/BAN_PICK_SHOP.md:29`
- evidence: `01_PRODUCT/REQUIREMENTS.md:73`
29. [MEDIUM] `DUP-NORMATIVE` `duplication/NORMATIVE_DUPLICATION` NORMATIVE_CONFLICT_WRITEBACK_TIMING - Write-back timing guidance is internally conflicting for ROOM* entities: some docs require game-start DB flush, while DB_NOTES states write-back as end-of-game reflection.
- evidence: `04_DOMAIN/DATA_MODEL.md:58`
- evidence: `04_DOMAIN/DATA_MODEL.md:60`
- evidence: `04_DOMAIN/REDIS_DB_TIMING.md:26`
30. [MEDIUM] `DUP-OWNERSHIP` `duplication/OWNERSHIP_VIOLATION` cross_area_redefinition.copy_ownership_drift - Design page requirement docs and Frontend state rules repeatedly state that alert copy is managed by Frontend, which conflicts with Product’s declared ownership of UI copy SSOT and creates ambiguous cross-area ownership.
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/LOGIN.md:23`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/BAN_PICK_SHOP.md:33`
- evidence: `05_FRONTEND/FE_STATE_RULES.md:44`
31. [MEDIUM] `DUP-TERMINOLOGY` `duplication/TERM_CONFLICT` ALIAS_WITHOUT_MAPPING_ROOM_LIST_ROUTE_STATE - `ROOM_LIST` is defined upstream as a MAIN-internal panel state, but frontend design mapping labels it as `Route` without an explicit canonical mapping (route vs panel-state key). This creates alias ambiguity and weak traceability.
- evidence: `01_PRODUCT/USER_FLOWS.md:26`
- evidence: `03_API/PAGE_MAP/ROOM_LIST.md:2`
- evidence: `05_FRONTEND/FE_DESIGN_MAPPING.md:12`
32. [MEDIUM] `AGENTSPEC-BACKEND` `agent_spec/BACKEND_AGENT_SKILL` required_reference_existence.backend_readme_unqualified_agent_paths - `AGENTS/CLAUDE/AGENTS/BACKEND/README.md` lists many agent files as bare filenames that do not exist relative to that directory, reducing SSOT traceability and causing ambiguous ownership navigation.
- evidence: `AGENTS/CLAUDE/AGENTS/BACKEND/README.md:22`
- evidence: `AGENTS/CLAUDE/AGENTS/BACKEND/README.md:24`
- evidence: `AGENTS/CLAUDE/AGENTS/BACKEND/README.md:33`
33. [MEDIUM] `TRACE-E2E` `traceability/E2E_TRACEABILITY` TRACE_ORPHAN_SPEC_DECLARATION_FE_NOTIFICATION - An orphan/misaligned spec declaration exists: Design README declares `FE_NOTIFICATION_MESSAGES.md` under `02_DESIGN/PAGE_REQUIREMENTS`, but the actual document lives in Frontend docs and is consumed there.
- evidence: `02_DESIGN/README.md:24`
- evidence: `02_DESIGN/PAGE_REQUIREMENTS/FE_NOTIFICATION_MESSAGES.md`
- evidence: `05_FRONTEND/FE_STATE_RULES.md:9`
34. [LOW] `AREA-06_BACKEND` `area/06_BACKEND` REQUIRED_DOC_DECLARED_BUT_MISSING - `06_BACKEND/README.md` declares `BE_AGENT_SPLIT.md` in the backend file structure, but that file is missing in the scoped area.
- evidence: `06_BACKEND/README.md:19`
- evidence: `06_BACKEND/BE_AGENT_SPLIT.md`
35. [LOW] `DUP-NORMATIVE` `duplication/NORMATIVE_DUPLICATION` NORMATIVE_DUPLICATION_SCALING_BASELINE - The same normative scaling statement ('1920x1080 is conversion baseline, not fixed resolution rule') is duplicated across DESIGN and FRONTEND docs despite FRONTEND already declaring DESIGN as source-of-truth, increasing drift risk.
- evidence: `02_DESIGN/TYPOGRAPHY_SYSTEM.md:5`
- evidence: `05_FRONTEND/FE_STYLING.md:3`
- evidence: `05_FRONTEND/FE_STYLING.md:12`
