# FE_STYLING

## 0. 문서 목적
- 디자인 토큰/레이아웃 규칙을 프론트 코드에 **일관되게 적용**하기 위한 규칙을 정의한다.
- 디자인의 단일 진실은 `[[02_DESIGN/*.md]]`이며, 본 문서는 적용 방식만 기술한다.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[02_DESIGN/TOKENS.json.md]]
- [[02_DESIGN/COMPONENTS.json.md]]

---
## 1. 토큰 적용 규칙
- 색상/타이포/스페이싱은 토큰 키로만 사용한다.
- 임의 색상/폰트 하드코딩 금지.
- 토큰은 CSS 변수로 매핑하여 사용한다.

---
## 2. CSS 변수 네이밍 규칙
- 토큰 키의 `.`를 `-`로 변환하여 변수명을 만든다.
- 예: `color.bg.page` → `--color-bg-page`
- 예: `font.display` → `--font-display`

---
## 3. SCSS 사용 규칙
- 스타일 파일 확장자는 `.scss`로 통일한다.
- 전역 스타일은 `src/styles/` 하위에만 둔다.
- 컴포넌트는 `<style scoped lang=\"scss\">`를 사용한다.

---
## 4. 16:9 스케일 규칙
- 레이아웃 기준은 1920x1080 캔버스다.
- 화면 크기 변화 시 전체 스케일만 적용하고 **재배치는 금지**한다.
- 스케일 계산은 `LAYOUT_RULES`의 비율 규칙을 따른다.

---
## 5. 컴포넌트 스타일 적용
- 컴포넌트 스타일은 [[02_DESIGN/COMPONENTS.json.md]] 매핑을 따른다.
- 공통 UI는 shared 컴포넌트에서만 정의한다.
- 컴포넌트 스타일은 기본적으로 scoped로 적용한다.

---
## 6. 금지
- inline style로 토큰을 직접 박는 행위 금지.
- 디자인 문서와 다른 레이아웃 재배치 금지.
