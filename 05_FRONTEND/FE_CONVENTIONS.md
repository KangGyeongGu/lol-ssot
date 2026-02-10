## 0. 문서 목적
- 프론트엔드 코드 작성 시 **일관된 컨벤션**을 강제한다.
- 팀/에이전트 간 코드 형태 불일치를 방지한다.

## 관련 문서
- [[05_FRONTEND/FE_STACK.md]]
- [[01_PRODUCT/COPY_TEXT.md]]

---
## 1. 네이밍 규칙
- Vue 컴포넌트 파일: `PascalCase.vue`
- 컴포저블: `useXxx.ts`
- Pinia 스토어: `useXxxStore.ts`
- 유틸/헬퍼: `xxx.util.ts`
- 타입/인터페이스: `xxx.types.ts`
- 상수: `xxx.constants.ts`
- DTO: `xxx.dto.ts`
- ViewModel: `xxx.vm.ts`

---
## 2. 파일/폴더 규칙
- 폴더명은 `kebab-case`를 사용한다.
- 한 파일에 하나의 역할만 둔다(예: API 호출 + UI 컴포넌트 혼합 금지).
- 라우트 단위 컴포넌트는 `src/pages/`에만 둔다.
- 페이지 전용 컴포넌트는 `src/pages/<Page>/components`에만 둔다.
- 범용 UI는 `src/shared/ui`에만 둔다.
- 범용 composables는 `src/shared/composables`에만 둔다.

---
## 3. Import 순서
- 외부 라이브러리 → 내부 절대경로(@/) → 상대경로 순서로 정렬한다.
- 동일 레벨 import는 알파벳 순서로 정렬한다.
- 순환 참조 금지.

---
## 4. Vue 컴포넌트 규칙
- `<script setup>`을 기본으로 사용한다.
- `defineProps`/`defineEmits`를 명시적으로 선언한다.
- props는 `camelCase`, 이벤트는 `kebab-case`로 노출한다.
- 컴포넌트에서 직접 REST/WS 호출 금지(스토어/서비스 통해 호출).
- 컴포넌트 스타일은 `<style scoped lang="scss">`를 기본으로 사용한다.

---
## 5. Sizing/Unit Rules (--gu)
- 모든 크기/간격/폰트/라운드는 `--gu` 기반 토큰만 사용한다.
- px/rem/em/vw/vh 직접 사용 금지(단, `--gu` 정의는 예외).
- 1920x1080은 **환산 기준**이며 고정 해상도 규칙이 아니다.
- 1px 헤어라인은 `calc(var(--gu) * 0.0625)`로 표현한다.
- 스케일링 컨테이너는 `aspect-ratio: 16 / 9`를 필수로 둔다.

---
## 6. i18n/문구 규칙
- UI 문구는 하드코딩 금지.
- 모든 문구는 [[01_PRODUCT/COPY_TEXT.md]] 키를 사용한다.

---
## 7. Vue Essential Rules (Priority A)
- 컴포넌트 이름은 반드시 멀티 워드로 작성한다(예: `BaseButton`).
- props는 반드시 명시적으로 정의한다.
- `v-for` 사용 시 항상 `key`를 지정한다(안정적인 고유 키 사용).
- `v-for`와 `v-if`를 같은 엘리먼트에 동시에 사용하지 않는다.

---
## 8. Composables 설계 규칙
- composable은 입력/출력 타입을 명시한다.
- 반환값은 객체 형태로 통일하고 필요한 값만 노출한다.
- 외부 API/WS 호출은 composable에서 직접 수행하지 않는다(스토어/서비스 경유).
- composable 내부 상태는 최소화하고 불변 데이터를 우선 사용한다.
- 공유 가능한 composable은 `src/shared/composables`에 둔다.
- 페이지/기능 전용 composable은 해당 폴더의 `composables/`에 둔다.

---
## 9. TypeScript 설계 규칙
- 암시적 `any` 금지.
- 외부 입력은 `unknown`으로 받고 경계에서 검증한다.
- `type`은 union/alias에 사용하고, `interface`는 확장 가능한 객체에 사용한다.
- 상수 맵은 `as const` 또는 `satisfies`로 고정한다.
- `enum` 사용 금지(상수 객체 + union 타입 사용).
