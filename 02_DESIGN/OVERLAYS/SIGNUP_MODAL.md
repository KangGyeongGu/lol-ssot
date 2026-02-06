# OVERLAY_SIGNUP_MODAL

## 목적
- WELCOME 화면 위에 표시되는 SIGNUP 오버레이 상태.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]
- [[02_DESIGN/PAGES/LOGIN.md]]

---
## Source
- `lol web mockup (before)/1-1. 회원가입 모달.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Modal | 28.1 | 20.4 | 43.8 | 51.9 | 540,220,840,560 | 중앙 모달 |
| Title | 31.2 | 23.1 | 37.5 | 4.6 | 600,250,720,50 | 모달 타이틀 |
| Nickname Input | 31.2 | 30.6 | 37.5 | 5.2 | 600,330,720,56 | 입력 필드 |
| Language Chips | 31.2 | 38.9 | 37.5 | 14.8 | 600,420,720,160 | 2열 그리드 |
| CTA | 31.2 | 56.5 | 37.5 | 5.2 | 600,610,720,56 | 완료 버튼 |

---
## Component Inventory
- modal x1
- input x1
- chipButton x6 (활성 3, 비활성 3)
- primaryButton x1 (완료)

---
## Notes
- 완료 버튼은 입력 전 비활성.
- 모달 외부 클릭 시 닫힘 방지.
