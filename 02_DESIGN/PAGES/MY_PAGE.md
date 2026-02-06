# PAGE_MY_PAGE

## 목적
- 내 프로필/통계/전적을 확인하는 개인 페이지.

## 관련 문서
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[01_PRODUCT/USER_FLOWS.md]]

---
## Source
- `lol web mockup (before)/9. 마이페이지.png`
- `lol web mockup (before)/9-1. 마이페이지 통계.png`
- `lol web mockup (before)/9-2. 마이페이지 전적.png`

---
## Layout Map (16:9 비율 기준)
| 영역 | x% | y% | w% | h% | ref(px) | 비고 |
|---|---:|---:|---:|---:|---|---|
| Profile Summary | 4.2 | 3.7 | 91.7 | 9.3 | 80,40,1760,100 | 프로필/코인/점수 |
| Tabs (Top) | 4.2 | 13.9 | 91.7 | 4.6 | 80,150,1760,50 | 내정보/대전기록 |
| Account Panel | 4.2 | 20.4 | 27.1 | 74.1 | 80,220,520,800 | 좌측 계정 정보 |
| Content Panel | 32.3 | 20.4 | 63.5 | 74.1 | 620,220,1220,800 | 우측 콘텐츠 |

---
## Component Inventory
- profileBar x1
- tabBar x1 (내정보/대전기록)
- accountCard x1
- tierCard x1
- statRing x3
- heatmap x1
- radarChart x1 (통계 서브탭)
- matchRow xN (대전기록 탭)

---
## 탭 구성
### 내정보 탭
- 우측 패널 상단: 티어/진행도/승률/해결률.
- 하단: 연간 히트맵.
- 우측 패널 상단 서브탭: 티어 / 통계.

### 통계 서브탭
- 레이더 차트 중앙 배치.

### 대전기록 탭
- 매치 리스트(행 높이 64px, 1열 스택).
- 각 행에 결과 배지/문제명/인원/시간/결과보기 버튼.

---
## Notes
- 탭 전환은 동일 페이지 내 컴포넌트 교체 방식.
- 좌측 계정 패널은 탭 전환과 무관하게 고정.
