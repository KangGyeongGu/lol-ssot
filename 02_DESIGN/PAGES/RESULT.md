# PAGE_RESULT

## 목적
- 게임 결과 및 보상 확인 화면.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]

---
## Source
- `lol web mockup (before)/8. 결과 페이지.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Header Info | 8.3 | 7.4 | 83.3 | 16.7 | 160,80,1600,180 | 문제명/방 정보 |
| Result Row | 8.3 | 25.9 | 83.3 | 11.1 | 160,280,1600,120 | 플레이어 결과 요약 |
| Rewards | 50.0 | 27.8 | 40.6 | 7.4 | 960,300,780,80 | 점수/코인/경험치 |
| CTA Row | 29.2 | 77.8 | 41.7 | 6.5 | 560,840,800,70 | 메인/마이페이지 |

---
## Component Inventory
- headerCard x1
- resultRow x1
- rewardChip x3
- primaryButton x1
- secondaryButton x1

---
## Notes
- 결과 상태(WIN/LOSE/DRAW)는 좌측 큰 텍스트 배지.
- 하단 CTA는 동일 폭 2분할.
