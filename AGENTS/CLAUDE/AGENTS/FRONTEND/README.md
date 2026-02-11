## 0. 문서 목적
- 프론트엔드 Claude Code 서브에이전트 분할 기준을 정의한다.
- 에이전트 간 충돌을 최소화한다.

## 관련 문서
- `05_FRONTEND/FE_ARCHITECTURE.md`
- `05_FRONTEND/FE_CONVENTIONS.md`
- `05_FRONTEND/FE_API_CLIENT.md`
- `05_FRONTEND/FE_STATE_RULES.md`
- `05_FRONTEND/FE_ROUTING_RULES.md`
- `05_FRONTEND/FE_REALTIME_RULES.md`
- `03_API/README.md`
- `02_DESIGN/README.md`

---
## 1. 분할 원칙
- 기능 영역 기준 수직 분할을 기본으로 한다.
- 에이전트 간 파일 소유권이 겹치지 않도록 한다.

---
## 2. 마스터/운영 에이전트
- Review Master: `FE_REVIEW_MASTER_AGENT.md`
- Review Partial Master: `FE_REVIEW_PARTIAL_MASTER_AGENT.md`
- Dev Master: `FE_DEV_MASTER_AGENT.md`
- Dev Partial Master: `FE_DEV_PARTIAL_MASTER_AGENT.md`
- Ad-hoc Dev: `FE_DEV_ADHOC_AGENT.md`
- QnA: `FE_QNA_AGENT.md`

---
## 3. 도메인 에이전트 분할 표
| 도메인 | Review Agent | Dev Agent | 소유 디렉토리(가이드) |
|---|---|---|---|
| API Integration | `API_REVIEW_AGENT.md` | `FE_DEV_API_AGENT.md` | `src/api`, `src/api/dtos` |
| State/Store | `STATE_REVIEW_AGENT.md` | `FE_DEV_STATE_AGENT.md` | `src/store`, `src/entities` |
| Routing/Guards | `ROUTING_REVIEW_AGENT.md` | `FE_DEV_ROUTING_AGENT.md` | `src/router`, `src/routes` |
| Realtime/Socket | `REALTIME_REVIEW_AGENT.md` | `FE_DEV_REALTIME_AGENT.md` | `src/realtime` |
| Quality/Perf | `QUALITY_REVIEW_AGENT.md` | `FE_DEV_QUALITY_AGENT.md` | 공통 개선 영역(필요 시 다수 경로) |

---
## 4. 경계 규칙
- API 에이전트는 `src/api` 외 영역을 직접 수정하지 않는다.
- State 에이전트는 스토어/엔티티 계층만 수정한다.
- Routing 에이전트는 라우팅/가드 관련 파일만 수정한다.
- Realtime 에이전트는 `src/realtime` 범위만 수정한다.
- Quality 에이전트의 교차 수정은 명확한 사유와 범위를 지정한다.
