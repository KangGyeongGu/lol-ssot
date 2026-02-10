## 목적
- WAITING_ROOM(LOBBY) 화면에 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/WAITING_ROOM.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

## Required Data
- room snapshot: roomId, title, gameType, maxPlayers, hostUserId
- players: userId, nickname, readyState, connectionState
- my role: isHost, myReadyState
- room chat messages (channel=INGAME, roomId)
- game start trigger (pageRoute)

## Required States
- loading (initial)
- kicked
- host changed
- error (REST/WS)

## Prohibited
- 플레이어 상태(READY/UNREADY) 없이 슬롯 표시
