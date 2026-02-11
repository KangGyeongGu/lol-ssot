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
- host transfer pending (방장 위임 요청 처리 중)
- error (REST/WS)

## Interactions
- 방장 위임 성공 이벤트(ROOM_HOST_CHANGED, reason=MANUAL)에서 대상이 본인이면 알림 컴포넌트로 `NOTICE.HOST_TRANSFERRED`를 표시한다.
- 플레이어 그리드에서 방장은 항상 1행 1열에 위치한다.
- 신규 입장자는 항상 마지막 슬롯에 배치한다.
- 방장을 제외한 플레이어는 입장 순서를 유지한다.
- 방장 변경 시 신규 방장은 1행 1열로 이동한다.
- 방장 변경 시 나머지 플레이어의 상대적 순서는 유지한다.
- ROOM_KICKED 수신 시 알림 컴포넌트로 `NOTICE.KICKED`를 표시한 뒤 MAIN으로 이동한다.
- 방장 위임 실패 시 알림을 표시한다(error.code: NOT_HOST, PLAYER_NOT_IN_ROOM, INVALID_PLAYER_STATE, VALIDATION_FAILED).
- 게임 시작 실패 시 알림을 표시한다(error.code: NOT_HOST, INVALID_PLAYER_STATE).
- 플레이어 강퇴 실패 시 알림을 표시한다(error.code: NOT_HOST, PLAYER_NOT_IN_ROOM, INVALID_PLAYER_STATE).
- 실시간 명령 실패(ERROR 이벤트) 수신 시 알림을 표시한다.
- 알림 문구는 서버 `error.code` 기준으로 프론트엔드에서 관리한다.

## Prohibited
- 플레이어 상태(READY/UNREADY) 없이 슬롯 표시
