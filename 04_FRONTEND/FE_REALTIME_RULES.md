# FE_REALTIME_RULES

## 0. 문서 목적
- 실시간(WebSocket/STOMP) 연결/구독 **관리 패턴**을 정의한다.
- 타이밍/토픽/이벤트 규칙은 관련 문서가 단일 진실이다.

## 관련 문서
- [[03_API/LIFECYCLE.md]]
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]
- [[04_FRONTEND/FE_STATE_RULES.md]]

---
## 1. 연결 관리 원칙
- WebSocket 연결은 단일 인스턴스로 유지한다.
- 연결/재연결/해제는 `realtime/` 모듈만 담당한다.
- 컴포넌트에서 직접 연결 생성 금지.

---
## 2. 구독 관리 원칙
- 구독/해제는 페이지/스토어 단위로 요청한다.
- `realtime/` 모듈은 구독 레지스트리를 유지하고 재연결 시 자동 복구한다.
- 구독 해제는 페이지 이탈 시점에 반드시 수행한다.

---
## 3. 이벤트 처리 원칙
- 이벤트 핸들러는 `type` 기준으로 분기한다.
- 이벤트 → 스토어 업데이트는 중앙 핸들러를 통해 수행한다.
- UI 컴포넌트에서 이벤트 직접 처리 금지.

---
## 4. 시간 동기화 원칙
- 시간 기준은 `meta.serverTime`이다.
- 클라이언트는 오프셋을 계산해 서버 시간을 추정한다.
  - offset = serverTime - ((clientSendTime + clientReceiveTime) / 2)
- 오프셋 샘플은 RTT가 가장 낮은 값 또는 중앙값을 사용한다.
- 로컬 타이머는 `performance.now()` 등 monotonic clock을 사용한다.
- 재동기화 주기:
  - 기본: 10초
  - BAN/PICK/SHOP 단계: 2초

---
## 5. 금지
- 페이지마다 별도 WebSocket 인스턴스 생성 금지.
- 이벤트 페이로드를 UI에서 직접 가공/추론 금지.
