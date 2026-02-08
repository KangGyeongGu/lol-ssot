# REALTIME_TOPICS

## 0. 문서 목적
- 실시간(WebSocket/STOMP) 구독 대상과 범위를 정의한다.
- 상세 이벤트/명령 형식은 EVENTS/COMMANDS 문서를 따른다.

## 관련 문서
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

---
## 1. 기본 규칙
- Prefix 규칙은 REALTIME_CONVENTIONS를 따른다.
- 초기 스냅샷은 REST로 조회하고, 이후 변경분은 이벤트로 동기화한다.
- room/game 구독은 해당 리소스에 참여한 사용자만 허용된다.
- 예외: `/topic/rooms/list`는 로그인 사용자 전역 구독을 허용한다.

---
## 2. Topic 목록
| Topic | 범위 | 주요 이벤트 | 설명 |
|---|---|---|---|
| /topic/chat/global | GLOBAL | CHAT_MESSAGE | 메인 전역 채팅 |
| /topic/rooms/list | GLOBAL | ROOM_LIST_UPSERT, ROOM_LIST_REMOVED | 방 목록 델타 변경(생성/삭제/상태 갱신) |
| /topic/rooms/{roomId}/chat | ROOM | CHAT_MESSAGE | 대기실~인게임 채팅(ROOM 스코프) |
| /topic/rooms/{roomId}/lobby | ROOM | ROOM_PLAYER_JOINED, ROOM_PLAYER_LEFT, ROOM_PLAYER_STATE_CHANGED, ROOM_HOST_CHANGED | 대기실 상태 변경 |
| /topic/rooms/{roomId}/typing | ROOM | TYPING_STATUS_CHANGED | 인게임 타이핑 상태 |
| /topic/games/{gameId} | GAME | GAME_STAGE_CHANGED, GAME_BAN_SUBMITTED, GAME_PICK_SUBMITTED, GAME_ITEM_PURCHASED, GAME_SPELL_PURCHASED, ITEM_EFFECT_APPLIED, SPELL_EFFECT_APPLIED, ITEM_EFFECT_BLOCKED, EFFECT_REMOVED, GAME_FINISHED | 게임 진행 이벤트 |
| /user/queue/errors | USER | ERROR | 명령 실패 응답 |
| /user/queue/inventory | USER | INVENTORY_SYNC | 인벤토리 동기화(본인) |
| /user/queue/rooms | USER | ROOM_KICKED | 강퇴 알림(본인) |

---
## 3. 구독 조합 (권장)
- MAIN: /topic/chat/global
- MAIN(ROOM_LIST 패널): /topic/rooms/list
- WAITING_ROOM: /topic/rooms/{roomId}/lobby, /topic/rooms/{roomId}/chat
- BAN_PICK_SHOP: /topic/games/{gameId}, /topic/rooms/{roomId}/chat
- IN_GAME: /topic/games/{gameId}, /topic/rooms/{roomId}/chat, /topic/rooms/{roomId}/typing
- RESULT: 추가 구독 없음 (GAME_FINISHED 수신 직후 표시)
