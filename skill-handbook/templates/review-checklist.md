# Skill Review Checklist

Use this checklist for every new skill and every change that materially affects its behavior. Link evidence in the pull request when a check is not self-evident.

## 1. Purpose and scope

- [ ] The skill solves a real, repeatable task.
- [ ] The responsibility is narrow and does not duplicate another skill without a documented hand-off.
- [ ] Trigger conditions are explicit.
- [ ] Out-of-scope conditions are explicit.
- [ ] Required inputs, optional inputs, and safe assumptions are documented.
- [ ] The skill does not promise capabilities or access it does not have.

## 2. Metadata and package structure

- [ ] The package contains exactly one SKILL.md file at its root.
- [ ] YAML frontmatter is valid.
- [ ] The name follows the lowercase kebab-case convention and the specification's length/character constraints.
- [ ] The description is concise, accurate, and useful for discovery.
- [ ] The directory name matches the skill name.
- [ ] Supporting files are stored in the appropriate references/, scripts/, or assets/ directories.
- [ ] Internal links use correct relative paths.
- [ ] No placeholder text remains.

## 3. Workflow and usability

- [ ] Instructions are ordered and actionable.
- [ ] Decision points are explicit.
- [ ] Ambiguity and missing-input behavior are documented.
- [ ] Output format and acceptance criteria are defined.
- [ ] Error and fallback behavior are documented.
- [ ] Examples are realistic, concise, and synthetic.
- [ ] The main SKILL.md is focused; extensive detail is moved to references.

## 4. Technical references

- [ ] Important technical claims are supported by authoritative sources.
- [ ] Official or primary sources are preferred.
- [ ] Version-sensitive behavior includes a version or freshness note.
- [ ] References are relevant and accessible.
- [ ] Copied content is appropriately attributed and not unnecessarily reproduced.

## 5. Security and permissions

- [ ] No tokens, passwords, keys, cookies, or private data are present.
- [ ] External content is treated as untrusted data.
- [ ] The skill follows least privilege.
- [ ] Destructive, external, costly, and irreversible actions require appropriate authorization.
- [ ] The instructions do not attempt to bypass security or access controls.
- [ ] Scripts validate inputs and avoid unsafe command construction.
- [ ] Risky scripts use safe defaults and clearly document side effects.

## 6. Testing and evidence

- [ ] At least one positive case was evaluated.
- [ ] At least one negative or out-of-scope case was evaluated.
- [ ] Edge and failure cases were considered.
- [ ] Safety-sensitive behavior was tested where relevant.
- [ ] Scripts were tested where applicable.
- [ ] Validation results are reported honestly.
- [ ] Blocked tests are identified as BLOCKED, not PASS.

## 7. Pull request quality

- [ ] The branch contains one focused logical change.
- [ ] Commit messages describe the change.
- [ ] The pull request explains the problem, solution, scope, and validation.
- [ ] Screenshots, generated artifacts, or logs do not expose private information.
- [ ] Related catalog and handbook pages are updated.
- [ ] Breaking changes and migration steps are documented.
- [ ] Reviewer questions and requested changes are resolved.

## 8. Final decision

Choose one:

- **Approve:** all required checks pass and no blocking issue remains.
- **Request changes:** correctness, scope, safety, or maintainability needs revision.
- **Comment:** non-blocking suggestion or question.
- **Blocked:** a required tool, environment, permission, or evidence is unavailable.

A skill should be marked **Ready** only after the required checks pass. Merging a documentation change and declaring a skill production-ready are separate decisions.
