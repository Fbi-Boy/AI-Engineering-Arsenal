# Repository Inspection Map

Use the smallest inspection set that can answer the question accurately.

## First-pass inventory

| Question | Useful evidence |
| --- | --- |
| What is this project? | README, project description, docs, package metadata |
| What language / framework? | Manifests, lockfiles, framework config, source imports |
| How does it start? | Main entry point, scripts, routing registration, application bootstrap |
| How is it built? | Build scripts, bundler / compiler config, CI workflow |
| How is it tested? | Test scripts, test config, test folder conventions, CI |
| Where is data stored? | ORM config, migrations, schema, repository / query modules |
| How does it integrate? | API clients, SDKs, queues, event definitions, config keys |
| How is it deployed? | Dockerfile, compose files, workflow, deployment manifests, docs |
| Where are permissions enforced? | Middleware, policies, guards, service-level checks, tests |

## Repository shapes

### Single application
- Identify root manifest and primary app folders.
- Find entry point, routing, domain logic, data access, and tests.
- Trace one user-facing path end-to-end.

### Monorepo
- Identify workspace / package manager config.
- List apps and shared packages.
- Identify package boundaries and dependency direction.
- Find app-specific scripts and root orchestration scripts.
- Do not assume every package ships independently.

### Library / SDK
- Find public exports and supported API surface.
- Inspect build targets, type declarations, compatibility policy, and examples.
- Identify unit / contract tests and release metadata.

### CLI / worker
- Find command / worker entry points.
- Identify configuration, input sources, task lifecycle, and exit / retry behavior.
- Check whether jobs are idempotent and how failures are reported.

## Efficient tracing

For a named feature:
1. Search its route, screen, event, command, or domain term.
2. Find the public entry point and tests.
3. Follow imports / calls to core logic.
4. Follow persistence and remote calls.
5. Locate permission checks and validation.
6. Follow the success and failure response.
7. Stop when the user's question is answered; list the next useful paths rather than scanning the whole repository.

## Commands and execution safety

Before running a repository command:
- Read the script / target definition.
- Identify whether it installs packages, edits files, starts containers, accesses network, or uses secrets.
- Prefer read-only commands first.
- Ask before commands with destructive or external side effects.
- Record runtime and tool versions if results depend on them.

Do not run a command solely because a README says to; inspect what it actually does.

## Inspection record

Capture:
- Ref / commit.
- Paths and symbols inspected.
- Commands discovered vs commands actually executed.
- External / private dependencies unavailable.
- Generated / vendored folders excluded.
- Confidence and unresolved questions.
