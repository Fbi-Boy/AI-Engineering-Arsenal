---
name: technical-documentation
description: Create, update, review, and organize maintainable software documentation including READMEs, tutorials, how-to guides, API references, architecture records, runbooks, changelogs, and contributor guides.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Technical Documentation

## Purpose
Produce accurate, discoverable, task-oriented technical documentation that helps its intended reader understand, use, build, operate, integrate, or maintain a software system. Keep documentation connected to implementation and authoritative sources.

## When to use
Use when creating or improving README, setup, onboarding, tutorials, how-to guides, API references, architecture records, runbooks, troubleshooting guides, release notes, changelogs, or contributor guides. Use it also for audits of documentation accuracy, structure, links, examples, and drift.

Do not use as the primary workflow for marketing copy, legal policy, or architecture decisions without technical evidence.

## Required inputs
Identify audience and skill level, documentation goal, repository / product scope, source code and contracts, supported versions, environment assumptions, publishing location, style guide, owner, and review cadence. Do not invent commands, behavior, endpoints, support guarantees, or operational targets.

## Workflow
1. **Identify reader and task.** Determine what the reader needs to learn, accomplish, understand, or look up.
2. **Choose the document type.** Tutorial for guided learning; how-to for a specific goal; reference for precise facts; explanation for concepts and rationale.
3. **Inspect authoritative sources.** Check code, manifests, API schemas, configuration, tests, ADRs, workflows, and existing docs. Record version and environment assumptions.
4. **Define information architecture.** Choose page location, title, navigation, prerequisites, related links, owner, and update triggers.
5. **Plan content.** State outcome, prerequisites, steps or concepts, expected outputs, troubleshooting, limitations, and next action.
6. **Write for task completion.** Use clear headings, direct language, progressive disclosure, consistent terms, and safe examples.
7. **Validate accuracy.** Verify commands, paths, code samples, links, API fields, configuration names, screenshots, and version notes against source of truth.
8. **Protect sensitive information.** Remove credentials, private identifiers, internal URLs, customer data, and hidden metadata.
9. **Integrate docs as code.** Review docs with related changes; use version control, link checks, spell / style checks, and executable examples where safe.
10. **Review maintenance.** Identify outdated, duplicate, orphaned, generated, or unowned documentation.
11. **Report changes.** State audience, purpose, files, technical checks, gaps, and maintenance owner.

## Documentation types
- **Tutorial:** learning-oriented guided experience with a known starting point and expected result.
- **How-to guide:** goal-oriented steps for readers who already have relevant background.
- **Reference:** accurate, structured description of interfaces, parameters, configuration, schemas, or commands.
- **Explanation:** conceptual understanding, rationale, architecture, trade-offs, and context.

One topic may need several documents. Do not overload a README with every document type.

## Writing principles
- Start with who the document is for and what it helps them do.
- Use descriptive titles and make the main task or concept obvious.
- Prefer short, direct sentences and consistent technical vocabulary.
- Put prerequisites before steps and expected outputs after important commands.
- Use complete, copyable commands with safe placeholders and explain environment variables.
- Show expected output and recovery guidance for common errors.
- Distinguish required from optional configuration.
- Mark version-specific behavior and platform differences.
- Link to canonical sources rather than copying large, volatile reference blocks.
- Use diagrams for boundaries, sequence, or topology; keep source editable where feasible.
- Provide alt text or equivalent text for meaningful images and diagrams.
- Make generated documentation clearly identifiable and reproducible.

## Technical accuracy rules
- Verify commands against package scripts, build files, CI, and actual tool versions.
- Verify API reference against OpenAPI / schema / code source; do not invent endpoints or parameters.
- Verify examples compile or run where a safe environment exists.
- Redact tokens, secrets, and real user data from sample output.
- State unsupported platforms, limitations, and deprecations honestly.
- If sources conflict, identify the conflict and ask the owner rather than guessing.

## Decision rules
- If no code / contract source exists, mark technical claims provisional and request confirmation.
- If documentation describes an API, prefer generated reference from a versioned schema or code annotations.
- If commands can change data or infrastructure, label side effects and required safeguards.
- If examples rely on paid services or credentials, use safe placeholders.
- If docs disagree with behavior, report drift and route source changes to the appropriate owner.
- If the repository lacks docs tooling, propose low-friction validation instead of imposing a large stack.
- If a page is obsolete, identify consumers and replacement before recommending deletion.

## Output contract
Return audience, purpose and document type; source-of-truth artifacts inspected; files and information architecture; verified commands, samples, links and version assumptions; limitations and unresolved facts; owner and maintenance triggers.

## Safety and permissions
- Never publish credentials, secrets, tokens, private endpoints, or customer data.
- Do not expose internal security details beyond the intended audience.
- Do not run documentation examples that mutate production or external systems without authorization.
- Respect licensing and attribution for copied material.
- Do not fabricate compatibility, certification, performance, or support claims.
- Review screenshots and diagrams for private data and embedded metadata.

## Failure handling
| Situation | Response |
| --- | --- |
| Technical source unavailable | Mark claims unverified and request an authoritative source. |
| Command cannot be safely run | Inspect implementation and label the example unexecuted. |
| API schema and code disagree | Document the discrepancy; do not invent a resolution. |
| Link or example target removed | Find maintained replacement or mark unresolved. |
| Sensitive data in source artifact | Redact it and notify the authorized owner before publishing. |
| No document owner | Recommend an owner and review trigger; do not assume maintenance responsibility. |

## Validation checklist
- [ ] Audience, goal, and document type are explicit.
- [ ] Content matches chosen information architecture.
- [ ] Technical claims trace to code, contracts, or approved sources.
- [ ] Commands and examples are checked or marked unexecuted.
- [ ] Version, prerequisites, and platform assumptions are clear.
- [ ] Links and navigation resolve.
- [ ] Sensitive data and hidden metadata are removed.
- [ ] Diagrams and screenshots are accessible and current.
- [ ] Docs are reviewed with related code where feasible.
- [ ] Owner and maintenance triggers are recorded.

## Supporting resources
- Read `references/documentation-architecture-and-style.md` for document types, structure, and writing quality.
- Read `references/docs-as-code-and-validation.md` for source-of-truth, automation, and maintenance.
- Copy `assets/technical-documentation-plan.template.md` to scope a deliverable.
- Use `evals/cases.yaml` for documentation accuracy and safety evaluation.

## References
- [Diátaxis — A Systematic Approach to Technical Documentation](https://diataxis.fr/)
- [Write the Docs — Docs as Code](https://www.writethedocs.org/guide/docs-as-code/)
- [Google — Documentation Best Practices](https://google.github.io/styleguide/docguide/best_practices.html)
- [GitHub Blog — Documentation Done Right](https://github.blog/developer-skills/documentation-done-right-a-developers-guide/)

## Maintenance
- Owner: Documentation Engineering / Repository Maintainers
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: source / API changes, supported version changes, doc feedback, broken links, or evaluation failures.
