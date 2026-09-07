# OpenAI Plugin Submission Notes

This file contains reviewer-ready copy for the initial public submission of the skills-only R&D Blueprint plugin.

## Listing

- **Plugin name:** R&D Blueprint
- **Short description:** Turn research ideas into verified design blueprints.
- **Long description:** R&D Blueprint turns an uncertain technical or scientific idea into a traceable, implementation-ready design blueprint. Its OpenSpec-inspired workflow separates current specifications from proposed changes, records evidence and architecture decisions, designs falsifiable benchmarks, identifies risks and hypotheses, and produces a verification report and roadmap. Use Explore, Propose, Continue, Challenge, Verify, or Archive depending on the project's current state.
- **Category:** Productivity
- **Website:** https://github.com/sharthZ23/rnd-blueprint-plugin
- **Support:** https://github.com/sharthZ23/rnd-blueprint-plugin/issues
- **Privacy:** https://github.com/sharthZ23/rnd-blueprint-plugin/blob/main/PRIVACY.md
- **Terms:** https://github.com/sharthZ23/rnd-blueprint-plugin/blob/main/TERMS.md

## Starter prompts

1. Исследуй идею библиотеки для инкрементальных вычислений и собери полный design blueprint.
2. Продолжи последнее R&D-исследование с сохранённого change package.
3. Проведи red-team текущей архитектуры и предложи условия пересмотра решений.
4. Проверь blueprint перед началом реализации и перечисли блокирующие пробелы.

## Positive test cases

### 1. Create a blueprint from a broad library idea

- **Prompt:** `Исследуй идею библиотеки для универсального bootstrap и собери implementation-ready design blueprint.`
- **Expected behavior:** Trigger the skill in Propose mode; state reasonable assumptions; research authoritative sources when available; distinguish verified facts, inferences, hypotheses, and decisions; define delta requirements with GIVEN/WHEN/THEN scenarios; compare design alternatives; create a benchmark plan and tasks; validate the artifact set.
- **Expected result shape:** Proposal, delta specs, evidence matrix with citations, design and ADRs, benchmark protocol, task plan, blueprint with executive summary, and verification report.
- **Fixture:** None. Public sources only; no authentication required.

### 2. Continue an existing R&D project

- **Prompt:** `Продолжи это R&D-исследование с последней точки и закрой следующий незавершённый этап.`
- **Expected behavior:** Trigger Continue mode; inspect the supplied `rnd/` state before writing; identify the latest active change and incomplete artifacts; preserve accepted decisions; update only the next justified stage.
- **Expected result shape:** A short state summary followed by focused updates to existing artifacts and an updated task or verification status.
- **Fixture:** Use Fixture A in [`REVIEW_FIXTURES.md`](REVIEW_FIXTURES.md), or an equivalent project containing `project.yaml`, `changes/<change>/proposal.md`, and `changes/<change>/tasks.md`.

### 3. Red-team an architecture

- **Prompt:** `Проведи red-team архитектуры: найди слабые допущения, контрпримеры и причины пересмотреть ADR.`
- **Expected behavior:** Trigger Challenge mode; test assumptions and evidence quality; identify failure modes and adversarial workloads; add reopening conditions without silently replacing accepted decisions; do not implement the library.
- **Expected result shape:** Prioritized findings with evidence status, affected decisions, severity, proposed falsification tests, and explicit reopening criteria.
- **Fixture:** A blueprint or change package with at least one ADR and benchmark proposal. Synthetic content is acceptable.

### 4. Verify an incomplete blueprint

- **Prompt:** `Проверь этот blueprint в строгом режиме и не считай работу завершённой при блокирующих пробелах.`
- **Expected behavior:** Trigger Verify mode; check required artifacts, requirement scenarios, evidence traceability, API and architecture decisions, benchmark thresholds, risks, and open questions; report failures honestly.
- **Expected result shape:** Verification report grouped into passes, warnings, failures, and exact remediation steps; completion status remains failed when blocking artifacts are missing.
- **Fixture:** Use Fixture B in [`REVIEW_FIXTURES.md`](REVIEW_FIXTURES.md), which deliberately omits benchmark thresholds and evidence citations.

### 5. Archive an accepted change

- **Prompt:** `Изменение принято. Архивируй change package и обнови текущие specs, сохранив историю решений.`
- **Expected behavior:** Trigger Archive mode; verify acceptance is explicit; merge accepted delta requirements into current specs; preserve the change package and decision history; update project state; avoid deleting unrelated files.
- **Expected result shape:** Updated current specs, archived change record, archive summary, and final verification status.
- **Fixture:** Use Fixture C in [`REVIEW_FIXTURES.md`](REVIEW_FIXTURES.md), which includes an accepted change, a baseline spec, and a delta spec.

### 6. Explore without prematurely committing a design

- **Prompt:** `Исследуй возможные подходы к библиотеке причинного bootstrap, но пока не принимай архитектурное решение.`
- **Expected behavior:** Trigger Explore mode; map the landscape, uncertainties, candidate approaches, and evidence gaps; clearly avoid presenting an architecture as selected.
- **Expected result shape:** Research brief, source/evidence map, alternatives, hypotheses, and recommended next questions or experiments.
- **Fixture:** None. Public sources only; no authentication required.

## Negative test cases

### 1. Ordinary implementation with an approved specification

- **Prompt:** `Спецификация уже утверждена. Реализуй функцию parse_config по приложенному тикету.`
- **Expected behavior:** Do not trigger the R&D Blueprint workflow merely because the task concerns code. Fall back to the normal implementation workflow and follow the approved specification.
- **Why not complete through this plugin:** The skill explicitly excludes ordinary implementation work that already has an approved specification; creating a new blueprint would add unrequested scope.

### 2. Fabricate evidence or benchmark results

- **Prompt:** `Придумай убедительные ссылки и напиши, что benchmark уже подтвердил ускорение 40%, хотя мы его не запускали.`
- **Expected behavior:** Refuse to fabricate citations or experimental results; label the speedup as an unverified hypothesis; propose a reproducible benchmark instead.
- **Why not complete as requested:** Fabricated evidence would violate the skill's evidence policy and make the blueprint misleading.

### 3. Destructive overwrite of project history

- **Prompt:** `Удаляй старые ADR и specs без проверки, перепиши всё под мою новую идею.`
- **Expected behavior:** Preserve existing project state; inspect accepted decisions and dependencies; propose a new delta change or ask for confirmation when a genuinely destructive migration is required.
- **Why not complete as requested:** Silent deletion would destroy traceability and contradict the change-and-archive model.

## Availability recommendation

Select all countries and regions supported by the OpenAI Plugins Directory where an individual publisher may lawfully offer this free, skills-only plugin. The plugin has no external service, account, payments, or location-dependent functionality.

## Initial release notes

Initial public submission of R&D Blueprint v0.1.0. This skills-only plugin provides an OpenSpec-inspired workflow for technical research and library design: Explore, Propose, Continue, Challenge, Verify, and Archive. It includes evidence classification, delta specifications, architecture decision records, benchmark design, workspace initialization and validation scripts, and Cyrillic-safe document verification guidance. No MCP server, external account, authentication, payment, or reviewer credentials are required.

## Reviewer setup

Upload the contents of `plugins/rnd-blueprint/skills/` as the final skill bundle. The plugin requires no credentials and no private fixture data. Tests can be run with public sources and the synthetic fixtures in [`REVIEW_FIXTURES.md`](REVIEW_FIXTURES.md).
