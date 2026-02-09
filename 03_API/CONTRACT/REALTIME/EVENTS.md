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
- TIME_SYNC
- ROOM_LIST_UPSERT
- ROOM_LIST_REMOVED
- ROOM_PLAYER_JOINED
- ROOM_PLAYER_LEFT
- ROOM_PLAYER_STATE_CHANGED
- ROOM_HOST_CHANGED
- ROOM_KICKED
- GAME_STAGE_CHANGED
- ROOM_GAME_STARTED
- GAME_BAN_SUBMITTED
- GAME_PICK_SUBMITTED
- GAME_ITEM_PURCHASED
- GAME_SPELL_PURCHASED
- GAME_FINISHED
- TYPING_STATUS_CHANGED
- ITEM_EFFECT_APPLIED
- SPELL_EFFECT_APPLIED
- ITEM_EFFECT_BLOCKED
- EFFECT_REMOVED
- INVENTORY_SYNC

---
## 2. 시간 동기화
### 2.1 TIME_SYNC
Topic: `/user/queue/time`

Type: `TIME_SYNC`

Data:
- serverTime: datetime (meta.serverTime과 동일)

Rules:
- 클라이언트는 TIME_SYNC로 오프셋을 재계산한다.
- TIME_SYNC는 기본 10초, BAN/PICK/SHOP 단계는 2초 주기로 전송한다.

---
## 3. 방 목록
### 3.1 ROOM_LIST_UPSERT
Topic: `/topic/rooms/list`

Type: `ROOM_LIST_UPSERT`

Data:
- room: RoomSummary (REST OPENAPI의 RoomSummary 스키마와 동일)
- listVersion: integer

Rules:
- 방 생성/상태 변경/인원수 변경 시 전송한다.
- 현재 화면에 표시 중인 roomId와 일치하면 즉시 카드 상태를 갱신한다.
- 현재 페이지 범위 밖 변화는 업데이트 인디케이터 누적으로 처리한다.

### 3.2 ROOM_LIST_REMOVED
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
## 4. 채팅
### 4.1 CHAT_MESSAGE
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
## 5. 대기실
### 5.1 ROOM_PLAYER_JOINED
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_PLAYER_JOINED`

Data:
- roomId: string
- userId: string
- nickname: string
- state: PlayerState (READY | UNREADY | DISCONNECTED)
- joinedAt: datetime

### 5.2 ROOM_PLAYER_LEFT
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_PLAYER_LEFT`

Data:
- roomId: string
- userId: string
- leftAt: datetime
- reason: LEAVE | KICKED

### 5.3 ROOM_PLAYER_STATE_CHANGED
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_PLAYER_STATE_CHANGED`

Data:
- roomId: string
- userId: string
- state: PlayerState (READY | UNREADY | DISCONNECTED)
- updatedAt: datetime

### 5.4 ROOM_HOST_CHANGED
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_HOST_CHANGED`

Data:
- roomId: string
- fromUserId: string
- toUserId: string
- reason: HostChangeReason (LEAVE | SYSTEM | MANUAL)
- changedAt: datetime

### 5.5 ROOM_KICKED
Topic: `/user/queue/rooms`

Type: `ROOM_KICKED`

Data:
- roomId: string
- kickedByUserId: string
- kickedAt: datetime

### 5.6 ROOM_GAME_STARTED
Topic: `/topic/rooms/{roomId}/lobby`

Type: `ROOM_GAME_STARTED`

Data:
- roomId: string
- gameId: string
- gameType: GameType (NORMAL | RANKED)
- stage: GameStage (BAN | PICK | SHOP | PLAY)
- pageRoute: PageRoute (BAN_PICK_SHOP | IN_GAME)
- stageStartedAt: datetime
- stageDeadlineAt: datetime
- remainingMs: integer

---
## 6. 게임 진행
### 6.1 GAME_STAGE_CHANGED
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

### 6.2 GAME_BAN_SUBMITTED
Topic: `/topic/games/{gameId}`

Type: `GAME_BAN_SUBMITTED`

Data:
- gameId: string
- roomId: string
- userId: string
- algorithmId: string
- submittedAt: datetime

### 6.3 GAME_PICK_SUBMITTED
Topic: `/topic/games/{gameId}`

Type: `GAME_PICK_SUBMITTED`

Data:
- gameId: string
- roomId: string
- userId: string
- algorithmId: string
- submittedAt: datetime

### 6.4 GAME_ITEM_PURCHASED
Topic: `/topic/games/{gameId}`

Type: `GAME_ITEM_PURCHASED`

Data:
- gameId: string
- roomId: string
- userId: string
- itemId: string
- quantity: integer
- unitPrice: integer
- totalPrice: integer
- purchasedAt: datetime

### 6.5 GAME_SPELL_PURCHASED
Topic: `/topic/games/{gameId}`

Type: `GAME_SPELL_PURCHASED`

Data:
- gameId: string
- roomId: string
- userId: string
- spellId: string
- quantity: integer
- unitPrice: integer
- totalPrice: integer
- purchasedAt: datetime

### 6.6 GAME_FINISHED
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
  - coinBefore: integer
  - coinDelta: integer
  - expBefore: number
  - expDelta: number
  - finalScoreValue: integer
  - solved: boolean

---
## 7. 타이핑 상태
### 7.1 TYPING_STATUS_CHANGED
Topic: `/topic/rooms/{roomId}/typing`

Type: `TYPING_STATUS_CHANGED`

Data:
- roomId: string
- userId: string
- isTyping: boolean
- updatedAt: datetime

---
## 8. 아이템/스펠 효과
### 8.1 ITEM_EFFECT_APPLIED
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
