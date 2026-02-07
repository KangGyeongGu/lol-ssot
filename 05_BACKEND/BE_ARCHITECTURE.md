# BE_ARCHITECTURE

## 0. 문서 목적
- 백엔드 모듈 경계와 책임 분리를 정의한다.
- 병렬 개발 시 충돌을 최소화한다.

## 관련 문서
- [[05_BACKEND/BE_CONVENTIONS.md]]
- [[05_BACKEND/BE_API_RULES.md]]
- [[05_BACKEND/BE_REALTIME_RULES.md]]
- [[05_BACKEND/BE_DATA_MODEL_RULES.md]]

---
## 1. 기본 모듈 구조(권장)
- `src/app`: 서버 부트스트랩
- `src/config`: 환경 설정/상수
- `src/common`: 공통 유틸/미들웨어/에러 핸들러
- `src/modules/<domain>`: 도메인 모듈 단위
- `src/modules/<domain>/controller`: HTTP 엔드포인트
- `src/modules/<domain>/service`: 비즈니스 로직
- `src/modules/<domain>/repo`: DB 접근
- `src/modules/<domain>/dto`: 요청/응답 DTO
- `src/realtime`: STOMP 연결/구독 처리
- `src/db`: DB 커넥션/마이그레이션
- `src/state`: Redis 실시간 상태 저장/조회

---
## 2. 책임 분리 원칙
- Controller는 요청/응답 매핑만 담당한다.
- Service는 비즈니스 규칙을 담당한다.
- Repo는 DB 접근만 담당한다.
- Realtime은 STOMP 이벤트 라우팅만 담당한다.
- DTO는 API 계약 스키마와 1:1로 유지한다.
- State는 Redis 실시간 상태 저장/조회 및 DB 스냅샷 반영을 담당한다.

---
## 3. 의존성 방향
- Controller → Service → Repo 단방향.
- Common은 어느 모듈도 참조하지 않는다.
- Realtime은 도메인 Service만 참조한다.
