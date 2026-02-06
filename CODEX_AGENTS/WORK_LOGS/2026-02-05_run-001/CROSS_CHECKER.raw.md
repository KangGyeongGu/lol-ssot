# CROSS_CHECKER REPORT
- run_id: 2026-02-05_run-001
- generated_at: 2026-02-05T08:18:27Z
- status: DONE

## 검사 결과
- Overall: FAIL

## 위반 목록
- Severity: Major
- File: `02_DESIGN/PAGES/LOGIN.md`
- Rule: 공통 용어 일치 여부(page 명칭)
- Evidence: `02_DESIGN/PAGES/LOGIN.md`는 `PAGE_LOGIN`을 사용하나, `01_PRODUCT/USER_FLOWS.md`는 서비스 페이지로 `WELCOME`를 정의하고 `03_API/PAGE_MAP/WELCOME.md`는 `PAGE_MAP_WELCOME`으로 매핑한다.
- Fix Direction: 로그인 페이지 명칭을 `WELCOME`로 통일하거나 문서 간 명칭 매핑을 명시한다.

- Severity: Minor
- File: `02_DESIGN/OVERLAYS/SIGNUP_MODAL.md`
- Rule: 공통 용어 일치 여부(overlay/state 명칭)
- Evidence: `01_PRODUCT/USER_FLOWS.md`는 `SIGNUP 오버레이`, `03_API/PAGE_MAP/SIGNUP.md`는 `SIGNUP`로 정의하는 반면 `02_DESIGN/OVERLAYS/SIGNUP_MODAL.md`는 `OVERLAY_SIGNUP_MODAL`로 표기한다.
- Fix Direction: `SIGNUP` 명칭으로 통일하거나 `SIGNUP_MODAL`이 동일 개념임을 명시한다.

## 정상 항목
- 게임 stage 전이 정의(LOBBY→BAN→PICK→SHOP→PLAY→FINISHED, NORMAL은 LOBBY→PLAY→FINISHED)가 제품/도메인/API 문서 간 일치한다.
- RESULT 표시가 `GAME_FINISHED` 이벤트 기반이며 재접속 시 자동 복귀하지 않는 흐름이 제품/라이프사이클/API 페이지맵에서 일치한다.
- 룸 채팅 스코프가 WAITING_ROOM→BAN_PICK_SHOP→IN_GAME 동안 유지되는 규칙이 제품/라이프사이클/API 문서 간 일치한다.
- MAIN 내 ROOM_LIST 패널은 `GET /rooms` 스냅샷 + `/topic/rooms/list` 델타 동기화를 사용한다는 규칙이 제품/디자인/API 문서 간 일치한다.