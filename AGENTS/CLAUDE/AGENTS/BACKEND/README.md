## 0. 문서 목적
- 백엔드 Claude Code 서브에이전트 분할 기준을 정의한다.
- 에이전트 간 충돌을 최소화한다.

## 관련 문서
- `06_BACKEND/SPEC/BE_ARCHITECTURE.md`
- `06_BACKEND/QUALITY/BE_CONVENTIONS.md`
- `06_BACKEND/SPEC/BE_API_RULES.md`
- `06_BACKEND/SPEC/BE_REALTIME_RULES.md`
- `06_BACKEND/SPEC/BE_DATA_MODEL_RULES.md`
- `03_API/README.md`
- `04_DOMAIN/DATA_MODEL.md`

---
## 1. 분할 원칙
- 도메인 기준 수직 분할을 기본으로 한다.
- 리뷰는 도메인별로 SSOT/QUALITY를 분리한다.
- 공통 기반은 Core/Infra 에이전트만 수정한다.
- 에이전트 간 파일 소유권이 겹치지 않도록 한다.

---
## 2. 마스터/운영 에이전트
- Review Master: `REVIEW/MASTER/BE_REVIEW_MASTER_AGENT.md`
- Review Partial Master: `REVIEW/MASTER/BE_REVIEW_PARTIAL_MASTER_AGENT.md`
- Dev Master: `DEV/BE_DEV_MASTER_AGENT.md`
- Dev Partial Master: `DEV/BE_DEV_PARTIAL_MASTER_AGENT.md`
- Ad-hoc Dev: `DEV/BE_DEV_ADHOC_AGENT.md`
- QnA: `DEV/BE_QNA_AGENT.md`

---
## 3. 도메인 에이전트 분할 표
| 도메인 | SSOT Review Agent | Quality Review Agent | Dev Agent |
|---|---|---|---|
| Core/Infra | `REVIEW/SSOT/CORE_INFRA_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/CORE_INFRA_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_CORE_INFRA_AGENT.md` |
| Auth/User | `REVIEW/SSOT/AUTH_USER_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/AUTH_USER_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_AUTH_USER_AGENT.md` |
| Room/Lobby | `REVIEW/SSOT/ROOM_LOBBY_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/ROOM_LOBBY_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_ROOM_LOBBY_AGENT.md` |
| Game Lifecycle | `REVIEW/SSOT/GAME_LIFECYCLE_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/GAME_LIFECYCLE_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_GAME_LIFECYCLE_AGENT.md` |
| Ban/Pick/Shop | `REVIEW/SSOT/BAN_PICK_SHOP_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/BAN_PICK_SHOP_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_BAN_PICK_SHOP_AGENT.md` |
| Realtime/Chat | `REVIEW/SSOT/REALTIME_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/REALTIME_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_REALTIME_CHAT_AGENT.md` |
| Redis/Cache | `REVIEW/SSOT/REDIS_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/REDIS_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_REDIS_AGENT.md` |
| JPA/DB | `REVIEW/SSOT/JPA_DB_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/JPA_DB_QUALITY_REVIEW_AGENT.md` | `DEV/BE_DEV_JPA_DB_AGENT.md` |

---
## 4. 경계 규칙
- SSOT 리뷰 에이전트는 명세 불일치 탐지에 집중한다.
- QUALITY 리뷰 에이전트는 코드 품질/구현 패턴을 독립적으로 검토한다.
- QUALITY 리뷰는 SSOT raw 보고서를 입력으로 사용하지 않는다.
- Core/Infra 외 에이전트는 `src/common`, `src/config` 공통 영역을 직접 수정하지 않는다.
- Realtime/Chat 에이전트만 `src/realtime`을 수정한다.
- Redis/Cache 변경은 Redis 에이전트가 단독으로 수행한다.
- DB 스키마/마이그레이션 변경은 JPA/DB 에이전트가 단독으로 수행한다.
