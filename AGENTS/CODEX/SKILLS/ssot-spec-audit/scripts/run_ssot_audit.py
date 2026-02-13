#!/usr/bin/env python3
"""Run multi-agent SSOT audit and emit a single human-readable REPORT.md."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

SEVERITY_ORDER = {
    "critical": 4,
    "high": 3,
    "medium": 2,
    "low": 1,
}

HUMAN_ARTIFACTS_TO_REMOVE = [
    "SUMMARY.md",
    "TOP_FINDINGS.md",
    "AREA_MATRIX.md",
    "RELATION_MATRIX.md",
    "DUPLICATION_MATRIX.md",
    "AGENT_SPEC_MATRIX.md",
    "TRACEABILITY_MATRIX.md",
    "AREA_MATRIX.csv",
    "RELATION_MATRIX.csv",
    "DUPLICATION_MATRIX.csv",
    "AGENT_SPEC_MATRIX.csv",
    "TRACEABILITY_MATRIX.csv",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run ssot-spec-audit and generate REPORT.md as the primary human-readable artifact."
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root path (default: current directory)",
    )
    parser.add_argument(
        "--keep-aux-files",
        action="store_true",
        help="Keep legacy human-readable files (SUMMARY/matrix/TOP_FINDINGS).",
    )
    parser.add_argument(
        "orchestrator_args",
        nargs=argparse.REMAINDER,
        help="Arguments forwarded to orchestrate_multi_agent_audit.py",
    )
    return parser.parse_args()


def max_severity(findings: List[Dict[str, Any]]) -> str:
    if not findings:
        return "low"
    return max(
        (finding.get("severity", "low") for finding in findings),
        key=lambda severity: SEVERITY_ORDER.get(severity, 0),
    )


def extract_run_dir(text: str) -> Path | None:
    pattern = re.compile(r"\[OK\]\s+Multi-agent audit completed:\s*(.+)")
    matches = pattern.findall(text)
    if not matches:
        return None
    return Path(matches[-1].strip())


def fallback_latest_run_dir(repo_root: Path) -> Path | None:
    base = repo_root / "AGENTS" / "CODEX" / "reports" / "ssot-spec-audit"
    if not base.exists():
        return None
    dirs = [path for path in base.iterdir() if path.is_dir()]
    if not dirs:
        return None
    return sorted(dirs, key=lambda path: path.stat().st_mtime)[-1]


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_results(run_dir: Path) -> List[Dict[str, Any]]:
    worker_dir = run_dir / "worker_results"
    if not worker_dir.exists():
        return []

    results = []
    for path in sorted(worker_dir.glob("*.json")):
        if path.name.endswith(".worker.json"):
            continue
        try:
            payload = read_json(path)
        except Exception:  # noqa: BLE001
            continue
        if isinstance(payload, dict):
            results.append(payload)

    results.sort(
        key=lambda result: (
            -SEVERITY_ORDER.get(max_severity(result.get("findings", [])), 0),
            result.get("task_id", ""),
        )
    )
    return results


def build_report_markdown(run_dir: Path, final_report: Dict[str, Any], results: List[Dict[str, Any]]) -> str:
    run_id = final_report.get("run_id", run_dir.name)
    status = str(final_report.get("status", "warn")).upper()
    fail_on = final_report.get("fail_on", "high")
    totals = final_report.get("severity_totals", {"critical": 0, "high": 0, "medium": 0, "low": 0})

    lines: List[str] = [
        "# SSOT Audit REPORT",
        "",
        f"- Run ID: `{run_id}`",
        f"- Final status: **{status}**",
        f"- Gate threshold: `{fail_on}`",
        f"- Generated at: `{datetime.now().isoformat(timespec='seconds')}`",
        "",
        "## 1) 종합 요약",
        "",
        f"- critical: {totals.get('critical', 0)}",
        f"- high: {totals.get('high', 0)}",
        f"- medium: {totals.get('medium', 0)}",
        f"- low: {totals.get('low', 0)}",
        "",
        "## 2) 우선 조치 대상 (Critical/High)",
        "",
    ]

    top_findings = final_report.get("top_findings", [])
    major = [finding for finding in top_findings if finding.get("severity") in {"critical", "high"}]
    if not major:
        lines.append("- 없음")
    else:
        for finding in major[:25]:
            lines.append(
                "- [{severity}] `{task}` `{target}` `{code}`: {message}".format(
                    severity=str(finding.get("severity", "low")).upper(),
                    task=finding.get("task_id", "-"),
                    target=f"{finding.get('target_kind', '-')}/{finding.get('target_id', '-')}",
                    code=finding.get("code", "UNSPECIFIED"),
                    message=finding.get("message", ""),
                )
            )

    lines.extend(
        [
            "",
            "## 3) 태스크별 분석",
            "",
            "형식:",
            "- 원인",
            "- 원인이라고 판단한 이유",
            "- 구체적인 수정 제안",
            "",
        ]
    )

    for result in results:
        task_id = result.get("task_id", "UNKNOWN")
        target = result.get("target", {})
        target_kind = target.get("kind", "-")
        target_id = target.get("id", "-")
        status_label = str(result.get("status", "error")).upper()
        findings = result.get("findings", [])
        max_sev = max_severity(findings).upper() if isinstance(findings, list) else "LOW"

        lines.append(
            f"### [{status_label}] {task_id} ({target_kind}/{target_id}, max={max_sev}, findings={len(findings) if isinstance(findings, list) else 0})"
        )
        lines.append("")

        if not findings:
            lines.append("- 원인: 검출 이슈 없음")
            lines.append("- 원인이라고 판단한 이유: 워커 결과의 finding 배열이 비어 있음")
            lines.append("- 구체적인 수정 제안: 없음")
            lines.append("")
            continue

        for idx, finding in enumerate(findings, start=1):
            severity = str(finding.get("severity", "low")).upper()
            code = finding.get("code", "UNSPECIFIED")
            message = finding.get("message", "No message")
            lines.append(f"{idx}. [{severity}] `{code}`")
            lines.append(f"- 원인: {message}")

            evidence = finding.get("evidence", [])
            evidence_items = []
            if isinstance(evidence, list):
                for ev in evidence[:4]:
                    if not isinstance(ev, dict):
                        continue
                    ev_path = ev.get("path")
                    if not ev_path:
                        continue
                    ev_line = ev.get("line")
                    if ev_line:
                        evidence_items.append(f"`{ev_path}:{ev_line}`")
                    else:
                        evidence_items.append(f"`{ev_path}`")

            if evidence_items:
                lines.append(
                    "- 원인이라고 판단한 이유: "
                    + ", ".join(evidence_items)
                    + " 경로에서 해당 정합성 위반이 보고됨"
                )
            else:
                lines.append("- 원인이라고 판단한 이유: 워커 메시지와 태스크 스코프 검증 결과를 근거로 판단")

            proposed_fix = str(finding.get("proposed_fix", "")).strip()
            if proposed_fix:
                lines.append(f"- 구체적인 수정 제안: {proposed_fix}")
            else:
                lines.append("- 구체적인 수정 제안: 관련 스코프 문서를 단일 SSOT 기준으로 정렬하고 중복/충돌 규칙을 제거")
            lines.append("")

    lines.extend(
        [
            "## 4) 참고 기계 산출물",
            "",
            "- `final_report.json`",
            "- `worker_results/*.json`",
            "",
        ]
    )

    return "\n".join(lines)


def cleanup_aux_files(run_dir: Path) -> None:
    for name in HUMAN_ARTIFACTS_TO_REMOVE:
        path = run_dir / name
        if path.exists() and path.is_file():
            path.unlink()


def run() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    orchestrator_path = (
        repo_root
        / "AGENTS"
        / "CODEX"
        / "SKILLS"
        / "ssot-spec-audit"
        / "scripts"
        / "orchestrate_multi_agent_audit.py"
    )
    if not orchestrator_path.exists():
        print(f"[ERROR] orchestrator not found: {orchestrator_path}", file=sys.stderr)
        return 2

    forwarded_args = list(args.orchestrator_args)
    if forwarded_args and forwarded_args[0] == "--":
        forwarded_args = forwarded_args[1:]

    command = ["python3", str(orchestrator_path)] + forwarded_args

    proc = subprocess.run(command, capture_output=True, text=True)

    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, file=sys.stderr, end="")

    run_dir = extract_run_dir((proc.stdout or "") + "\n" + (proc.stderr or ""))
    if run_dir is None:
        run_dir = fallback_latest_run_dir(repo_root)

    if run_dir is None or not run_dir.exists():
        print("[WARN] run directory not found; REPORT.md generation skipped", file=sys.stderr)
        return proc.returncode

    final_report_path = run_dir / "final_report.json"
    if not final_report_path.exists():
        print(f"[WARN] final_report.json missing at {final_report_path}; REPORT.md generation skipped", file=sys.stderr)
        return proc.returncode

    final_report = read_json(final_report_path)
    results = load_results(run_dir)

    report_text = build_report_markdown(run_dir, final_report, results)
    report_path = run_dir / "REPORT.md"
    report_path.write_text(report_text + "\n", encoding="utf-8")

    if not args.keep_aux_files:
        cleanup_aux_files(run_dir)

    print(f"[OK] Human report generated: {report_path}")
    if not args.keep_aux_files:
        print("[OK] Removed auxiliary human-check files (SUMMARY/matrix/TOP_FINDINGS)")

    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(run())
