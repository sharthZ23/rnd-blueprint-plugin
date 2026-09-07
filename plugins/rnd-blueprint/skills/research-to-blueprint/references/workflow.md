# R&D workflow

This workflow adapts the OpenSpec model to research and library design. OpenSpec's core principles are: fluid rather than rigid, iterative rather than waterfall, lightweight, and friendly to existing systems. Its key separation is between current `specs/` and proposed `changes/`.

Primary reference: https://github.com/Fission-AI/OpenSpec

## State model

```text
Explore (optional)
   -> Propose a focused change
   -> Research and refine artifacts in any useful order
   -> Verify evidence, specs, design, benchmarks, and tasks
   -> Accept or revise
   -> Archive: merge delta specs and preserve the change package
```

The artifacts are mutually informative. New evidence may change requirements; benchmark design may expose an underspecified API; implementation constraints may reopen an ADR. Update earlier artifacts instead of forcing forward progress.

## Explore

Use Explore when the problem or solution space is uncertain.

1. Restate the problem, intended users, and why a library or research project may be warranted.
2. Identify adjacent categories, established terminology, and plausible substitutes.
3. Produce an initial map of competitors, research questions, and unknowns.
4. Identify the smallest question whose answer could invalidate the project.
5. End with a proposed change scope or a reason not to proceed.

Exploration may remain conversational. Persist it when it contains decisions, evidence, or hypotheses that would be costly to rediscover.

## Propose and research

Create one change folder for one coherent design increment. An initial blueprint is a valid change; later examples include `add-filtering-contract`, `revise-backend-protocol`, or `validate-rust-kernel`.

Recommended order when starting from a broad idea:

1. `proposal.md`: intent, problem, scope, non-goals, stakeholders, constraints, success criteria.
2. `evidence.csv`: claims and sources discovered during landscape research.
3. `specs/`: ADDED, MODIFIED, and REMOVED behavioral requirements.
4. `design.md`: domain model, architecture, API, data contracts, extension points, failure model.
5. `decisions.md`: ADR-style decisions and alternatives.
6. `benchmarks.md`: falsification and evaluation protocol.
7. `tasks.md`: ordered research and implementation work with dependencies and acceptance checks.

This order is a default, not a phase gate.

## Continue

1. Locate the current project manifest and active changes.
2. Read the latest change package and verification report.
3. Summarize in no more than five bullets: accepted decisions, active hypothesis, last completed task, current blocker, next highest-information action.
4. Continue from that action. Do not repeat completed landscape research unless freshness or a detected gap requires it.
5. Update the artifacts before ending the session.

## Challenge

Challenge is an adversarial review, not generic criticism.

- Search for a simpler substitute, contrary evidence, and production failures.
- Test whether the proposed abstraction leaks across backends or workloads.
- Look for benchmark leakage, weak baselines, unrealistic datasets, and metrics that reward the design by construction.
- Identify decisions made before evidence and requirements that merely restate implementation.
- For each serious issue, provide impact, evidence, repair, and a re-verification test.

Do not silently change accepted decisions during Challenge. Propose a new change or record the condition for reopening them.

## Verify

Verification checks four traceability chains:

1. Problem -> requirement.
2. Requirement -> design/API element.
3. Design claim -> evidence or explicit hypothesis.
4. Performance claim -> benchmark and acceptance threshold.

Also check that tasks cover every accepted requirement and that unresolved high-risk hypotheses appear before dependent implementation tasks.

The report must distinguish failures, warnings, and informational gaps. Never declare completion with unresolved failures.

## Archive

Archive only after the user accepts the change or explicitly asks to finalize it.

1. Merge ADDED requirements into current specs.
2. Replace MODIFIED requirements while preserving history in the archived change.
3. Remove REMOVED requirements from current specs.
4. Update the decision index and blueprint.
5. Move the complete change package under `archive/<date>-<change-id>/`.
6. Leave current specs describing the system as it is now intended to be, not the history of how it was designed.

## Mobile interaction

Default to a low-friction experience:

- infer a sensible mode from the user's request;
- keep questions short and grouped in one round;
- provide status as decisions and gaps, not file-operation detail;
- offer one-tap conceptual next actions: continue research, challenge design, compile blueprint, or archive;
- produce durable artifacts so the next session does not depend on scrollback.
