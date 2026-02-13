## 0. 문서 목적
- 프론트엔드 Claude Code 서브에이전트 분할 기준을 정의한다.
- 에이전트 간 충돌을 최소화한다.

## 관련 문서
- `05_FRONTEND/SPEC/FE_ARCHITECTURE.md`
- `05_FRONTEND/QUALITY/FE_CONVENTIONS.md`
- `05_FRONTEND/SPEC/FE_API_CLIENT.md`
- `05_FRONTEND/SPEC/FE_STATE_RULES.md`
- `05_FRONTEND/SPEC/FE_ROUTING_RULES.md`
- `05_FRONTEND/SPEC/FE_REALTIME_RULES.md`
- `03_API/README.md`
- `02_DESIGN/README.md`

---
## 1. 분할 원칙
- 기능 영역 기준 수직 분할을 기본으로 한다.
- 리뷰는 도메인별로 SSOT/QUALITY를 분리한다.
- 에이전트 간 파일 소유권이 겹치지 않도록 한다.

---
## 2. 마스터/운영 에이전트
- Review Master: `REVIEW/MASTER/FE_REVIEW_MASTER_AGENT.md`
- Review Partial Master: `REVIEW/MASTER/FE_REVIEW_PARTIAL_MASTER_AGENT.md`
- Dev Master: `DEV/FE_DEV_MASTER_AGENT.md`
- Dev Partial Master: `DEV/FE_DEV_PARTIAL_MASTER_AGENT.md`
- Ad-hoc Dev: `DEV/FE_DEV_ADHOC_AGENT.md`
- QnA: `DEV/FE_QNA_AGENT.md`

---
## 3. 도메인 에이전트 분할 표
| 도메인 | SSOT Review Agent | Quality Review Agent | Dev Agent |
|---|---|---|---|
| API Integration | `REVIEW/SSOT/API_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/API_QUALITY_REVIEW_AGENT.md` | `DEV/FE_DEV_API_AGENT.md` |
| State/Store | `REVIEW/SSOT/STATE_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/STATE_QUALITY_REVIEW_AGENT.md` | `DEV/FE_DEV_STATE_AGENT.md` |
| Routing/Guards | `REVIEW/SSOT/ROUTING_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/ROUTING_QUALITY_REVIEW_AGENT.md` | `DEV/FE_DEV_ROUTING_AGENT.md` |
| Realtime/Socket | `REVIEW/SSOT/REALTIME_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/REALTIME_QUALITY_REVIEW_AGENT.md` | `DEV/FE_DEV_REALTIME_AGENT.md` |
| UI/Quality | `REVIEW/SSOT/QUALITY_SSOT_REVIEW_AGENT.md` | `REVIEW/QUALITY/QUALITY_QUALITY_REVIEW_AGENT.md` | `DEV/FE_DEV_QUALITY_AGENT.md` |

---
## 4. 경계 규칙
- SSOT 리뷰 에이전트는 명세 불일치 탐지에 집중한다.
- QUALITY 리뷰 에이전트는 코드 품질/구현 패턴을 독립적으로 검토한다.
- QUALITY 리뷰는 SSOT raw 보고서를 입력으로 사용하지 않는다.
- API 에이전트는 `src/api` 외 영역을 직접 수정하지 않는다.
- State 에이전트는 스토어/엔티티 계층만 수정한다.
- Routing 에이전트는 라우팅/가드 관련 파일만 수정한다.
- Realtime 에이전트는 `src/realtime` 범위만 수정한다.
- Quality 에이전트의 교차 수정은 명확한 사유와 범위를 지정한다.
