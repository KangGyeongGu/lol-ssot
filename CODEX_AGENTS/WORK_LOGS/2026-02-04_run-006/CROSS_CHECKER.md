`CROSS_CHECKER` 검증 결과: `FAIL`

**FAIL**
1. `stage/pageRoute` 의미 충돌  
`01_PRODUCT/GAME_RULES.md:43`에서 RANKED를 “`IN_GAME` 내부 단계(BAN→PICK→SHOP→PLAY)”로 정의했지만,  
`01_PRODUCT/USER_FLOWS.md:17`, `03_API/PAGE_MAP/BAN_PICK_SHOP.md:4`, `03_API/LIFECYCLE.md:102`는 `BAN_PICK_SHOP`을 `IN_GAME`과 분리된 페이지로 정의합니다.

2. 대기실 수용 인원 모델 충돌  
인원 상한은 `2~6`으로 정의되어 있는데(`01_PRODUCT/REQUIREMENTS.md:45`, `03_DOMAIN/DATA_MODEL.md:347`, `03_API/CONTRACT/REST/OPENAPI.yaml.md:235`),  
디자인 대기실은 슬롯 `4개(2x2)`로 고정되어 있습니다(`02_DESIGN/PAGES/WAITING_ROOM.md:20`, `02_DESIGN/PAGES/WAITING_ROOM.md:27`).

3. 대기실 방장 강퇴 액션 UI 명세 누락  
제품/계약은 방장 강퇴를 필수 액션으로 정의합니다(`01_PRODUCT/USER_FLOWS.md:116`, `01_PRODUCT/REQUIREMENTS.md:67`, `03_API/PAGE_MAP/WAITING_ROOM.md:26`).  
하지만 대기실 디자인 컴포넌트 인벤토리에는 강퇴 컨트롤이 명시되지 않습니다(`02_DESIGN/PAGES/WAITING_ROOM.md:27`).

**PASS**
1. 공통 용어 정합  
`PlayerState`, `GameStage`, `ChatChannel` 핵심 enum은 API/도메인/이벤트 문서에서 일관됩니다(`03_API/CONTRACT/REST/CONVENTIONS.md:123`, `03_DOMAIN/DATA_MODEL.md:317`, `03_API/CONTRACT/REALTIME/EVENTS.md:76`, `03_API/CONTRACT/REALTIME/EVENTS.md:171`).

2. 링크 범위 정합  
스코프( `01_PRODUCT`, `02_DESIGN`, `03_API`, `03_DOMAIN` ) 내 위키 링크 기준으로 깨진 링크는 확인되지 않았습니다.

파일 수정: 없음