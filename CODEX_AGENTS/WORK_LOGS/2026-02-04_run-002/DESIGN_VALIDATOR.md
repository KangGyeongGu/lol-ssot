`DESIGN_VALIDATOR` 기준 검증 결과만 보고합니다.

- `RUN_ID`: `20260204-204938`
- `SCOPE`: `02_DESIGN/` 전체
- `RESULT`: `FAIL`
- `파일 수정`: 없음

`PASS`
- 16:9 기준 레이아웃 맵 표기(`x%/y%/w%/h% + ref(px)`)는 페이지/섹션/오버레이 전반에서 유지됨 (`02_DESIGN/PAGES/*.md`, `02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md`, `02_DESIGN/OVERLAYS/*.md`).

`FAIL`
1. 페이지-섹션 분해 구조 충돌  
`02_DESIGN/PAGES/MAIN.md:48`~`02_DESIGN/PAGES/MAIN.md:52`는 교체 영역을 `y=10.2%`부터로 정의하지만, `02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md:20`의 `Header Bar`는 `y=3.7%`로 상단 헤더 영역에 걸침. 또한 `02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md:4`, `02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md:37`의 “헤더 하단 영역” 설명과 좌표가 상충.

2. 모달 크기 규칙 충돌  
`02_DESIGN/LAYOUT_RULES.md:38`(모달 최대폭 720~900), `02_DESIGN/COMPONENTS.json.md:41`(`modal.maxWidth: 900`) 대비 `02_DESIGN/OVERLAYS/ROOM_CREATE_MODAL.md:20`의 모달 폭 `960px`이 초과.

3. 컴포넌트 명명/토큰 네임스페이스 일관성 부족  
컴포넌트 기준명(`modal`, `input`, `chat`)은 `02_DESIGN/COMPONENTS.json.md:36`, `02_DESIGN/COMPONENTS.json.md:43`, `02_DESIGN/COMPONENTS.json.md:128`인데, 문서 인벤토리에 `modalCard`, `textInput`, `chatPanel` 등 별칭이 혼재(`02_DESIGN/OVERLAYS/ROOM_CREATE_MODAL.md:30`, `02_DESIGN/OVERLAYS/ROOM_CREATE_MODAL.md:31`, `02_DESIGN/PAGES/MAIN.md:33`).  
또한 토큰 참조는 `bg.panel` 형태(`02_DESIGN/COMPONENTS.json.md:31`)인데 토큰 정의 루트는 `color.bg.panel`(`02_DESIGN/TOKENS.json.md:7`~`02_DESIGN/TOKENS.json.md:12`)로 표기 체계가 분리됨.

4. 컴포넌트 크기와 페이지 배치 수치 불일치  
`stageTabs.height=56`(`02_DESIGN/COMPONENTS.json.md:71`) vs `Stage Tabs` 영역 `60px`(`02_DESIGN/PAGES/BAN_PICK_SHOP.md:21`),  
`editorToolbar.height=48`(`02_DESIGN/COMPONENTS.json.md:112`) vs `Toolbar` `60px`(`02_DESIGN/PAGES/IN_GAME.md:55`).