#!/usr/bin/env python3
"""Run SSOT consistency audit with multiple Codex worker agents in parallel."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence

SEVERITY_ORDER = {
    "critical": 4,
    "high": 3,
    "medium": 2,
    "low": 1,
}

TARGET_KIND_ORDER = {
    "area": 0,
    "relation": 1,
    "duplication": 2,
    "agent_spec": 3,
    "traceability": 4,
}

VALID_SEVERITIES = set(SEVERITY_ORDER.keys())
VALID_STATUSES = {"pass", "warn", "fail", "error"}

DEFAULT_FAIL_ON = "high"


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    agent_id: str
    kind: str
    target_id: str
    scope_paths: Sequence[str]
    checks: Sequence[str]
    objective: str


def build_full_task_catalog() -> List[TaskSpec]:
    area_tasks = [
        TaskSpec(
            task_id="AREA-01_PRODUCT",
            agent_id="area-auditor",
            kind="area",
            target_id="01_PRODUCT",
            scope_paths=["01_PRODUCT"],
            checks=[
                "required_docs",
                "broken_links",
                "ssot_scope_boundary",
                "normative_statement_clarity",
            ],
            objective="Validate product requirement specs are complete, linked, and not redefining other area ownership.",
        ),
        TaskSpec(
            task_id="AREA-02_DESIGN",
            agent_id="area-auditor",
            kind="area",
            target_id="02_DESIGN",
            scope_paths=["02_DESIGN"],
            checks=[
                "required_docs",
                "broken_links",
                "token_consistency",
                "ssot_scope_boundary",
            ],
            objective="Validate design specs and token definitions with clear boundaries.",
        ),
        TaskSpec(
            task_id="AREA-03_API",
            agent_id="area-auditor",
            kind="area",
            target_id="03_API",
            scope_paths=["03_API"],
            checks=[
                "required_docs",
                "broken_links",
                "contract_completeness",
                "page_map_contract_alignment",
            ],
            objective="Validate API contract area integrity and page map alignment.",
        ),
        TaskSpec(
            task_id="AREA-04_DOMAIN",
            agent_id="area-auditor",
            kind="area",
            target_id="04_DOMAIN",
            scope_paths=["04_DOMAIN"],
            checks=[
                "required_docs",
                "broken_links",
                "domain_model_ownership",
                "cross_area_redefinition",
            ],
            objective="Validate domain model specs as SSOT for entities and persistence semantics.",
        ),
        TaskSpec(
            task_id="AREA-05_FRONTEND",
            agent_id="area-auditor",
            kind="area",
            target_id="05_FRONTEND",
            scope_paths=["05_FRONTEND"],
            checks=[
                "required_docs",
                "broken_links",
                "routing_state_api_alignment",
                "anti_pattern_consistency",
            ],
            objective="Validate frontend architecture and rules against upstream SSOT dependencies.",
        ),
        TaskSpec(
            task_id="AREA-06_BACKEND",
            agent_id="area-auditor",
            kind="area",
            target_id="06_BACKEND",
            scope_paths=["06_BACKEND"],
            checks=[
                "required_docs",
                "broken_links",
                "architecture_rule_consistency",
                "test_rule_coverage_statements",
            ],
            objective="Validate backend spec rules and architecture boundaries.",
        ),
    ]

    relation_tasks = [
        TaskSpec(
            task_id="REL-PRODUCT-DESIGN",
            agent_id="relation-auditor",
            kind="relation",
            target_id="PRODUCT_DESIGN",
            scope_paths=["01_PRODUCT", "02_DESIGN"],
            checks=[
                "required_link_presence",
                "intent_to_design_mapping",
                "duplication_and_conflict",
            ],
            objective="Ensure product requirements and design requirements maintain explicit and non-duplicated relationships.",
        ),
        TaskSpec(
            task_id="REL-PRODUCT-API",
            agent_id="relation-auditor",
            kind="relation",
            target_id="PRODUCT_API",
            scope_paths=["01_PRODUCT", "03_API"],
            checks=[
                "required_link_presence",
                "requirement_to_contract_mapping",
                "duplication_and_conflict",
            ],
            objective="Ensure user/product requirements are traceable to API contracts.",
        ),
        TaskSpec(
            task_id="REL-DESIGN-FRONTEND",
            agent_id="relation-auditor",
            kind="relation",
            target_id="DESIGN_FRONTEND",
            scope_paths=["02_DESIGN", "05_FRONTEND"],
            checks=[
                "required_link_presence",
                "token_usage_mapping",
                "duplication_and_conflict",
            ],
            objective="Ensure frontend rules correctly consume design tokens and page requirements.",
        ),
        TaskSpec(
            task_id="REL-API-FRONTEND",
            agent_id="relation-auditor",
            kind="relation",
            target_id="API_FRONTEND",
            scope_paths=["03_API", "05_FRONTEND"],
            checks=[
                "required_link_presence",
                "contract_usage_mapping",
                "duplication_and_conflict",
            ],
            objective="Ensure frontend API usage rules align with API contract SSOT.",
        ),
        TaskSpec(
            task_id="REL-API-BACKEND",
            agent_id="relation-auditor",
            kind="relation",
            target_id="API_BACKEND",
            scope_paths=["03_API", "06_BACKEND"],
            checks=[
                "required_link_presence",
                "implementation_contract_mapping",
                "duplication_and_conflict",
            ],
            objective="Ensure backend API implementation rules align with API contract SSOT.",
        ),
        TaskSpec(
            task_id="REL-DOMAIN-API",
            agent_id="relation-auditor",
            kind="relation",
            target_id="DOMAIN_API",
            scope_paths=["04_DOMAIN", "03_API"],
            checks=[
                "required_link_presence",
                "entity_contract_mapping",
                "duplication_and_conflict",
            ],
            objective="Ensure domain model and API contract references are consistent.",
        ),
        TaskSpec(
            task_id="REL-DOMAIN-BACKEND",
            agent_id="relation-auditor",
            kind="relation",
            target_id="DOMAIN_BACKEND",
            scope_paths=["04_DOMAIN", "06_BACKEND"],
            checks=[
                "required_link_presence",
                "domain_rule_usage_mapping",
                "duplication_and_conflict",
            ],
            objective="Ensure backend rules correctly reference domain model SSOT.",
        ),
    ]

    duplication_tasks = [
        TaskSpec(
            task_id="DUP-NORMATIVE",
            agent_id="duplication-auditor",
            kind="duplication",
            target_id="NORMATIVE_DUPLICATION",
            scope_paths=[
                "01_PRODUCT",
                "02_DESIGN",
                "03_API",
                "04_DOMAIN",
                "05_FRONTEND",
                "06_BACKEND",
            ],
            checks=[
                "duplicate_normative_statements",
                "conflicting_normative_statements",
            ],
            objective="Find duplicated or conflicting normative rules across SSOT areas.",
        ),
        TaskSpec(
            task_id="DUP-TERMINOLOGY",
            agent_id="duplication-auditor",
            kind="duplication",
            target_id="TERM_CONFLICT",
            scope_paths=[
                "01_PRODUCT",
                "02_DESIGN",
                "03_API",
                "04_DOMAIN",
                "05_FRONTEND",
                "06_BACKEND",
            ],
            checks=[
                "term_definition_conflict",
                "alias_without_mapping",
            ],
            objective="Find conflicting terms and definitions across SSOT areas.",
        ),
        TaskSpec(
            task_id="DUP-OWNERSHIP",
            agent_id="duplication-auditor",
            kind="duplication",
            target_id="OWNERSHIP_VIOLATION",
            scope_paths=[
                "01_PRODUCT",
                "02_DESIGN",
                "03_API",
                "04_DOMAIN",
                "05_FRONTEND",
                "06_BACKEND",
            ],
            checks=[
                "source_of_truth_violation",
                "cross_area_redefinition",
            ],
            objective="Find ownership violations where non-owner docs redefine another area's SSOT.",
        ),
    ]

    agent_spec_tasks = [
        TaskSpec(
            task_id="AGENTSPEC-BACKEND",
            agent_id="agent-spec-auditor",
            kind="agent_spec",
            target_id="BACKEND_AGENT_SKILL",
            scope_paths=[
                "AGENTS/CLAUDE/AGENTS/BACKEND",
                "AGENTS/CLAUDE/SKILLS/BACKEND",
                "AGENTS/CLAUDE/AGENTS/COMMON",
                "AGENTS/CLAUDE/SKILLS/COMMON",
            ],
            checks=[
                "role_scope_completeness",
                "domain_mapping_completeness",
                "required_reference_existence",
                "master_subskill_wiring",
            ],
            objective="Validate backend agent and skill system wiring against SSOT references.",
        ),
        TaskSpec(
            task_id="AGENTSPEC-FRONTEND",
            agent_id="agent-spec-auditor",
            kind="agent_spec",
            target_id="FRONTEND_AGENT_SKILL",
            scope_paths=[
                "AGENTS/CLAUDE/AGENTS/FRONTEND",
                "AGENTS/CLAUDE/SKILLS/FRONTEND",
                "AGENTS/CLAUDE/AGENTS/COMMON",
                "AGENTS/CLAUDE/SKILLS/COMMON",
            ],
            checks=[
                "role_scope_completeness",
                "domain_mapping_completeness",
                "required_reference_existence",
                "master_subskill_wiring",
            ],
            objective="Validate frontend agent and skill system wiring against SSOT references.",
        ),
    ]

    traceability_tasks = [
        TaskSpec(
            task_id="TRACE-E2E",
            agent_id="traceability-auditor",
            kind="traceability",
            target_id="E2E_TRACEABILITY",
            scope_paths=[
                "01_PRODUCT",
                "02_DESIGN",
                "03_API",
                "04_DOMAIN",
                "05_FRONTEND",
                "06_BACKEND",
            ],
            checks=[
                "requirement_to_design_to_api",
                "requirement_to_domain_to_backend",
                "requirement_to_api_to_frontend",
                "orphan_spec_detection",
            ],
            objective="Validate end-to-end traceability chain across all SSOT layers.",
        ),
    ]

    return area_tasks + relation_tasks + duplication_tasks + agent_spec_tasks + traceability_tasks


def infer_partial_relevant_targets(changed_files: Sequence[str]) -> Dict[str, set[str]]:
    mapping = {
        "area": set(),
        "relation": set(),
        "duplication": {"NORMATIVE_DUPLICATION", "TERM_CONFLICT", "OWNERSHIP_VIOLATION"},
        "agent_spec": set(),
        "traceability": {"E2E_TRACEABILITY"},
    }

    for path in changed_files:
        p = path.strip()
        if not p:
            continue

        if p.startswith("01_PRODUCT/"):
            mapping["area"].add("01_PRODUCT")
            mapping["relation"].update({"PRODUCT_DESIGN", "PRODUCT_API"})
        if p.startswith("02_DESIGN/"):
            mapping["area"].add("02_DESIGN")
            mapping["relation"].update({"PRODUCT_DESIGN", "DESIGN_FRONTEND"})
        if p.startswith("03_API/"):
            mapping["area"].add("03_API")
            mapping["relation"].update({"PRODUCT_API", "API_FRONTEND", "API_BACKEND", "DOMAIN_API"})
        if p.startswith("04_DOMAIN/"):
            mapping["area"].add("04_DOMAIN")
            mapping["relation"].update({"DOMAIN_API", "DOMAIN_BACKEND"})
        if p.startswith("05_FRONTEND/"):
            mapping["area"].add("05_FRONTEND")
            mapping["relation"].update({"DESIGN_FRONTEND", "API_FRONTEND"})
        if p.startswith("06_BACKEND/"):
            mapping["area"].add("06_BACKEND")
            mapping["relation"].update({"API_BACKEND", "DOMAIN_BACKEND"})
        if p.startswith("AGENTS/CLAUDE/AGENTS/BACKEND/") or p.startswith("AGENTS/CLAUDE/SKILLS/BACKEND/"):
            mapping["agent_spec"].add("BACKEND_AGENT_SKILL")
        if p.startswith("AGENTS/CLAUDE/AGENTS/FRONTEND/") or p.startswith("AGENTS/CLAUDE/SKILLS/FRONTEND/"):
            mapping["agent_spec"].add("FRONTEND_AGENT_SKILL")

    return mapping


def select_tasks(mode: str, changed_files: Sequence[str]) -> List[TaskSpec]:
    all_tasks = build_full_task_catalog()
    if mode == "full":
        return all_tasks

    relevant = infer_partial_relevant_targets(changed_files)
    selected: List[TaskSpec] = []
    for task in all_tasks:
        if task.kind in {"duplication", "traceability"}:
            selected.append(task)
            continue

        selected_ids = relevant.get(task.kind, set())
        if task.target_id in selected_ids:
            selected.append(task)

    if not selected:
        selected = [task for task in all_tasks if task.kind in {"traceability", "duplication"}]

    return selected


def timestamp_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def parse_json_text(raw: str) -> Any:
    text = raw.strip()
    if not text:
        raise ValueError("empty JSON text")

    if text.startswith("```"):
        lines = text.splitlines()
        lines = [line for line in lines if not line.startswith("```")]
        text = "\n".join(lines).strip()

    return json.loads(text)


def max_severity(findings: Sequence[Dict[str, Any]]) -> str:
    if not findings:
        return "low"
    return max((finding.get("severity", "low") for finding in findings), key=lambda s: SEVERITY_ORDER.get(s, 0))


def compute_status_from_findings(findings: Sequence[Dict[str, Any]]) -> str:
    if not findings:
        return "pass"

    sev = max_severity(findings)
    if sev in {"critical", "high"}:
        return "fail"
    return "warn"


def normalize_worker_result(result: Dict[str, Any], request_payload: Dict[str, Any]) -> Dict[str, Any]:
    payload = dict(result)

    payload.setdefault("run_id", request_payload["run_id"])
    payload.setdefault("agent_id", request_payload["agent_id"])
    payload.setdefault("task_id", request_payload["task_id"])
    payload.setdefault("target", request_payload["target"])
    payload.setdefault("summary", "No summary provided")
    payload.setdefault("metrics", {})
    payload.setdefault("findings", [])
    payload.setdefault("started_at", timestamp_now())
    payload.setdefault("finished_at", timestamp_now())

    findings: List[Dict[str, Any]] = []
    for raw_finding in payload.get("findings", []):
        finding = dict(raw_finding)
        severity = finding.get("severity", "low")
        if severity not in VALID_SEVERITIES:
            severity = "low"
        finding["severity"] = severity

        finding.setdefault("code", "UNSPECIFIED")
        finding.setdefault("message", "No message provided")
        evidence = finding.get("evidence", [])
        if not isinstance(evidence, list):
            evidence = []
        cleaned_evidence = []
        for item in evidence:
            if not isinstance(item, dict):
                continue
            if not item.get("path"):
                continue
            cleaned_item = {"path": str(item["path"])}
            if isinstance(item.get("line"), int) and item["line"] > 0:
                cleaned_item["line"] = item["line"]
            if isinstance(item.get("snippet"), str) and item["snippet"].strip():
                cleaned_item["snippet"] = item["snippet"]
            cleaned_evidence.append(cleaned_item)
        finding["evidence"] = cleaned_evidence
        findings.append(finding)

    payload["findings"] = findings

    status = payload.get("status", "")
    if status not in VALID_STATUSES:
        status = compute_status_from_findings(findings)
    payload["status"] = status

    return payload


def build_worker_prompt(request_payload: Dict[str, Any]) -> str:
    target = request_payload["target"]
    pretty_request = json.dumps(request_payload, indent=2, ensure_ascii=False)

    lines = [
        "You are a specialized SSOT audit worker.",
        "",
        "Mission:",
        f"- Agent ID: {request_payload['agent_id']}",
        f"- Task ID: {request_payload['task_id']}",
        f"- Target Kind: {target['kind']}",
        f"- Target ID: {target['id']}",
        f"- Objective: {target.get('objective', '')}",
        "",
        "Execution Rules:",
        "- Audit only the provided scope paths.",
        "- Do not modify or create repository files.",
        "- Use shell read commands as needed to inspect markdown and agent files.",
        "- When evidence exists, provide precise file paths and optional line numbers.",
        "- If no issue is found, return an empty findings array and status pass.",
        "",
        "Severity Policy:",
        "- critical: missing mandatory references or hard SSOT violations",
        "- high: mapping/wiring mismatch causing incorrect orchestration",
        "- medium: relationship drift, weak traceability, or ambiguous ownership",
        "- low: minor documentation quality concerns",
        "",
        "Output Contract:",
        "- Return ONLY a JSON object matching the provided output schema.",
        "- No markdown fences, no commentary, no prose outside JSON.",
        "",
        "Worker Request JSON:",
        pretty_request,
    ]

    return "\n".join(lines)


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_single_worker(
    request_payload: Dict[str, Any],
    prompt_text: str,
    response_schema_path: Path,
    stdout_path: Path,
    stderr_path: Path,
    timeout_seconds: int,
    model: str,
    dry_run: bool,
    search: bool,
) -> Dict[str, Any]:
    started_at = timestamp_now()

    if dry_run:
        result = {
            "run_id": request_payload["run_id"],
            "agent_id": request_payload["agent_id"],
            "task_id": request_payload["task_id"],
            "target": {
                "kind": request_payload["target"]["kind"],
                "id": request_payload["target"]["id"],
            },
            "status": "pass",
            "summary": "Dry-run mode: no Codex worker executed.",
            "findings": [],
            "metrics": {
                "files_scanned": 0,
                "links_checked": 0,
                "relations_checked": 0,
            },
            "started_at": started_at,
            "finished_at": timestamp_now(),
        }
        stdout_path.write_text("[DRY-RUN] Skipped codex exec\n", encoding="utf-8")
        stderr_path.write_text("", encoding="utf-8")
        return result

    response_path = Path(request_payload["output_path"]).resolve()

    command = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "-C",
        request_payload["repo_root"],
        "--full-auto",
        "-s",
        "workspace-write",
        "--output-schema",
        str(response_schema_path),
        "-o",
        str(response_path),
    ]

    if model:
        command.extend(["-m", model])
    if search:
        command.append("--search")

    command.append("-")

    proc = subprocess.run(
        command,
        input=prompt_text,
        text=True,
        capture_output=True,
        timeout=timeout_seconds,
    )

    stdout_path.write_text(proc.stdout or "", encoding="utf-8")
    stderr_path.write_text(proc.stderr or "", encoding="utf-8")

    if proc.returncode != 0:
        return {
            "run_id": request_payload["run_id"],
            "agent_id": request_payload["agent_id"],
            "task_id": request_payload["task_id"],
            "target": {
                "kind": request_payload["target"]["kind"],
                "id": request_payload["target"]["id"],
            },
            "status": "error",
            "summary": f"Worker execution failed with code {proc.returncode}",
            "findings": [
                {
                    "severity": "high",
                    "code": "WORKER_EXECUTION_FAILED",
                    "message": "codex exec returned non-zero exit code",
                    "evidence": [
                        {
                            "path": stderr_path.as_posix(),
                        }
                    ],
                }
            ],
            "metrics": {},
            "started_at": started_at,
            "finished_at": timestamp_now(),
        }

    if not response_path.exists():
        return {
            "run_id": request_payload["run_id"],
            "agent_id": request_payload["agent_id"],
            "task_id": request_payload["task_id"],
            "target": {
                "kind": request_payload["target"]["kind"],
                "id": request_payload["target"]["id"],
            },
            "status": "error",
            "summary": "Worker did not produce output JSON",
            "findings": [
                {
                    "severity": "high",
                    "code": "WORKER_OUTPUT_MISSING",
                    "message": "Expected output file was not created",
                    "evidence": [
                        {
                            "path": response_path.as_posix(),
                        }
                    ],
                }
            ],
            "metrics": {},
            "started_at": started_at,
            "finished_at": timestamp_now(),
        }

    try:
        raw_result = parse_json_text(response_path.read_text(encoding="utf-8", errors="replace"))
    except Exception as exc:  # noqa: BLE001
        return {
            "run_id": request_payload["run_id"],
            "agent_id": request_payload["agent_id"],
            "task_id": request_payload["task_id"],
            "target": {
                "kind": request_payload["target"]["kind"],
                "id": request_payload["target"]["id"],
            },
            "status": "error",
            "summary": "Worker output was not valid JSON",
            "findings": [
                {
                    "severity": "high",
                    "code": "WORKER_OUTPUT_INVALID_JSON",
                    "message": str(exc),
                    "evidence": [
                        {
                            "path": response_path.as_posix(),
                        }
                    ],
                }
            ],
            "metrics": {},
            "started_at": started_at,
            "finished_at": timestamp_now(),
        }

    if not isinstance(raw_result, dict):
        raw_result = {
            "status": "error",
            "summary": "Worker output root must be JSON object",
            "findings": [
                {
                    "severity": "high",
                    "code": "WORKER_OUTPUT_ROOT_NOT_OBJECT",
                    "message": "JSON output root was not an object",
                    "evidence": [
                        {
                            "path": response_path.as_posix(),
                        }
                    ],
                }
            ],
            "metrics": {},
            "started_at": started_at,
            "finished_at": timestamp_now(),
        }

    return normalize_worker_result(raw_result, request_payload)


def severity_totals(results: Sequence[Dict[str, Any]]) -> Dict[str, int]:
    totals = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for result in results:
        for finding in result.get("findings", []):
            severity = finding.get("severity")
            if severity in totals:
                totals[severity] += 1
    return totals


def threshold_exceeded(totals: Dict[str, int], fail_on: str) -> bool:
    threshold = SEVERITY_ORDER[fail_on]
    for severity, count in totals.items():
        if count > 0 and SEVERITY_ORDER[severity] >= threshold:
            return True
    return False


def report_status(totals: Dict[str, int], fail_on: str) -> str:
    if threshold_exceeded(totals, fail_on):
        return "fail"
    if sum(totals.values()) > 0:
        return "warn"
    return "pass"


def finding_rows(results: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for result in results:
        for finding in result.get("findings", []):
            rows.append(
                {
                    "task_id": result["task_id"],
                    "agent_id": result["agent_id"],
                    "target_kind": result["target"]["kind"],
                    "target_id": result["target"]["id"],
                    "severity": finding.get("severity", "low"),
                    "code": finding.get("code", "UNSPECIFIED"),
                    "message": finding.get("message", ""),
                    "evidence": finding.get("evidence", []),
                    "proposed_fix": finding.get("proposed_fix", ""),
                }
            )

    rows.sort(key=lambda row: -SEVERITY_ORDER.get(row["severity"], 0))
    return rows


def matrix_rows(results: Sequence[Dict[str, Any]], kind: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for result in results:
        if result["target"]["kind"] != kind:
            continue
        findings = result.get("findings", [])
        rows.append(
            {
                "task_id": result["task_id"],
                "target_id": result["target"]["id"],
                "agent_id": result["agent_id"],
                "status": result.get("status", "error"),
                "max_severity": max_severity(findings) if findings else "low",
                "finding_count": len(findings),
                "summary": result.get("summary", ""),
            }
        )

    rows.sort(key=lambda row: (row["target_id"], row["task_id"]))
    return rows


def write_matrix_markdown(path: Path, title: str, rows: Sequence[Dict[str, Any]]) -> None:
    lines = [f"# {title}", ""]
    lines.append("| Task | Target | Agent | Status | Max Severity | Findings | Summary |")
    lines.append("|---|---|---|---|---|---:|---|")

    if not rows:
        lines.append("| - | - | - | PASS | - | 0 | No tasks |")
    else:
        for row in rows:
            lines.append(
                "| {task} | {target} | {agent} | {status} | {max_severity} | {count} | {summary} |".format(
                    task=row["task_id"],
                    target=row["target_id"],
                    agent=row["agent_id"],
                    status=row["status"].upper(),
                    max_severity=row["max_severity"],
                    count=row["finding_count"],
                    summary=row["summary"].replace("|", "/"),
                )
            )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_findings_markdown(path: Path, rows: Sequence[Dict[str, Any]]) -> None:
    lines = ["# Top Findings", ""]
    if not rows:
        lines.append("- None")
    else:
        for idx, row in enumerate(rows[:100], start=1):
            lines.append(
                f"{idx}. [{row['severity'].upper()}] `{row['task_id']}` `{row['target_kind']}/{row['target_id']}` {row['code']} - {row['message']}"
            )
            for evidence in row.get("evidence", [])[:3]:
                ev = evidence.get("path", "")
                line = evidence.get("line")
                if line:
                    lines.append(f"- evidence: `{ev}:{line}`")
                else:
                    lines.append(f"- evidence: `{ev}`")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary_markdown(
    path: Path,
    run_id: str,
    mode: str,
    fail_on: str,
    status: str,
    totals: Dict[str, int],
    results: Sequence[Dict[str, Any]],
) -> None:
    by_kind = {
        "area": matrix_rows(results, "area"),
        "relation": matrix_rows(results, "relation"),
        "duplication": matrix_rows(results, "duplication"),
        "agent_spec": matrix_rows(results, "agent_spec"),
        "traceability": matrix_rows(results, "traceability"),
    }

    lines: List[str] = [
        "# SSOT Multi-Agent Audit Summary",
        "",
        f"- Run ID: `{run_id}`",
        f"- Mode: `{mode}`",
        f"- Gate threshold: `{fail_on}`",
        f"- Final status: **{status.upper()}**",
        f"- Generated at: `{timestamp_now()}`",
        "",
        "## Severity Totals",
        "",
        f"- critical: {totals['critical']}",
        f"- high: {totals['high']}",
        f"- medium: {totals['medium']}",
        f"- low: {totals['low']}",
        "",
        "## Task Coverage",
        "",
        f"- area tasks: {len(by_kind['area'])}",
        f"- relation tasks: {len(by_kind['relation'])}",
        f"- duplication tasks: {len(by_kind['duplication'])}",
        f"- agent_spec tasks: {len(by_kind['agent_spec'])}",
        f"- traceability tasks: {len(by_kind['traceability'])}",
        "",
        "## Output Files",
        "",
        "- `AREA_MATRIX.md`",
        "- `RELATION_MATRIX.md`",
        "- `DUPLICATION_MATRIX.md`",
        "- `AGENT_SPEC_MATRIX.md`",
        "- `TRACEABILITY_MATRIX.md`",
        "- `TOP_FINDINGS.md`",
        "- `final_report.json`",
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")


def write_matrix_csv(path: Path, rows: Sequence[Dict[str, Any]]) -> None:
    headers = [
        "task_id",
        "target_id",
        "agent_id",
        "status",
        "max_severity",
        "finding_count",
        "summary",
    ]

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def parse_changed_files(args_changed: str, changed_file_list_path: str) -> List[str]:
    changed: List[str] = []

    if args_changed.strip():
        changed.extend([item.strip() for item in args_changed.split(",") if item.strip()])

    if changed_file_list_path.strip():
        file_path = Path(changed_file_list_path).resolve()
        if file_path.exists():
            for line in file_path.read_text(encoding="utf-8", errors="replace").splitlines():
                line = line.strip()
                if line:
                    changed.append(line)

    deduped = []
    seen = set()
    for item in changed:
        if item not in seen:
            deduped.append(item)
            seen.add(item)

    return deduped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run SSOT audit via parallel Codex worker agents.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root path",
    )
    parser.add_argument(
        "--output-dir",
        default="",
        help="Output directory. Default: AGENTS/CODEX/reports/ssot-spec-audit/<run_id>",
    )
    parser.add_argument(
        "--mode",
        choices=["full", "partial"],
        default="full",
        help="Execution mode",
    )
    parser.add_argument(
        "--changed-files",
        default="",
        help="Comma-separated changed file paths (used for partial mode)",
    )
    parser.add_argument(
        "--changed-files-list",
        default="",
        help="Path to newline-delimited changed files list",
    )
    parser.add_argument(
        "--fail-on",
        choices=["critical", "high", "medium", "low"],
        default=DEFAULT_FAIL_ON,
        help="Fail gate threshold",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=6,
        help="Maximum concurrent codex workers",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=900,
        help="Per worker timeout",
    )
    parser.add_argument(
        "--model",
        default="",
        help="Optional model override for codex exec",
    )
    parser.add_argument(
        "--search",
        action="store_true",
        help="Enable web search tool for workers",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip codex execution and emit synthetic worker outputs",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists():
        raise SystemExit(f"[ERROR] repo root does not exist: {repo_root}")

    run_id = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = (
        Path(args.output_dir).resolve()
        if args.output_dir
        else repo_root / "AGENTS" / "CODEX" / "reports" / "ssot-spec-audit" / run_id
    )

    requests_dir = output_dir / "requests"
    prompts_dir = output_dir / "prompts"
    worker_results_dir = output_dir / "worker_results"
    logs_dir = output_dir / "logs"

    for directory in (output_dir, requests_dir, prompts_dir, worker_results_dir, logs_dir):
        ensure_dir(directory)

    changed_files = parse_changed_files(args.changed_files, args.changed_files_list)
    tasks = select_tasks(args.mode, changed_files)

    request_schema_path = (
        repo_root
        / "AGENTS"
        / "CODEX"
        / "SKILLS"
        / "ssot-spec-audit"
        / "schemas"
        / "worker_request.schema.json"
    )
    response_schema_path = (
        repo_root
        / "AGENTS"
        / "CODEX"
        / "SKILLS"
        / "ssot-spec-audit"
        / "schemas"
        / "worker_result.schema.json"
    )

    if not request_schema_path.exists() or not response_schema_path.exists():
        raise SystemExit("[ERROR] required schema files are missing")

    run_context = {
        "run_id": run_id,
        "repo_root": str(repo_root),
        "mode": args.mode,
        "changed_files": changed_files,
        "fail_on": args.fail_on,
        "max_workers": args.max_workers,
        "dry_run": args.dry_run,
        "task_count": len(tasks),
        "generated_at": timestamp_now(),
    }
    write_json(output_dir / "RUN_CONTEXT.json", run_context)

    work_items: List[Dict[str, Any]] = []
    for task in tasks:
        request_payload = {
            "run_id": run_id,
            "agent_id": task.agent_id,
            "task_id": task.task_id,
            "repo_root": str(repo_root),
            "mode": args.mode,
            "changed_files": changed_files,
            "target": {
                "kind": task.kind,
                "id": task.target_id,
                "scope_paths": list(task.scope_paths),
                "checks": list(task.checks),
                "objective": task.objective,
            },
            "severity_policy": {
                "fail_on": args.fail_on,
            },
            "output_path": str((worker_results_dir / f"{task.task_id}.worker.json").resolve()),
        }

        request_path = requests_dir / f"{task.task_id}.request.json"
        prompt_path = prompts_dir / f"{task.task_id}.prompt.md"

        write_json(request_path, request_payload)
        prompt_text = build_worker_prompt(request_payload)
        prompt_path.write_text(prompt_text + "\n", encoding="utf-8")

        work_items.append(
            {
                "task": task,
                "request": request_payload,
                "prompt": prompt_text,
                "stdout_path": logs_dir / f"{task.task_id}.stdout.log",
                "stderr_path": logs_dir / f"{task.task_id}.stderr.log",
            }
        )

    results: List[Dict[str, Any]] = []

    max_workers = max(1, args.max_workers)
    with ThreadPoolExecutor(max_workers=min(max_workers, len(work_items) or 1)) as pool:
        future_map = {}
        for item in work_items:
            future = pool.submit(
                run_single_worker,
                item["request"],
                item["prompt"],
                response_schema_path,
                item["stdout_path"],
                item["stderr_path"],
                args.timeout_seconds,
                args.model,
                args.dry_run,
                args.search,
            )
            future_map[future] = item

        for future in as_completed(future_map):
            item = future_map[future]
            task_id = item["task"].task_id
            result_path = worker_results_dir / f"{task_id}.json"
            try:
                worker_result = future.result()
            except Exception as exc:  # noqa: BLE001
                worker_result = {
                    "run_id": run_id,
                    "agent_id": item["task"].agent_id,
                    "task_id": task_id,
                    "target": {
                        "kind": item["task"].kind,
                        "id": item["task"].target_id,
                    },
                    "status": "error",
                    "summary": f"Unhandled exception: {exc}",
                    "findings": [
                        {
                            "severity": "high",
                            "code": "WORKER_UNHANDLED_EXCEPTION",
                            "message": str(exc),
                            "evidence": [
                                {
                                    "path": item["stderr_path"].as_posix(),
                                }
                            ],
                        }
                    ],
                    "metrics": {},
                    "started_at": timestamp_now(),
                    "finished_at": timestamp_now(),
                }

            normalized = normalize_worker_result(worker_result, item["request"])
            write_json(result_path, normalized)
            results.append(normalized)

    results.sort(
        key=lambda result: (
            TARGET_KIND_ORDER.get(result["target"]["kind"], 99),
            result["target"]["id"],
            result["task_id"],
        )
    )

    totals = severity_totals(results)
    status = report_status(totals, args.fail_on)

    area_matrix = matrix_rows(results, "area")
    relation_matrix = matrix_rows(results, "relation")
    duplication_matrix = matrix_rows(results, "duplication")
    agent_spec_matrix = matrix_rows(results, "agent_spec")
    traceability_matrix = matrix_rows(results, "traceability")

    all_findings = finding_rows(results)

    open_actions: List[Dict[str, Any]] = []
    for row in all_findings:
        if row["severity"] not in {"critical", "high"}:
            continue
        open_actions.append(
            {
                "task_id": row["task_id"],
                "target": f"{row['target_kind']}/{row['target_id']}",
                "severity": row["severity"],
                "code": row["code"],
                "action": row.get("proposed_fix") or row["message"],
            }
        )

    final_report = {
        "run_id": run_id,
        "status": status,
        "fail_on": args.fail_on,
        "generated_at": timestamp_now(),
        "mode": args.mode,
        "dry_run": args.dry_run,
        "task_count": len(tasks),
        "severity_totals": totals,
        "area_matrix": area_matrix,
        "relation_matrix": relation_matrix,
        "duplication_matrix": duplication_matrix,
        "agent_spec_matrix": agent_spec_matrix,
        "traceability_matrix": traceability_matrix,
        "top_findings": all_findings[:50],
        "open_actions": open_actions,
    }

    write_json(output_dir / "final_report.json", final_report)
    write_summary_markdown(output_dir / "SUMMARY.md", run_id, args.mode, args.fail_on, status, totals, results)
    write_matrix_markdown(output_dir / "AREA_MATRIX.md", "Area Matrix", area_matrix)
    write_matrix_markdown(output_dir / "RELATION_MATRIX.md", "Relation Matrix", relation_matrix)
    write_matrix_markdown(output_dir / "DUPLICATION_MATRIX.md", "Duplication Matrix", duplication_matrix)
    write_matrix_markdown(output_dir / "AGENT_SPEC_MATRIX.md", "Agent Spec Matrix", agent_spec_matrix)
    write_matrix_markdown(output_dir / "TRACEABILITY_MATRIX.md", "Traceability Matrix", traceability_matrix)
    write_findings_markdown(output_dir / "TOP_FINDINGS.md", all_findings)

    write_matrix_csv(output_dir / "AREA_MATRIX.csv", area_matrix)
    write_matrix_csv(output_dir / "RELATION_MATRIX.csv", relation_matrix)
    write_matrix_csv(output_dir / "DUPLICATION_MATRIX.csv", duplication_matrix)
    write_matrix_csv(output_dir / "AGENT_SPEC_MATRIX.csv", agent_spec_matrix)
    write_matrix_csv(output_dir / "TRACEABILITY_MATRIX.csv", traceability_matrix)

    print(f"[OK] Multi-agent audit completed: {output_dir}")
    print(f"[OK] Status: {status.upper()} | totals={totals}")

    if status == "fail":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
