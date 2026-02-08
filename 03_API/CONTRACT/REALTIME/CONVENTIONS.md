# REALTIME_CONVENTIONS

## 0. 문서 목적
- 이 문서는 실시간(WebSocket/STOMP) 통신 규칙을 정의한다.
- 채팅/타이핑/단계 전환 알림/아이템 효과는 본 문서와 EVENT/COMMAND/ TOPIC 문서를 따른다.
- REST는 스냅샷 + 명령만 담당한다.

## 관련 문서
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 1. 전송 방식
- WebSocket 기반 실시간 통신을 사용한다.
- STOMP 사용을 전제로 하며, 아래 destination 규칙을 따른다.

### 1.1 Prefix
- Publish(서버 → 클라이언트): `/topic/**`
- User Queue(서버 → 특정 사용자): `/user/queue/**`
- Command(클라이언트 → 서버): `/app/**`

### 1.2 WebSocket Endpoint
- 기본 경로: `/ws`
- 예시:
  - prod: `wss://{host}/ws`
  - dev: `ws://{host}/ws`
- 실제 호스트/프로토콜은 배포 환경 설정을 따른다.

---
## 2. 인증
- 연결 시 `Authorization: Bearer <JWT>` 헤더를 사용한다.
- 인증 실패 시 연결이 거부된다.

---
## 3. 메시지 Envelope
### 3.1 Event (서버 → 클라이언트)
```json
{
  "type": "EVENT_TYPE",
  "data": {},
  "meta": {
    "eventId": "string",
    "serverTime": "2026-01-26T12:34:56Z"
  }
}
```

### 3.2 Command (클라이언트 → 서버)
```json
{
  "type": "COMMAND_TYPE",
  "data": {},
  "meta": {
    "commandId": "string"
  }
}
```
- `type` 값은 EVENTS/COMMANDS 문서의 타입 목록과 일치해야 한다.

---
## 4. 시간/정렬 규칙
- 모든 시간은 ISO-8601 UTC 문자열을 사용한다.
- `meta.serverTime`이 기준이며, 클라이언트는 이 값을 타이머 동기화에 사용한다.

### 4.1 클라이언트 시간 동기화
- 클라이언트는 서버 시간을 권위 시간으로 사용한다.
- TIME_SYNC 이벤트는 `/user/queue/time`으로 전송된다.
- 오프셋 계산식(예시):
  - offset = serverTime - ((clientSendTime + clientReceiveTime) / 2)
- 오프셋 샘플은 RTT가 가장 낮은 값 또는 중앙값을 사용한다.
- 로컬 타이머는 `performance.now()` 등 monotonic clock을 사용한다.
- 재동기화 주기:
  - 기본: 10초
  - BAN/PICK/SHOP 단계: 2초
- remainingMs는 `stage_deadline_at - meta.serverTime` 기준으로 계산한다.

---
## 5. 오류 처리
- 실시간 명령 실패 시 `/user/queue/errors`로 ERROR 이벤트를 전송한다.
- ERROR 이벤트의 `data.code`는 REST ERROR_MODEL의 코드를 사용한다.

---
## 6. 범위 원칙
- 채팅/타이핑/단계 전환/효과 알림은 실시간으로 전달한다.
- 밴/픽/구매/제출은 REST로 수행한다.
- 밴/픽/구매 결과는 `/topic/games/{gameId}` 이벤트로 전파한다.
- 아이템/스펠 **사용** 명령은 실시간(Command)으로 수행한다.

---
## 7. 채팅 채널 스코프
- GLOBAL 채팅
  - Topic: `/topic/chat/global`
  - `channelType = GLOBAL`
  - `roomId = null`
- INGAME 채팅
  - Topic: `/topic/rooms/{roomId}/chat`
  - `channelType = INGAME`
  - `roomId` 필수
  - 범위: WAITING_ROOM ~ IN_GAME

---
## 8. ROOM_LIST 동기화 규칙
- MAIN 내부 ROOM_LIST 패널은 `GET /rooms` 스냅샷 + `/topic/rooms/list` 델타 이벤트를 함께 사용한다.
- 현재 화면에 보이는 방(row)의 상태 변화는 이벤트 수신 즉시 UI에 반영한다.
- 현재 페이지 범위 밖 구조 변화(생성/삭제/정렬 영향)는 즉시 리스트 재배열하지 않고 업데이트 인디케이터로 누적한다.
- 사용자가 업데이트 버튼을 누르면 현재 필터/페이지 기준으로 `GET /rooms` 재조회한다.
- 보정 재동기화(권장): ROOM_LIST 패널 체류 중 20~30초 간격으로 `GET /rooms` 재조회.
