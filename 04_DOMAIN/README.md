**목적**
- 도메인 모델 및 DB 규칙의 단일 진실(SSOT)을 정의한다.

**범위**
- 포함: 데이터 모델, DB 설계 노트, Redis 타이밍 규칙
- 제외: 구현 코드, API 계약 세부

**파일 구조**
```text
04_DOMAIN/
  README.md # 이 문서
  DATA_MODEL.md # 엔티티/관계/도메인 모델 기준
  DB_NOTES.md # DB 설계/정합성 메모
  REDIS_DB_TIMING.md # Redis/DB 동기화 타이밍 규칙
```

**변경 원칙**
- 데이터 모델 변경은 `04_DOMAIN/`에서 먼저 수정한다.
