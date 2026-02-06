# REMEDIATION_PLAN
- run_id: 2026-02-05_run-001
- generated_at: 2026-02-05T08:19:52Z
- status: DONE

## 근거 요약
- API_VALIDATOR: PASS - API 계약/페이지맵/enum 일치 확인.
- CROSS_CHECKER: FAIL - 페이지/오버레이 명칭 불일치 2건 발견.
- DESIGN_VALIDATOR: FAIL - LAYOUT_RULES 패널 비율/배치 4건, 컴포넌트 높이 1건 불일치.
- DOMAIN_VALIDATOR: PASS - 도메인 모델/DB/enum 정합성 확인.
- PRODUCT_VALIDATOR: PASS - 제품 요구사항/플로우/룰 일관성 확인.

## 작업 큐
- [RQ-001] Priority=P0 | Source=CROSS_CHECKER | Type=DOC_FIX | Action=LOGIN 페이지 명칭을 `WELCOME`로 통일하거나 문서 간 명칭 매핑을 명시 | Evidence=CROSS_CHECKER.raw: LOGIN.md PAGE_LOGIN vs USER_FLOWS WELCOME / PAGE_MAP_WELCOME | DoneWhen=01_PRODUCT/USER_FLOWS.md, 02_DESIGN/PAGES/LOGIN.md, 03_API/PAGE_MAP/WELCOME.md에서 명칭 또는 매핑이 일치
- [RQ-002] Priority=P1 | Source=CROSS_CHECKER | Type=DOC_FIX | Action=SIGNUP 오버레이 명칭을 `SIGNUP`로 통일하거나 `SIGNUP_MODAL` 동의어 표기를 명시 | Evidence=CROSS_CHECKER.raw: SIGNUP 명칭 vs OVERLAY_SIGNUP_MODAL 불일치 | DoneWhen=01_PRODUCT/USER_FLOWS.md, 02_DESIGN/OVERLAYS/SIGNUP_MODAL.md, 03_API/PAGE_MAP/SIGNUP.md 간 명칭 일치 또는 매핑 표기
- [RQ-003] Priority=P0 | Source=DESIGN_VALIDATOR | Type=DOC_FIX | Action=MAIN 우측 보조 패널 폭을 30~40%로 조정하거나 예외 기준을 문서에 명시 | Evidence=DESIGN_VALIDATOR.raw: MAIN right panel w=25.8% < 30~40 | DoneWhen=02_DESIGN/PAGES/MAIN.md 레이아웃 맵이 규칙 충족 또는 예외 기준 문서화
- [RQ-004] Priority=P0 | Source=DESIGN_VALIDATOR | Type=DOC_FIX | Action=WAITING_ROOM 우측 보조 패널 폭을 30~40%로 조정하거나 예외 기준을 문서에 명시 | Evidence=DESIGN_VALIDATOR.raw: WAITING_ROOM right panel w=27.1% < 30~40 | DoneWhen=02_DESIGN/PAGES/WAITING_ROOM.md 레이아웃 맵이 규칙 충족 또는 예외 기준 문서화
- [RQ-005] Priority=P0 | Source=DESIGN_VALIDATOR | Type=DOC_FIX | Action=MY_PAGE 메인 콘텐츠를 좌측 60~70%로 배치하거나 예외 기준을 문서에 명시 | Evidence=DESIGN_VALIDATOR.raw: MY_PAGE 메인 콘텐츠 우측 배치(좌 27.1% / 우 63.5%) | DoneWhen=02_DESIGN/PAGES/MY_PAGE.md 레이아웃 맵이 규칙 충족 또는 예외 기준 문서화
- [RQ-006] Priority=P0 | Source=DESIGN_VALIDATOR | Type=DOC_FIX | Action=BAN_PICK_SHOP 좌/우 패널 비율을 규칙(좌 60~70%, 우 30~40)으로 조정하거나 예외 기준을 문서에 명시 | Evidence=DESIGN_VALIDATOR.raw: BAN_PICK_SHOP 좌 21.9% / 우 68.8% | DoneWhen=02_DESIGN/PAGES/BAN_PICK_SHOP.md 레이아웃 맵이 규칙 충족 또는 예외 기준 문서화
- [RQ-007] Priority=P1 | Source=DESIGN_VALIDATOR | Type=DOC_FIX | Action=MY_PAGE 탭 높이를 44px로 맞추거나 `tabBar` 별도 높이 규칙을 문서에 반영 | Evidence=DESIGN_VALIDATOR.raw: Tabs h=50px vs 기본 44px | DoneWhen=02_DESIGN/PAGES/MY_PAGE.md 및 02_DESIGN/COMPONENTS.json.md에 높이 규칙 일치

## 비고
- raw 기준 종합이며, 필요 시 해당 validator만 재실행한다.