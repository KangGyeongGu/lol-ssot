# BE_STACK

## 0. 문서 목적
- 백엔드 기술 스택의 **고정값**을 정의한다.
- 임의 변경/혼용을 금지한다.

---
## 1. 고정 스택
- Framework: Spring Boot
- ORM: Spring Data JPA
- Database: PostgreSQL
- Realtime State: Redis

---
## 2. 금지
- 다른 ORM/쿼리 도구(MyBatis, jOOQ 등) 도입 금지.
- 다른 DB로의 임의 변경 금지.
- Redis 외 임의 캐시/상태 저장소 도입 금지.
