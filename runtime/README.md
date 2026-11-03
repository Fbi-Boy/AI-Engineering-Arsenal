# AI Engineering Runtime v0.1

This is the first executable foundation for the AI Engineering Arsenal. It
provides a provider-neutral Python package that discovers and validates
SKILL.md packages on disk.

## Requirements

- Python 3.11+
- No runtime third-party dependencies

## Install locally

From the repository root:

\`\`\`bash
python -m pip install -e .
\`\`\`

## Commands

\`\`\`bash
aea-runtime list --skills-dir skills
aea-runtime validate --skills-dir skills
\`\`\`

The CLI reads package metadata only. It does not execute skill instructions,
invoke a model, access a browser, or perform filesystem writes.

## Registry contract

A package is discovered from skills/<skill-name>/SKILL.md. The frontmatter
must contain non-empty top-level name and description string fields. Names
must use lowercase kebab-case and match the package directory. Discovery is
deterministic and rejects symlinked package directories or manifest files.

The frontmatter reader deliberately supports only the scalar and block-scalar
subset needed for these two fields. It does not evaluate YAML tags, aliases,
or arbitrary objects.

## Current boundary

v0.1 is a registry foundation, not yet an AI orchestrator. Model-backed
intent routing, skill invocation, workflow execution, persistence, approval
enforcement, and observability are planned runtime layers. Those layers must
use explicit adapters and enforce permissions before side effects; merely
loading a skill must never grant it authority.
