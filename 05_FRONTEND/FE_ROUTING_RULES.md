## 0. 문서 목적
- 라우팅/가드/전환의 **구현 패턴**을 정의한다.
- 사용자 흐름은 [[01_PRODUCT/USER_FLOWS.md]]가 단일 진실이다.

## 관련 문서
- [[01_PRODUCT/USER_FLOWS.md]]
- [[03_API/CONTRACT/REST/CONVENTIONS.md]]
- `[[03_API/PAGE_MAP/*.md]]`
- [[05_FRONTEND/FE_DESIGN_MAPPING.md]]
- [[05_FRONTEND/FE_STATE_RULES.md]]

---
## 1. 라우트 네이밍 규칙
- Route name은 `PageRoute`와 동일한 대문자 식별자를 사용한다.
- PageRoute 목록은 [[03_API/CONTRACT/REST/CONVENTIONS.md]]를 따른다.
- 예: `WELCOME`, `MAIN`, `WAITING_ROOM`, `BAN_PICK_SHOP`, `IN_GAME`, `RESULT`, `MY_PAGE`

---
## 2. 가드 배치 규칙
- 전역 라우팅 가드는 `router` 초기화 시 1회만 등록한다.
- 인증/active game 체크는 **가드에서 수행**하며, 세부 규칙은 [[01_PRODUCT/USER_FLOWS.md]]를 따른다.
- 가드 로직에서 직접 REST 호출 금지(스토어/서비스를 통해 호출).

---
## 3. 전환 규칙
- 페이지 전환은 `PageRoute` 기준으로만 수행한다.
- API 응답의 `pageRoute`가 유일한 전환 기준이다.
- 게임 FINISHED는 active game 대상이 아니며, RESULT는 이벤트 기반으로만 노출한다.

---
## 4. 코드 스플리팅 규칙
- 라우트 컴포넌트는 `dynamic import`로 지연 로드한다.
- 예외가 필요할 경우 사유를 주석으로 명시한다.

---
## 5. 페이지 데이터 로딩 규칙
- 페이지 초기 로딩은 페이지 전용 스토어/컴포저블에서 수행한다.
- 하위 컴포넌트에서 전역 로딩을 직접 트리거하지 않는다.

---
## 6. 디자인 참조 규칙
- 모든 라우트 구현은 [[05_FRONTEND/FE_DESIGN_MAPPING.md]]에 매핑된 디자인 문서를 반드시 참조한다.
