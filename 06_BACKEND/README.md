**목적**
- 백엔드 구현 규칙/패턴/컨벤션의 단일 진실(SSOT)을 정의한다.

**범위**
- 포함: 아키텍처, API 규칙, 실시간 규칙, 데이터 모델 규칙, 테스트 규칙
- 제외: 구현 코드, 인프라 프로비저닝

**파일 구조**
```text
06_BACKEND/
  README.md # 이 문서
  BE_STACK.md # 백엔드 기술 스택 고정값
  BE_ARCHITECTURE.md # 모듈 경계/레이어 책임 규칙
  BE_CONVENTIONS.md # 네이밍/구조/코딩 컨벤션
  BE_API_RULES.md # REST 구현 규칙
  BE_REALTIME_RULES.md # 실시간(STOMP) 구현 규칙
  BE_DATA_MODEL_RULES.md # 데이터 모델/DB 규칙
  BE_TEST_RULES.md # 테스트 전략/규칙
  BE_AGENT_SPLIT.md # 병렬 에이전트 분할 기준
```

**관련 SSOT**
- 제품/정책: `01_PRODUCT/`
- API 계약: `03_API/`
- 도메인/DB: `04_DOMAIN/`

**변경 원칙**
- 백엔드 구현 규칙 변경은 `06_BACKEND/`에서만 정의한다.
