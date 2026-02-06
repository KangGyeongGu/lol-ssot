 # PAGE_BAN_PICK_SHOP

## 목적
- RANKED의 BAN/PICK/SHOP 단계를 한 페이지에서 처리.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]

---
## Source
- `lol web mockup (before)/4. 밴 단계.png`
- `lol web mockup (before)/5. 픽 단계.png`
- `lol web mockup (before)/6. 구매 단계.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Stage Tabs | 4.2 | 3.7 | 91.7 | 5.2 | 80,40,1760,56 | BAN/PICK/SHOP 진행 표시 |
| Player Card | 4.2 | 11.1 | 21.9 | 9.3 | 80,120,420,100 | 상단 좌측 |
| Room Chat | 4.2 | 21.3 | 21.9 | 71.3 | 80,230,420,770 | 채팅 패널 |
| Main Panel | 27.1 | 11.1 | 68.8 | 81.5 | 520,120,1320,880 | 단계별 콘텐츠 |

---
## Component Inventory
- stageTabs x1
- playerCard x1
- chat x1
- algorithmCard x16 (BAN/PICK)
- shopItemCard xN (SHOP)
- shopSpellCard xN (SHOP)
- primaryButton x1 (선택/구매)
- countdownTimer x1

---
## 단계별 내부 배치
### BAN/PICK
- Main Panel 상단: 타이머(중앙 큰 숫자).
- 그 아래: 알고리즘 카드 4열 그리드(카드 220x120, gap 24).
- 하단: “선택” CTA 중앙 배치.

### SHOP
- Main Panel 상단: 타이머 + 코인 표시(우측).
- 중단: 아이템 영역(좌), 스펠 영역(우).
- 하단: 선택 슬롯 + 총 비용 + 구매 CTA.

---
## Notes
- 단계 전환 시 상단 탭만 강조 변경.
- 밴된 카드에는 “BANNED” 오버레이.
