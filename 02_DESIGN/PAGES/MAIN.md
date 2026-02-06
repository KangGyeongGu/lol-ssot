# PAGE_MAIN

## 목적
- 메인 대시보드(대회 소개, 랭킹, 채팅, 방 진입).

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]
- [[02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md]]
- [[02_DESIGN/OVERLAYS/ROOM_CREATE_MODAL.md]]

---
## Source
- `lol web mockup (before)/2. 메인페이지.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Header | 4.2 | 2.8 | 91.7 | 5.6 | 80,30,1760,60 | 로고 중앙, 우측 코인/프로필 |
| Hero Card | 4.2 | 10.2 | 64.6 | 23.1 | 80,110,1240,250 | 대회 소개 + Join |
| Right Panel A | 70.0 | 10.2 | 25.8 | 27.8 | 1344,110,496,300 | Most Banned/Picked |
| Right Panel B | 70.0 | 38.9 | 25.8 | 33.3 | 1344,420,496,360 | Top Players |
| CTA Row | 4.2 | 34.3 | 64.6 | 7.4 | 80,370,1240,80 | 대전 생성/찾기 |
| Global Chat | 4.2 | 43.5 | 64.6 | 46.3 | 80,470,1240,500 | 전역 채팅 패널 |

---
## Component Inventory
- heroCard x1
- statPanel x2
- primaryButton x2 (대전 생성/찾기)
- chat x1
- coinBadge x1
- profileAvatar x1

---
## Notes
- 좌측 1240px / 우측 496px 고정 분할.
- Hero Card 내부 CTA는 우측 하단에 배치.

---
## Page States
### 기본 상태: Main Dashboard
- 히어로 카드 + 우측 랭킹/통계 패널 노출.

### 전환 상태: Room List Panel
- 메인 헤더 하단 영역만 교체된다.
- 상세 레이아웃은 `[[02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md]]` 참조.
- 교체 영역(16:9 기준):
  - x=4.2% y=10.2% w=91.7% h=85.2%
  - ref(px)=80,110,1760,920
- Room List Panel에서는 목록 외부 변경 누적 시 헤더 새로고침 버튼에 하이라이트/카운트 배지가 표시된다.

### Overlay: Room Create Modal
- 대전 생성 버튼 클릭 시 오버레이 표시.
- 상세 레이아웃은 `[[02_DESIGN/OVERLAYS/ROOM_CREATE_MODAL.md]]` 참조.
