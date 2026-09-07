# Reviewer Fixtures

These synthetic fixtures contain no private data. Create the listed files in a temporary directory when a test needs existing project state.

## Fixture A: active project for Continue mode

`rnd/project.yaml`

```yaml
project: Incremental Compute
status: active
active_change: initial-blueprint
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
