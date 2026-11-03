# AI Engineering Runtime v0.1

This is the executable foundation for the AI Engineering Arsenal. It provides
a provider-neutral Python package for discovering and validating skill
manifests, routing task drafts, planning multi-skill workflows, and executing
ready plans through explicitly registered application handlers.

## Requirements

- Python 3.11+
- No runtime third-party dependencies

## Install locally

From the repository root:

```bash
python -m pip install -e .
```

## Commands

```bash
aea-runtime list --skills-dir skills
aea-runtime validate --skills-dir skills
aea-runtime route --request "Design a database schema" --skills-dir skills
aea-runtime plan --input runtime/examples/workflow.json --skills-dir skills
```

The `plan` command accepts an explicit JSON task list. Each task requires an
`id`, `description`, and `acceptance_criteria` array; `depends_on` is optional.
See [WORKFLOW_PLANNING.md](WORKFLOW_PLANNING.md) for the contract and
[runtime/examples/workflow.json](examples/workflow.json) for a sample.

## Workflow execution API

Execution is currently a Python API, not a CLI command. Applications register
trusted callables by skill name and call `execute_workflow` with a ready plan
and an `ExecutionApproval` attestation. The executor performs preflight checks,
runs tasks sequentially, records state transitions, blocks dependents after
failure, and continues independent tasks. See [EXECUTION.md](EXECUTION.md) and [PERSISTENCE.md](PERSISTENCE.md) for the persistence API and its recovery contract.

The approval attestation is not authentication or policy enforcement. Handlers
are trusted Python code and may perform arbitrary actions; never register
untrusted skill content as a handler. The runtime does not interpret
`SKILL.md` as code.

## Registry contract

A package is discovered from skills/<skill-name>/SKILL.md. The frontmatter
must contain non-empty top-level name and description string fields. Names
must use lowercase kebab-case and match the package directory. Discovery is
deterministic and rejects symlinked package directories or manifest files.

The frontmatter reader deliberately supports only the scalar and block-scalar
subset needed for these two fields. It does not evaluate YAML tags, aliases,
or arbitrary objects.

## Current boundary

The router uses lexical metadata matching. The workflow planner validates
explicit task drafts and dependency graphs; it does not automatically
decompose arbitrary natural-language requests. The executor invokes only
explicitly registered Python handlers and runs sequentially. Model-backed
decomposition, durable state, authentication and permission enforcement,
browser/local tool adapters, retries, cancellation, safe concurrency, and
observability remain future runtime layers. The optional SQLite persistence primitive is available through `SQLiteStateStore`, but the executor does not integrate with it automatically. Loading or selecting a skill
must never grant it authority.
