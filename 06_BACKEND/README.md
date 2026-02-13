**목적**
- 백엔드 구현 규칙/패턴/컨벤션의 단일 진실(SSOT)을 정의한다.

**범위**
- 포함: 명세 정합성 기준(SPEC), 코드 품질 기준(QUALITY), 리뷰 참조 맵
- 제외: 구현 코드, 인프라 프로비저닝

**파일 구조**
```text
06_BACKEND/
  README.md # 이 문서
  REVIEW_REFERENCE_MAP.md # 도메인별 SSOT/QUALITY 참조 맵
  SPEC/ # BE 정합성(명세) 기준
    BE_ARCHITECTURE.md # 모듈/의존성 경계 명세
    BE_API_RULES.md # REST 계약 구현 명세
    BE_DATA_MODEL_RULES.md # 데이터모델/저장정책 명세
    BE_REALTIME_RULES.md # 실시간 계약 구현 명세
    RULE_INDEX.md # BE-S-* 룰 ID 인덱스
  QUALITY/ # BE 코드 품질 기준
    BE_CONVENTIONS.md # 코드/레이어/예외처리 품질 규칙
    BE_STACK.md # 스택/도구 사용 정책
    BE_TEST_RULES.md # 테스트 품질 규칙
```

**관련 SSOT**
- 제품/정책: `01_PRODUCT/`
- API 계약: `03_API/`
- 도메인/DB: `04_DOMAIN/`

**변경 원칙**
- 백엔드 구현 규칙 변경은 `06_BACKEND/`에서만 정의한다.
