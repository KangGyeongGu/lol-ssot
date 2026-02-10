## 목적
- RESULT 화면의 결과 수신/표시 기준을 REST/실시간 계약에 맞춰 매핑한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

---
## 1. 진입 기준
| 구분 | 소스 | 기준 |
|---|---|---|
| 연결 유지 중 게임 종료 | 실시간 이벤트 | `/topic/games/{gameId}`의 `GAME_FINISHED` 수신 시 RESULT 표시 |
| 새로고침/재접속 | REST | `GET /users/me/active-game`은 FINISHED를 반환하지 않으므로 RESULT 자동 복귀 없음 |

---
## 2. 데이터 소스
| 화면 데이터 | 소스 | 필드 |
|---|---|---|
| 결과 목록(승/패/무, 순위, 보상) | GAME_FINISHED | result, rankInGame, scoreDelta(RANKED), coinDelta(RANKED), expDelta(NORMAL/RANKED), solved |
| 게임 메타 | GAME_FINISHED | gameId, roomId, finishedAt |

---
## 3. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 목적 |
|---|---|---|---|
| 메인 이동 | GET | /users/me/active-game | 진행 중 게임 없음을 확인 후 MAIN 이동 |
| 마이페이지 이동 | GET | /users/me | MY_PAGE 헤더 기본 정보 로드 |

---
## 4. 이탈 시 처리
- RESULT 표시 시점에 게임 단위 구독(`/topic/games/{gameId}`)을 해제한다.
- RESULT에서는 추가 구독을 설정하지 않는다.
