# Skill Package Anatomy

This section defines the expected structure of a skill package and the responsibilities of each file.

## 1. Minimum package

A portable Agent Skill is a directory containing at least one SKILL.md file:

~~~text
skill-name/
└── SKILL.md
~~~

A practical package may add supporting resources:

~~~text
skill-name/
├── SKILL.md
├── references/
│   ├── domain-standard.md
│   └── output-schema.md
├── scripts/
│   └── validate_output.py
└── assets/
    ├── template.md
    └── example.json
~~~

Only add a directory when it provides real value. Empty folders and placeholder files make a package harder to understand.

## 2. SKILL.md metadata

The file begins with YAML frontmatter, followed by Markdown instructions.

~~~yaml
---
name: database-erd-design
description: Design and validate entity-relationship diagrams from software requirements. Use when a task requires entities, relationships, keys, cardinalities, or database schema planning.
---
~~~

Required fields in the open Agent Skills specification:

| Field | Requirement |
| --- | --- |
| name | Required; 1–64 lowercase ASCII letters and digits separated by single hyphens; no leading, trailing, or consecutive hyphens; must exactly match the skill directory name |
| description | Required; non-empty; maximum 1024 characters; explain capability and activation conditions |

The directory name should match the metadata name. Keep the description specific: it is a routing signal, not a marketing slogan.

The optional allowed-tools field is implementation-dependent. Do not rely on it for security or assume every host supports it. Tool permission must be enforced by the runtime.

## 3. What belongs in each location?

### SKILL.md

Keep the instructions needed to execute the task:

- Role and purpose, stated briefly.
- When to use the skill and when not to use it.
- Required and optional inputs.
- Ordered workflow and decision points.
- Tool usage expectations and limitations.
- Output contract.
- Error handling and final validation.
- Links to supporting resources.

Keep this file focused. The specification recommends keeping the main file under 500 lines and moving detailed material to references.

### references/

Use for material the agent may need to consult selectively:

- Official technical documentation excerpts or links.
- Domain-specific standards and conventions.
- Detailed schemas and format definitions.
- Complex decision tables.
- Background explanations that are not required on every execution.

Keep files focused and avoid deeply nested reference chains. Prefer links relative to the skill directory, for example: references/normalization.md.

### scripts/

Use for deterministic operations that are clearer and safer as code than as prose:

- Parsing or transforming structured files.
- Validating schemas or generated artifacts.
- Running repeatable checks.
- Preparing deterministic project scaffolding.

Every script must document its purpose, inputs, outputs, dependencies, invocation, and failure behavior. Validate inputs and use safe defaults. Never hide destructive behavior in a helper script.

### assets/

Use for static resources:

- Reusable templates.
- Example input and output files.
- Diagram source templates.
- Configuration samples.
- Small fixtures required by a workflow.

Do not store secrets, private customer data, or unnecessary binaries in a skill package.

### agents/

Some hosts support host-specific metadata such as agents/openai.yaml. Treat these as optional integration files, not part of the minimum portable format. Document which host consumes them and keep the core workflow usable without them.

## 4. Progressive disclosure

A skill should reveal detail in layers:

1. **Discovery metadata:** name and description help the agent recognize a possible match.
2. **Core instructions:** SKILL.md explains the workflow after activation.
3. **On-demand resources:** references, scripts, and assets are loaded or used only when the workflow needs them.

This keeps unrelated technical detail out of the initial context. It also makes it easier to maintain specialized reference material without bloating the core instructions.

## 5. File and naming conventions

- Use lowercase kebab-case for skill directories and names.
- Use descriptive, stable filenames.
- Prefer one topic per reference file.
- Use relative paths from the skill root in links.
- Keep examples small, synthetic, and safe to publish.
- Avoid duplicate SKILL.md files in one skill bundle.
- Do not make a skill depend on a local absolute path that will not exist for other users.

## 6. Portability and host differences

The open format standardizes the package shape; it does not guarantee identical tool access or execution behavior in every AI product. Before claiming compatibility, test the package in the intended host.

For host-specific features, state:

- Which host or runtime is required.
- Which optional metadata or tools it uses.
- What happens when the feature is unavailable.
- Whether a portable fallback exists.

## 7. References

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI — Build skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Developers — Skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Developers — Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI Developers — Skills in plugins](https://developers.openai.com/plugins/concepts/skills)
