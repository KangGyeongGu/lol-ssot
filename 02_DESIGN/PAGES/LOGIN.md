# PAGE_LOGIN

## 목적
- WELCOME(로그인) 진입 화면(사이버펑크 히어로 + 카카오 로그인 CTA).

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]
- [[02_DESIGN/OVERLAYS/SIGNUP_MODAL.md]]

---
## Source
- `lol web mockup (before)/1. 로그인페이지.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Logo/Title | 21.4 | 14.8 | 57.3 | 16.7 | 410,160,1100,180 | 로고 타이틀 중앙 정렬 |
| Subtitle | 29.2 | 27.8 | 41.7 | 3.7 | 560,300,800,40 | 타이틀 하단 문구 |
| CTA Stack | 35.4 | 33.3 | 29.2 | 7.4 | 680,360,560,80 | 카카오 버튼 1개 |
| Footer Copy | 35.4 | 50.0 | 29.2 | 3.7 | 680,540,560,40 | 소셜 로그인 안내 문구 |

---
## Component Inventory
- logoTitle x1
- subtitleText x1
- primaryButton x1 (카카오)
- helperText x1

---
## Notes
- 배경은 풀스크린 일러스트 + 어두운 오버레이.
- CTA 버튼은 카카오 단일 진입 버튼으로 사용한다.
