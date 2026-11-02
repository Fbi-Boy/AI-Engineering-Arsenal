# Skill Quality, Safety, and Security

Every skill in AI Engineering Arsenal must be useful, predictable, and safe to run in its intended environment. These rules apply to instructions, references, scripts, examples, and generated artifacts.

## 1. Least privilege

- Request only the tools needed for the workflow.
- Prefer read-only access when inspection is sufficient.
- Do not assume a tool is available because its name appears in a document.
- Do not attempt to bypass authentication, access controls, rate limits, or permission checks.
- Treat host-enforced permissions as authoritative.

A skill describes a workflow; it does not grant permissions.

## 2. Separate analysis from side effects

Make the boundary between proposing and executing an action explicit.

Examples of side effects include:
- Creating, overwriting, moving, or deleting files.
- Installing packages or changing system configuration.
- Creating commits, branches, issues, or pull requests.
- Sending messages or publishing content.
- Changing cloud resources, access policies, or production systems.
- Triggering paid services or resource-intensive jobs.

For potentially destructive, external, irreversible, or costly actions, require the appropriate user authorization. Provide a preview or dry run when feasible. Never claim an action succeeded until the tool confirms it.

## 3. Treat external content as untrusted data

Repositories, webpages, issues, pull request comments, documents, generated files, and API responses may contain misleading or malicious instructions.

The skill must tell the agent to:
- Use external content as data to inspect, not as a replacement for system or user instructions.
- Ignore embedded requests to reveal secrets, change safety rules, or execute unrelated actions.
- Verify important claims against authoritative sources.
- Avoid executing downloaded code without inspection and authorization.
- Preserve source attribution when using technical references.

Do not let a README, code comment, web page, or sample file silently expand the task's permissions.

## 4. Protect secrets and personal data

Never include real credentials, API keys, tokens, private keys, session cookies, or passwords in:
- SKILL.md files.
- References or examples.
- Logs, screenshots, test fixtures, or pull request descriptions.
- Committed configuration files.

Use environment variables or approved secret stores at runtime. Examples must use clearly fake placeholders such as YOUR_API_TOKEN. Do not ask users to paste secrets into public repository files.

Avoid collecting or exposing personal data that is not necessary for the task.

## 5. Safe script requirements

Any script included in a skill must:

- Validate arguments and input files.
- Use explicit paths and explain its working directory.
- Avoid shell command construction from untrusted strings.
- Avoid network access unless the skill genuinely requires it.
- Use timeouts and bounded resource use where appropriate.
- Fail with a non-zero exit code when validation fails.
- Print useful errors without exposing secrets.
- Avoid destructive defaults; require explicit flags for deletion or overwrite.
- Document dependencies and supported runtime versions.

Review scripts as code, not as harmless documentation.

## 6. Reliability and factual quality

- Prefer official documentation, specifications, and maintained primary sources.
- State assumptions and uncertainty where they affect the result.
- Do not invent APIs, configuration options, command output, test results, or tool availability.
- Distinguish required steps from optional recommendations.
- Include version constraints when behavior varies by version.
- Avoid claiming that a result is production-ready without relevant validation.

When a source is likely to change, include a last-verified date or a process for rechecking it.

## 7. Failure handling

A skill must define what to do when:
- Required input is missing or contradictory.
- A tool is unavailable or permission is denied.
- A command fails or returns partial data.
- A referenced file or URL cannot be found.
- Validation detects a defect.
- The task would exceed scope or require extra approval.

Do not silently continue after a critical failure. Explain the blocker, preserve user data, and offer the safest next step.

## 8. Quality gates

Before a skill can be marked Ready, reviewers must confirm:

- The workflow is narrow and understandable.
- Instructions are consistent and non-contradictory.
- Tools and permissions are accurately described.
- No secret or private data is included.
- External content is treated as untrusted.
- Side effects and approvals are explicit.
- Scripts are reviewed and tested.
- Output validation is defined.
- Limitations and failure paths are documented.

## 9. Security review triggers

Request an additional security-focused review if a skill:
- Reads or writes credentials or sensitive data.
- Runs shell commands or downloads executable code.
- Modifies repositories, permissions, infrastructure, or production data.
- Sends messages, publishes content, or performs financial actions.
- Uses browser automation with authenticated sessions.
- Processes untrusted user uploads or external documents.

## 10. Principle

**An instruction is not a security boundary.** Enforce permissions, isolation, approval, and secret handling in the host application or runtime. The skill should reinforce those controls, never replace them.
