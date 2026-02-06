# FE_STACK

## 0. 문서 목적
- 프론트엔드 런타임/빌드/의존성의 **기본 전제**를 정의한다.
- 버전의 단일 진실은 실제 코드 레포의 `package.json`이며, 본 문서는 **종류와 사용 원칙**만 정의한다.

## 관련 문서
- [[04_FRONTEND/FE_CONVENTIONS.md]]

---
## 1. 기본 스택
- Build: Vite
- Framework: Vue 3
- Component: Single File Component (.vue)
- API Style: REST + WebSocket(STOMP)
- Styling: SCSS/Sass
- Language: TypeScript

---
## 2. 언어/구문 규칙
- Vue는 Composition API를 기본으로 사용한다.
- `<script setup>` 스타일을 기본으로 사용한다.
- TypeScript만 사용하며 JavaScript 사용은 금지한다.

---
## 3. 환경 변수 규칙
- 프론트에서 사용하는 환경 변수는 `VITE_` prefix를 사용한다.
- 환경 변수 이름/의미는 `README.md`에 테이블로 기록한다.

---
## 4. 필수 의존성 원칙
- 라우팅: Vue Router
- 상태 관리: Pinia (프로젝트 단일 사용)
- HTTP 클라이언트: 프로젝트 단일 선택(fetch 또는 axios 중 택1)
- WebSocket/STOMP 클라이언트: 프로젝트 단일 선택
- CSS Preprocessor: Sass(dart-sass) 단일 사용

---
## 5. 금지
- 동일 역할 라이브러리의 혼용 금지(예: axios + fetch 동시 사용 금지)
- Vue Options API 사용 금지
- CSS-in-JS 도입 금지
