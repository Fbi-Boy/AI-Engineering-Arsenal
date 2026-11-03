# Docs as Code and Validation

## Workflow
- Store documentation in version control with the product.
- Review documentation alongside related code / contract changes.
- Use pull requests, owners, and review checklists.
- Run link, formatting, spelling, and structural checks.
- Execute code samples in a safe environment where practical.
- Generate volatile API references from schemas or source annotations.
- Keep change history and identify document versions.

## Validation layers
1. **Structure:** files, headings, navigation, metadata, and required sections.
2. **Links:** internal paths, anchors, and external links where automated checks are appropriate.
3. **Code samples:** syntax, compilation, or execution in a safe isolated environment.
4. **Commands:** compare against manifests, scripts, CLI help, and supported versions.
5. **API / schemas:** validate generated or described interfaces against a canonical contract.
6. **Accessibility:** alt text, meaningful link labels, table structure, and readable diagrams.
7. **Security:** secret scanning, placeholder review, screenshot inspection, and sensitive metadata removal.
8. **Freshness:** owners, review triggers, version notes, and stale-page reports.

## Maintenance controls
- Assign an owner or owning team.
- Define triggers such as API changes, runtime upgrades, or repeated user confusion.
- Identify generated documents and the source that regenerates them.
- Avoid editing generated output by hand unless documented.
- Remove obsolete docs only after checking inbound links, external consumers, and replacement guidance.
- Prefer deleting duplicate / stale content over accumulating competing instructions.

## Reporting
Distinguish checked links from checked external availability, snippets that executed from snippets only inspected, and generated from manually maintained docs. Report exact commands and gaps.
