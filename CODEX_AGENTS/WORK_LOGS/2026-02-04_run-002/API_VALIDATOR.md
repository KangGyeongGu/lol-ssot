검증 결과: **FAIL** (정합성 이슈 3건)

[FAIL] REST 상태코드 선언 불일치  
- `03_API/CONTRACT/REST/CONVENTIONS.md:141`~`03_API/CONTRACT/REST/CONVENTIONS.md:149`와 `03_API/CONTRACT/REST/ERROR_MODEL.md:66`~`03_API/CONTRACT/REST/ERROR_MODEL.md:75`는 `429`, `500`을 표준 매핑으로 선언함.  
- `03_API/CONTRACT/REST/OPENAPI.yaml.md`의 응답 코드 정의에는 `200/400/401/403/404/409`만 존재하고 `429/500` 정의가 없음.

[FAIL] REALTIME Topic 범위 표기 불일치  
- `03_API/CONTRACT/REALTIME/TOPICS.md:23`에서 `/topic/rooms/{roomId}/chat` 범위를 `INGAME`으로 표기.  
- 같은 행 설명은 “대기실~인게임”이고, `03_API/LIFECYCLE.md:56`~`03_API/LIFECYCLE.md:59`는 WAITING_ROOM에서도 해당 토픽을 구독하도록 명시함.

[FAIL] `PageRoute` 사용 가능 값과 active-game 규칙 불일치  
- `03_API/CONTRACT/REST/OPENAPI.yaml.md:133`에서 `PageRoute`에 `RESULT` 포함.  
- 그러나 `03_API/CONTRACT/REST/OPENAPI.yaml.md:213`~`03_API/CONTRACT/REST/OPENAPI.yaml.md:216`, `03_API/CONTRACT/REST/CONVENTIONS.md:138`, `03_API/LIFECYCLE.md:39`, `03_API/PAGE_MAP/RESULT.md:16`은 FINISHED/RESULT를 active-game 복귀 대상으로 보지 않음.

[PASS] OPENAPI ↔ API_SUMMARY 엔드포인트/메서드 일치  
- `03_API/CONTRACT/REST/OPENAPI.yaml.md`와 `03_API/CONTRACT/REST/API_SUMMARY.md`의 REST endpoint set 동일.

[PASS] REALTIME TOPICS/EVENTS/COMMANDS 핵심 타입 연결 일치  
- `03_API/CONTRACT/REALTIME/TOPICS.md`, `03_API/CONTRACT/REALTIME/EVENTS.md`, `03_API/CONTRACT/REALTIME/COMMANDS.md` 간 이벤트/명령 참조는 주요 항목 기준 정합.

파일 수정은 수행하지 않았습니다.