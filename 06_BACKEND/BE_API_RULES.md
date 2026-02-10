## 0. 문서 목적
- REST API 계약을 백엔드 코드로 구현하는 규칙을 정의한다.
- 계약의 단일 진실은 `03_API` 문서다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REST/CONVENTIONS.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]
- [[03_API/CONTRACT/REST/AUTH_GUARDS.md]]

---
## 1. 계약 준수 규칙
- OPENAPI에 없는 엔드포인트 추가 금지.
- 요청/응답 스키마는 OPENAPI와 1:1로 일치해야 한다.
- 모든 응답은 공통 Envelope를 사용한다.

---
## 2. 인증/가드 규칙
- 인증/가드 실패 코드는 AUTH_GUARDS.md와 일치해야 한다.
- 가드는 프론트에서 추론하지 않으며, 서버가 authoritative하다.

---
## 3. 에러 코드 규칙
- 모든 실패는 ERROR_MODEL.md의 code만 사용한다.
- 신규 에러 추가 시 ERROR_MODEL.md를 먼저 갱신한다.

---
## 4. 버전/경로 규칙
- REST prefix는 `/api/v1`로 고정한다.
- Path/Query 네이밍 규칙은 CONVENTIONS.md를 따른다.
