## 0. 문서 목적
- 프론트엔드 모듈 경계와 책임 분리를 정의한다.
- 코드가 “어디에 위치해야 하는지”를 통제한다.

## 관련 문서
- [[05_FRONTEND/QUALITY/FE_CONVENTIONS.md]]
- [[05_FRONTEND/SPEC/FE_ROUTING_RULES.md]]
- [[05_FRONTEND/SPEC/FE_STATE_RULES.md]]
- [[05_FRONTEND/SPEC/FE_API_CLIENT.md]]
- [[05_FRONTEND/SPEC/FE_REALTIME_RULES.md]]

---
## 1. 기본 폴더 구조(권장)
- `src/app`: 앱 초기화, 라우터/스토어 등록
- `src/router`: 라우트 정의, 가드
- `src/pages`: 라우트 단위 페이지
- `src/pages/<Page>/components`: 해당 페이지 전용 컴포넌트
- `src/pages/<Page>/composables`: 해당 페이지 전용 composables
- `src/features`: 사용자 액션 단위 기능
- `src/features/<Feature>/composables`: 기능 전용 composables
- `src/entities`: 도메인 데이터 표현/변환
- `src/widgets`: 페이지 조합용 UI 블록
- `src/shared/ui`: 범용 UI 컴포넌트
- `src/shared/composables`: 범용 composables
- `src/shared/types`: 공용 타입
- `src/shared/utils`: 공용 유틸
- `src/shared/constants`: 공용 상수
- `src/stores`: Pinia 스토어
- `src/api`: REST 클라이언트
- `src/api/dtos`: API 요청/응답 DTO
- `src/realtime`: WebSocket/STOMP 클라이언트
- `src/styles`: 전역 스타일/토큰 매핑
- `src/assets`: 정적 리소스

---
## 2. 책임 분리 원칙
- `api/`는 HTTP 호출만 담당한다.
- `realtime/`는 WebSocket 연결/구독만 담당한다.
- `stores/`는 상태/동기화의 단일 진실이다.
- `pages/`는 UI 조합과 화면 상태 연결만 담당한다.
- `pages/<Page>/components`는 해당 페이지 전용 UI만 둔다.
- `shared/ui`, `widgets`는 순수 UI 렌더링 중심으로 유지한다.
- `entities/`는 DTO → ViewModel 변환과 도메인 타입을 담당한다.

---
## 3. 의존성 방향
- 상위 레이어는 하위 레이어만 참조한다.
- `shared`는 어떤 레이어도 참조하지 않는다.
- `pages`는 `api/realtime`을 직접 참조하지 않는다.
