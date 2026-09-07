---
name: research-to-blueprint
description: Turn broad technical or scientific ideas into versioned, evidence-backed, spec-driven design blueprints. Use when exploring, designing, continuing, challenging, or validating a software library, algorithm, research program, architecture, API, or benchmark plan. Skip ordinary implementation work that already has an approved specification.
---

# Research to Blueprint

Convert an uncertain idea into durable intent: current specifications, traceable evidence, explicit decisions, falsifiable benchmarks, and an implementation plan. Follow OpenSpec's fluid, iterative, delta-based model while adapting its artifacts to R&D work.

## Choose the operating mode

- **Explore**: investigate a fuzzy idea without committing a change package.
- **Propose**: create or update a change package. This is the default when the user asks for a design blueprint.
- **Continue**: resume the latest active change from its recorded state.
- **Challenge**: red-team assumptions, evidence, architecture, and benchmark design.
- **Verify**: check traceability and internal consistency without implementing.
- **Archive**: merge accepted delta specs into the current source of truth and preserve the change history.

Treat `Explore -> Propose -> Verify -> Archive` as a loop, not a waterfall. Revise earlier artifacts whenever later evidence changes the conclusion.

## Load only the guidance needed

- Read [references/workflow.md](references/workflow.md) for a full run, continuation, challenge, or archive.
- Read [references/artifact-contract.md](references/artifact-contract.md) when creating or updating project files.
- Read [references/evidence-policy.md](references/evidence-policy.md) before source-heavy research.
- Read [references/blueprint-contract.md](references/blueprint-contract.md) before compiling or verifying a final blueprint.

## Essential behavior

1. Inspect any existing project state before proposing new structure. Preserve user files and accepted decisions.
2. Ask at most three short questions only when answers would materially change scope, audience, constraints, or deliverables. Otherwise state assumptions and proceed.
3. Prefer original papers, official documentation, standards, source repositories, and reproducible benchmark results. Use ordinary web research unless the user explicitly requests Deep Research.
4. Separate every important statement as **verified fact**, **inference**, **hypothesis**, or **decision** in the evidence/decision artifacts. Do not present a hypothesis as established fact.
5. Write behavioral requirements with `SHALL` or `MUST` and concrete `GIVEN / WHEN / THEN` scenarios. Keep implementation choices in design or ADRs unless they are themselves contractual.
6. For competing designs, record the decision criteria, alternatives, selected option, consequences, and conditions that would reopen the decision.
7. Every central performance or quality claim needs a benchmark, baseline, metric, dataset/workload, acceptance threshold, and failure interpretation.
8. Save useful checkpoints during long work. A user should be able to say “continue” in a new session without reconstructing prior reasoning.
9. Do not implement the researched library unless the user asks. A blueprint request authorizes research and artifact creation, not product implementation.

## Project state

For repository-backed work, use the existing R&D directory if present; otherwise use `rnd/`. For chat-first work, save the same logical structure as durable user-facing artifacts when persistent storage is available. If neither is available, return a complete artifact bundle and clearly identify the continuity limitation.

When shell execution is available, initialize with:

```bash
python3 scripts/init_rnd_workspace.py <project-root> --project "Project name" --change initial-blueprint
```

Validate drafts with `validate_rnd_workspace.py`; use `--strict` before declaring a blueprint complete. If scripts cannot run, enforce the contracts manually.

## Completion standard

A full run is complete only when it produces:

- an explicit proposal and scope;
- current or delta requirements with scenarios;
- an evidence matrix with live citations;
- architecture and public API decisions with alternatives;
- a falsifiable benchmark and validation program;
- risks, hypotheses, unresolved questions, and implementation tasks;
- a readable design blueprint plus a concise executive summary;
- a verification report stating passes, warnings, and known gaps.

When producing DOCX or PDF, use fonts with the required language coverage and render the result for visual inspection. For Cyrillic, explicitly verify that letters render instead of replacement squares.
