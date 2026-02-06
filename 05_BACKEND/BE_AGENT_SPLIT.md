# BE_AGENT_SPLIT

## 0. 문서 목적
- Claude Code 서브에이전트 병렬 실행을 위한 작업 분할 기준을 정의한다.
- 에이전트 간 충돌을 최소화한다.

## 관련 문서
- [[05_BACKEND/BE_ARCHITECTURE.md]]
- [[05_BACKEND/BE_CONVENTIONS.md]]
- [[05_BACKEND/BE_API_RULES.md]]
- [[05_BACKEND/BE_REALTIME_RULES.md]]
- [[05_BACKEND/BE_DATA_MODEL_RULES.md]]
- [[03_API/README.md]]
- [[03_DOMAIN/DATA_MODEL.md]]

---
## 1. 분할 원칙
- 도메인 기준 수직 분할을 기본으로 한다.
- 공통 기반은 Core/Infra 에이전트만 수정한다.
- 에이전트 간 파일 소유권이 겹치지 않도록 한다.

---
## 2. 에이전트 분할 표
| Agent | 범위 | 소유 디렉토리 |
|---|---|---|
| Core/Infra | 서버 부트스트랩, 공통 미들웨어, 에러/응답 포맷, 인증 가드, DB 연결 | `src/app`, `src/config`, `src/common`, `src/db` |
| Auth/User | 카카오 로그인/회원가입/유저 프로필 | `src/modules/auth`, `src/modules/user` |
| Room/Lobby | 방 생성/조회/참가, 대기실 상태 | `src/modules/room`, `src/modules/lobby` |
| Game Lifecycle | 게임 시작/스테이지 전환/active game | `src/modules/game` |
| Ban/Pick/Shop + Inventory | 밴/픽/구매, 아이템/스펠, 효과 적용 | `src/modules/shop`, `src/modules/inventory` |
| Realtime/Chat | STOMP 연결, 채팅/타이핑 이벤트 | `src/realtime`, `src/modules/chat` |
| Stats/Ranking | 실시간 랭킹/알고리즘 통계 | `src/modules/stats` |

---
## 3. 경계 규칙
- Core/Infra 외 에이전트는 `src/common`, `src/db`를 수정하지 않는다.
- Realtime/Chat 에이전트만 `src/realtime`을 수정한다.
- 도메인 로직은 해당 모듈 안에서만 수정한다.
