#!/usr/bin/env bash
set -euo pipefail

RUN_ID=""

usage() {
  cat <<'USAGE'
Usage:
  CODEX_AGENTS/scripts/repair_run_outputs.sh --run-id RUN_ID

Description:
  Normalize validator reports in an existing WORK_LOGS run directory,
  regenerate SUMMARY.md and REMEDIATION_PLAN.md without rerunning validators.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --run-id)
      RUN_ID="${2:-}"
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

if [[ -z "${RUN_ID}" ]]; then
  echo "--run-id is required" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
RUN_DIR="${AGENTS_DIR}/WORK_LOGS/${RUN_ID}"

if [[ ! -d "${RUN_DIR}" ]]; then
  echo "Run directory not found: ${RUN_DIR}" >&2
  exit 1
fi

AGENT_KEYS=(
  "PRODUCT_VALIDATOR"
  "DESIGN_VALIDATOR"
  "API_VALIDATOR"
  "DOMAIN_VALIDATOR"
  "CROSS_CHECKER"
)

OVERALLS=()
STATUSES=()
REMEDIATIONS=()
RAW_PATHS=()

for _ in "${AGENT_KEYS[@]}"; do
  OVERALLS+=("UNKNOWN")
  STATUSES+=("NOT_RUN")
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
  if grep -Eq '검증 결과:[[:space:]]*\*\*PASS\*\*|검증 결과:[[:space:]]*`PASS`|검증 결과:.*PASS' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '검증 결과:[[:space:]]*\*\*FAIL\*\*|검증 결과:[[:space:]]*`FAIL`|검증 결과:.*FAIL' "${file}"; then
    echo "FAIL"
    return
  fi
  if grep -Eq '결과:[[:space:]]*`PASS`|결과:[[:space:]]*PASS' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '결과:[[:space:]]*`FAIL`|결과:[[:space:]]*FAIL' "${file}"; then
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
  if grep -Eq '`RESULT`:[[:space:]]*`PASS`|RESULT:[[:space:]]*`PASS`|RESULT:[[:space:]]*PASS' "${file}"; then
    echo "PASS"
    return
  fi
  if grep -Eq '`RESULT`:[[:space:]]*`FAIL`|RESULT:[[:space:]]*`FAIL`|RESULT:[[:space:]]*FAIL' "${file}"; then
    echo "FAIL"
    return
  fi

  echo "UNKNOWN"
}

default_remediation() {
  local key="$1"
  local overall="$2"
  local status="$3"

  if [[ "${status}" == "DONE" && "${overall}" == "PASS" ]]; then
    echo "없음"
    return
  fi

  if [[ "${overall}" == "FAIL" ]]; then
    echo "Priority=P0 | Source=${key} | Type=DOC_FIX | Action=FAIL 근거를 기준으로 문서 수정 패스를 수행한다. | Evidence=${key}.raw.md의 FAIL 항목 | DoneWhen=${key} 재검증 결과가 PASS다."
    return
  fi

  if [[ "${status}" == "ERROR" ]]; then
    echo "Priority=P0 | Source=${key} | Type=FORMAT_FIX | Action=누락/손상된 결과 파일을 보정한다. | Evidence=raw 파일 누락 또는 손상 | DoneWhen=raw 파일이 생성되고 Overall 판정이 가능하다."
    return
  fi

  echo "Priority=P1 | Source=${key} | Type=PARSER_FIX | Action=raw_output를 근거로 후속 수정 작업을 정의하고 파서/정규화 규칙을 보정한다. | Evidence=Overall=UNKNOWN | DoneWhen=동일 raw에서 Overall이 PASS 또는 FAIL로 판정된다."
}

write_report() {
  local key="$1"
  local raw_file="$2"
  local out_file="$3"
  local overall="$4"
  local status="$5"
  local remediation="$6"
  local now_utc

  now_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  {
    echo "# ${key} REPORT"
    echo "- run_id: ${RUN_ID}"
    echo "- generated_at: ${now_utc}"
    echo "- status: ${status}"
    echo "- raw_output: ${raw_file}"
    echo
    echo "## 검사 결과"
    echo "- Overall: ${overall}"
    echo
    echo "## 위반 목록"

    if [[ "${overall}" == "PASS" && "${status}" == "DONE" ]]; then
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
      echo "- Rule: 결과 파일 누락 또는 출력 파싱 실패"
      echo "- Evidence: status=${status}, overall=${overall}"
      echo "- Fix Direction: 출력 형식/누락 문제 해결 후 validator 재실행"
    fi

    echo
    echo "## 정상 항목"
    if [[ "${overall}" == "PASS" && "${status}" == "DONE" ]]; then
      echo "- validator 보고서 기준 정상"
    else
      echo "- raw_output 파일 참조"
    fi

    echo
    echo "## Remediation"
    echo "- ${remediation}"
  } > "${out_file}"
}

for idx in "${!AGENT_KEYS[@]}"; do
  KEY="${AGENT_KEYS[$idx]}"
  OUT_FILE="${RUN_DIR}/${KEY}.md"
  RAW_FILE="${RUN_DIR}/${KEY}.raw.md"

  if [[ ! -f "${RAW_FILE}" ]]; then
    if [[ -f "${OUT_FILE}" ]]; then
      cp "${OUT_FILE}" "${RAW_FILE}"
      STATUS="DONE"
    else
      {
        echo "[repair] missing validator output"
        echo "- key: ${KEY}"
      } > "${RAW_FILE}"
      STATUS="ERROR"
    fi
  else
    STATUS="DONE"
  fi

  OVERALL="$(detect_overall "${RAW_FILE}")"
  if [[ "${STATUS}" == "DONE" && "${OVERALL}" == "UNKNOWN" ]]; then
    STATUS="DONE_WITH_PARSE_WARNING"
  fi

  REMED="$(default_remediation "${KEY}" "${OVERALL}" "${STATUS}")"

  OVERALLS[$idx]="${OVERALL}"
  STATUSES[$idx]="${STATUS}"
  REMEDIATIONS[$idx]="${REMED}"
  RAW_PATHS[$idx]="${RAW_FILE}"

  write_report "${KEY}" "${RAW_FILE}" "${OUT_FILE}" "${OVERALL}" "${STATUS}" "${REMED}"
done

NOW_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
SUMMARY_FILE="${RUN_DIR}/SUMMARY.md"
REMED_FILE="${RUN_DIR}/REMEDIATION_PLAN.md"

BLOCKING=0
MAJOR=0
MINOR=0
RUN_STATUS="DONE"
HAS_ACTION=0
RQ=1

for idx in "${!AGENT_KEYS[@]}"; do
  if [[ "${STATUSES[$idx]}" != "DONE" && "${STATUSES[$idx]}" != "DONE_WITH_PARSE_WARNING" ]]; then
    BLOCKING=$((BLOCKING + 1))
    RUN_STATUS="PARTIAL"
    continue
  fi
  if [[ "${OVERALLS[$idx]}" == "FAIL" ]]; then
    MAJOR=$((MAJOR + 1))
    RUN_STATUS="PARTIAL"
    continue
  fi
  if [[ "${OVERALLS[$idx]}" == "UNKNOWN" ]]; then
    BLOCKING=$((BLOCKING + 1))
    RUN_STATUS="PARTIAL"
  fi
done

{
  echo "# SUMMARY"
  echo "- run_id: ${RUN_ID}"
  echo "- generated_at: ${NOW_UTC}"
  echo "- status: ${RUN_STATUS}"
  echo
  echo "## 결과 요약"
  echo "- Blocking: ${BLOCKING}"
  echo "- Major: ${MAJOR}"
  echo "- Minor: ${MINOR}"
  echo
  echo "## Validator Status"
  for idx in "${!AGENT_KEYS[@]}"; do
    echo "- ${AGENT_KEYS[$idx]}: overall=${OVERALLS[$idx]}, status=${STATUSES[$idx]}, raw=${RAW_PATHS[$idx]}"
  done
  echo
  echo "## 다음 액션"
  for idx in "${!AGENT_KEYS[@]}"; do
    if [[ "${REMEDIATIONS[$idx]}" != "없음" ]]; then
      HAS_ACTION=1
      echo "- [RQ-$(printf '%03d' "${RQ}")] ${REMEDIATIONS[$idx]}"
      RQ=$((RQ + 1))
    fi
  done
  if [[ "${HAS_ACTION}" -eq 0 ]]; then
    echo "- 없음"
  fi
} > "${SUMMARY_FILE}"

HAS_ACTION=0
RQ=1
{
  echo "# REMEDIATION_PLAN"
  echo "- run_id: ${RUN_ID}"
  echo "- generated_at: ${NOW_UTC}"
  echo "- status: ${RUN_STATUS}"
  echo
  echo "## 작업 큐"
  for idx in "${!AGENT_KEYS[@]}"; do
    if [[ "${REMEDIATIONS[$idx]}" != "없음" ]]; then
      HAS_ACTION=1
      echo "- [RQ-$(printf '%03d' "${RQ}")] ${REMEDIATIONS[$idx]}"
      RQ=$((RQ + 1))
    fi
  done
  if [[ "${HAS_ACTION}" -eq 0 ]]; then
    echo "- 없음"
  fi
} > "${REMED_FILE}"

echo "repaired: ${RUN_DIR}"
