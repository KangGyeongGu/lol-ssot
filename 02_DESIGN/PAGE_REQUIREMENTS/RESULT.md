## 목적
- RESULT 화면에 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/RESULT.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

## Required Data
- result list: result, rankInGame, scoreDelta, coinDelta, expDelta, solved
- game meta: gameId, roomId, finishedAt

## Required States
- loading (result wait)
- error (event missing/invalid)

## Interactions
- GAME_FINISHED 데이터 누락/불일치 시 에러 상태를 표시한다.
- 알림 문구는 서버 `error.code` 기준으로 프론트엔드에서 관리한다.

## Prohibited
- 결과 없이 보상 영역 표시
