# OVERLAY_ROOM_CREATE_MODAL

## 목적
- MAIN 페이지에서 방 생성 클릭 시 표시되는 모달.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]
- [[02_DESIGN/PAGES/MAIN.md]]

---
## Source
- `lol web mockup (before)/2-1. 방생성 모달.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Modal | 26.6 | 17.6 | 46.9 | 64.8 | 510,190,900,700 | 중앙 모달 (maxWidth 900) |
| Title | 30.2 | 21.3 | 39.6 | 5.6 | 580,230,760,60 | "새 게임 생성" |
| Room Name Input | 30.2 | 28.7 | 39.6 | 5.2 | 580,310,760,56 | 글자수 카운트 포함 |
| Game Type Toggle | 30.2 | 36.1 | 39.6 | 5.2 | 580,390,760,56 | 랭크/일반 2분할 |
| Player Count Chips | 30.2 | 43.5 | 39.6 | 5.6 | 580,470,760,60 | 2~6 칩 |
| Language Grid | 30.2 | 51.9 | 39.6 | 14.8 | 580,560,760,160 | 2행 그리드 |
| CTA Row | 30.2 | 68.5 | 39.6 | 5.2 | 580,740,760,56 | 취소/생성 |

---
## Component Inventory
- modal x1
- input x1
- toggleButton x2
- chipButton x5
- languageButton x6
- primaryButton x1
- secondaryButton x1

---
## Notes
- 선택 항목만 네온 강조.
- 생성 버튼은 필수 입력 충족 시 활성.
