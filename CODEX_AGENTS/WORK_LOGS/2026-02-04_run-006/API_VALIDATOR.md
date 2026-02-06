[API_VALIDATOR]

범위: `03_API/**`  
결과: `PASS`

1. `OPENAPI/API_SUMMARY/CONVENTIONS/ERROR_MODEL` 정합성: `PASS`
- `03_API/CONTRACT/REST/OPENAPI.yaml.md`와 `03_API/CONTRACT/REST/API_SUMMARY.md`의 REST method/path 목록이 일치합니다.
- `03_API/CONTRACT/REST/CONVENTIONS.md`의 핵심 규칙(`/api/v1`, 인증 예외 2개, PUT/DELETE 미사용, `listVersion`)이 `03_API/CONTRACT/REST/OPENAPI.yaml.md`에 반영되어 있습니다.
- `03_API/CONTRACT/REST/ERROR_MODEL.md`의 에러 엔벨로프 구조와 `03_API/CONTRACT/REST/OPENAPI.yaml.md`의 `ErrorEnvelope` 구조가 충돌하지 않습니다.

2. REALTIME `TOPICS/EVENTS/COMMANDS` 정합성: `PASS`
- `03_API/CONTRACT/REALTIME/TOPICS.md`의 이벤트 목록과 `03_API/CONTRACT/REALTIME/EVENTS.md` EventType 목록이 일치합니다.
- `03_API/CONTRACT/REALTIME/COMMANDS.md`의 CommandType/Destination과 `03_API/PAGE_MAP/*.md`, `03_API/LIFECYCLE.md`의 사용 맥락이 일관됩니다.
- Prefix 규칙(`/topic/**`, `/user/queue/**`, `/app/**`)이 문서 간 충돌 없이 유지됩니다.

3. `LIFECYCLE` 타이밍 ↔ `PAGE_MAP` 매핑: `PASS`
- `03_API/LIFECYCLE.md`와 `03_API/PAGE_MAP/MAIN.md`, `03_API/PAGE_MAP/ROOM_LIST.md`, `03_API/PAGE_MAP/WAITING_ROOM.md`, `03_API/PAGE_MAP/BAN_PICK_SHOP.md`, `03_API/PAGE_MAP/IN_GAME.md`, `03_API/PAGE_MAP/RESULT.md`의 연결/구독/해제/호출 타이밍이 일관됩니다.
- `FINISHED` 이후 active game 제외 규칙과 RESULT 진입 규칙도 일치합니다.

4. enum/type 재사용 일관성: `PASS`
- `GameType`, `PlayerState`, `GameStage`, `PageRoute`, `MatchResult` 값 충돌 없음.
- REALTIME 문서의 `RoomSummary`, `Inventory` 참조가 REST 스키마와 충돌하지 않습니다.

FAIL 항목: 없음 (`0건`)  
파일 수정: 없음