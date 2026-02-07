# BE_DATA_MODEL_RULES

## 0. 문서 목적
- 데이터 모델/DB 구현 규칙을 정의한다.
- 단일 진실은 `03_DOMAIN` 문서다.

## 관련 문서
- [[03_DOMAIN/DATA_MODEL.md]]
- [[03_DOMAIN/DB_NOTES.md]]

---
## 1. 모델 준수 규칙
- 엔티티/필드/관계는 DATA_MODEL.md와 1:1로 일치해야 한다.
- storage 타입(persistent/ephemeral/derived)은 변경 금지.
- storage 의미는 다음을 따른다.
  - persistent: DB 영속 저장(JPA Entity/Repository 대상)
  - ephemeral/derived: Redis 실시간 상태(DB 테이블/마이그레이션 금지)
- write policy는 DATA_MODEL.md의 매핑을 따른다.
- write-through: 상태 변경 즉시 DB에 기록한다.
- write-back: Redis가 실시간 단일 진실이다. 종료 시점에 DB 스냅샷을 반영한다.
- write-back 대상은 GAME_FINISHED 또는 룸/게임 종료 시 DB 반영이 필수다.

---
## 2. 마이그레이션 규칙
- 스키마 변경은 마이그레이션으로만 반영한다.
- 마이그레이션은 되돌릴 수 있어야 한다.

---
## 3. ID/시간 규칙
- 모든 ID는 문자열로 취급한다.
- 시간 포맷은 ISO-8601 UTC 문자열을 사용한다.
