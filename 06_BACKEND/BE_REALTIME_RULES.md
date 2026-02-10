## 0. 문서 목적
- 실시간(STOMP) 이벤트/커맨드 구현 규칙을 정의한다.
- 계약의 단일 진실은 `03_API/CONTRACT/REALTIME` 문서다.

## 관련 문서
- [[03_API/LIFECYCLE.md]]
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 1. 연결 규칙
- WebSocket endpoint는 `/ws`로 고정한다.
- 인증 헤더 규칙은 `REALTIME_CONVENTIONS`를 따른다.

---
## 2. 이벤트/커맨드 규칙
- 모든 메시지는 Envelope 포맷을 사용한다.
- `type` 값은 EVENTS/COMMANDS 목록과 일치해야 한다.
- 서버 시간은 `meta.serverTime`으로 제공한다.

---
## 3. 오류 처리
- 실시간 명령 실패는 `/user/queue/errors`로 ERROR 이벤트를 전송한다.
