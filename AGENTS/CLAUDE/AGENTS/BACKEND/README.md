## 0. 문서 목적
- 백엔드 Claude Code 서브에이전트 분할 기준을 정의한다.
- 에이전트 간 충돌을 최소화한다.

## 관련 문서
- `06_BACKEND/BE_ARCHITECTURE.md`
- `06_BACKEND/BE_CONVENTIONS.md`
- `06_BACKEND/BE_API_RULES.md`
- `06_BACKEND/BE_REALTIME_RULES.md`
- `06_BACKEND/BE_DATA_MODEL_RULES.md`
- `03_API/README.md`
- `04_DOMAIN/DATA_MODEL.md`

---
## 1. 분할 원칙
- 도메인 기준 수직 분할을 기본으로 한다.
- 공통 기반은 Core/Infra 에이전트만 수정한다.
- 에이전트 간 파일 소유권이 겹치지 않도록 한다.

---
## 2. 마스터/운영 에이전트
- Review Master: `BE_REVIEW_MASTER_AGENT.md`
- Review Partial Master: `BE_REVIEW_PARTIAL_MASTER_AGENT.md`
- Dev Master: `BE_DEV_MASTER_AGENT.md`
- Dev Partial Master: `BE_DEV_PARTIAL_MASTER_AGENT.md`
- Ad-hoc Dev: `BE_DEV_ADHOC_AGENT.md`
- QnA: `BE_QNA_AGENT.md`

---
## 3. 도메인 에이전트 분할 표
| 도메인 | Review Agent | Dev Agent | 소유 디렉토리(가이드) |
|---|---|---|---|
| Core/Infra | `CORE_INFRA_REVIEW_AGENT.md` | `BE_DEV_CORE_INFRA_AGENT.md` | `src/app`, `src/config`, `src/common`, `src/db` |
| Auth/User | `AUTH_USER_REVIEW_AGENT.md` | `BE_DEV_AUTH_USER_AGENT.md` | `src/modules/auth`, `src/modules/user` |
| Room/Lobby | `ROOM_LOBBY_REVIEW_AGENT.md` | `BE_DEV_ROOM_LOBBY_AGENT.md` | `src/modules/room`, `src/modules/lobby` |
| Game Lifecycle | `GAME_LIFECYCLE_REVIEW_AGENT.md` | `BE_DEV_GAME_LIFECYCLE_AGENT.md` | `src/modules/game` |
| Ban/Pick/Shop + Inventory | `BAN_PICK_SHOP_REVIEW_AGENT.md` | `BE_DEV_BAN_PICK_SHOP_AGENT.md` | `src/modules/shop`, `src/modules/inventory` |
| Realtime/Chat | `REALTIME_CHAT_REVIEW_AGENT.md` | `BE_DEV_REALTIME_CHAT_AGENT.md` | `src/realtime`, `src/modules/chat` |
| Redis/Cache | `REDIS_REVIEW_AGENT.md` | `BE_DEV_REDIS_AGENT.md` | `src/redis`, `src/cache`, `src/config/redis` |
| JPA/DB | `JPA_DB_REVIEW_AGENT.md` | `BE_DEV_JPA_DB_AGENT.md` | `src/db`, `src/migrations`, `src/repository`, `src/entity` |

---
## 4. 경계 규칙
- Core/Infra 외 에이전트는 `src/common`, `src/config`의 공통 영역을 직접 수정하지 않는다.
- Realtime/Chat 에이전트만 `src/realtime`을 수정한다.
- Redis/Cache 변경은 Redis 에이전트가 단독으로 수행한다.
- DB 스키마/마이그레이션 변경은 JPA/DB 에이전트가 단독으로 수행한다.
- 도메인 로직은 해당 모듈 안에서만 수정한다.
