# REALTIME_EVENTS

## 0. 문서 목적
- 실시간 이벤트 타입과 payload를 정의한다.
- Event Envelope는 REALTIME_CONVENTIONS를 따른다.

## 관련 문서
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]

---
## 1. 공통 규칙
- 모든 ID는 문자열(userId, roomId, gameId 등).
- Enum 값은 UPPER_SNAKE_CASE.
- 시간은 ISO-8601 UTC 문자열.
- remainingMs는 `stage_deadline_at - meta.serverTime` 기반 파생값이다.

### 1.1 EventType 목록
- ERROR
- CHAT_MESSAGE
- ROOM_LIST_UPSERT
- ROOM_LIST_REMOVED
- ROOM_PLAYER_JOINED
- ROOM_PLAYER_LEFT
- ROOM_PLAYER_STATE_CHANGED
- ROOM_HOST_CHANGED
- ROOM_KICKED
- GAME_STAGE_CHANGED
- GAME_FINISHED
- TYPING_STATUS_CHANGED
- ITEM_EFFECT_APPLIED
- SPELL_EFFECT_APPLIED
- ITEM_EFFECT_BLOCKED
- EFFECT_REMOVED
- INVENTORY_SYNC

---
## 2. 방 목록
### 2.1 ROOM_LIST_UPSERT
Topic: `/topic/rooms/list`

Type: `ROOM_LIST_UPSERT`

Data:
- room: RoomSummary (REST OPENAPI의 RoomSummary 스키마와 동일)
- listVersion: integer

Rules:
- 방 생성/상태 변경/인원수 변경 시 전송한다.
- 현재 화면에 표시 중인 roomId와 일치하면 즉시 카드 상태를 갱신한다.
- 현재 페이지 범위 밖 변화는 업데이트 인디케이터 누적으로 처리한다.

### 2.2 ROOM_LIST_REMOVED
Topic: `/topic/rooms/list`

Type: `ROOM_LIST_REMOVED`

Data:
- roomId: string
- listVersion: integer
- reason: ROOM_CLOSED | DELETED

Rules:
- 방이 목록에서 제외될 때 전송한다.
- 현재 화면에 보이는 roomId면 즉시 제거하고, 아니면 업데이트 인디케이터 누적으로 처리한다.

---
## 3. 채팅
### 3.1 CHAT_MESSAGE
Topic: `/topic/chat/global` 또는 `/topic/rooms/{roomId}/chat`

Type: `CHAT_MESSAGE`

Data:
- messageId: string
- channelType: ChatChannel (GLOBAL | INGAME)
- roomId: string | null
- sender: { userId: string, nickname: string }
- message: string
- createdAt: datetime

Rules:
- GLOBAL 채널은 `/topic/chat/global`로만 전송되며 `roomId = null`
- INGAME 채널은 `/topic/rooms/{roomId}/chat`로 전송되며 `roomId` 필수

Example:
```json
{
  "type": "CHAT_MESSAGE",
  "data": {
    "messageId": "msg_123",
    "channelType": "INGAME",
    "roomId": "room_1",
    "sender": { "userId": "u1", "nickname": "neo" },
    "message": "gg",
    "createdAt": "2026-02-03T12:01:02Z"
  },
  "meta": { "eventId": "evt_1", "serverTime": "2026-02-03T12:01:02Z" }
}
```

---
## 4. 대기실
### 4.1 ROOM_PLAYER_JOINED
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_PLAYER_JOINED`

Data:
- roomId: string
- userId: string
- nickname: string
- state: PlayerState (READY | UNREADY | DISCONNECTED)
- joinedAt: datetime

### 4.2 ROOM_PLAYER_LEFT
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_PLAYER_LEFT`

Data:
- roomId: string
- userId: string
- leftAt: datetime
- reason: LEAVE | KICKED

### 4.3 ROOM_PLAYER_STATE_CHANGED
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_PLAYER_STATE_CHANGED`

Data:
- roomId: string
- userId: string
- state: PlayerState (READY | UNREADY | DISCONNECTED)
- updatedAt: datetime

### 4.4 ROOM_HOST_CHANGED
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_HOST_CHANGED`

Data:
- roomId: string
- fromUserId: string
- toUserId: string
- reason: HostChangeReason (LEAVE | SYSTEM | MANUAL)
- changedAt: datetime

### 4.5 ROOM_KICKED
Topic: `/user/queue/rooms`

Type: `ROOM_KICKED`

Data:
- roomId: string
- kickedByUserId: string
- kickedAt: datetime

---
## 5. 게임 진행
### 5.1 GAME_STAGE_CHANGED
Topic: `/topic/games/{gameId}`

Type: `GAME_STAGE_CHANGED`

Data:
- gameId: string
- roomId: string
- gameType: GameType (NORMAL | RANKED)
- stage: GameStage (LOBBY | BAN | PICK | SHOP | PLAY | FINISHED)
- stageStartedAt: datetime
- stageDeadlineAt: datetime
- remainingMs: integer

### 5.2 GAME_FINISHED
Topic: `/topic/games/{gameId}`

Type: `GAME_FINISHED`

Data:
- gameId: string
- roomId: string
- finishedAt: datetime
- results: array
  - userId: string
  - nickname: string
  - result: MatchResult (WIN | LOSE | DRAW)
  - rankInGame: integer
  - scoreDelta: integer
  - coinDelta: integer
  - expDelta: number
  - finalScoreValue: integer
  - solved: boolean

---
## 6. 타이핑 상태
### 6.1 TYPING_STATUS_CHANGED
Topic: `/topic/rooms/{roomId}/typing`

Type: `TYPING_STATUS_CHANGED`

Data:
- roomId: string
- userId: string
- isTyping: boolean
- updatedAt: datetime

---
## 7. 아이템/스펠 효과
### 7.1 ITEM_EFFECT_APPLIED
Topic: `/topic/games/{gameId}`

Type: `ITEM_EFFECT_APPLIED`

Data:
- effectId: string (ITEM_USAGE.id)
- gameId: string
- itemId: string
- fromUserId: string
- toUserId: string
- durationSec: integer
- startedAt: datetime
- expiresAt: datetime

### 7.2 SPELL_EFFECT_APPLIED
Topic: `/topic/games/{gameId}`

Type: `SPELL_EFFECT_APPLIED`

Data:
- effectId: string (SPELL_USAGE.id)
- gameId: string
- spellId: string
- userId: string
- durationSec: integer
- startedAt: datetime
- expiresAt: datetime

### 7.3 ITEM_EFFECT_BLOCKED
Topic: `/topic/games/{gameId}`

Type: `ITEM_EFFECT_BLOCKED`

Data:
- effectId: string (ITEM_USAGE.id)
- gameId: string
- itemId: string
- fromUserId: string
- toUserId: string
- blockedBySpellId: string
- blockedAt: datetime

### 7.4 EFFECT_REMOVED
Topic: `/topic/games/{gameId}`

Type: `EFFECT_REMOVED`

Data:
- effectId: string
- gameId: string
- effectType: ITEM | SPELL
- targetUserId: string
- reason: EXPIRED | DISPELLED | CONSUMED
- removedAt: datetime

---
## 8. 인벤토리 동기화
### 8.1 INVENTORY_SYNC
Topic: `/user/queue/inventory`

Type: `INVENTORY_SYNC`

Data:
- gameId: string
- inventory: Inventory (REST OPENAPI의 Inventory 스키마와 동일)

---
## 9. 오류
### 9.1 ERROR
Topic: `/user/queue/errors`

Type: `ERROR`

Data:
- code: string (ERROR_MODEL.code)
- message: string
- details: object | null
