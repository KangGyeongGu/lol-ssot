검증 결과: **FAIL**  
범위 준수: `01_PRODUCT`, `02_DESIGN`, `03_API`, `03_DOMAIN`만 참조  
파일 수정: 없음

1. `FAIL` 공통 용어 불일치 (`pageRoute`/페이지 명명)
- `WELCOME/SIGNUP/ROOM_LIST`를 페이지로 정의했지만 디자인은 `LOGIN` 페이지 + `SIGNUP` 모달 + `ROOM_LIST` 패널로 표현됨.  
`01_PRODUCT/USER_FLOWS.md:21` `01_PRODUCT/USER_FLOWS.md:22` `01_PRODUCT/USER_FLOWS.md:24` `02_DESIGN/PAGES/LOGIN.md:1` `02_DESIGN/OVERLAYS/SIGNUP_MODAL.md:1` `02_DESIGN/PAGES/MAIN.md:47`
- `ActiveGame`은 FINISHED 복귀 제외 규칙인데 `PageRoute` enum에 `RESULT`가 포함됨.  
`03_API/CONTRACT/REST/OPENAPI.yaml.md:133` `03_API/CONTRACT/REST/OPENAPI.yaml.md:213` `03_API/PAGE_MAP/RESULT.md:16`

2. `FAIL` 제품 흐름 vs API lifecycle/page map 충돌
- 제품/페이지맵은 `ROOM_LIST`를 독립 화면으로 다루는데, lifecycle은 MAIN 내부 패널로 기술함.  
`01_PRODUCT/USER_FLOWS.md:83` `03_API/PAGE_MAP/ROOM_LIST.md:1` `03_API/LIFECYCLE.md:51`
- RESULT 시점 게임 토픽 구독 정책이 문서 간 상충됨.  
`03_API/LIFECYCLE.md:121` `03_API/CONTRACT/REALTIME/TOPICS.md:38` `03_API/PAGE_MAP/RESULT.md:34`

3. `FAIL` 디자인 구조 vs 제품 페이지 모델 충돌
- 로그인 수단: 제품/API는 카카오만인데 디자인은 구글 버튼 포함.  
`01_PRODUCT/REQUIREMENTS.md:17` `03_API/PAGE_MAP/WELCOME.md:19` `02_DESIGN/PAGES/LOGIN.md:22` `02_DESIGN/PAGES/LOGIN.md:30`
- 제품은 SIGNUP “페이지” 흐름인데 디자인은 LOGIN 위 모달.  
`01_PRODUCT/USER_FLOWS.md:55` `02_DESIGN/OVERLAYS/SIGNUP_MODAL.md:4`
- IN_GAME 필수 요소(타이핑 상태 바, 방 채팅)가 디자인 명세에 없음.  
`01_PRODUCT/USER_FLOWS.md:161` `01_PRODUCT/USER_FLOWS.md:163` `02_DESIGN/PAGES/IN_GAME.md:16` `02_DESIGN/PAGES/IN_GAME.md:25`
- RESULT 액션이 제품/API(`MAIN`,`MY_PAGE`)와 다르게 디자인은 `다시 도전/메인`.  
`01_PRODUCT/USER_FLOWS.md:186` `01_PRODUCT/USER_FLOWS.md:187` `03_API/PAGE_MAP/RESULT.md:29` `03_API/PAGE_MAP/RESULT.md:30` `02_DESIGN/PAGES/RESULT.md:22`

4. `PASS` 링크 범위 검증
- 위키 링크는 스코프 디렉토리 내부 문서들로만 연결됨 (`01_PRODUCT`, `02_DESIGN`, `03_API`, `03_DOMAIN`).