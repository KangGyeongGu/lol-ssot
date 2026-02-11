## 목적
- IN_GAME(PLAY) 화면에 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/IN_GAME.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

## Required Data
- game state: remainingMs, players, coin, inventory
- active effects: item/spell effects and removals
- room chat messages (channel=INGAME, roomId)
- inventory sync (per user queue)

## Required States
- loading (initial)
- submission pending
- reconnecting
- error (REST/WS)

## Interactions
- 코드 제출 실패 시 알림을 표시한다(error.code: SUBMISSION_REJECTED, INVALID_LANGUAGE, INVALID_STAGE_ACTION, GAME_ALREADY_FINISHED, GAME_NOT_FOUND, VALIDATION_FAILED, UNAUTHORIZED).
- ITEM_USE / SPELL_USE 실패(ERROR 이벤트) 수신 시 알림을 표시한다.
- CHAT_SEND 실패(ERROR 이벤트) 수신 시 알림을 표시한다.
- 알림 문구는 서버 `error.code` 기준으로 프론트엔드에서 관리한다.

## Prohibited
- remainingMs 없이 플레이 상태 표시
