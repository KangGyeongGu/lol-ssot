## 목적
- MAIN 화면에서 사용하는 REST/실시간 계약을 페이지 기준으로 매핑한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 1. 진입 전/진입 시 REST
| 시점 | 메서드 | 엔드포인트 | 목적 |
|---|---|---|---|
| MAIN 진입 전 공통 | GET | /users/me/active-game | 진행 중 게임 복귀 필요 여부 확인 (없을 때 MAIN 진입) |
| MAIN 진입 직후 | GET | /users/me | 상단 프로필/코인/점수/레벨/경험치 표시 |
| MAIN 진입 직후 | GET | /stats/realtime/player-rankings | 실시간 플레이어 랭킹 표시 |
| MAIN 진입 직후 | GET | /stats/realtime/algorithm-pick-ban-rates | 실시간 알고리즘 밴/픽률 표시 |

---
## 2. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 비고 |
|---|---|---|---|
| 방 생성(모달) | POST | /rooms | 성공 시 생성된 roomId 기준 WAITING_ROOM 진입 |
| ROOM_LIST 패널 열기 | GET | /rooms | MAIN 내부 ROOM_LIST 패널 진입 시 목록 조회(listVersion 포함) |

---
## 3. 실시간 구독/발행
### 3.1 구독
| 채널 | 이벤트 타입 | 목적 |
|---|---|---|
| /topic/chat/global | CHAT_MESSAGE | 전역 채팅 수신 |
| /topic/rooms/list | ROOM_LIST_UPSERT, ROOM_LIST_REMOVED | ROOM_LIST 패널 활성 중 목록 변경 감지 |
| /user/queue/errors | ERROR | 실시간 명령 실패 수신 |

### 3.2 발행 (Command)
| Destination | Command Type | Data 핵심 필드 |
|---|---|---|
| /app/chat.send | CHAT_SEND | channelType=GLOBAL, roomId=null, message |

---
## 4. 이탈 시 처리
- MAIN 이탈 시 `/topic/chat/global` 구독을 해제한다.
