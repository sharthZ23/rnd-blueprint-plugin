# Blueprint contract

The blueprint is a decision document for future implementation and experimentation. It must be readable as a narrative while remaining traceable to specs, evidence, and tasks.

## Recommended structure

1. Executive summary
2. Problem, users, and why now
3. Goals, non-goals, constraints, and success criteria
4. Terminology and domain model
5. Research landscape and prior art
6. Requirements and representative scenarios
7. Architecture and component boundaries
8. Public API and data contracts
9. Agent-native delivery and reuse-versus-generation boundary
10. Alternatives, ADRs, and trade-offs
11. Performance, correctness, and benchmark program
12. Reliability, reproducibility, compatibility, and security
13. Risks, hypotheses, and open questions
14. Implementation roadmap and release slices
15. Verification report
16. References

Change the order when it improves the story, but do not omit a relevant concern silently.

## Quality gates

### Problem and scope

- The target user and painful job are explicit.
- A library is compared with simpler alternatives such as a module, notebook, service, wrapper, or contribution to an existing project.
- Goals have measurable success criteria; non-goals bound the first release.

### Architecture and API

- Domain entities and vocabulary are consistent.
- Public API examples cover normal use, composition, extension, and failure.
- Backend abstractions are tested against at least two materially different implementations.
- Data ownership, mutability, copying, streaming, concurrency, and serialization are explicit where relevant.
- Versioning and compatibility strategy match the proposed maturity level.

### Agent-native delivery

- The primary consumer is identified as a human, agent, or both.
- A library is compared with skill, tool/service, DSL/IR, generated code, and hybrid delivery where relevant.
- Expensive-to-rediscover or reverify knowledge is separated from cheap task-specific adaptation.
- Stable capabilities expose selection conditions, typed contracts, invariants, side effects, failure modes, and an oracle where these affect safe use.
- Instructions are progressively disclosed; ordinary syntax is not duplicated as prose.
- Long-running work has explicit structured state and durable artifacts rather than relying on chat history.
- Interoperability is defined through artifacts, protocols, or a minimal IR instead of an unnecessary shared framework.

### Evidence and decisions

- Central claims have primary citations or are labeled inference/hypothesis.
- Alternatives are evaluated using stated criteria.
- ADRs include consequences and reopening conditions.
- Conflicting evidence and negative findings are retained.

### Benchmarks

- Each important claim can fail.
- Workloads represent intended and adversarial use.
- Baselines are credible and versioned.
- Correctness and performance are evaluated separately.
- Metrics, thresholds, repetitions, seeds, runtime, and hardware are specified.
- The plan states which decision changes for each meaningful failure.
- Agent-facing systems compare reuse and generation under matched conditions; token cost is not used as the sole success metric.

### Roadmap

- Research spikes precede work that depends on uncertain assumptions.
- The first release proves the narrow value proposition.
- Later ambitions are hypotheses, not hidden v0.1 scope.
- Every milestone has an observable exit criterion.

## Verification verdict

Use one verdict:

- `PASS`: no failures; remaining warnings are explicitly accepted.
- `PASS WITH WARNINGS`: usable for the stated next step, with bounded gaps.
- `FAIL`: a missing or contradictory artifact makes implementation unsafe or research conclusions unsupported.

List failures first, then warnings, then strengths. A long document is not evidence of completeness.

## Deliverable formats

Maintain Markdown as the inspectable source. Produce DOCX or PDF when the user requests a reading artifact. For code-heavy projects, optionally add a notebook or repository scaffold.

Before delivering a document:

- validate links and citation placement;
- render every page and inspect layout;
- ensure tables do not overflow;
- verify code and equations are legible;
- embed or select fonts that cover every script used;
- for Russian text, inspect multiple pages for Cyrillic replacement squares;
- ensure the executive summary and final recommendations agree with the accepted decisions.
