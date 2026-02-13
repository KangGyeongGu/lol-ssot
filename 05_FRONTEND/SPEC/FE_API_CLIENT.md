## 0. 문서 목적
- REST 호출 구조와 에러 분기 **코드 패턴**을 정의한다.
- API 규약/스키마는 `03_API/CONTRACT/REST/*.md`가 단일 진실이다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REST/CONVENTIONS.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]
- [[01_PRODUCT/COPY_TEXT.md]]
- [[05_FRONTEND/SPEC/FE_STATE_RULES.md]]

---
## 1. 호출 구조 원칙
- 모든 REST 호출은 `api/` 모듈에서만 수행한다.
- 컴포넌트/페이지에서 직접 `fetch/axios` 사용 금지.
- 스토어는 `api/` 모듈을 통해서만 서버와 통신한다.

---
## 2. 응답 처리 규칙
- 성공 응답은 `data`만 사용한다.
- 실패 응답은 HTTP status가 아니라 `error.code`로 분기한다.
- `error.code` 목록은 [[03_API/CONTRACT/REST/ERROR_MODEL.md]]만 사용한다.

---
## 3. DTO vs ViewModel 분리
- DTO 타입은 `src/api/dtos`에만 둔다.
- ViewModel 타입은 `src/entities` 또는 `src/shared/types`에 둔다.
- DTO → ViewModel 변환은 `src/entities`에서 수행한다.
- 스토어/컴포넌트는 DTO를 직접 사용하지 않는다.

---
## 4. 에러 분기 표준
- 모든 에러 분기는 `error.code` switch 기반으로 처리한다.
- UI 메시지는 [[01_PRODUCT/COPY_TEXT.md]] 키로만 표시한다.
- 공통 에러 처리(UNAUTHORIZED 등)는 전역 에러 핸들러에서 수행한다.

---
## 5. 금지
- API 응답 스키마를 프론트에서 재정의 금지.
- 상태 코드를 직접 분기 기준으로 사용하는 것 금지.
