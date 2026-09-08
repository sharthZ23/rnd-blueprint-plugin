# Agent-native design

Use this guidance for libraries, developer tools, services, workflows, and other systems that an agent may discover, compose, execute, or modify. Do not force an agent surface onto a purely explanatory research result.

## The design question

Do not begin with a class tree. Begin with two questions:

1. What knowledge or behavior is expensive to rediscover, reverify, optimize, or operate?
2. What adaptation is local, task-specific, cheap to regenerate, and easy to check?

The first category is a candidate for a stable reusable kernel. The second is a candidate for generation. Token savings are one criterion, not the objective; include correctness, runtime cost, latency, compatibility, maintenance, security, and failure recovery.

## Compare delivery modes

Record one primary mode and any supporting modes:

- `library`: stable in-process contracts and implementations;
- `skill`: usage policy, procedures, examples, and operational knowledge;
- `tool`: a structured operation executed outside the model context;
- `service`: stateful, shared, privileged, or independently scalable execution;
- `dsl`: a declarative plan or intermediate representation compiled by a runtime;
- `generated`: task-local code produced from a specification and verified by an oracle;
- `hybrid`: a stable semantic kernel plus generated adapters, plans, or orchestration.

Reject both false extremes: thousands of tiny agent tools create discovery and schema cost, while one opaque mega-tool removes useful control and diagnosability. Prefer a small capability-oriented surface with typed inputs and outputs.

Treat `semantic kernel + generative shell` as a candidate, not an automatic conclusion. Reopen the decision when model capability, generation cost, workload frequency, or verification cost materially changes.

## Partition the system

For each proposed component classify:

- **Stable kernel**: invariants, algorithms, numerical behavior, optimized implementations, security boundaries, state transitions, compatibility contracts, and correctness oracles.
- **Operational knowledge**: when to use the capability, parameter policy, pitfalls, escalation conditions, and worked examples. Package this as progressively disclosed instructions or skills.
- **Generated shell**: schema mapping, feature wiring, adapters, configuration, reports, and other local glue with cheap deterministic checks.
- **External execution**: long-running, data-heavy, privileged, shared-state, or remote work exposed through a tool or service.

Every stable abstraction needs evidence of repeated value or expensive verification. A hypothetical future consumer is not enough.

## Agent capability contract

Describe each public capability using only fields that affect selection or safe execution:

```yaml
capability: temporal_split
intent: Split interactions without using future information.
when_to_use: Time-ordered recommendation evaluation.
inputs: InteractionDataset
outputs: TrainValidationTest
preconditions:
  - timestamps are available and comparable
invariants:
  - no future interaction enters an earlier partition
side_effects: none
cost: O(n log n) time
failure_modes:
  - sparse validation users
oracle:
  - leakage_check
composes_with:
  - candidate_generation
```

Do not expose internal helpers as capabilities. Prefer intent-revealing operations, deterministic errors, inspectable plans, idempotent reads, and explicit side effects.

## Discovery, composition, and state

- Provide a compact manifest that lets an agent decide whether deeper instructions are relevant.
- Load detailed references, examples, and tool schemas only on demand.
- Define compatibility through shared artifact contracts or a minimal IR, not shared implementation classes alone.
- For long-running work, make current state explicit and structured. Do not require reconstruction from chat history or logs.
- Return compact results and durable artifact references rather than injecting large datasets or telemetry into model context.

## Verification economy

Compare at least these regimes when the delivery decision is central:

1. generation from requirements only;
2. conventional library and documentation;
3. reusable kernel plus operational skill;
4. semantic kernel plus generated shell.

Hold model, task, execution environment, and budget fixed where possible. Measure task success, correctness failures, model tokens, wall time, compute cost, runtime performance, dependency cost, recovery after a requirement change, and human intervention. Include a simple one-off task and repeated or adversarial variants.

The benchmark must state what result would favor pure generation, conventional reuse, or the hybrid. Do not declare the agent-native architecture successful merely because it consumes fewer tokens.

## Minimal instruction policy

Keep the default path short. Explain ordinary API syntax through types and examples. Add instruction text only when it carries non-obvious selection policy, unique behavior, failure recovery, or a correctness constraint that the interface cannot express.

## Evidence anchors

- [Repo-To-Skill](https://arxiv.org/abs/2609.02749): operational knowledge as verified, progressively disclosed skills under matched downstream budgets.
- [SKILL.state](https://arxiv.org/abs/2608.26263): explicit structured execution state instead of append-only conversational history.
- [CodeAct](https://arxiv.org/abs/2402.01030): executable code as a flexible composition surface for agent actions.
- [Design Docs Are All You Need](https://arxiv.org/abs/2609.05364): design-doc DAGs, regenerated code, worked examples, and reconciliation anchors.
- [OpenAI Tool Search](https://developers.openai.com/api/docs/guides/tools-tool-search): dynamic loading and namespace guidance for reducing tool-definition context.
- [MCP Tasks](https://tasks.extensions.modelcontextprotocol.io/): durable state and progress for long-running tool execution.

Treat recent preprints as provisional evidence. Record their scope, author-reported status, and missing independent replication in the evidence matrix.
