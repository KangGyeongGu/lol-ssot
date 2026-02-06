# API_VALIDATOR REPORT
- run_id: 20260205_080955Z
- generated_at: 2026-02-05T08:09:55Z
- status: DONE

## 검사 결과
- Overall: PASS

## 위반 목록
- 없음

## 정상 항목
- `03_API/CONTRACT/REST/OPENAPI.yaml.md`, `03_API/CONTRACT/REST/API_SUMMARY.md`, `03_API/CONTRACT/REST/CONVENTIONS.md`, `03_API/CONTRACT/REST/ERROR_MODEL.md` 간 엔드포인트/스키마/규칙 일치 확인
- `03_API/CONTRACT/REALTIME/TOPICS.md`, `03_API/CONTRACT/REALTIME/EVENTS.md`, `03_API/CONTRACT/REALTIME/COMMANDS.md` 상호 참조 및 이벤트 타입 일치 확인
- `03_API/LIFECYCLE.md`의 구독/REST 타이밍과 `03_API/PAGE_MAP/*.md` 매핑 일관성 확인
- 공통 enum/type(GameType, GameStage, PlayerState, MatchResult, PageRoute 등) 재사용 일관성 확인