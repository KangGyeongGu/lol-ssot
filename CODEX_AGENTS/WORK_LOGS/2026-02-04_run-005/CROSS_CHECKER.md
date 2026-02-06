RESULT: `FAIL`

FAIL
1. 스펠 대상 규칙이 디렉토리 간 충돌합니다.  
`01_PRODUCT/REQUIREMENTS.md:106`, `01_PRODUCT/GAME_RULES.md:72`는 “스펠은 자기 자신에게 적용”으로 고정인데, `01_PRODUCT/CATALOG.md:39`는 감시자를 “상대방 화면 감시”로 정의합니다. API도 `03_API/CONTRACT/REALTIME/COMMANDS.md:97`에서 감시자에 `targetUserId`를 요구하고, `03_API/CONTRACT/REALTIME/EVENTS.md:236`도 `targetUserId`를 포함합니다. 반면 도메인 저장 모델 `03_DOMAIN/DATA_MODEL.md:491`의 `SPELL_USAGE`에는 대상 필드가 없습니다.
2. `stage` 용어 모델이 문서군 간 다릅니다.  
`01_PRODUCT/GAME_RULES.md:16`은 상위 상태로 `IN_GAME`을 두고 그 하위에 `BAN/PICK/SHOP/PLAY`를 둡니다. 하지만 API/도메인은 권위 enum을 평탄화해서 `LOBBY|BAN|PICK|SHOP|PLAY|FINISHED`로만 정의합니다 (`03_API/CONTRACT/REST/CONVENTIONS.md:128`, `03_DOMAIN/DATA_MODEL.md:317`, `03_API/CONTRACT/REST/OPENAPI.yaml.md:123`).

PASS
1. `pageRoute`는 제품 흐름과 API 계약이 일치합니다.  
`01_PRODUCT/USER_FLOWS.md:39`, `03_API/CONTRACT/REST/CONVENTIONS.md:139`, `03_API/CONTRACT/REST/OPENAPI.yaml.md:131`
2. 채널/플레이어 상태 용어는 일치합니다.  
`01_PRODUCT/USER_FLOWS.md:105`, `03_API/CONTRACT/REALTIME/CONVENTIONS.md:79`, `03_DOMAIN/DATA_MODEL.md:316`
3. ROOM_LIST 패널 흐름(헤더 하단 교체 + 실시간 델타 + 업데이트 적용)은 제품/디자인/API 간 정합합니다.  
`01_PRODUCT/USER_FLOWS.md:85`, `02_DESIGN/PAGES/MAIN.md:48`, `02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md:37`, `03_API/LIFECYCLE.md:51`
4. 링크 검증: 스코프 내 위키 링크 기준 out-of-scope 0건, 누락 링크 0건.