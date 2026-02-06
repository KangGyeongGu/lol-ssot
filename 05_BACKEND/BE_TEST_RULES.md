# BE_TEST_RULES

## 0. 문서 목적
- Spring Boot + JPA + PostgreSQL 환경의 테스트 전략/케이스 작성 규칙을 정의한다.
- 단일 진실(계약/도메인 규칙)은 다른 문서를 따른다.

## 관련 문서
- [[05_BACKEND/BE_STACK.md]]
- [[05_BACKEND/BE_CONVENTIONS.md]]
- [[05_BACKEND/BE_API_RULES.md]]
- [[05_BACKEND/BE_REALTIME_RULES.md]]
- [[05_BACKEND/BE_DATA_MODEL_RULES.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]
- [[03_API/CONTRACT/REST/AUTH_GUARDS.md]]
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

---
## 1. 테스트 분류 및 사용 기준
- Web 계층: Controller 검증은 @WebMvcTest 기반으로 작성한다.
- Repository 계층: JPA 검증은 @DataJpaTest 기반으로 작성한다.
- 통합 테스트: 전체 컨텍스트 검증은 @SpringBootTest를 사용한다.
- DB 통합 테스트: PostgreSQL은 Testcontainers로 검증한다.

---
## 2. REST 테스트 케이스 규칙
- 각 엔드포인트는 성공 케이스 1개 이상 작성한다.
- 실패 케이스는 `ERROR_MODEL`에 정의된 주요 코드 기준으로 작성한다.
- 인증/가드 실패 케이스는 `AUTH_GUARDS` 규칙을 따른다.
- 응답 Envelope와 `error.code`를 검증한다.

---
## 3. 실시간 테스트 케이스 규칙
- 이벤트 타입/Envelope 포맷은 REALTIME_CONVENTIONS를 따른다.
- `type` 불일치, 권한 실패 케이스를 포함한다.

---
## 4. 데이터 정합성 테스트
- DTO → Entity 매핑 테스트를 작성한다.
- DTO → ViewModel 변환은 API와 1:1로 검증한다.
- ID/시간 포맷은 ISO-8601 UTC 기준으로 검증한다.

---
## 5. Spring Boot 테스트 설정 규칙
- @WebMvcTest는 MVC 컴포넌트만 대상으로 하며, 필요한 협력자는 Mock으로 대체한다.
- @DataJpaTest는 기본적으로 in-memory DB를 사용하므로, Postgres Testcontainers 사용 시 교체 설정을 적용한다.
- 전체 서버 테스트는 @SpringBootTest(webEnvironment=RANDOM_PORT)로 실행한다.
- Testcontainers 사용 시 @ServiceConnection을 통해 연결 정보를 주입한다.

---
## 6. 금지
- 인메모리 DB로 Postgres 고유 동작을 대체하지 않는다.
- 계약(OpenAPI/Realtime)을 테스트에서 임의 변경하지 않는다.
