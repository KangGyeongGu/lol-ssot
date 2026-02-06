# PAGE_MAP_WAITING_ROOM

## 목적
- WAITING_ROOM(LOBBY 단계) 화면의 REST/실시간 매핑을 정의한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 1. 진입 시 REST
| 메서드 | 엔드포인트 | 목적 |
|---|---|---|
| GET | /rooms/{roomId} | 플레이어 목록/방 설정/현재 상태 스냅샷 조회 |

---
## 2. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 비고 |
|---|---|---|---|
| READY | POST | /rooms/{roomId}/ready | 본인 상태 READY 전환 |
| UNREADY | POST | /rooms/{roomId}/unready | 본인 상태 UNREADY 전환 |
| 방 나가기 | POST | /rooms/{roomId}/leave | 성공 시 MAIN 복귀(필요 시 ROOM_LIST 패널 상태 진입) |
| 게임 시작(방장) | POST | /rooms/{roomId}/start | 성공 시 ActiveGame(pageRoute) 기준 다음 화면 이동 |
| 플레이어 강퇴(방장) | POST | /rooms/{roomId}/kick | body.targetUserId 필수 |

---
## 3. 실시간 구독/발행
### 3.1 구독
| 채널 | 이벤트 타입 | 목적 |
|---|---|---|
| /topic/rooms/{roomId}/lobby | ROOM_PLAYER_JOINED | 입장자 슬롯 반영 |
| /topic/rooms/{roomId}/lobby | ROOM_PLAYER_LEFT | 퇴장/강퇴 슬롯 반영 |
| /topic/rooms/{roomId}/lobby | ROOM_PLAYER_STATE_CHANGED | READY/UNREADY/DISCONNECTED 반영 |
| /topic/rooms/{roomId}/lobby | ROOM_HOST_CHANGED | 방장 변경 반영 |
| /topic/rooms/{roomId}/chat | CHAT_MESSAGE | 인게임(룸 스코프) 채팅 수신 |
| /user/queue/rooms | ROOM_KICKED | 본인 강퇴 알림 처리 |
| /user/queue/errors | ERROR | 실시간 명령 실패 처리 |

### 3.2 발행 (Command)
| Destination | Command Type | Data 핵심 필드 |
|---|---|---|
| /app/chat.send | CHAT_SEND | channelType=INGAME, roomId, message |

---
## 4. 이탈 시 처리
- WAITING_ROOM 이탈 시 `/topic/rooms/{roomId}/lobby` 구독을 해제한다.
- 룸 채팅(`/topic/rooms/{roomId}/chat`)은 BAN_PICK_SHOP/IN_GAME까지 동일 roomId 기준으로 유지 가능하다.
