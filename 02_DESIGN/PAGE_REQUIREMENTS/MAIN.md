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

## Interactions
- 방 생성 실패 시 알림을 표시한다(error.code: ACTIVE_GAME_EXISTS, VALIDATION_FAILED, RATE_LIMITED, UNAUTHORIZED, FORBIDDEN).
- 전역 채팅 전송 실패(ERROR 이벤트) 수신 시 알림을 표시한다.
- 알림 문구는 서버 `error.code` 기준으로 프론트엔드에서 관리한다.

## Prohibited
- 하드코딩된 UI 문구
- 목록 상태 없이 무한 스크롤 표시
