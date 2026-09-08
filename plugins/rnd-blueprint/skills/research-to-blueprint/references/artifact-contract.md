# Artifact contract

Use this logical structure for repository-backed and durable chat-first projects.

```text
rnd/
├── project.yaml
├── specs/
│   └── <domain>/spec.md
├── changes/
│   └── <change-id>/
│       ├── proposal.md
│       ├── evidence.csv
│       ├── design.md
│       ├── agent-contract.md
│       ├── decisions.md
│       ├── benchmarks.md
│       ├── tasks.md
│       └── specs/<domain>/spec.md
├── archive/
├── blueprint.md
└── verification.md
```

## `project.yaml`

Required fields:

```yaml
schema_version: 2
project: Example project
slug: example-project
status: exploring
language: en
source_of_truth: rnd/specs
active_change: initial-blueprint
primary_consumer: both
delivery_mode: undecided
```

Allowed status values: `exploring`, `proposed`, `researching`, `verified`, `archived`, `paused`.

Allowed `primary_consumer` values: `human`, `agent`, `both`. Allowed `delivery_mode` values: `undecided`, `library`, `skill`, `tool`, `service`, `dsl`, `generated`, `hybrid`. Version 1 workspaces remain readable; upgrade them when the active change makes an implementation-facing decision.

## `proposal.md`

Required sections:

- Intent
- Problem
- Users and use cases
- Scope
- Non-goals
- Constraints
- Success criteria
- High-impact unknowns

Scope should be testable. Non-goals prevent a research project from expanding every time a related idea appears.

## Specs

Organize current specs by domain or bounded context. A delta spec uses any of:

- `## ADDED Requirements`
- `## MODIFIED Requirements`
- `## REMOVED Requirements`

Each active requirement must include:

```markdown
### Requirement: Stable backend protocol
The library SHALL expose one backend-neutral query contract.

#### Scenario: Backend substitution
- **GIVEN** two compatible ANN backends
- **WHEN** a caller switches the configured backend
- **THEN** the public result schema remains unchanged
```

Use `MUST` for genuine invariants and `SHALL` for contractual behavior. Avoid `should`, `fast`, `easy`, or `scalable` unless a measurable threshold follows.

## `evidence.csv`

Required columns:

```text
id,claim,status,source_type,title,url,published_at,accessed_at,scope,notes
```

`status` is one of `verified`, `inference`, `hypothesis`, `decision`, `disputed`. A decision should link to its supporting evidence IDs in `notes`.

## `design.md`

Include only relevant sections, but cover:

- context and design drivers;
- domain model and vocabulary;
- architecture and component responsibilities;
- public API and data contracts;
- extension and backend protocols;
- state, concurrency, reproducibility, and caching;
- failure model and observability;
- compatibility, migration, packaging, and security where applicable;
- rejected shortcuts and known limits.

## `agent-contract.md`

Required for schema version 2. For a non-executable research result, state why no agent execution surface is warranted instead of inventing one.

Required sections:

- Primary consumer and jobs;
- Expensive-to-rediscover knowledge;
- Reuse-versus-generation boundary;
- Delivery mode decision;
- Capability contracts;
- Discovery and progressive disclosure;
- Composition and state;
- Verification and comparison.

For each public agent capability, record its intent, activation conditions, typed inputs and outputs, preconditions, invariants, side effects, cost, failure modes, oracle, and composition links where relevant. Omit fields that do not affect selection or safe use.

The reuse-versus-generation boundary must classify stable kernels, operational knowledge, generated task-specific glue, and external execution. A component belongs in the stable kernel only when reuse or expensive verification justifies it.

## `decisions.md`

Each decision has:

```markdown
## ADR-001: Decision title
Status: proposed | accepted | superseded
Evidence: E001, E004

### Context
### Decision criteria
### Options considered
### Decision
### Consequences
### Reopen when
```

“Reopen when” is mandatory for assumptions likely to change with scale, benchmark results, ecosystem maturity, or user feedback.

## `benchmarks.md`

Every benchmark case records:

- claim or hypothesis under test;
- representative and adversarial workloads;
- datasets and licensing/provenance;
- exact baselines and versions;
- metrics, confidence/uncertainty treatment, and acceptance thresholds;
- warm-up, repetitions, seeds, hardware/runtime, and resource limits;
- correctness oracle;
- ablations and sensitivity checks;
- failure interpretation and the decision it would reopen;
- reproducible command or notebook target.

When reuse versus generation is a central decision, include matched regimes for requirements-only generation, conventional library use, skill-assisted reuse, and the proposed hybrid. Measure correctness and intervention as well as tokens and runtime.

## `tasks.md`

Tasks use checkboxes and stable IDs. Each task includes its output or acceptance check.

```markdown
- [ ] R1 Reproduce baseline X — output: benchmark/raw/x.json
- [ ] D2 Decide filtering contract — acceptance: ADR-004 accepted
- [ ] I3 Implement protocol — blocked by: D2
```

Use prefixes such as `R` research, `D` decision, `V` validation, `I` implementation, and `W` writing. Put research that can invalidate implementation before the dependent implementation task.

## `blueprint.md` and `verification.md`

`blueprint.md` is a readable synthesis of current specs and accepted decisions, not a dump of change artifacts. `verification.md` records the exact state checked, failures, warnings, gaps, and final verdict.
