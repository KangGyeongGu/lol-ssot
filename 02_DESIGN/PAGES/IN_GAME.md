# PAGE_IN_GAME

## 목적
- 플레이(코딩) 단계 UI.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]

---
## Source
- `lol web mockup (before)/7. 플레이 단계.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Stream Row | 4.2 | 3.7 | 91.7 | 14.8 | 80,40,1760,160 | 타 플레이어 화면 공유 영역 |
| Typing Status Bar | 4.2 | 19.4 | 91.7 | 3.7 | 80,210,1760,40 | 플레이어 타이핑 상태 표시 |
| Problem Panel | 4.2 | 25.0 | 27.1 | 70.4 | 80,270,520,760 | 문제 영역 |
| Editor Panel | 32.3 | 25.0 | 49.0 | 70.4 | 620,270,940,760 | 코드 에디터 영역 |
| Inventory Panel | 82.3 | 25.0 | 13.5 | 43.5 | 1580,270,260,470 | 아이템/스펠 영역 |
| Room Chat | 82.3 | 70.4 | 13.5 | 25.0 | 1580,760,260,270 | 룸 채팅 영역 |

---
## Component Inventory
- webrtcTile xN (상단 스트림 영역)
- problemCard x1
- editor x1
- editorToolbar x1
- resultDrawer x1 (슬라이드)
- inventorySlot x6
- chat x1 (룸 채팅)
- typingStatusBar x1
- primaryButton x1 (채점)
- secondaryButton x1 (조기종료)
- statusChip x1 (남은 시간/상태)

---
## Notes
- 상단 스트림 영역은 균등 분할.
- 타이핑 상태 바는 활성 타이핑 사용자 목록을 실시간 배지로 표시한다.
- 문제 영역 상단: 좌측 문제 제목, 우측 남은 시간 정렬.
- 에디터 상단 툴바: 좌측(언어, 글자 크기 ±, 다크/라이트), 우측(조기종료, 채점).
- 채점 결과는 에디터 하단에서 슬라이드로 확장/축소.
- 우측 컬럼은 상단 인벤토리, 하단 룸 채팅 2분할로 구성한다.

---
## Sub-layout: Problem Panel
| 영역 | 기준 | 비고 |
|---|---|---|
| Header Row | 패널 높이의 7.4% (ref 56px) | 제목 좌측, 타이머 우측 |
| Body | 나머지 영역 | 문제 설명/예제 스크롤 |

---
## Sub-layout: Editor Panel
| 영역 | 기준 | 비고 |
|---|---|---|
| Toolbar | 패널 높이의 6.3% (ref 48px) | 좌측: 언어/폰트/테마, 우측: 조기종료/채점 |
| Editor Body | 패널 높이의 64.7% (ref 492px) | 코드 입력 영역 |
| Result Drawer | 패널 높이의 28.9% (ref 220px) | 하단 슬라이드 영역 |
