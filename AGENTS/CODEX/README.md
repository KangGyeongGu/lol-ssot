**목적**
- SSOT 문서 정합성 검증을 위한 에이전트 정의를 제공한다.
- 검증 절차/로그 포맷을 표준화한다.

**범위**
- 포함: 검증 에이전트, 실행 스크립트
- 제외: 구현 코드 변경

**디렉토리 구조**
```text
AGENTS/CODEX/
  README.md # 이 문서
  INDEX.md # 공통 규칙/실행 가이드
  PRODUCT_VALIDATOR.md # 01_PRODUCT 검증
  DESIGN_VALIDATOR.md # 02_DESIGN 검증
  API_VALIDATOR.md # 03_API 검증
  DOMAIN_VALIDATOR.md # 04_DOMAIN 검증
  CROSS_CHECKER.md # 디렉토리 간 불일치 검증
  REMEDIATION_SYNTHESIZER.md # 수정 계획 통합
  scripts/
    init_run.sh # 실행 폴더 생성
    repair_run_outputs.sh # 결과 복구/정리
    run_all_validators.sh # 전체 검증 실행
```
