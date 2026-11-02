# AI Engineering Arsenal

A curated, modular library of reusable AI agent skills for building software projects with more consistency, quality, and less repetitive work.

> **Mission:** turn repeatable engineering work into documented, testable, reusable workflows that an AI agent can discover and execute safely.

## What this repository contains

- **`skill-handbook/`** — the engineering playbook: how to design, write, validate, secure, test, review, and maintain skills.
- **`skills/`** — the actual reusable skill packages. Each skill lives in its own directory and has a `SKILL.md` manifest.
- **`catalog/`** — (planned) searchable metadata and capability maps once the skill library grows.

## Design principles

1. **Task-focused:** one skill should solve one coherent class of tasks.
2. **Progressive disclosure:** keep the main instructions concise; move detailed references, examples, and scripts into separate files.
3. **Evidence-based:** cite authoritative documentation and distinguish facts, assumptions, and recommendations.
4. **Safe by default:** never expose secrets, execute destructive actions, or make external changes without the required authorization.
5. **Verifiable:** define expected outputs and checks for every skill.
6. **Portable:** follow the open Agent Skills folder format where possible, and document host-specific behavior explicitly.
7. **Maintainable:** use small changes, clear commits, and pull requests that are easy to review.

## Start here

1. Read the [Skill Handbook](skill-handbook/README.md).
2. Use the [skill template](skill-handbook/templates/SKILL.template.md) when authoring a new skill.
3. Follow the [review checklist](skill-handbook/templates/review-checklist.md) before proposing a skill.
4. Browse the [skills directory](skills/README.md) for the library roadmap and future packages.

> The handbook and templates are being added through focused pull requests. Links will become available as those PRs are merged.

## Contribution workflow

- Create one focused branch per logical handbook section or skill.
- Keep each commit scoped to one meaningful change.
- Open a pull request against `main`, describe the problem and solution, and include validation evidence.
- Review the change before merging. Do not merge merely because a file was committed.
- Update the catalog and relevant documentation when a skill is added or changed.

Branch convention: `docs/<topic>`, `feat/skills/<skill-name>`, `fix/<topic>`, or `chore/<topic>`.

Commit convention: `docs: ...`, `feat(skill-name): ...`, `fix(skill-name): ...`, `test(skill-name): ...`, or `chore: ...`.

## Project status

This repository is in its foundation phase. The first milestone establishes authoring standards and governance before adding a large number of skills. A skill is considered ready only after its instructions, resources, safety boundaries, and evaluation checks have been reviewed.

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI API — Skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Developers — Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI Developers — Skills in plugins](https://developers.openai.com/plugins/concepts/skills)
