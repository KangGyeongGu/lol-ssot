## 목적
- IN_GAME(PLAY 단계) 화면의 REST/실시간 매핑을 정의한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 1. 진입 시 REST
| 메서드 | 엔드포인트 | 목적 |
|---|---|---|
| GET | /games/{gameId}/state | PLAY 시점 스냅샷(remainingMs, players, coin, inventory) 동기화 |

---
## 2. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 비고 |
|---|---|---|---|
| 코드 제출 | POST | /games/{gameId}/submissions | stage=PLAY에서만 허용 |

---
## 3. 실시간 구독/발행
### 3.1 구독
| 채널 | 이벤트 타입 | 목적 |
|---|---|---|
| /topic/games/{gameId} | GAME_STAGE_CHANGED | stage/remainingMs 동기화 |
| /topic/games/{gameId} | ITEM_EFFECT_APPLIED | 아이템 효과 적용 반영 |
| /topic/games/{gameId} | SPELL_EFFECT_APPLIED | 스펠 효과 적용 반영 |
| /topic/games/{gameId} | ITEM_EFFECT_BLOCKED | 보호막 등 차단 결과 반영 |
| /topic/games/{gameId} | EFFECT_REMOVED | 효과 종료/해제 반영 |
| /topic/games/{gameId} | GAME_FINISHED | 결과 화면 전환 트리거 |
| /topic/rooms/{roomId}/chat | CHAT_MESSAGE | 룸 채팅 수신 |
| /user/queue/inventory | INVENTORY_SYNC | 본인 인벤토리 동기화 |
| /user/queue/errors | ERROR | 명령 실패 처리 |

### 3.2 발행 (Command)
| Destination | Command Type | Data 핵심 필드 |
|---|---|---|
| /app/chat.send | CHAT_SEND | channelType=INGAME, roomId, message |
| /app/games/{gameId}/items.use | ITEM_USE | itemId, targetUserId |
| /app/games/{gameId}/spells.use | SPELL_USE | spellId |

---
## 4. 이탈 시 처리
- `GAME_FINISHED` 수신 시 RESULT를 표시한다.
- 게임 컨텍스트 종료 후 `/topic/games/{gameId}` 구독을 해제한다.
