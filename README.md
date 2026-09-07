# R&D Blueprint

R&D Blueprint is a spec-driven ChatGPT/Codex plugin that turns a technical idea into an evidence-backed, implementation-ready design blueprint.

The workflow is inspired by OpenSpec: research findings are captured as explicit artifacts, decisions are traceable, and changes are expressed as deltas rather than silently rewriting the baseline.

## What it does

- frames the research question and success criteria;
- maintains an evidence ledger with source quality and confidence;
- compares alternatives and records architecture decisions;
- designs falsifiable benchmarks and red-team checks;
- compiles the result into a detailed design blueprint;
- validates that the expected artifact set is complete.

The plugin is skills-only: it does not require credentials, external services, or an MCP server.

## Install from this marketplace

On a computer with Codex CLI installed:

```bash
codex plugin marketplace add sharthZ23/rnd-blueprint-plugin
codex plugin add rnd-blueprint@rnd-blueprint
```

Start a new chat after installation so the skill is loaded. Example prompts:

- `Исследуй идею библиотеки для инкрементальных вычислений и собери design blueprint.`
- `Продолжи последнее R&D-исследование.`
- `Проведи red-team текущей архитектуры.`

## Using it on Android

The repository is a development and installation source, not an Android deep link. The public release is distributed through the universal Plugins Directory shared by ChatGPT and Codex. Until review and publication are complete, use the repository marketplace from Codex on a computer.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/rnd-blueprint/
  .codex-plugin/plugin.json
  assets/icon.svg
  skills/research-to-blueprint/
```

## Local validation

From a checkout of this repository:

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py plugins/rnd-blueprint
python3 /path/to/skill-creator/scripts/quick_validate.py plugins/rnd-blueprint/skills/research-to-blueprint
```

The included workspace validator can also check the artifacts produced by a research run:

```bash
python3 plugins/rnd-blueprint/skills/research-to-blueprint/scripts/validate_rnd_workspace.py /path/to/research-workspace --strict
```

## License

MIT

## Policies and support

- [Privacy policy](PRIVACY.md)
- [Terms of service](TERMS.md)
- [Support](SUPPORT.md)
