## 목적
- MAIN 내부 ROOM_LIST 패널 상태에서 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/ROOM_LIST.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

## Required Data
- room list: roomId, title, gameType, status, currentPlayers, maxPlayers, joinable
- listVersion
- filter/query params (roomName, language, gameType)
- pagination (cursor, limit)
- update indicator count (listVersion diff)

## Required States
- loading (initial/search/update)
- empty list
- error (REST/WS)

## Prohibited
- listVersion 없이 실시간 업데이트 반영
