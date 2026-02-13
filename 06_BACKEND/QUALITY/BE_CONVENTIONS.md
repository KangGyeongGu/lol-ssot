## 0. 문서 목적
- 백엔드 코드 작성 시 일관된 컨벤션을 강제한다.

## 관련 문서
- [[06_BACKEND/SPEC/BE_ARCHITECTURE.md]]
- [[06_BACKEND/QUALITY/BE_STACK.md]]
- [[03_API/CONTRACT/REST/CONVENTIONS.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]

---
## 1. 네이밍 규칙
- 모듈명: `room`, `game`, `auth` 등 도메인 소문자.
- Controller: `<Domain>Controller`.
- Service: `<Domain>Service`.
- Repo: `<Domain>Repository`.
- DTO: `<Domain><Action>Request`, `<Domain><Action>Response`.

---
## 2. 파일/폴더 규칙
- 폴더명은 `kebab-case`를 사용한다.
- 도메인 모듈 밖에 비즈니스 로직을 두지 않는다.
- 공통 유틸은 `src/common`에만 둔다.

---
## 3. Spring 규칙
- DI는 생성자 주입을 사용한다(필드 주입 금지).
- `@RestController`, `@Service`, `@Repository` 역할을 명확히 분리한다.
- `@Transactional`은 Service 레이어에서만 사용한다.
- Entity를 API 응답으로 직접 노출하지 않는다(DTO 사용).

---
## 4. 에러 처리 규칙
- 에러 코드는 [[03_API/CONTRACT/REST/ERROR_MODEL.md]]만 사용한다.
- HTTP 상태 코드는 [[03_API/CONTRACT/REST/CONVENTIONS.md]] 규칙을 따른다.
- 에러 메시지는 로그용이며 클라이언트 노출 금지.

---
## 5. 시간/ID 규칙
- 모든 시간은 ISO-8601 UTC 문자열을 사용한다.
- 모든 ID는 문자열로 취급한다.
