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

## Prohibited
- remainingMs 없이 플레이 상태 표시
