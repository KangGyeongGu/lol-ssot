#!/usr/bin/env bash
set -euo pipefail

MODE="date"
CUSTOM_ID=""

usage() {
  cat <<'EOF'
Usage:
  CODEX_AGENTS/scripts/init_run.sh [--mode date|count] [--id RUN_ID]

Options:
  --mode date|count   date: YYYY-MM-DD_run-001, count: run-001 (default: date)
  --id RUN_ID         custom run id (mode option ignored)
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="${2:-}"
      shift 2
      ;;
    --id)
      CUSTOM_ID="${2:-}"
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
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
LOG_ROOT="${ROOT_DIR}/WORK_LOGS"

mkdir -p "${LOG_ROOT}"

if [[ -n "${CUSTOM_ID}" ]]; then
  RUN_ID="${CUSTOM_ID}"
else
  case "${MODE}" in
    date)
      DAY="$(date +%F)"
      COUNT=$(find "${LOG_ROOT}" -maxdepth 1 -type d -name "${DAY}_run-*" | wc -l | tr -d ' ')
      NEXT=$((COUNT + 1))
      RUN_ID="$(printf "%s_run-%03d" "${DAY}" "${NEXT}")"
      ;;
    count)
      COUNT=$(find "${LOG_ROOT}" -maxdepth 1 -type d -name "run-*" | wc -l | tr -d ' ')
      NEXT=$((COUNT + 1))
      RUN_ID="$(printf "run-%03d" "${NEXT}")"
      ;;
    *)
      echo "Invalid mode: ${MODE}" >&2
      exit 1
      ;;
  esac
fi

RUN_DIR="${LOG_ROOT}/${RUN_ID}"
if [[ -d "${RUN_DIR}" ]]; then
  echo "Run directory already exists: ${RUN_DIR}" >&2
  exit 1
fi

mkdir -p "${RUN_DIR}"

GEN_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
AGENTS=(
  "PRODUCT_VALIDATOR"
  "DESIGN_VALIDATOR"
  "API_VALIDATOR"
  "DOMAIN_VALIDATOR"
  "CROSS_CHECKER"
)

for AGENT in "${AGENTS[@]}"; do
  FILE="${RUN_DIR}/${AGENT}.md"
  cat > "${FILE}" <<EOF
# ${AGENT} REPORT
- run_id: ${RUN_ID}
- generated_at: ${GEN_AT}
- status: TODO

## 검사 결과
- Overall: PASS | FAIL

## 위반 목록
- Severity: Blocking | Major | Minor
- File:
- Rule:
- Evidence:
- Fix Direction:

## 정상 항목
-
EOF
done

cat > "${RUN_DIR}/SUMMARY.md" <<EOF
# SUMMARY
- run_id: ${RUN_ID}
- generated_at: ${GEN_AT}
- status: TODO

## 결과 요약
- Blocking:
- Major:
- Minor:

## 다음 액션
-
EOF

cat > "${RUN_DIR}/REMEDIATION_PLAN.md" <<EOF
# REMEDIATION_PLAN
- run_id: ${RUN_ID}
- generated_at: ${GEN_AT}
- status: TODO

## 작업 큐
-
EOF

cat > "${RUN_DIR}/REMEDIATION_PLAN.raw.md" <<EOF
# REMEDIATION_PLAN
- run_id: ${RUN_ID}
- generated_at: ${GEN_AT}
- status: TODO

## 근거 요약
-

## 작업 큐
-
EOF

echo "${RUN_ID}"
