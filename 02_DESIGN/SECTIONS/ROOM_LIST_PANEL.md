# SECTION_ROOM_LIST_PANEL

## 목적
- MAIN 페이지 내 **헤더 하단 영역**에서 Room List가 표시되는 패널.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]
- [[02_DESIGN/PAGES/MAIN.md]]

---
## Source
- `lol web mockup (before)/2-2. 방리스트 조회 페이지.png`

---
## Layout Map (16:9 비율 기준)
| 영역             |   x% |   y% |   w% |   h% | ref(px)         | 비고                   |
| -------------- | ---: | ---: | ---: | ---: | --------------- | -------------------- |
| Header Bar     |  4.2 | 10.2 | 91.7 |  5.6 | 80,110,1760,60  | 리스트 새로고침, 업데이트 배지, 뒤로가기/필터/검색 |
| Room Grid Area |  4.2 | 17.6 | 64.6 | 77.6 | 80,190,1240,838 | 방 카드 리스트             |
| View Toggle    | 70.0 | 11.1 |  6.2 |  3.7 | 1344,120,120,40 | 그리드/리스트 토글           |
| Pagination     | 47.9 | 11.1 | 12.5 |  3.7 | 920,120,240,40  | 페이지 인디케이터            |

---
## Component Inventory
- filterBar x1
- input x1 (검색)
- roomCard xN
- toggleButton x2
- paginationDots x1
- updateButton x1
- updateBadge x1 (updateButton 우상단 부착)

---
## Notes
- 이 패널은 MAIN 교체영역(`x=4.2% y=10.2% w=91.7% h=85.2%`) 안에서만 렌더링된다.
- 방 카드는 3열 그리드 기준(카드 폭 360, 간격 24).
- 필터 바는 상단 고정.
- 현재 화면에 보이는 방 카드의 상태값은 실시간 이벤트 수신 즉시 자동 갱신된다.
- 현재 페이지 범위 밖 변화는 updateBadge 카운트만 증가시키고, updateButton 클릭 시 목록 전체를 최신화한다.
