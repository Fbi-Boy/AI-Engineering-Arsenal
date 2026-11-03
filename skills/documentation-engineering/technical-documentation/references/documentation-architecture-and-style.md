# Documentation Architecture and Style

## Four reader needs
| Type | Reader need | Primary content |
| --- | --- | --- |
| Tutorial | Learn by doing | Guided path, prerequisites, expected outcome |
| How-to guide | Achieve a specific goal | Steps, options, troubleshooting |
| Reference | Look up exact facts | Parameters, fields, schemas, commands, defaults |
| Explanation | Understand why / how | Concepts, architecture, trade-offs, history |

A topic may need several forms. Keep each page focused on one reader need and link related material.

## Common repository information architecture
- **README:** project purpose, audience, quick start, status, and navigation.
- **Getting started:** prerequisites and first successful local run.
- **Tutorials:** guided learning tasks.
- **How-to guides:** common developer / operator workflows.
- **Reference:** API, CLI, configuration, schema, error codes, compatibility.
- **Architecture:** system context, components, data flow, decision records.
- **Operations:** deployment, monitoring, recovery, troubleshooting, runbooks.
- **Contributing:** local development, tests, style, PR expectations.
- **Release notes / changelog:** user-impacting changes, deprecations, and migration steps.

## Style
- Write for a named audience rather than "everyone".
- Use consistent names and terms.
- Prefer active voice and direct instructions.
- Put warnings before risky actions.
- Explain expected results and likely errors.
- Avoid unexplained acronyms and ambiguous pronouns.
- Use minimal, realistic, safe-to-copy examples.
- Keep pages scannable with descriptive headings and links.

## Diagrams
Use diagrams for component relationships, trust boundaries, sequence, state, and deployment topology. Keep diagram source under version control where possible. Add alt text or a textual equivalent and update diagrams when architecture changes.

## API reference
Treat a machine-readable contract or implementation annotations as source of truth. Explain authentication, error semantics, pagination, rate limits, examples, versioning, and deprecation behavior. Do not manually drift from the API contract.
