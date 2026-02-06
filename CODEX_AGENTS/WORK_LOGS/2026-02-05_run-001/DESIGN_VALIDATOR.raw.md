# DESIGN_VALIDATOR REPORT
- run_id: 2026-02-05_run-001
- generated_at: 2026-02-05T08:07:14Z
- status: DONE

## 검사 결과
- Overall: FAIL

## 위반 목록
- Severity: Major
- File: `02_DESIGN/PAGES/MAIN.md`
- Rule: LAYOUT_RULES "패널 배치 기본: 좌측 메인 콘텐츠(60~70%), 우측 보조 패널(30~40%)."
- Evidence: Layout Map에서 Right Panel A/B `w=25.8% (ref 496px)`로 30~40% 범위를 하회.
- Fix Direction: 우측 보조 패널 폭을 30~40% 범위로 조정하거나 예외 기준을 문서에 명시.

- Severity: Major
- File: `02_DESIGN/PAGES/WAITING_ROOM.md`
- Rule: LAYOUT_RULES "패널 배치 기본: 좌측 메인 콘텐츠(60~70%), 우측 보조 패널(30~40%)."
- Evidence: Room Settings / Room Chat 영역 `w=27.1% (ref 520px)`로 30~40% 범위를 하회.
- Fix Direction: 우측 보조 패널 폭을 30~40% 범위로 조정하거나 예외 기준을 문서에 명시.

- Severity: Major
- File: `02_DESIGN/PAGES/MY_PAGE.md`
- Rule: LAYOUT_RULES "좌측 메인 콘텐츠(60~70%), 우측 보조 패널(30~40%)."
- Evidence: Account Panel `w=27.1%`(좌측), Content Panel `w=63.5%`(우측)로 메인 콘텐츠가 우측에 배치됨.
- Fix Direction: 메인 콘텐츠를 좌측 60~70%로 배치하거나 예외 기준을 문서에 명시.

- Severity: Major
- File: `02_DESIGN/PAGES/BAN_PICK_SHOP.md`
- Rule: LAYOUT_RULES "좌측 메인 콘텐츠(60~70%), 우측 보조 패널(30~40%)."
- Evidence: Player Card/Room Chat column `w=21.9%`(좌측), Main Panel `w=68.8%`(우측)로 좌측 메인 콘텐츠 기준 불충족.
- Fix Direction: 좌/우 패널 비율을 규칙에 맞게 조정하거나 예외 기준을 문서에 명시.

- Severity: Minor
- File: `02_DESIGN/PAGES/MY_PAGE.md`
- Rule: COMPONENTS.json.md `tab` height 44 및 `tabBar`가 `tab`을 base로 상속.
- Evidence: Tabs (Top) `h=4.6% (ref 50px)`로 컴포넌트 기본 높이(44px)와 불일치.
- Fix Direction: Tabs 높이를 44px에 맞추거나 `tabBar`에 별도 높이를 정의하고 문서에 반영.

## 정상 항목
- 모든 레이아웃 맵이 16:9 기준의 `x%/y%/w%/h%` 좌표와 `ref(px)`를 병기해 좌표 규칙을 유지함.
- 모달 폭이 `720~900px` 범위 내에 있으며 중앙 정렬 카드형 구조를 준수함.
- 페이지별 Component Inventory가 `02_DESIGN/COMPONENTS.json.md`에 정의된 컴포넌트 명칭을 일관되게 사용함.