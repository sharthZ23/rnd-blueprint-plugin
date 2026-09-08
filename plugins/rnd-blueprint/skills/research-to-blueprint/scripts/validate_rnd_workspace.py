#!/usr/bin/env python3
"""Validate structural and traceability invariants of an R&D workspace."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REQUIRED_CHANGE_FILES = (
    "proposal.md",
    "evidence.csv",
    "design.md",
    "decisions.md",
    "benchmarks.md",
    "tasks.md",
)
V2_CHANGE_FILES = ("agent-contract.md",)
EVIDENCE_COLUMNS = {
    "id",
    "claim",
    "status",
    "source_type",
    "title",
    "url",
    "published_at",
    "accessed_at",
    "scope",
    "notes",
}
VALID_EVIDENCE_STATUS = {
    "verified",
    "inference",
    "hypothesis",
    "decision",
    "disputed",
}
VALID_PRIMARY_CONSUMERS = {"human", "agent", "both"}
VALID_DELIVERY_MODES = {
    "undecided",
    "library",
    "skill",
    "tool",
    "service",
    "dsl",
    "generated",
    "hybrid",
}
AGENT_CONTRACT_SECTIONS = (
    "## Primary consumer and jobs",
    "## Expensive-to-rediscover knowledge",
    "## Reuse-versus-generation boundary",
    "## Delivery mode decision",
    "## Capability contracts",
    "## Discovery and progressive disclosure",
    "## Composition and state",
    "## Verification and comparison",
)


def manifest_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip("\"'") if match else None


def markdown_section_has_content(text: str, heading: str) -> bool:
    match = re.search(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return False
    tail = text[match.end() :]
    next_section = re.search(r"^##(?!#)\s+", tail, re.MULTILINE)
    body = tail[: next_section.start()] if next_section else tail
    return any(
        line.strip()
        and not line.lstrip().startswith("#")
        and line.strip() not in {"```", "```yaml", "```json"}
        for line in body.splitlines()
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    rnd = args.project_root.expanduser().resolve() / "rnd"
    failures: list[str] = []
    warnings: list[str] = []

    manifest = rnd / "project.yaml"
    if not manifest.is_file():
        failures.append("missing rnd/project.yaml")
        manifest_text = ""
    else:
        manifest_text = manifest.read_text(encoding="utf-8")

    schema_raw = manifest_value(manifest_text, "schema_version")
    try:
        schema_version = int(schema_raw) if schema_raw is not None else 1
    except ValueError:
        failures.append(f"project.yaml has invalid schema_version: {schema_raw}")
        schema_version = 1

    delivery_mode = manifest_value(manifest_text, "delivery_mode")
    if schema_version >= 2:
        primary_consumer = manifest_value(manifest_text, "primary_consumer")
        if primary_consumer not in VALID_PRIMARY_CONSUMERS:
            failures.append(
                "project.yaml primary_consumer must be one of "
                f"{sorted(VALID_PRIMARY_CONSUMERS)}"
            )
        if delivery_mode not in VALID_DELIVERY_MODES:
            failures.append(
                "project.yaml delivery_mode must be one of "
                f"{sorted(VALID_DELIVERY_MODES)}"
            )

    active_change = manifest_value(manifest_text, "active_change")
    if not active_change:
        failures.append("project.yaml has no active_change")
        change = None
    else:
        change = rnd / "changes" / active_change
        if not change.is_dir():
            failures.append(f"missing active change directory: {change}")

    for directory in (rnd / "specs", rnd / "changes", rnd / "archive"):
        if not directory.is_dir():
            failures.append(f"missing directory: {directory}")

    if change and change.is_dir():
        required_files = REQUIRED_CHANGE_FILES + (V2_CHANGE_FILES if schema_version >= 2 else ())
        for name in required_files:
            if not (change / name).is_file():
                failures.append(f"missing change artifact: {name}")
        if not (change / "specs").is_dir():
            failures.append("missing change delta specs directory")

        evidence_path = change / "evidence.csv"
        if evidence_path.is_file():
            with evidence_path.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                columns = set(reader.fieldnames or [])
                rows = list(reader)
            missing = EVIDENCE_COLUMNS - columns
            if missing:
                failures.append(f"evidence.csv missing columns: {sorted(missing)}")
            for index, row in enumerate(rows, start=2):
                status = row.get("status", "")
                if status not in VALID_EVIDENCE_STATUS:
                    failures.append(f"evidence.csv row {index} has invalid status: {status}")
                if status == "verified" and not row.get("url"):
                    failures.append(f"verified evidence row {index} has no URL")
            if not rows:
                warnings.append("evidence matrix has no claims")

        specs = list((change / "specs").rglob("*.md")) if (change / "specs").is_dir() else []
        if not specs:
            warnings.append("active change has no delta specs")
        for spec in specs:
            text = spec.read_text(encoding="utf-8")
            if "### Requirement:" not in text:
                failures.append(f"spec has no requirements: {spec}")
            if not all(token in text for token in ("GIVEN", "WHEN", "THEN")):
                failures.append(f"spec lacks GIVEN/WHEN/THEN scenario: {spec}")
            if not re.search(r"\b(?:SHALL|MUST)\b", text):
                failures.append(f"spec lacks SHALL/MUST contract language: {spec}")

        agent_contract = change / "agent-contract.md"
        if schema_version >= 2 and agent_contract.is_file():
            agent_text = agent_contract.read_text(encoding="utf-8")
            for section in AGENT_CONTRACT_SECTIONS:
                if section not in agent_text:
                    failures.append(f"agent-contract.md missing section: {section}")
                elif args.strict and not markdown_section_has_content(agent_text, section):
                    failures.append(f"strict: agent-contract.md empty section: {section}")

        benchmarks = change / "benchmarks.md"
        if schema_version >= 2 and args.strict and benchmarks.is_file():
            regime_section = "## Reuse-versus-generation regimes"
            benchmark_text = benchmarks.read_text(encoding="utf-8")
            if not markdown_section_has_content(benchmark_text, regime_section):
                failures.append(f"strict: benchmarks.md empty section: {regime_section}")

    if args.strict:
        if schema_version >= 2 and delivery_mode == "undecided":
            failures.append("strict: delivery_mode is still undecided")
        if warnings:
            failures.extend(f"strict: {warning}" for warning in warnings)
        for name in ("blueprint.md", "verification.md"):
            if not (rnd / name).is_file():
                failures.append(f"strict: missing {name}")

    for item in failures:
        print(f"FAIL: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    if not failures:
        print("PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
