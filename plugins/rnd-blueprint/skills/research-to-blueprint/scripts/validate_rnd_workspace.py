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


def manifest_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip("\"'") if match else None


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
        for name in REQUIRED_CHANGE_FILES:
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

    if args.strict:
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
