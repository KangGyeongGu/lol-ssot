# Project Implementation Strategy

## 1. 개요
본 문서는 `league-of-algologic` 프론트엔드 프로젝트의 전체 구현 순서와 전략을 정의합니다.
실무 표준인 **"Feature-First + Thin Core Layer"** 방식을 채택하여, 화면 단위의 빠른 검증과 안정적인 인프라 구축을 동시에 달성합니다.

## 2. 채택 전략: Feature-First + Thin Core Layer

### 핵심 원칙
1.  **Thin Core First**: 기능 개발 전, `API Client`, `Auth Token`, `Global Error/Loading` 등 최소한의 공통 인프라를 먼저 구축합니다.
2.  **Vertical Slicing**: 이후 각 기능(로그인, 메인 등)은 `API` → `Store` → `UI`를 수직으로 한 번에 구현하여 즉시 검증합니다.
3.  **Refactoring Rule**: 중복 코드는 처음부터 공통화하지 않고, **2개 이상의 Feature에서 사용될 때** `shared`로 이동시킵니다.

## 3. 전체 구현 로드맵

### Phase 0: Thin Core Layer (선구축)
모든 기능의 기반이 되는 최소 공통 레이어입니다.
- **API Client**: Axios/Fetch 래퍼, Interceptor (Req/Res), Error Handling (`FE_API_CLIENT.md` 준수)
- **Auth Management**: JWT 토큰 저장/갱신 로직, 로그인 가드 기초
- **Global UI**: Root Layout, Global Toast/Modal, Loading Indicator

### Phase 1: Authentication Feature (Vertical)
사용자 진입과 인증 흐름을 완성합니다.
- **Domain**: `users`
- **Pages**: `LOGIN` (Kakao Auth), `SIGNUP`, `WELCOME`
- **Key Logic**: 인가 코드 처리, 회원가입 폼 전송, 토큰 저장

### Phase 2: Lobby Feature (Vertical)
메인 활동 공간을 구현합니다.
- **Domain**: `rooms`
- **Pages**: `MAIN` (Lobby), `MY_PAGE`
- **Key Logic**: 프로필 조회, 방 목록 조회(WebSocket 연결 전 HTTP 조회 우선 검증)

### Phase 3: Room & Realtime System (Vertical)
실시간성이 중요한 기능을 구현합니다.
- **Domain**: `realtime`
- **Pages**: `WAITING_ROOM`
- **Key Logic**: WebSocket 연결/구독, 방 멤버 동기화, 채팅

### Phase 4: Game Play (Vertical)
핵심 게임 로직을 구현합니다.
- **Domain**: `games`
- **Pages**: `BAN_PICK_SHOP`, `IN_GAME`
- **Key Logic**: IDE 통합, 게임 상태 동기화, 타이머

---

## 4. 상세 작업 워크플로우 (Workflow)

기능 구현(Log 단위) 시 아래 순서를 따릅니다.

1.  **Infra Check**: 해당 기능에 필요한 Core가 부족하다면 보강 (예: 새 API 에러 코드 대응)
2.  **DTO/Type**: OpenAPI 기준 입출력 타입 정의 (`src/api/dtos`)
3.  **API Method**: `src/api`에 엔드포인트 추가
4.  **Store**: `src/stores`에 상태/액션 추가 (데이터 페칭, 가공)
5.  **View/Component**: `src/pages` 및 `src/features` UI 구현
6.  **Integration**: 라우터 연결 및 E2E 테스트 (Browser)

이 전략에 따라 **Log 004**는 **[Phase 0 + Phase 1] Core Layer 구축 및 인증 기능 구현**으로 통합하여 진행하는 것을 권장합니다.
