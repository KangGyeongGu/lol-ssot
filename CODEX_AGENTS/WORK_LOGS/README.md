# CODEX_AGENTS_WORK_LOGS

## 목적
- 서브에이전트 검증 수행 결과를 실행 단위로 보관한다.
- 실행 단위 폴더 안에 에이전트별 .md 보고서를 저장한다.
- 이 파일은 운영 가이드 문서이며, 스크립트 런타임 의존 파일은 아니다.

## 폴더 규칙
- 날짜 기반 실행: YYYY-MM-DD_run-001
- 횟수 기반 실행: run-001

## 실행 폴더 생성
- 날짜 기반(기본): CODEX_AGENTS/scripts/init_run.sh --mode date
- 횟수 기반: CODEX_AGENTS/scripts/init_run.sh --mode count

## 전체 validator 실행
- 기본: read-only, 날짜 기반 실행 폴더 생성 후 5개 validator 순차 실행
  - CODEX_AGENTS/scripts/run_all_validators.sh --mode date
- 횟수 기반 실행
  - CODEX_AGENTS/scripts/run_all_validators.sh --mode count
- 기존 실행 폴더 보정(재실행 없이 포맷/요약/remediation 재생성)
  - CODEX_AGENTS/scripts/repair_run_outputs.sh --run-id <RUN_ID>

## 생성되는 기본 파일
- PRODUCT_VALIDATOR.md
- DESIGN_VALIDATOR.md
- API_VALIDATOR.md
- DOMAIN_VALIDATOR.md
- CROSS_CHECKER.md
- SUMMARY.md
- REMEDIATION_PLAN.md
- REMEDIATION_PLAN.raw.md

## 출력 표준화 정책
- 최종 보고서(`*_VALIDATOR.md`, `CROSS_CHECKER.md`)는 공통 포맷으로 정규화되어 저장된다.
- 각 validator의 원본 출력은 별도 파일(`*.raw.md`)로 보관된다.
- SUMMARY는 항상 validator별 `overall/status/exit_code`를 기록한다.
- 서브에이전트 체인 마지막에 `REMEDIATION_SYNTHESIZER`가 `*.raw.md`를 종합해 `REMEDIATION_PLAN.md`를 생성한다.
- `REMEDIATION_SYNTHESIZER` 실행 실패 시에만 스크립트 fallback 로직으로 최소 작업 큐를 채운다.

## 예시 실행
- RUN_ID 생성: CODEX_AGENTS/scripts/init_run.sh --mode date
- 단일 실행:
  - codex exec -s read-only -C /Users/kanggyeonggu/Documents/league-of-algologic
  - "CODEX_AGENTS/PRODUCT_VALIDATOR.md 규칙만 사용해 검증만 수행한다. 파일 수정 금지."
  - -o "CODEX_AGENTS/WORK_LOGS/${RUN_ID}/PRODUCT_VALIDATOR.md"
