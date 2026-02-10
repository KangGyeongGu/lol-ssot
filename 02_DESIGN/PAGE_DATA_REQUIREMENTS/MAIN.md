## 목적
- MAIN 화면에 반드시 표시되어야 하는 데이터/상태를 정의한다(레이아웃 제외).

## 관련 문서
- [[03_API/PAGE_MAP/MAIN.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

## Required Data
- 사용자 요약: nickname, tier, score, level, exp, coin
- 방 목록 스냅샷: roomId, title, gameType, status, currentPlayers, maxPlayers, joinable
- 실시간 플레이어 랭킹 리스트
- 알고리즘 밴/픽률 리스트
- 전역 채팅 메시지(channel=GLOBAL)

## Required States
- loading (initial)
- empty room list
- error (REST/WS)

## Prohibited
- 하드코딩된 UI 문구
- 목록 상태 없이 무한 스크롤 표시
