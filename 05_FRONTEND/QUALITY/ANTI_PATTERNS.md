## 0. 문서 목적
- 프론트엔드 구현에서 **금지되는 패턴**을 명시한다.

## 관련 문서
- [[05_FRONTEND/QUALITY/FE_CONVENTIONS.md]]
- [[05_FRONTEND/SPEC/FE_API_CLIENT.md]]
- [[05_FRONTEND/SPEC/FE_REALTIME_RULES.md]]
- [[02_DESIGN/COLOR_SYSTEM.md]]
- [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]

---
## 1. 데이터/통신
- 컴포넌트에서 직접 REST 호출
- 컴포넌트에서 직접 WebSocket 연결/구독
- HTTP status 기반 분기(반드시 `error.code` 사용)

---
## 2. UI/문구
- UI 문구 하드코딩
- 토큰 없는 색상/폰트 사용
- `--gu` 없이 크기/간격/폰트 지정
- px/rem/em/vw/vh 직접 사용
- 16:9 스케일 컨테이너의 aspect-ratio 누락

---
## 3. 상태/구조
- 스토어 상태를 컴포넌트에서 직접 변형
- 동일 데이터의 중복 저장
- 레이어 역참조(`shared`가 상위 레이어 참조)

---
## 4. Vue Essential 위반
- 단일 단어 컴포넌트 이름 사용
- `v-for`에 `key` 누락
- `v-for`와 `v-if`를 같은 엘리먼트에 동시 사용

---
## 5. TypeScript 안티패턴
- `any` 또는 암시적 `any` 사용
- `@ts-ignore`, `@ts-nocheck` 사용
- `as unknown as` 이중 캐스팅
- 비검증 외부 입력을 바로 사용
- DTO를 UI/스토어에서 직접 사용
- `enum` 사용
