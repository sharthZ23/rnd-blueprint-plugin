#!/usr/bin/env python3
"""Initialize a lightweight OpenSpec-inspired R&D workspace."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def valid_slug(value: str) -> str:
    if not SLUG_RE.fullmatch(value):
        raise argparse.ArgumentTypeError(
            "use lower-case letters, digits, and single hyphens"
        )
    return value


def write_new(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--project", required=True)
    parser.add_argument("--slug", type=valid_slug)
    parser.add_argument("--change", type=valid_slug, default="initial-blueprint")
    parser.add_argument("--language", default="en")
    parser.add_argument(
        "--primary-consumer",
        choices=("human", "agent", "both"),
        default="both",
    )
    parser.add_argument(
        "--delivery-mode",
        choices=("undecided", "library", "skill", "tool", "service", "dsl", "generated", "hybrid"),
        default="undecided",
    )
    args = parser.parse_args()

    root = args.project_root.expanduser().resolve()
    rnd = root / "rnd"
    if rnd.exists():
        raise FileExistsError(f"refusing to replace existing workspace {rnd}")

    slug = args.slug or re.sub(r"[^a-z0-9]+", "-", args.project.lower()).strip("-")
    if not slug or not SLUG_RE.fullmatch(slug):
        raise ValueError("could not derive a valid slug; pass --slug")

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    change = rnd / "changes" / args.change
    (rnd / "specs").mkdir(parents=True)
    (rnd / "archive").mkdir(parents=True)
    (change / "specs").mkdir(parents=True)

    write_new(
        rnd / "project.yaml",
        f"""schema_version: 2
project: {args.project}
slug: {slug}
status: proposed
language: {args.language}
source_of_truth: rnd/specs
active_change: {args.change}
primary_consumer: {args.primary_consumer}
delivery_mode: {args.delivery_mode}
created_at: {now}
updated_at: {now}
""",
    )
    write_new(
        change / "proposal.md",
        """# Proposal

## Intent

## Problem

## Users and use cases

## Scope

## Non-goals

## Constraints

## Success criteria

## High-impact unknowns
""",
    )
    write_new(
        change / "evidence.csv",
        "id,claim,status,source_type,title,url,published_at,accessed_at,scope,notes\n",
    )
    write_new(
        change / "design.md",
        """# Design

## Context and design drivers

## Domain model

## Architecture

## Public API and data contracts

## Agent-native delivery

## Reuse-versus-generation boundary

## Extension points

## Failure model and observability

## Known limits
""",
    )
    write_new(
        change / "agent-contract.md",
        """# Agent contract

## Primary consumer and jobs

## Expensive-to-rediscover knowledge

## Reuse-versus-generation boundary

### Stable kernel

### Operational knowledge

### Generated shell

### External execution

## Delivery mode decision

## Capability contracts

## Discovery and progressive disclosure

## Composition and state

## Verification and comparison
""",
    )
    write_new(
        change / "decisions.md",
        """# Decisions

## ADR-001: Initial architecture direction
Status: proposed
Evidence:

### Context

### Decision criteria

### Options considered

### Decision

### Consequences

### Reopen when
""",
    )
    write_new(
        change / "benchmarks.md",
        """# Benchmark and validation program

## Claims under test

## Workloads and datasets

## Baselines

## Metrics and acceptance thresholds

## Correctness oracle

## Reuse-versus-generation regimes

## Reproducibility protocol

## Ablations and sensitivity

## Failure interpretation
""",
    )
    write_new(
        change / "tasks.md",
        """# Tasks

- [ ] R1 Complete the evidence matrix — output: evidence.csv
- [ ] D1 Resolve the initial architecture direction — acceptance: ADR-001 accepted
- [ ] D2 Decide the delivery mode and generation boundary — acceptance: agent-contract.md complete
- [ ] V1 Run strict blueprint verification — output: rnd/verification.md
""",
    )
    print(rnd)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
