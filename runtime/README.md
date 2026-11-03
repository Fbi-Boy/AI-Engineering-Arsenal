# AI Engineering Runtime v0.1

This is the executable foundation for the AI Engineering Arsenal. It provides
a provider-neutral Python package for discovering and validating skill
manifests, routing task drafts, and planning multi-skill workflows.

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
decompose arbitrary natural-language requests. Planning and routing are
advisory: no skill instructions are executed, no model is invoked, no browser
is accessed, and no external side effects are performed. Model-backed
decomposition, workflow execution, persistence, approval enforcement, and
observability remain future runtime layers. Loading or selecting a skill
must never grant it authority.
