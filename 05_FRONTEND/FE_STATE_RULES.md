## 0. 문서 목적
- 상태 관리 원칙과 스토어 구조 패턴을 정의한다.
- 서버가 authoritative이며, 프론트는 상태를 추론하지 않는다.

## 관련 문서
- [[03_API/CONTRACT/REST/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/LIFECYCLE.md]]
- [[05_FRONTEND/FE_NOTIFICATION_MESSAGES.md]]

---
## 1. 상태 분류 규칙
- Local State: 컴포넌트 내부에서만 사용
- UI State: 페이지/패널 상태(스토어 관리)
- Server State: REST/실시간 데이터(스토어 관리)

---
## 2. 스토어 구조 원칙
- 스토어는 도메인 단위로 분리한다.
- 스토어는 **서버 스냅샷 + 실시간 이벤트**를 단일 상태로 통합한다.
- 동일 데이터를 여러 스토어에 중복 보관 금지.
- 스토어 상태는 ViewModel 타입만 보관한다.

---
## 3. 데이터 흐름 규칙
- 데이터 흐름은 `api/realtime → store → page/component` 단방향만 허용한다.
- 페이지/컴포넌트는 스토어를 통해서만 서버 상태를 읽는다.

---
## 4. 동기화 원칙
- REST 응답은 스냅샷으로 취급하고 항상 덮어쓴다.
- 실시간 이벤트는 스냅샷 이후에만 반영한다.
- 서버 타임(`meta.serverTime`) 기준으로 타이머를 동기화한다.
- TIME_SYNC 이벤트(`/user/queue/time`)로 오프셋을 갱신한다.
- BAN/PICK/SHOP 단계 타이머는 10초 고정 규칙을 따른다.

---
## 5. 금지
- 서버 규칙을 클라이언트에서 추론/복제 금지.
- 컴포넌트에서 스토어 상태를 직접 변형 금지.

---
## 6. 알림/에러 문구 규칙
- 서버 응답의 `error.code`에 대한 안내 문구는 프론트엔드에서 관리한다.
- 동일 `error.code`는 동일 문구로 매핑되며, 서버에서 문구를 전달하지 않는다.
- 이벤트 기반 알림은 `NOTICE.*` 키를 사용한다.
