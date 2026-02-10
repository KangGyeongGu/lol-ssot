## 0. 문서 목적
- UI 컴포넌트 API 설계 규칙을 정의한다.
- 디자인 토큰은 [[02_DESIGN/COLOR_SYSTEM.md]], [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]를 따른다.

## 관련 문서
- [[02_DESIGN/COLOR_SYSTEM.md]]
- [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]
- [[05_FRONTEND/FE_CONVENTIONS.md]]

---
## 1. Props 규칙
- props는 최소 단위로 분리한다(예: `size`, `variant`, `disabled`).
- boolean props는 `isXxx` 또는 `hasXxx` 네이밍을 사용한다.
- props 타입은 `defineProps<T>()` 제네릭으로 명시한다.
- 기본값은 컴포넌트 내부에서 정의한다.

---
## 2. Events 규칙
- 이벤트 이름은 `kebab-case`로 노출한다.
- `v-model` 사용 시 `modelValue` + `update:modelValue` 규칙을 따른다.
- emits 타입은 `defineEmits<T>()` 제네릭으로 명시한다.
- 이벤트는 의도 기반(예: `submit`, `confirm`)으로 정의한다.

---
## 3. Slots 규칙
- 슬롯은 `default` + 명시적 named slot만 사용한다.
- 불필요한 슬롯 남발 금지.

---
## 4. 디자인 토큰 매핑
- 컴포넌트의 색상/폰트는 토큰 키로만 지정한다.
- 토큰 매핑은 [[02_DESIGN/COLOR_SYSTEM.md]], [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]] 기준으로만 정의한다.
