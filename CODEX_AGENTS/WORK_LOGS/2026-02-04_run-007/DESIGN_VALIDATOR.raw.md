**DESIGN_VALIDATOR 결과**
- `RESULT: FAIL`
- 검증 범위: `02_DESIGN/` 하위만 사용
- 파일 수정: 없음
- 스코프 외 참조: 없음

**PASS**
- `16:9 좌표 정책`: 페이지/섹션/오버레이의 `x%/y%/w%/h%`와 `ref(px)` 정합이 전반적으로 일치함(검출된 오차 없음).
- `분해 구조`: 페이지-섹션-오버레이 참조 구조가 문서 내에서 유효하게 연결됨.
- `컴포넌트 명명`: 인벤토리의 컴포넌트명이 `02_DESIGN/COMPONENTS.json.md`에 모두 존재함(누락 없음).

**FAIL**
1. `playerCard` 크기 충돌  
`02_DESIGN/PAGES/BAN_PICK_SHOP.md:22`의 `Player Card`는 `420x100`인데, 토큰 정의는 `02_DESIGN/COMPONENTS.json.md:132`(`width: 360`), `02_DESIGN/COMPONENTS.json.md:134`(`height: 96`)로 상이함.
2. `toggleButton` 높이 충돌  
`02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md:22`의 `View Toggle` 높이는 `40`인데, `toggleButton`의 베이스 `tab` 높이는 `44`(`02_DESIGN/COMPONENTS.json.md:79`, `02_DESIGN/COMPONENTS.json.md:89`)로 상이함.