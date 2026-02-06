#!/usr/bin/env bash
set -uo pipefail

MODE="date"
CUSTOM_RUN_ID=""
SANDBOX="read-only"
MODEL=""

usage() {
  cat <<'USAGE'
Usage:
  CODEX_AGENTS/scripts/run_all_validators.sh [options]

Options:
  --mode date|count       run id generation mode (default: date)
  --run-id RUN_ID         custom run id
  --sandbox MODE          codex sandbox (default: read-only)
  --model MODEL           codex model override
  -h, --help              show help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="${2:-}"
      shift 2
      ;;
    --run-id)
      CUSTOM_RUN_ID="${2:-}"
      shift 2
      ;;
    --sandbox)
      SANDBOX="${2:-}"
      shift 2
      ;;
    --model)
      MODEL="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ROOT_DIR="$(cd "${AGENTS_DIR}/.." && pwd)"

if [[ -n "${CUSTOM_RUN_ID}" ]]; then
  RUN_ID="$(${SCRIPT_DIR}/init_run.sh --id "${CUSTOM_RUN_ID}")"
else
  RUN_ID="$(${SCRIPT_DIR}/init_run.sh --mode "${MODE}")"
fi

RUN_DIR="${AGENTS_DIR}/WORK_LOGS/${RUN_ID}"

AGENT_KEYS=(
  "PRODUCT_VALIDATOR"
  "DESIGN_VALIDATOR"
  "API_VALIDATOR"
  "DOMAIN_VALIDATOR"
  "CROSS_CHECKER"
)

OVERALLS=()
EXEC_STATUSES=()
EXIT_CODES=()
REMEDIATIONS=()
RAW_PATHS=()
REMEDIATION_LLM_USED=0
REMEDIATION_LLM_STATUS="NOT_RUN"

for _ in "${AGENT_KEYS[@]}"; do
  OVERALLS+=("UNKNOWN")
  EXEC_STATUSES+=("NOT_RUN")
  EXIT_CODES+=("-1")
  REMEDIATIONS+=("미실행")
  RAW_PATHS+=("")
done

detect_overall() {
  local file="$1"

  if [[ ! -s "${file}" ]]; then
    echo "UNKNOWN"
    return
  fi

  if grep -Fq 'Overall: PASS | FAIL' "${file}" || grep -Fq 'Overall: FAIL | PASS' "${file}"; then
    echo "UNKNOWN"
    return
  fi

  if grep -Eq '^PASS$|^FAIL$' "${file}"; then
    grep -E '^PASS$|^FAIL$' "${file}" | head -n1
    return
  fi
  if grep -Eq 'Overall:[[:space:]]*PASS' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq 'Overall:[[:space:]]*FAIL' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '검증 결과:[[:space:]]*\*\*PASS\*\*' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '검증 결과:[[:space:]]*\*\*FAIL\*\*' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '검증 결과:[[:space:]]*`PASS`' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '검증 결과:[[:space:]]*`FAIL`' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '검증 결과:.*PASS' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '검증 결과:.*FAIL' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '결과:[[:space:]]*`PASS`' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '결과:[[:space:]]*`FAIL`' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '결과:[[:space:]]*PASS' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '결과:[[:space:]]*FAIL' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '전체 판정:[[:space:]]*`PASS`' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '전체 판정:[[:space:]]*`FAIL`' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '`RESULT`:[[:space:]]*`PASS`' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '`RESULT`:[[:space:]]*`FAIL`' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq 'RESULT:[[:space:]]*`PASS`' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq 'RESULT:[[:space:]]*`FAIL`' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq 'RESULT:[[:space:]]*PASS' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq 'RESULT:[[:space:]]*FAIL' "${file}"; then
    echo "FAIL"
    return
  fi

  echo "UNKNOWN"
}

normalize_exec_status() {
  local exit_code="$1"
  local overall="$2"

  if [[ "${exit_code}" -eq 0 ]]; then
    if [[ "${overall}" == "UNKNOWN" ]]; then
      echo "DONE_WITH_PARSE_WARNING"
    else
      echo "DONE"
    fi
    return
  fi

  if [[ "${exit_code}" -eq 130 || "${exit_code}" -eq 143 ]]; then
    echo "INTERRUPTED"
    return
  fi

  echo "ERROR"
}

default_remediation() {
  local key="$1"
  local overall="$2"
  local exec_status="$3"

  if [[ "${exec_status}" == "DONE" && "${overall}" == "PASS" ]]; then
    echo "없음"
    return
  fi

  if [[ "${overall}" == "FAIL" ]]; then
    echo "Priority=P0 | Source=${key} | Type=DOC_FIX | Action=FAIL 근거를 기준으로 문서 수정 패스를 수행한다. | Evidence=${key}.raw.md의 FAIL 항목 | DoneWhen=${key} 재검증 결과가 PASS다."
    return
  fi

  if [[ "${exec_status}" == "INTERRUPTED" ]]; then
    echo "Priority=P0 | Source=${key} | Type=RERUN | Action=중단 원인을 제거하고 해당 validator를 재실행한다. | Evidence=exec_status=INTERRUPTED | DoneWhen=raw 출력이 완전하고 Overall 판정이 생성된다."
    return
  fi

  if [[ "${exec_status}" == "ERROR" ]]; then
    echo "Priority=P0 | Source=${key} | Type=RERUN | Action=실행 오류 원인(환경/명령)을 수정한 뒤 validator를 재실행한다. | Evidence=exit_code!=0 | DoneWhen=validator exit_code=0 및 Overall 판정이 생성된다."
    return
  fi

  echo "Priority=P1 | Source=${key} | Type=PARSER_FIX | Action=raw_output를 근거로 후속 수정 작업을 정의하고 파서/정규화 규칙을 보정한다. | Evidence=Overall=UNKNOWN | DoneWhen=동일 raw에서 Overall이 PASS 또는 FAIL로 판정된다."
}

write_normalized_report() {
  local key="$1"
  local raw_file="$2"
  local out_file="$3"
  local overall="$4"
  local exec_status="$5"
  local exit_code="$6"
  local remediation="$7"
  local now_utc

  now_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  {
    echo "# ${key} REPORT"
    echo "- run_id: ${RUN_ID}"
    echo "- generated_at: ${now_utc}"
    echo "- status: ${exec_status}"
    echo "- exit_code: ${exit_code}"
    echo "- raw_output: ${raw_file}"
    echo
    echo "## 검사 결과"
    echo "- Overall: ${overall}"
    echo
    echo "## 위반 목록"

    if [[ "${overall}" == "PASS" && "${exec_status}" == "DONE" ]]; then
      echo "- 없음"
    elif [[ "${overall}" == "FAIL" ]]; then
      echo "- Severity: Major"
      echo "- File: ${raw_file}"
      echo "- Rule: validator reported FAIL"
      echo "- Evidence: raw_output 파일의 FAIL 항목 참조"
      echo "- Fix Direction: FAIL 항목별 수정 후 동일 validator 재검증"
    else
      echo "- Severity: Blocking"
      echo "- File: ${raw_file}"
      echo "- Rule: validator 실행 또는 결과 파싱 실패"
      echo "- Evidence: status=${exec_status}, exit_code=${exit_code}, overall=${overall}"
      echo "- Fix Direction: 실행/출력 형식 문제 해결 후 validator 재실행"
    fi

    echo
    echo "## 정상 항목"
    if [[ "${overall}" == "PASS" && "${exec_status}" == "DONE" ]]; then
      echo "- validator 보고서 기준 정상"
    else
      echo "- raw_output 파일 참조"
    fi

    echo
    echo "## Remediation"
    echo "- ${remediation}"
  } > "${out_file}"
}

write_fallback_remediation_file() {
  local remediation_file="$1"
  local now_utc="$2"
  local overall_run_status="$3"
  local any_pending=0
  local rq=1

  {
    echo "# REMEDIATION_PLAN"
    echo "- run_id: ${RUN_ID}"
    echo "- generated_at: ${now_utc}"
    echo "- status: ${overall_run_status}"
    echo
    echo "## 작업 큐"
    for idx in "${!AGENT_KEYS[@]}"; do
      if [[ "${REMEDIATIONS[$idx]}" != "없음" ]]; then
        any_pending=1
        echo "- [RQ-$(printf '%03d' "${rq}")] ${REMEDIATIONS[$idx]}"
        rq=$((rq + 1))
      fi
    done
    if [[ "${any_pending}" -eq 0 ]]; then
      echo "- 없음"
    fi
  } > "${remediation_file}"
}

run_llm_remediation() {
  local rem_spec rem_raw_rel rem_raw_abs rem_file rem_prompt
  local raw_inputs raw_list
  local rem_rc=0

  rem_spec="CODEX_AGENTS/REMEDIATION_SYNTHESIZER.md"
  rem_raw_rel="CODEX_AGENTS/WORK_LOGS/${RUN_ID}/REMEDIATION_PLAN.raw.md"
  rem_raw_abs="${RUN_DIR}/REMEDIATION_PLAN.raw.md"
  rem_file="${RUN_DIR}/REMEDIATION_PLAN.md"

  raw_list=""
  while IFS= read -r raw_inputs; do
    raw_list="${raw_list}
- ${raw_inputs#${ROOT_DIR}/}"
  done < <(find "${RUN_DIR}" -maxdepth 1 -type f -name '*.raw.md' ! -name 'REMEDIATION_PLAN.raw.md' | sort)

  rem_prompt="${rem_spec} 규칙만 사용해 최종 remediation plan을 생성한다. 대상 RUN_ID는 ${RUN_ID}다. 아래 입력 raw 목록은 RUN_ID 디렉토리의 *.raw.md 전체다(출력 파일 제외).${raw_list}
파일 수정은 금지하고, 출력 템플릿을 엄격히 따른다."

  CMD=(codex exec --skip-git-repo-check -s "${SANDBOX}" -C "${ROOT_DIR}")
  if [[ -n "${MODEL}" ]]; then
    CMD+=(-m "${MODEL}")
  fi
  CMD+=("${rem_prompt}" -o "${rem_raw_rel}")

  echo "-> REMEDIATION_SYNTHESIZER 실행 중..."
  "${CMD[@]}" || rem_rc=$?

  if [[ "${rem_rc}" -ne 0 ]]; then
    REMEDIATION_LLM_STATUS="ERROR(${rem_rc})"
    return
  fi

  if [[ ! -s "${rem_raw_abs}" ]]; then
    REMEDIATION_LLM_STATUS="EMPTY_OUTPUT"
    return
  fi

  if grep -Fq '# REMEDIATION_PLAN' "${rem_raw_abs}" && grep -Fq '## 작업 큐' "${rem_raw_abs}"; then
    cp "${rem_raw_abs}" "${rem_file}"
    REMEDIATION_LLM_USED=1
    REMEDIATION_LLM_STATUS="DONE"
    return
  fi

  REMEDIATION_LLM_STATUS="INVALID_FORMAT"
}

finalize_summary() {
  local now_utc summary_file remediation_file
  local blocking=0 major=0 minor=0
  local overall_run_status="DONE"
  local any_pending=0
  local rq=1

  if [[ -z "${RUN_DIR:-}" || ! -d "${RUN_DIR}" ]]; then
    return
  fi

  now_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  summary_file="${RUN_DIR}/SUMMARY.md"
  remediation_file="${RUN_DIR}/REMEDIATION_PLAN.md"

  for idx in "${!AGENT_KEYS[@]}"; do
    if [[ "${EXEC_STATUSES[$idx]}" != "DONE" && "${EXEC_STATUSES[$idx]}" != "DONE_WITH_PARSE_WARNING" ]]; then
      blocking=$((blocking + 1))
      overall_run_status="PARTIAL"
      continue
    fi

    if [[ "${OVERALLS[$idx]}" == "FAIL" ]]; then
      major=$((major + 1))
      overall_run_status="PARTIAL"
      continue
    fi

    if [[ "${OVERALLS[$idx]}" == "UNKNOWN" ]]; then
      blocking=$((blocking + 1))
      overall_run_status="PARTIAL"
    fi
  done

  {
    echo "# SUMMARY"
    echo "- run_id: ${RUN_ID}"
    echo "- generated_at: ${now_utc}"
    echo "- status: ${overall_run_status}"
    echo
    echo "## 결과 요약"
    echo "- Blocking: ${blocking}"
    echo "- Major: ${major}"
    echo "- Minor: ${minor}"
    echo
    echo "## Validator Status"
    for idx in "${!AGENT_KEYS[@]}"; do
      echo "- ${AGENT_KEYS[$idx]}: overall=${OVERALLS[$idx]}, status=${EXEC_STATUSES[$idx]}, exit_code=${EXIT_CODES[$idx]}, raw=${RAW_PATHS[$idx]}"
    done
    echo "- REMEDIATION_SYNTHESIZER: ${REMEDIATION_LLM_STATUS}"
    echo
    echo "## 다음 액션"
    if [[ "${REMEDIATION_LLM_USED}" -eq 1 && -s "${remediation_file}" ]]; then
      while IFS= read -r action; do
        if [[ "${action}" != "없음" && -n "${action}" ]]; then
          any_pending=1
          echo "- ${action}"
        fi
      done < <(awk '
        /^## 작업 큐/ {in_queue=1; next}
        /^## / {if (in_queue) exit}
        in_queue && /^- / {sub(/^- /, ""); print}
      ' "${remediation_file}")
    else
      rq=1
      for idx in "${!AGENT_KEYS[@]}"; do
        if [[ "${REMEDIATIONS[$idx]}" != "없음" ]]; then
          any_pending=1
          echo "- [RQ-$(printf '%03d' "${rq}")] ${REMEDIATIONS[$idx]}"
          rq=$((rq + 1))
        fi
      done
    fi
    if [[ "${any_pending}" -eq 0 ]]; then
      echo "- 없음"
    fi
  } > "${summary_file}"

  if [[ "${REMEDIATION_LLM_USED}" -ne 1 ]]; then
    write_fallback_remediation_file "${remediation_file}" "${now_utc}" "${overall_run_status}"
  fi
}

trap finalize_summary EXIT

echo "RUN_ID: ${RUN_ID}"
echo "RUN_DIR: ${RUN_DIR}"

for idx in "${!AGENT_KEYS[@]}"; do
  KEY="${AGENT_KEYS[$idx]}"
  SPEC_FILE="CODEX_AGENTS/${KEY}.md"
  RAW_FILE="CODEX_AGENTS/WORK_LOGS/${RUN_ID}/${KEY}.raw.md"
  OUT_FILE="CODEX_AGENTS/WORK_LOGS/${RUN_ID}/${KEY}.md"

  PROMPT="${SPEC_FILE} 규칙만 사용해 검증만 수행한다. 스코프 외 참조 금지. 파일 수정 금지. 출력은 반드시 PASS/FAIL 구조를 포함한다."

  CMD=(codex exec --skip-git-repo-check -s "${SANDBOX}" -C "${ROOT_DIR}")
  if [[ -n "${MODEL}" ]]; then
    CMD+=(-m "${MODEL}")
  fi
  CMD+=("${PROMPT}" -o "${RAW_FILE}")

  echo "-> ${KEY} 실행 중..."
  RC=0
  "${CMD[@]}" || RC=$?

  if [[ ! -s "${RAW_FILE}" ]]; then
    {
      echo "[runner] output missing"
      echo "- key: ${KEY}"
      echo "- exit_code: ${RC}"
      echo "- message: codex exec output file not written"
    } > "${RAW_FILE}"
  fi

  OVERALL="$(detect_overall "${RAW_FILE}")"
  EXEC_STATUS="$(normalize_exec_status "${RC}" "${OVERALL}")"
  REMED="$(default_remediation "${KEY}" "${OVERALL}" "${EXEC_STATUS}")"

  OVERALLS[$idx]="${OVERALL}"
  EXEC_STATUSES[$idx]="${EXEC_STATUS}"
  EXIT_CODES[$idx]="${RC}"
  REMEDIATIONS[$idx]="${REMED}"
  RAW_PATHS[$idx]="${RAW_FILE}"

  write_normalized_report "${KEY}" "${RAW_FILE}" "${OUT_FILE}" "${OVERALL}" "${EXEC_STATUS}" "${RC}" "${REMED}"
done

run_llm_remediation

echo "완료: ${RUN_DIR}/SUMMARY.md"
echo "완료: ${RUN_DIR}/REMEDIATION_PLAN.md"
