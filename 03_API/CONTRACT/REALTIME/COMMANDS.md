## 0. 문서 목적
- 실시간 명령(클라이언트 → 서버)의 타입과 payload를 정의한다.
- Command Envelope는 REALTIME_CONVENTIONS를 따른다.

## 관련 문서
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

---
## 1. 공통 규칙
- REST로 처리하는 명령: 밴/픽/구매/제출.
- WebSocket 명령: 채팅, 아이템/스펠 사용.
- 성공 응답은 이벤트로 브로드캐스트된다.
- 실패는 `/user/queue/errors`로 ERROR 이벤트를 반환한다.

### 1.1 CommandType 목록
- CHAT_SEND
- ITEM_USE
- SPELL_USE

---
## 2. 명령 목록
### 2.1 CHAT_SEND
Destination: `/app/chat.send`

Type: `CHAT_SEND`

Data:
- channelType: ChatChannel (GLOBAL | INGAME)
- roomId: string | null (INGAME일 때 필수)
- message: string
- clientMessageId: string | null (중복 전송 방지용)

Success:
- CHAT_MESSAGE 이벤트가 해당 채널 Topic으로 전송된다.

Error (예시):
- UNAUTHORIZED
- PLAYER_NOT_IN_ROOM
- VALIDATION_FAILED
- RATE_LIMITED

---
### 2.2 ITEM_USE
Destination: `/app/games/{gameId}/items.use`

Type: `ITEM_USE`

Data:
- itemId: string
- targetUserId: string

Constraints:
- gameType = RANKED
- stage = PLAY
- 보유 수량 > 0

Success:
- ITEM_EFFECT_APPLIED 또는 ITEM_EFFECT_BLOCKED 이벤트 전송
- INVENTORY_SYNC (본인) 이벤트 전송

Error (예시):
- UNAUTHORIZED
- GAME_NOT_FOUND
- INVALID_STAGE_ACTION
- GAME_ALREADY_FINISHED
- VALIDATION_FAILED

---
### 2.3 SPELL_USE
Destination: `/app/games/{gameId}/spells.use`

Type: `SPELL_USE`

Data:
- spellId: string

Constraints:
- gameType = RANKED
- stage = PLAY
- 보유 수량 > 0

Success:
- SPELL_EFFECT_APPLIED 이벤트 전송
- 정화 스펠 사용 시 EFFECT_REMOVED 이벤트 전송
- INVENTORY_SYNC (본인) 이벤트 전송

Error (예시):
- UNAUTHORIZED
- GAME_NOT_FOUND
- INVALID_STAGE_ACTION
- GAME_ALREADY_FINISHED
- VALIDATION_FAILED
