# PAGE_MAP_BAN_PICK_SHOP

## 목적
- BAN/PICK/SHOP 단일 페이지(RANKED 전용)의 REST/실시간 매핑을 정의한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 1. 진입 시 REST
| 메서드 | 엔드포인트 | 목적 |
|---|---|---|
| GET | /games/{gameId}/state | 현재 stage/remainingMs/coin/inventory 조회 |
| GET | /catalog/algorithms | 밴/픽 선택 목록 조회 |
| GET | /catalog/items | 상점 아이템 목록(가격/지속시간) 조회 |
| GET | /catalog/spells | 상점 스펠 목록(가격/지속시간) 조회 |

---
## 2. 사용자 액션 → REST
| 내부 단계 | 사용자 액션 | 메서드 | 엔드포인트 |
|---|---|---|---|
| BAN | 알고리즘 밴 제출 | POST | /games/{gameId}/ban |
| PICK | 알고리즘 픽 제출 | POST | /games/{gameId}/pick |
| SHOP | 아이템 구매 | POST | /games/{gameId}/shop/items |
| SHOP | 스펠 구매 | POST | /games/{gameId}/shop/spells |

---
## 3. 실시간 구독/발행
### 3.1 구독
| 채널 | 이벤트 타입 | 목적 |
|---|---|---|
| /topic/games/{gameId} | GAME_STAGE_CHANGED | BAN→PICK→SHOP→PLAY 단계 전환 반영 |
| /topic/rooms/{roomId}/chat | CHAT_MESSAGE | 룸 채팅 수신 |
| /user/queue/errors | ERROR | 명령 실패 처리 |

### 3.2 발행 (Command)
| Destination | Command Type | Data 핵심 필드 |
|---|---|---|
| /app/chat.send | CHAT_SEND | channelType=INGAME, roomId, message |

---
## 4. 이탈 시 처리
- stage가 PLAY로 변경되면 IN_GAME으로 전환한다.
- ROOM 채팅 구독은 동일 roomId 기준으로 IN_GAME까지 유지 가능하다.
