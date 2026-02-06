# PAGE_WAITING_ROOM

## 목적
- 대기실에서 플레이어 상태/채팅/게임 시작을 관리한다.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]

---
## Source
- `lol web mockup (before)/3. 대기실.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Top Bar | 4.2 | 3.7 | 91.7 | 6.5 | 80,40,1760,70 | 방번호/유형/방장 |
| Player Grid | 4.2 | 12.0 | 63.5 | 57.4 | 80,130,1220,620 | 슬롯 2~6개(최대 3x2) |
| Room Settings | 69.0 | 12.0 | 27.1 | 24.1 | 1324,130,520,260 | 게임유형/인원/시간/언어 |
| Room Chat | 69.0 | 38.0 | 27.1 | 32.4 | 1324,410,520,350 | 룸 채팅 |
| Action Bar | 4.2 | 72.2 | 91.7 | 8.3 | 80,780,1760,90 | 나가기/준비/게임시작 |

---
## Component Inventory
- playerCard x1
- lobbySlot x1~5 (최대 6인 구성)
- settingsPanel x1
- chat x1
- primaryButton x1 (게임 시작)
- secondaryButton x1 (준비 완료)
- outlineButton x1 (나가기)
- dangerButton xN (방장 전용 강퇴)

---
## Notes
- 방장 표시는 상단 바 우측 배지.
- 빈 슬롯은 점선 보더 처리.
- 방장 전용 컨트롤 영역에서 각 대상 플레이어에 대해 강퇴 버튼이 노출된다.
