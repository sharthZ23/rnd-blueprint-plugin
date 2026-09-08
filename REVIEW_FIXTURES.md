# Reviewer Fixtures

These synthetic fixtures contain no private data. Create the listed files in a temporary directory when a test needs existing project state.

## Fixture A: active project for Continue mode

`rnd/project.yaml`

```yaml
schema_version: 2
project: Incremental Compute
status: researching
active_change: initial-blueprint
primary_consumer: both
delivery_mode: hybrid
```

`rnd/changes/initial-blueprint/proposal.md`

```markdown
# Proposal

Build a small library that caches pure computations and invalidates dependent results after input changes.

## Success criteria

- Correctness matches uncached execution.
- The public API supports explicit dependency keys.
```

`rnd/changes/initial-blueprint/tasks.md`

```markdown
# Tasks

- [x] Define scope
- [ ] Compare invalidation strategies
- [ ] Design benchmark matrix
- [ ] Compile blueprint
```

`rnd/changes/initial-blueprint/agent-contract.md`

```markdown
# Agent contract

## Primary consumer and jobs
Humans define cache policy; agents may generate dependency wiring.

## Expensive-to-rediscover knowledge
Invalidation semantics, concurrency guarantees, and correctness oracles.

## Reuse-versus-generation boundary
Keep cache behavior stable; generate task-local dependency declarations.

## Delivery mode decision
Hybrid library plus generated integration code.

## Capability contracts
Typed cache lookup, invalidation, and inspection operations.

## Discovery and progressive disclosure
Expose a compact capability index; load backend details on demand.

## Composition and state
Dependency keys and cache version form explicit state.

## Verification and comparison
Compare pure generation, conventional reuse, skill-assisted reuse, and the hybrid on correctness, tokens, runtime, and change recovery.
```

## Fixture B: incomplete project for Verify mode

Use Fixture A and add:

`rnd/changes/initial-blueprint/benchmarks.md`

```markdown
# Benchmarks

Compare recomputation with cached execution on small and large dependency graphs.

Acceptance thresholds: TBD.
```

`rnd/changes/initial-blueprint/evidence.csv`

```csv
id,type,claim,source,confidence,status
E-001,hypothesis,Caching will reduce median latency,,low,unverified
```

Expected strict verification outcome: fail because thresholds and supporting citations are missing.

## Fixture C: accepted change for Archive mode

Use Fixture A, set `status: accepted`, and add:

`rnd/specs/cache/spec.md`

```markdown
# Cache specification

## Requirement: deterministic lookup

The cache MUST return the stored value for an unchanged dependency key.
```

`rnd/changes/initial-blueprint/specs/cache/spec.md`

```markdown
# Delta: explicit invalidation

## ADDED Requirement: dependency invalidation

The cache MUST invalidate a value when any declared dependency changes.

### Scenario

GIVEN a cached result with dependency `source-a`
WHEN `source-a` changes
THEN the next lookup MUST recompute the result
```

Expected archive outcome: merge the added requirement into the current cache spec, preserve the accepted change history, and update project state.

## Fixture D: agent-native boundary review

Prompt: `Design a recommendation-system toolkit for agents that can build baselines across varied datasets.`

Expected behavior:

- do not assume that every reusable operation belongs in a Python package;
- identify leakage-safe splits, metric semantics, optimized retrieval, and correctness oracles as stable-kernel candidates;
- identify schema mapping, feature wiring, experiment configuration, and reports as generated-shell candidates;
- compare library, skill, tool/service, DSL/IR, pure generation, and hybrid delivery;
- choose a primary mode only after stating criteria and a falsification benchmark;
- keep default instructions minimal while documenting unique non-obvious behavior progressively.
