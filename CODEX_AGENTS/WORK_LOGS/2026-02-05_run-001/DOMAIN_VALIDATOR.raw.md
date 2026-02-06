# DOMAIN_VALIDATOR REPORT
- run_id: 2026-02-05_run-001
- generated_at: 2026-02-05T08:13:50Z
- status: DONE

## 검사 결과
- Overall: PASS

## 위반 목록
- None

## 정상 항목
- `03_DOMAIN/DATA_MODEL.md`와 `03_DOMAIN/DB_NOTES.md` 간 유니크/인덱스 정의가 상호 일치함.
- 엔티티 관계 방향(ROOM↔GAME, USER↔GAME_PLAYER 등)과 FK 필드가 문서 전반에서 일관됨.
- enum 집합과 사용 위치(GameType, GameStage, PlayerState, GamePlayerState 등) 표기가 충돌 없이 유지됨.
- 로그성 테이블(SUBMISSION, GAME_*_PURCHASE, *_USAGE, CHAT_MESSAGE)의 저장 의도와 필드 의미가 명확히 정의됨.