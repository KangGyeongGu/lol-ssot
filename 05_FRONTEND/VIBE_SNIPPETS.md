## 0. 문서 목적
- 디자인 규칙을 적용하는 **짧은 스니펫 예시**를 모아둔다.
- 규칙의 단일 진실은 [[02_DESIGN/COLOR_SYSTEM.md]], [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]이며, 본 문서는 예시 전용이다.

## 관련 문서
- [[02_DESIGN/COLOR_SYSTEM.md]]
- [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]

---
## 1. Glass Panel (예시)
```css
.panel {
  background: var(--color-bg-panel);
  border: 1px solid var(--color-border-cyan);
  box-shadow: var(--shadow-panel);
  backdrop-filter: blur(12px);
}
```

---
## 2. Neon Border (예시)
```css
.neon {
  border: 1px solid var(--color-border-magenta);
  box-shadow: var(--glow-magenta);
}
```
