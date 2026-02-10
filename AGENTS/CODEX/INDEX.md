## 목적
- 이 파일은 공통 진입점 + 에이전트 인덱스를 함께 정의한다.
- 역할별 서브 에이전트 정의는 [[AGENTS/CODEX/PRODUCT_VALIDATOR.md]], [[AGENTS/CODEX/DESIGN_VALIDATOR.md]], [[AGENTS/CODEX/API_VALIDATOR.md]], [[AGENTS/CODEX/DOMAIN_VALIDATOR.md]], [[AGENTS/CODEX/CROSS_CHECKER.md]], [[AGENTS/CODEX/REMEDIATION_SYNTHESIZER.md]] 파일만 사용한다.
- 검증 시 에이전트 규칙 참조는 [[AGENTS/CODEX/INDEX.md]]에 링크된 에이전트 파일만 허용한다.

## 공통 운영 원칙
- 검증 작업은 2단계로 분리한다.
  1) 검증 패스: read-only, PASS/FAIL 보고만 수행
  2) 수정 패스: 승인된 항목만 수정
- 검증 패스에서 신규 설계 추가, 임의 정책 확장은 금지한다.
- 역할별 상세 규칙은 아래 에이전트 파일을 따른다.

## 에이전트 목록
- [[AGENTS/CODEX/PRODUCT_VALIDATOR.md]]
- [[AGENTS/CODEX/DESIGN_VALIDATOR.md]]
- [[AGENTS/CODEX/API_VALIDATOR.md]]
- [[AGENTS/CODEX/DOMAIN_VALIDATOR.md]]
- [[AGENTS/CODEX/CROSS_CHECKER.md]]
- [[AGENTS/CODEX/REMEDIATION_SYNTHESIZER.md]]

## 작업 내역 저장
- 작업 내역 루트: [[AGENTS/CODEX/WORK_LOGS/README.md]]
- 실행 폴더 생성 스크립트: [[AGENTS/CODEX/scripts/init_run.sh]]
- 전체 검증 실행 스크립트: [[AGENTS/CODEX/scripts/run_all_validators.sh]]
- 실행 폴더 규칙:
  - 날짜 기반: YYYY-MM-DD_run-001
  - 횟수 기반: run-001
- 각 실행 폴더에는 에이전트별 보고서 .md 파일을 생성한다.

## 실행 순서 (권장)
1. Product
2. Design
3. API
4. Domain
5. Cross-check
6. Remediation Synthesizer (raw 종합)

## 공통 출력 포맷
```md
# <AGENT_KEY> REPORT
- run_id: <RUN_ID>
- generated_at: <UTC_ISO8601>
- status: DONE

## 검사 결과
- Overall: PASS | FAIL

## 위반 목록
- Severity: Blocking | Major | Minor
- File: <path>
- Rule: <검사 기준>
- Evidence: <근거 문장/섹션>
- Fix Direction: <수정 방향 한 줄>

## 정상 항목
- <핵심 PASS 항목>
```

## 출력 원칙
- 모든 validator 결과는 PASS/FAIL 구조로 보고한다.
- 위반 항목은 Severity + File + Evidence + Fix Direction을 포함한다.

## 실행 예시
- RUN_ID 생성: AGENTS/CODEX/scripts/init_run.sh --mode date
- 단일 실행:
  - codex exec -s read-only -C /Users/kanggyeonggu/Documents/league-of-algologic
  - "AGENTS/CODEX/API_VALIDATOR.md 규칙만 사용해 검증만 수행한다. 파일 수정 금지."
  - -o "AGENTS/CODEX/WORK_LOGS/${RUN_ID}/API_VALIDATOR.md"
- 전체 실행:
  - AGENTS/CODEX/scripts/run_all_validators.sh --mode date
