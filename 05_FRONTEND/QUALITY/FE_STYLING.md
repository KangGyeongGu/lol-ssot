## 0. 문서 목적
- `--gu` 기반 스케일링과 토큰 적용 규칙을 정의한다.
- 디자인의 단일 진실은 [[02_DESIGN/COLOR_SYSTEM.md]], [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]이며, 본 문서는 적용 방식만 기술한다.

## 관련 문서
- [[02_DESIGN/COLOR_SYSTEM.md]]
- [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]

---
## 1. --gu 정의
- `--gu`는 **16:9 컨테이너 너비의 1%**다.
- 1920x1080은 **환산 기준**이며 고정 해상도 규칙이 아니다.
- 기준 환산: 1920 기준 `1gu = 19.2px`
- 환산 공식: `gu = px / 19.2`, `px = gu * 19.2`

---
## 2. --gu 계산 규칙
- 기본값: `--gu = 1vw`
- 화면이 16:9보다 넓을 때(height가 병목)에는 `--gu = calc(100vh * 16 / 900)`를 사용한다.
- 화면이 16:9보다 좁을 때(width가 병목)에는 `--gu = 1vw`를 유지한다.

---
## 3. 토큰/단위 규칙
- 모든 크기/간격/폰트/라운드/그림자는 `calc(var(--gu) * N)` 또는 토큰 변수만 사용한다.
- px/rem/em/vw/vh 직접 사용 금지(단, `--gu` 계산 정의는 예외).
- 1px 헤어라인은 `calc(var(--gu) * 0.0625)`로 표현한다(1920 기준 1px).
- 토큰 네이밍 예시: `--fontSize-*`, `--space-*`, `--radius-*`, `--shadow-*`, `--glow-*`.

---
## 4. 16:9 컨테이너 규칙
- 스케일링 컨테이너는 `aspect-ratio: 16 / 9`를 반드시 지정한다.
- 기준 크기는 `width: calc(var(--gu) * 100)`, `height: calc(var(--gu) * 56.25)`를 사용한다.
- 레이아웃 재배치는 금지하고 **스케일링만 허용**한다.

---
## 5. CSS 변수 네이밍 규칙
- 토큰 키의 `.`를 `-`로 변환하여 변수명을 만든다.
- 예: `color.bg.page` → `--color-bg-page`
- 예: `font.display` → `--font-display`

---
## 6. SCSS 사용 규칙
- 스타일 파일 확장자는 `.scss`로 통일한다.
- 전역 스타일은 `src/styles/` 하위에만 둔다.
- 컴포넌트는 `<style scoped lang="scss">`를 사용한다.

---
## 7. 컴포넌트 스타일 적용
- 공통 UI는 `shared` 컴포넌트에서만 정의한다.
- 컴포넌트 스타일은 기본적으로 scoped로 적용한다.

---
## 8. 금지
- px/rem/em/vw/vh 직접 사용
- `--gu` 없이 임의 크기/간격/폰트 지정
- 16:9 컨테이너의 aspect-ratio 누락
