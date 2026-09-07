# Evidence policy

The goal is decision-grade evidence, not a long bibliography.

## Source hierarchy

Prefer, in order appropriate to the claim:

1. Standards, official specifications, original papers, and official project documentation.
2. Source code, release notes, issue trackers, and maintainer statements.
3. Reproducible benchmark suites and datasets with clear methodology.
4. High-quality independent replications or technical analyses.
5. Secondary summaries for discovery and context only.

For technical questions, search primary sources first. A repository README may establish an advertised capability; it does not establish performance or production fitness.

## Claim classification

- **Verified fact**: directly supported by cited evidence in the scope stated.
- **Inference**: a reasoned conclusion from multiple facts; explain the bridge.
- **Hypothesis**: plausible but unverified; attach a falsification test.
- **Decision**: a chosen path; attach criteria, alternatives, and evidence IDs.
- **Disputed**: credible sources conflict or evidence is not reproducible.

Do not let citation density hide weak support. One precise primary citation is better than several adjacent links that do not support the claim.

## Search protocol

1. Define the decision or claim the search must inform.
2. Search using canonical terminology and known synonyms.
3. Open the underlying paper, documentation, repository, or dataset; do not rely on snippets.
4. Record scope and limitations: version, workload, population, hardware, date, and whether the source reports measured or advertised results.
5. Search explicitly for contrary evidence, failed replications, open issues, and abandoned implementations.
6. Stop when new sources no longer change the decision or materially reduce uncertainty. Record remaining uncertainty instead of padding the bibliography.

Use current web research for ecosystem state, versions, APIs, benchmarks, and recommendations. If the user explicitly requests Deep Research, use that workflow and integrate its findings into the same evidence matrix.

## Traceability

Assign stable evidence IDs (`E001`, `E002`, ...). Cite them in design claims, ADRs, requirements where provenance matters, and benchmark rationale. Keep clickable URLs near claims in the final blueprint as well; the matrix is not a substitute for readable citations.

For each central claim ask:

- Does the source support this exact claim?
- Is the source primary and current enough?
- Does the source's scope match our intended workload?
- Is this measured evidence, author opinion, or marketing?
- What observation would make us change the conclusion?

## Comparisons and benchmarks

Never compare only against weak or obsolete baselines. Include:

- the dominant production alternative;
- the simplest credible baseline;
- the strongest relevant research baseline that can be reproduced;
- an ablation that removes the proposed innovation;
- a cost or complexity baseline when performance is not the only objective.

Report uncertainty and practical significance, not just point estimates. Preserve raw results and environment metadata when experiments are actually run.

## Copyright and quotations

Paraphrase by default. Use only short quotations when exact wording is necessary and keep citations adjacent. Do not reproduce substantial portions of articles, papers, or documentation.
