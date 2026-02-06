# CROSS_CHECKER REPORT
- run_id: 2026-02-05_run-001
- generated_at: 2026-02-05T08:19:34Z
- status: DONE
- exit_code: 0
- raw_output: CODEX_AGENTS/WORK_LOGS/2026-02-05_run-001/CROSS_CHECKER.raw.md

## 검사 결과
- Overall: FAIL

## 위반 목록
- Severity: Major
- File: CODEX_AGENTS/WORK_LOGS/2026-02-05_run-001/CROSS_CHECKER.raw.md
- Rule: validator reported FAIL
- Evidence: raw_output 파일의 FAIL 항목 참조
- Fix Direction: FAIL 항목별 수정 후 동일 validator 재검증

## 정상 항목
- raw_output 파일 참조

## Remediation
- Priority=P0 | Source=CROSS_CHECKER | Type=DOC_FIX | Action=FAIL 근거를 기준으로 문서 수정 패스를 수행한다. | Evidence=CROSS_CHECKER.raw.md의 FAIL 항목 | DoneWhen=CROSS_CHECKER 재검증 결과가 PASS다.
