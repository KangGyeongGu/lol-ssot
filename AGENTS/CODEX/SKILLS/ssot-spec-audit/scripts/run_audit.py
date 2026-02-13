#!/usr/bin/env python3
"""One-shot SSOT spec audit for domain-level consistency checks."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Set, Tuple

MAJOR_AREAS = [
    "01_PRODUCT",
    "02_DESIGN",
    "03_API",
    "04_DOMAIN",
    "05_FRONTEND",
    "06_BACKEND",
]

SEVERITY_ORDER = {
    "none": 0,
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}

STATUS_ORDER = {
    "fail": 0,
    "warn": 1,
    "pass": 2,
}

MAX_PREVIEW_ITEMS = 8


@dataclass(frozen=True)
class DomainSpec:
    lane: str
    domain: str
    review_agent: str
    dev_agent: str
    review_skill: str
    dev_skill: str
    review_command: str
    dev_command: str


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str


DOMAIN_SPECS: Sequence[DomainSpec] = (
    DomainSpec(
        lane="be",
        domain="auth_user",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/AUTH_USER_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_AUTH_USER_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-auth-user/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-auth-user/SKILL.md",
        review_command="be-review-auth-user",
        dev_command="be-dev-auth-user",
    ),
    DomainSpec(
        lane="be",
        domain="room_lobby",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/ROOM_LOBBY_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_ROOM_LOBBY_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-room-lobby/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-room-lobby/SKILL.md",
        review_command="be-review-room-lobby",
        dev_command="be-dev-room-lobby",
    ),
    DomainSpec(
        lane="be",
        domain="game_lifecycle",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/GAME_LIFECYCLE_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_GAME_LIFECYCLE_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-game-lifecycle/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-game-lifecycle/SKILL.md",
        review_command="be-review-game-lifecycle",
        dev_command="be-dev-game-lifecycle",
    ),
    DomainSpec(
        lane="be",
        domain="ban_pick_shop",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/BAN_PICK_SHOP_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_BAN_PICK_SHOP_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-ban-pick-shop/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-ban-pick-shop/SKILL.md",
        review_command="be-review-ban-pick-shop",
        dev_command="be-dev-ban-pick-shop",
    ),
    DomainSpec(
        lane="be",
        domain="realtime",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/REALTIME_CHAT_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_REALTIME_CHAT_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-realtime/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-realtime/SKILL.md",
        review_command="be-review-realtime",
        dev_command="be-dev-realtime",
    ),
    DomainSpec(
        lane="be",
        domain="redis",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/REDIS_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_REDIS_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-redis/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-redis/SKILL.md",
        review_command="be-review-redis",
        dev_command="be-dev-redis",
    ),
    DomainSpec(
        lane="be",
        domain="jpa_db",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/JPA_DB_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_JPA_DB_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-jpa-db/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-jpa-db/SKILL.md",
        review_command="be-review-jpa-db",
        dev_command="be-dev-jpa-db",
    ),
    DomainSpec(
        lane="be",
        domain="core_infra",
        review_agent="AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/CORE_INFRA_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_CORE_INFRA_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review-core-infra/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/BACKEND/DEV/be-dev-core-infra/SKILL.md",
        review_command="be-review-core-infra",
        dev_command="be-dev-core-infra",
    ),
    DomainSpec(
        lane="fe",
        domain="api",
        review_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/REVIEW/API_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/DEV/FE_DEV_API_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/REVIEW/fe-review-api/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/DEV/fe-dev-api/SKILL.md",
        review_command="fe-review-api",
        dev_command="fe-dev-api",
    ),
    DomainSpec(
        lane="fe",
        domain="state",
        review_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/REVIEW/STATE_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/DEV/FE_DEV_STATE_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/REVIEW/fe-review-state/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/DEV/fe-dev-state/SKILL.md",
        review_command="fe-review-state",
        dev_command="fe-dev-state",
    ),
    DomainSpec(
        lane="fe",
        domain="routing",
        review_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/REVIEW/ROUTING_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/DEV/FE_DEV_ROUTING_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/REVIEW/fe-review-routing/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/DEV/fe-dev-routing/SKILL.md",
        review_command="fe-review-routing",
        dev_command="fe-dev-routing",
    ),
    DomainSpec(
        lane="fe",
        domain="realtime",
        review_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/REVIEW/REALTIME_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/DEV/FE_DEV_REALTIME_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/REVIEW/fe-review-realtime/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/DEV/fe-dev-realtime/SKILL.md",
        review_command="fe-review-realtime",
        dev_command="fe-dev-realtime",
    ),
    DomainSpec(
        lane="fe",
        domain="quality",
        review_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/REVIEW/QUALITY_REVIEW_AGENT.md",
        dev_agent="AGENTS/CLAUDE/AGENTS/FRONTEND/DEV/FE_DEV_QUALITY_AGENT.md",
        review_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/REVIEW/fe-review-quality/SKILL.md",
        dev_skill="AGENTS/CLAUDE/SKILLS/FRONTEND/DEV/fe-dev-quality/SKILL.md",
        review_command="fe-review-quality",
        dev_command="fe-dev-quality",
    ),
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(text: str) -> Dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n?", text, flags=re.DOTALL)
    if not match:
        return {}

    data: Dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if value.startswith(("\"", "'")) and value.endswith(("\"", "'")) and len(value) >= 2:
            value = value[1:-1]
        data[key] = value
    return data


def clean_reference(raw_ref: str) -> str:
    ref = raw_ref.strip()
    if not ref:
        return ""
    ref = ref.split("|", 1)[0].strip()
    ref = ref.split("#", 1)[0].strip()
    ref = ref.strip("<>")
    return ref


def extract_wikilinks(text: str) -> Set[str]:
    refs: Set[str] = set()
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        ref = clean_reference(raw)
        if ref:
            refs.add(ref)
    return refs


def extract_markdown_links(text: str) -> Set[str]:
    refs: Set[str] = set()
    for raw in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        ref = raw.strip()
        if not ref or ref.startswith(("http://", "https://", "mailto:", "#")):
            continue
        ref = clean_reference(ref)
        if ref:
            refs.add(ref)
    return refs


def resolve_reference(repo_root: Path, file_path: Path, reference: str) -> Path:
    normalized = reference.lstrip("./")
    if not normalized:
        return repo_root / ""

    if reference.startswith("/"):
        return repo_root / normalized

    repo_candidate = repo_root / normalized
    if repo_candidate.exists():
        return repo_candidate

    local_candidate = (file_path.parent / reference).resolve()
    if local_candidate.exists():
        return local_candidate

    return repo_candidate


def reference_exists(repo_root: Path, file_path: Path, reference: str) -> bool:
    if any(token in reference for token in ("*", "?", "[")):
        repo_pattern = reference.lstrip("/").lstrip("./")
        if repo_pattern and list(repo_root.glob(repo_pattern)):
            return True
        if list(file_path.parent.glob(reference)):
            return True
        return False

    return resolve_reference(repo_root, file_path, reference).exists()


def extract_mapping(agent_path: Path) -> Dict[str, str]:
    if not agent_path.exists():
        return {}

    text = read_text(agent_path)
    mapping: Dict[str, str] = {}
    for domain, command in re.findall(r"^\s*-\s*([a-z_]+)\s*->\s*/([a-z0-9-]+)\s*$", text, flags=re.MULTILINE):
        mapping[domain] = command
    return mapping


def extract_slash_commands(skill_path: Path) -> Set[str]:
    if not skill_path.exists():
        return set()

    text = read_text(skill_path)
    return set(re.findall(r"^\s*-\s*/([a-z0-9-]+)\s*$", text, flags=re.MULTILINE))


def list_agent_refs(path: Path) -> Set[str]:
    if not path.exists():
        return set()

    text = read_text(path)
    return extract_wikilinks(text)


def highest_severity(issues: Sequence[Issue]) -> str:
    if not issues:
        return "none"
    return max((issue.severity for issue in issues), key=lambda severity: SEVERITY_ORDER[severity])


def status_from_severity(severity: str) -> str:
    if severity in {"critical", "high"}:
        return "fail"
    if severity in {"medium", "low"}:
        return "warn"
    return "pass"


def preview(items: Sequence[str], limit: int = MAX_PREVIEW_ITEMS) -> str:
    if not items:
        return "-"
    sliced = list(items[:limit])
    suffix = "" if len(items) <= limit else f" (+{len(items) - limit} more)"
    return ", ".join(sliced) + suffix


def area_audit(repo_root: Path, area: str) -> Dict[str, object]:
    area_dir = repo_root / area
    issues: List[Issue] = []

    if not area_dir.exists():
        issues.append(Issue("critical", "AREA_MISSING", f"Area directory is missing: {area}"))
        return {
            "area": area,
            "status": status_from_severity(highest_severity(issues)),
            "max_severity": highest_severity(issues),
            "issue_count": len(issues),
            "issues": [issue.__dict__ for issue in issues],
            "markdown_files": 0,
            "broken_references": [],
            "thin_files": [],
            "readme_exists": False,
        }

    readme_path = area_dir / "README.md"
    if not readme_path.exists():
        issues.append(Issue("high", "AREA_README_MISSING", f"README.md is missing in {area}"))

    markdown_files = sorted(area_dir.rglob("*.md"))
    broken_refs: List[Tuple[str, str]] = []
    thin_files: List[str] = []

    for md_file in markdown_files:
        text = read_text(md_file)
        if len(text.strip()) < 120:
            thin_files.append(str(md_file.relative_to(repo_root)))

        references = extract_wikilinks(text) | extract_markdown_links(text)
        for ref in sorted(references):
            if not reference_exists(repo_root, md_file, ref):
                broken_refs.append((str(md_file.relative_to(repo_root)), ref))

    if broken_refs:
        issues.append(
            Issue(
                "high",
                "BROKEN_SSOT_REFERENCE",
                f"Detected {len(broken_refs)} broken markdown/wiki reference(s) in {area}",
            )
        )

    if thin_files:
        issues.append(
            Issue(
                "low",
                "THIN_DOC_FILE",
                f"Detected {len(thin_files)} short markdown file(s) (<120 chars) in {area}",
            )
        )

    max_severity = highest_severity(issues)
    return {
        "area": area,
        "status": status_from_severity(max_severity),
        "max_severity": max_severity,
        "issue_count": len(issues),
        "issues": [issue.__dict__ for issue in issues],
        "markdown_files": len(markdown_files),
        "broken_references": [
            {"file": file_path, "reference": reference}
            for file_path, reference in broken_refs
        ],
        "thin_files": thin_files,
        "readme_exists": readme_path.exists(),
    }


def build_baseline_refs(specs: Sequence[DomainSpec], lane: str, agent_kind: str, repo_root: Path) -> Set[str]:
    lane_specs = [spec for spec in specs if spec.lane == lane]
    reference_sets: List[Set[str]] = []

    for spec in lane_specs:
        agent_path = repo_root / (spec.review_agent if agent_kind == "review" else spec.dev_agent)
        refs = list_agent_refs(agent_path)
        if refs:
            reference_sets.append(refs)

    if not reference_sets:
        return set()

    baseline = set(reference_sets[0])
    for refs in reference_sets[1:]:
        baseline &= refs
    return baseline


def add_issue(issues: List[Issue], severity: str, code: str, message: str) -> None:
    issues.append(Issue(severity=severity, code=code, message=message))


def validate_frontmatter_name(path: Path, expected_name: str, issues: List[Issue], code_prefix: str) -> Dict[str, str]:
    if not path.exists():
        return {}

    frontmatter = parse_frontmatter(read_text(path))
    actual_name = frontmatter.get("name", "")
    if actual_name != expected_name:
        add_issue(
            issues,
            "high",
            f"{code_prefix}_NAME_MISMATCH",
            f"Expected frontmatter name '{expected_name}' in {path}, got '{actual_name or '<missing>'}'",
        )
    return frontmatter


def audit_domain(
    spec: DomainSpec,
    repo_root: Path,
    review_master_mapping: Dict[str, Dict[str, str]],
    partial_review_master_mapping: Dict[str, Dict[str, str]],
    dev_master_mapping: Dict[str, Dict[str, str]],
    full_review_skill_calls: Dict[str, Set[str]],
    review_baseline_refs: Dict[str, Set[str]],
    dev_baseline_refs: Dict[str, Set[str]],
) -> Dict[str, object]:
    issues: List[Issue] = []

    artifact_paths = {
        "review_agent": repo_root / spec.review_agent,
        "dev_agent": repo_root / spec.dev_agent,
        "review_skill": repo_root / spec.review_skill,
        "dev_skill": repo_root / spec.dev_skill,
    }

    for label, path in artifact_paths.items():
        if not path.exists():
            add_issue(
                issues,
                "critical",
                "DOMAIN_ARTIFACT_MISSING",
                f"Missing {label}: {path.relative_to(repo_root)}",
            )

    review_refs = list_agent_refs(artifact_paths["review_agent"])
    dev_refs = list_agent_refs(artifact_paths["dev_agent"])

    broken_review_refs = [
        ref for ref in sorted(review_refs) if not (repo_root / ref).exists()
    ]
    broken_dev_refs = [
        ref for ref in sorted(dev_refs) if not (repo_root / ref).exists()
    ]

    for ref in broken_review_refs:
        add_issue(
            issues,
            "critical",
            "BROKEN_REVIEW_REFERENCE",
            f"Review agent reference does not exist: {ref}",
        )
    for ref in broken_dev_refs:
        add_issue(
            issues,
            "critical",
            "BROKEN_DEV_REFERENCE",
            f"Dev agent reference does not exist: {ref}",
        )

    expected_review_command = spec.review_command
    expected_dev_command = spec.dev_command

    mapped_review_command = review_master_mapping.get(spec.lane, {}).get(spec.domain)
    mapped_partial_review_command = partial_review_master_mapping.get(spec.lane, {}).get(spec.domain)
    mapped_dev_command = dev_master_mapping.get(spec.lane, {}).get(spec.domain)

    if mapped_partial_review_command != expected_review_command:
        add_issue(
            issues,
            "high",
            "PARTIAL_REVIEW_MAPPING_MISMATCH",
            (
                f"Partial review master mapping mismatch for {spec.domain}: "
                f"expected /{expected_review_command}, got "
                f"/{mapped_partial_review_command if mapped_partial_review_command else '<missing>'}"
            ),
        )

    if mapped_dev_command != expected_dev_command:
        add_issue(
            issues,
            "high",
            "DEV_MAPPING_MISMATCH",
            (
                f"Dev master mapping mismatch for {spec.domain}: "
                f"expected /{expected_dev_command}, got "
                f"/{mapped_dev_command if mapped_dev_command else '<missing>'}"
            ),
        )

    if expected_review_command not in full_review_skill_calls.get(spec.lane, set()):
        add_issue(
            issues,
            "high",
            "FULL_REVIEW_SKILL_COMMAND_MISSING",
            f"/{expected_review_command} not listed in full review skill workflow",
        )

    review_agent_frontmatter = validate_frontmatter_name(
        artifact_paths["review_agent"],
        expected_review_command,
        issues,
        "REVIEW_AGENT",
    )
    dev_agent_frontmatter = validate_frontmatter_name(
        artifact_paths["dev_agent"],
        expected_dev_command,
        issues,
        "DEV_AGENT",
    )

    review_skill_frontmatter = validate_frontmatter_name(
        artifact_paths["review_skill"],
        expected_review_command,
        issues,
        "REVIEW_SKILL",
    )
    dev_skill_frontmatter = validate_frontmatter_name(
        artifact_paths["dev_skill"],
        expected_dev_command,
        issues,
        "DEV_SKILL",
    )

    expected_review_agent_name = review_agent_frontmatter.get("name")
    actual_review_skill_agent = review_skill_frontmatter.get("agent")
    if expected_review_agent_name and actual_review_skill_agent != expected_review_agent_name:
        add_issue(
            issues,
            "high",
            "REVIEW_SKILL_AGENT_MISMATCH",
            (
                f"Review skill agent mismatch for {spec.domain}: expected '{expected_review_agent_name}', "
                f"got '{actual_review_skill_agent or '<missing>'}'"
            ),
        )

    expected_dev_agent_name = dev_agent_frontmatter.get("name")
    actual_dev_skill_agent = dev_skill_frontmatter.get("agent")
    if expected_dev_agent_name and actual_dev_skill_agent != expected_dev_agent_name:
        add_issue(
            issues,
            "high",
            "DEV_SKILL_AGENT_MISMATCH",
            (
                f"Dev skill agent mismatch for {spec.domain}: expected '{expected_dev_agent_name}', "
                f"got '{actual_dev_skill_agent or '<missing>'}'"
            ),
        )

    baseline_review = review_baseline_refs.get(spec.lane, set())
    baseline_dev = dev_baseline_refs.get(spec.lane, set())

    missing_review_baseline = sorted(baseline_review - review_refs)
    missing_dev_baseline = sorted(baseline_dev - dev_refs)

    if missing_review_baseline:
        add_issue(
            issues,
            "medium",
            "MISSING_REVIEW_BASELINE_REFS",
            f"Missing review baseline refs: {preview(missing_review_baseline)}",
        )

    if missing_dev_baseline:
        add_issue(
            issues,
            "medium",
            "MISSING_DEV_BASELINE_REFS",
            f"Missing dev baseline refs: {preview(missing_dev_baseline)}",
        )

    review_only_refs = sorted(review_refs - dev_refs)
    dev_only_refs = sorted(dev_refs - review_refs)

    if review_only_refs or dev_only_refs:
        add_issue(
            issues,
            "medium",
            "CROSS_ROLE_REFERENCE_DRIFT",
            (
                f"Review-only refs: {preview(review_only_refs)} | "
                f"Dev-only refs: {preview(dev_only_refs)}"
            ),
        )

    max_severity = highest_severity(issues)
    status = status_from_severity(max_severity)

    severity_counts = {key: 0 for key in ("critical", "high", "medium", "low")}
    for issue in issues:
        if issue.severity in severity_counts:
            severity_counts[issue.severity] += 1

    return {
        "lane": spec.lane,
        "domain": spec.domain,
        "status": status,
        "max_severity": max_severity,
        "issue_count": len(issues),
        "severity_counts": severity_counts,
        "issues": [issue.__dict__ for issue in issues],
        "review_refs": sorted(review_refs),
        "dev_refs": sorted(dev_refs),
        "review_only_refs": review_only_refs,
        "dev_only_refs": dev_only_refs,
        "missing_review_baseline_refs": missing_review_baseline,
        "missing_dev_baseline_refs": missing_dev_baseline,
        "broken_review_refs": broken_review_refs,
        "broken_dev_refs": broken_dev_refs,
        "mapped_review_command": mapped_review_command,
        "mapped_partial_review_command": mapped_partial_review_command,
        "mapped_dev_command": mapped_dev_command,
        "expected_review_command": expected_review_command,
        "expected_dev_command": expected_dev_command,
        "artifacts": {k: str(v.relative_to(repo_root)) for k, v in artifact_paths.items()},
    }


def write_domain_detail(output_dir: Path, result: Dict[str, object]) -> None:
    detail_path = output_dir / f"{result['lane']}-{result['domain']}.md"
    issues = result["issues"]

    lines: List[str] = []
    lines.append(f"# Domain Audit: {result['lane']}/{result['domain']}")
    lines.append("")
    lines.append(f"- Status: **{result['status'].upper()}**")
    lines.append(f"- Max Severity: **{result['max_severity']}**")
    lines.append(f"- Issue Count: **{result['issue_count']}**")
    lines.append("")

    lines.append("## Artifact Paths")
    lines.append("")
    for label, path in result["artifacts"].items():
        lines.append(f"- {label}: `{path}`")
    lines.append("")

    lines.append("## Mapping Check")
    lines.append("")
    lines.append(
        f"- Partial review master mapping: expected `/{result['expected_review_command']}`, actual `/{result['mapped_partial_review_command'] if result['mapped_partial_review_command'] else '<missing>'}`"
    )
    lines.append(
        f"- Dev master mapping: expected `/{result['expected_dev_command']}`, actual `/{result['mapped_dev_command'] if result['mapped_dev_command'] else '<missing>'}`"
    )
    lines.append("")

    lines.append("## Reference Drift")
    lines.append("")
    lines.append(f"- Review refs: {len(result['review_refs'])}")
    lines.append(f"- Dev refs: {len(result['dev_refs'])}")
    lines.append(
        f"- Review-only refs: {len(result['review_only_refs'])} ({preview(result['review_only_refs'])})"
    )
    lines.append(
        f"- Dev-only refs: {len(result['dev_only_refs'])} ({preview(result['dev_only_refs'])})"
    )
    lines.append("")

    lines.append("## Issues")
    lines.append("")
    if not issues:
        lines.append("- None")
    else:
        for issue in issues:
            lines.append(f"- [{issue['severity'].upper()}] {issue['code']}: {issue['message']}")

    detail_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_domain_matrix_csv(output_path: Path, results: Sequence[Dict[str, object]]) -> None:
    header = [
        "lane",
        "domain",
        "status",
        "max_severity",
        "issue_count",
        "critical",
        "high",
        "medium",
        "low",
        "review_ref_count",
        "dev_ref_count",
        "review_only_count",
        "dev_only_count",
        "broken_review_refs",
        "broken_dev_refs",
        "missing_review_baseline_refs",
        "missing_dev_baseline_refs",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        for result in results:
            severity_counts = result["severity_counts"]
            writer.writerow(
                [
                    result["lane"],
                    result["domain"],
                    result["status"],
                    result["max_severity"],
                    result["issue_count"],
                    severity_counts["critical"],
                    severity_counts["high"],
                    severity_counts["medium"],
                    severity_counts["low"],
                    len(result["review_refs"]),
                    len(result["dev_refs"]),
                    len(result["review_only_refs"]),
                    len(result["dev_only_refs"]),
                    len(result["broken_review_refs"]),
                    len(result["broken_dev_refs"]),
                    len(result["missing_review_baseline_refs"]),
                    len(result["missing_dev_baseline_refs"]),
                ]
            )


def write_domain_matrix_md(output_path: Path, results: Sequence[Dict[str, object]]) -> None:
    lines: List[str] = []
    lines.append("# Domain Matrix")
    lines.append("")
    lines.append("| Lane | Domain | Status | Max | Issues | Missing Artifacts | Broken Refs | Review-only Refs | Dev-only Refs | Detail |")
    lines.append("|---|---|---|---|---:|---:|---:|---:|---:|---|")

    for result in results:
        missing_artifacts = sum(
            1 for issue in result["issues"] if issue["code"] == "DOMAIN_ARTIFACT_MISSING"
        )
        broken_refs = len(result["broken_review_refs"]) + len(result["broken_dev_refs"])
        detail_file = Path("details") / f"{result['lane']}-{result['domain']}.md"
        lines.append(
            "| {lane} | {domain} | {status} | {max_sev} | {issues} | {missing} | {broken} | {review_only} | {dev_only} | `{detail}` |".format(
                lane=result["lane"],
                domain=result["domain"],
                status=result["status"].upper(),
                max_sev=result["max_severity"],
                issues=result["issue_count"],
                missing=missing_artifacts,
                broken=broken_refs,
                review_only=len(result["review_only_refs"]),
                dev_only=len(result["dev_only_refs"]),
                detail=detail_file.as_posix(),
            )
        )

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary(
    output_path: Path,
    repo_root: Path,
    area_results: Sequence[Dict[str, object]],
    domain_results: Sequence[Dict[str, object]],
    workers: int,
    fail_on: str,
) -> None:
    lines: List[str] = []
    lines.append("# SSOT Spec Audit Summary")
    lines.append("")
    lines.append(f"- Generated at: `{dt.datetime.now().isoformat(timespec='seconds')}`")
    lines.append(f"- Repo root: `{repo_root}`")
    lines.append(f"- Workers: `{workers}`")
    lines.append(f"- Fail policy: `{fail_on}`")
    lines.append("")

    all_domain_issues = [issue for result in domain_results for issue in result["issues"]]
    all_area_issues = [issue for result in area_results for issue in result["issues"]]

    severity_totals = {key: 0 for key in ("critical", "high", "medium", "low")}
    for issue in all_domain_issues + all_area_issues:
        if issue["severity"] in severity_totals:
            severity_totals[issue["severity"]] += 1

    lines.append("## Severity Totals")
    lines.append("")
    for severity in ("critical", "high", "medium", "low"):
        lines.append(f"- {severity}: {severity_totals[severity]}")
    lines.append("")

    lines.append("## Domain Status")
    lines.append("")
    status_totals = {"fail": 0, "warn": 0, "pass": 0}
    for result in domain_results:
        status_totals[result["status"]] += 1
    lines.append(f"- fail: {status_totals['fail']}")
    lines.append(f"- warn: {status_totals['warn']}")
    lines.append(f"- pass: {status_totals['pass']}")
    lines.append("")

    lines.append("## Area Status")
    lines.append("")
    lines.append("| Area | Status | Max Severity | Markdown Files | Broken Refs | Thin Files |")
    lines.append("|---|---|---|---:|---:|---:|")
    for result in sorted(area_results, key=lambda item: item["area"]):
        lines.append(
            "| {area} | {status} | {max_sev} | {md} | {broken} | {thin} |".format(
                area=result["area"],
                status=result["status"].upper(),
                max_sev=result["max_severity"],
                md=result["markdown_files"],
                broken=len(result["broken_references"]),
                thin=len(result["thin_files"]),
            )
        )
    lines.append("")

    lines.append("## Top Findings")
    lines.append("")
    if not all_domain_issues and not all_area_issues:
        lines.append("- None")
    else:
        prioritized: List[Tuple[str, str, str]] = []

        for result in domain_results:
            for issue in result["issues"]:
                prioritized.append(
                    (
                        issue["severity"],
                        f"{result['lane']}/{result['domain']}",
                        f"{issue['code']}: {issue['message']}",
                    )
                )

        for result in area_results:
            for issue in result["issues"]:
                prioritized.append(
                    (
                        issue["severity"],
                        result["area"],
                        f"{issue['code']}: {issue['message']}",
                    )
                )

        prioritized.sort(key=lambda item: -SEVERITY_ORDER[item[0]])
        for severity, scope, message in prioritized[:40]:
            lines.append(f"- [{severity.upper()}] `{scope}` {message}")

    lines.append("")
    lines.append("## Output Files")
    lines.append("")
    lines.append("- `DOMAIN_MATRIX.md`")
    lines.append("- `DOMAIN_MATRIX.csv`")
    lines.append("- `raw.json`")
    lines.append("- `details/*.md`")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def should_fail(fail_on: str, domain_results: Sequence[Dict[str, object]], area_results: Sequence[Dict[str, object]]) -> bool:
    threshold = SEVERITY_ORDER[fail_on]

    severities: List[str] = [
        result["max_severity"]
        for result in domain_results
    ]
    severities.extend(result["max_severity"] for result in area_results)

    return any(SEVERITY_ORDER[severity] >= threshold for severity in severities)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a parallel SSOT spec audit and generate a consolidated report.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root path (default: current directory)",
    )
    parser.add_argument(
        "--output-dir",
        default="",
        help=(
            "Output directory. If omitted, write to "
            "AGENTS/CODEX/reports/ssot-spec-audit/<timestamp>/"
        ),
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Parallel workers for area/domain checks (default: 8)",
    )
    parser.add_argument(
        "--fail-on",
        choices=["none", "low", "medium", "high", "critical"],
        default="high",
        help="Exit non-zero when findings at or above this severity exist (default: high)",
    )
    parser.add_argument(
        "--lanes",
        choices=["all", "be", "fe"],
        default="all",
        help="Limit domain audits to one lane (default: all)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists():
        raise SystemExit(f"[ERROR] repo root does not exist: {repo_root}")

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = (
        Path(args.output_dir).resolve()
        if args.output_dir
        else repo_root / "AGENTS" / "CODEX" / "reports" / "ssot-spec-audit" / timestamp
    )
    details_dir = output_dir / "details"
    details_dir.mkdir(parents=True, exist_ok=True)

    workers = max(1, args.workers)

    selected_specs = [
        spec
        for spec in DOMAIN_SPECS
        if args.lanes == "all" or spec.lane == args.lanes
    ]

    review_master_mapping = {
        "be": {},
        "fe": {},
    }
    partial_review_master_mapping = {
        "be": extract_mapping(repo_root / "AGENTS/CLAUDE/AGENTS/BACKEND/REVIEW/BE_REVIEW_PARTIAL_MASTER_AGENT.md"),
        "fe": extract_mapping(repo_root / "AGENTS/CLAUDE/AGENTS/FRONTEND/REVIEW/FE_REVIEW_PARTIAL_MASTER_AGENT.md"),
    }
    dev_master_mapping = {
        "be": extract_mapping(repo_root / "AGENTS/CLAUDE/AGENTS/BACKEND/DEV/BE_DEV_MASTER_AGENT.md"),
        "fe": extract_mapping(repo_root / "AGENTS/CLAUDE/AGENTS/FRONTEND/DEV/FE_DEV_MASTER_AGENT.md"),
    }

    full_review_skill_calls = {
        "be": extract_slash_commands(repo_root / "AGENTS/CLAUDE/SKILLS/BACKEND/REVIEW/be-review/SKILL.md"),
        "fe": extract_slash_commands(repo_root / "AGENTS/CLAUDE/SKILLS/FRONTEND/REVIEW/fe-review/SKILL.md"),
    }

    review_baseline_refs = {
        "be": build_baseline_refs(selected_specs, "be", "review", repo_root),
        "fe": build_baseline_refs(selected_specs, "fe", "review", repo_root),
    }
    dev_baseline_refs = {
        "be": build_baseline_refs(selected_specs, "be", "dev", repo_root),
        "fe": build_baseline_refs(selected_specs, "fe", "dev", repo_root),
    }

    with ThreadPoolExecutor(max_workers=min(workers, len(MAJOR_AREAS))) as executor:
        area_results = list(executor.map(lambda area: area_audit(repo_root, area), MAJOR_AREAS))

    with ThreadPoolExecutor(max_workers=min(workers, len(selected_specs) or 1)) as executor:
        domain_results = list(
            executor.map(
                lambda spec: audit_domain(
                    spec,
                    repo_root,
                    review_master_mapping,
                    partial_review_master_mapping,
                    dev_master_mapping,
                    full_review_skill_calls,
                    review_baseline_refs,
                    dev_baseline_refs,
                ),
                selected_specs,
            )
        )

    area_results.sort(key=lambda item: item["area"])
    domain_results.sort(key=lambda item: (item["lane"], STATUS_ORDER[item["status"]], item["domain"]))

    for result in domain_results:
        write_domain_detail(details_dir, result)

    write_domain_matrix_csv(output_dir / "DOMAIN_MATRIX.csv", domain_results)
    write_domain_matrix_md(output_dir / "DOMAIN_MATRIX.md", domain_results)
    write_summary(output_dir / "SUMMARY.md", repo_root, area_results, domain_results, workers, args.fail_on)

    raw_payload = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "repo_root": str(repo_root),
        "workers": workers,
        "fail_on": args.fail_on,
        "areas": area_results,
        "domains": domain_results,
        "baselines": {
            "review": {lane: sorted(refs) for lane, refs in review_baseline_refs.items()},
            "dev": {lane: sorted(refs) for lane, refs in dev_baseline_refs.items()},
        },
    }
    (output_dir / "raw.json").write_text(json.dumps(raw_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"[OK] Audit completed: {output_dir}")

    if args.fail_on != "none" and should_fail(args.fail_on, domain_results, area_results):
        print(f"[FAIL] Findings meet/exceed fail threshold: {args.fail_on}")
        return 1

    print("[OK] No findings exceeded fail threshold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
