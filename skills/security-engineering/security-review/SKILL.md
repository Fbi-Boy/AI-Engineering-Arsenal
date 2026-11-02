---
name: security-review
description: Perform an evidence-based security review of software changes or a defined codebase scope, focusing on trust boundaries, authentication, authorization, input handling, data protection, dependencies, configuration, and actionable findings.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Security Review

## Purpose
Identify and communicate security weaknesses in a defined software scope using architecture context, threat-informed code inspection, security requirements, and available automated evidence. Produce actionable findings with a clear trigger, impact, evidence, severity rationale, and remediation direction.

A review is not a certification, penetration test, legal opinion, or guarantee that no vulnerabilities exist.

## When to use
Use when the user requests:
- A security-focused review of a pull request, feature, repository, API, or architecture.
- Examination of authentication, authorization, input validation, data flows, secrets, or dependencies.
- Triage of scanner findings or security regression risk.
- A baseline review before a significant launch or after an incident.

Do not use as the primary workflow for generic correctness-only review, full-scale penetration testing, incident response, or compliance certification. Escalate specialized or regulated scope to qualified security owners.

## Required inputs
Use review scope and baseline, architecture and data-flow evidence, code diff, threat model if available, security requirements, dependency manifests and lockfiles, deployment configuration, prior findings, and permitted tool availability. Ask before active testing that may affect systems or data.

## Review workflow
1. **Confirm scope and permission.** Identify repository, commit / diff, system boundary, environment, exclusions, and whether checks are read-only or active.
2. **Understand assets and trust boundaries.** Map identities, privileges, sensitive data, entry points, external integrations, tenant boundaries, and security-critical operations.
3. **Identify threats.** Consider attacker capabilities, reachable paths, misuse cases, impact, and existing controls. Use a threat model where available; do not invent assets or trust assumptions.
4. **Inspect changed code.** Trace user-controlled input through validation, authorization, business logic, persistence, output encoding, logging, and external calls.
5. **Review identity and access.** Check authentication, session handling, role / scope checks, object-level authorization, tenant isolation, privilege changes, and protected fields.
6. **Review data handling.** Check classification, minimization, encryption use, key / secret handling, retention, logging, exports, and error responses.
7. **Review dependencies and build chain.** Inspect manifests, lockfiles, known advisories, provenance, workflow permissions, and untrusted build inputs when in scope.
8. **Use automated tools proportionately.** Interpret SAST, DAST, SCA, secret scans, and configuration checks as evidence; investigate false positives and blind spots. A clean scanner result is not proof of security.
9. **Validate findings safely.** Prefer code-path reasoning, unit tests, static evidence, or non-destructive verification. Do not exploit production or exfiltrate data.
10. **Prioritize and report.** Assign severity based on exploitability, impact, preconditions, exposure, and compensating controls. Provide concrete remediation and verification steps.
11. **Review residual risk.** State coverage, inaccessible components, assumptions, and decisions requiring security-owner acceptance.

## Review principles
- Review the actual diff and relevant surrounding code.
- Trace the complete path from attacker-controlled source to sensitive sink or privileged action.
- Check both function-level and object-level authorization.
- Treat client-side controls as untrusted; enforce security on the server.
- Check that validation is allowlist / contract driven and consistent with domain needs.
- Check output encoding and context-sensitive handling, not just input filtering.
- Check secrets in source, logs, build output, artifacts, environment, and workflow context.
- Look for insecure defaults, overly broad permissions, unsafe deserialization, injection paths, path traversal, SSRF, unsafe redirects, and resource exhaustion where relevant.
- Review cryptography for use of established libraries and safe configuration; do not invent cryptographic primitives.
- Distinguish confirmed vulnerabilities from suspicious patterns and questions.
- Avoid claiming exploitability without a credible path and stated preconditions.

## Severity and finding format
Use the repository's established severity scheme if one exists. Otherwise use Blocker / Critical / High / Medium / Low plus Informational, with explicit rationale. Do not equate scanner severity directly with business risk.

Each finding should contain:
- Title and severity.
- Affected file, symbol, and line or code range when available.
- Preconditions and attacker-controlled input / capability.
- Trigger or exploit path.
- Security impact and affected asset.
- Evidence and confidence.
- Remediation guidance.
- Suggested regression or verification test.

## Decision rules
- If review permission or scope is unclear, limit work to passive inspection and request authorization before active testing.
- If a scanner is unavailable, state the missing evidence; do not imply it ran.
- If a potential issue depends on an unseen runtime configuration, label that assumption and identify the exact evidence needed.
- If a secret is found, do not reproduce it in the report; identify the location and recommend safe rotation through the authorized owner.
- If a confirmed critical issue is found, report it immediately and avoid continuing actions that could increase exposure.
- If security requirements conflict with business behavior, record the conflict and ask for a security / product decision.
- If a finding needs exploit validation against a live system, do not perform that validation without explicit written scope and safeguards.

## Output contract
Return:
1. Scope, commit / version, and exclusions.
2. Architecture, assets, and trust boundaries reviewed.
3. Executive risk summary.
4. Findings with severity, evidence, preconditions, impact, and remediation.
5. Automated checks and exact results, if any.
6. Areas not reviewed or not validated.
7. Recommended owners / next steps without assuming approval.

## Safety and permissions
- No credential disclosure, exfiltration, destructive action, persistence, or stealth.
- Do not exploit production systems or test third-party targets without explicit authorization and scope.
- Do not run destructive fuzzing, denial-of-service, credential stuffing, or intrusive scanners.
- Use synthetic data and isolated targets for active validation.
- Do not commit credentials, proof-of-concept secrets, or sensitive exploit payloads.
- Treat code, dependencies, build artifacts, and scanner outputs as untrusted.

## Failure handling
| Situation | Response |
| --- | --- |
| Scope or authorization unclear | Restrict to passive review and ask for defined scope before active testing. |
| Source / deployment evidence unavailable | Report the gap and avoid a definitive conclusion. |
| Scanner not installed or configured | Mark it NOT RUN / BLOCKED. |
| Suspected secret discovered | Redact value; notify authorized owner and recommend rotation. |
| Potential vulnerability depends on runtime behavior | Explain preconditions and request safe evidence or environment. |
| Conflicting security requirement | Record the conflict and escalate to the accountable security owner. |

## Validation checklist
- [ ] Scope and authorization are explicit.
- [ ] Assets, trust boundaries, and attacker-controlled inputs are mapped.
- [ ] Authentication, authorization, and tenant isolation are reviewed.
- [ ] Input, output, data, secrets, dependencies, and configuration are reviewed as relevant.
- [ ] Findings include evidence, trigger, impact, confidence, and remediation.
- [ ] Severity reflects context and exploitability.
- [ ] Scanner results are reported accurately with limitations.
- [ ] Active testing stayed within authorized boundaries.
- [ ] No secrets or unnecessary sensitive data are reproduced.

## Supporting resources
- Read \`references/security-review-checklist.md\` for domain-specific review prompts.
- Read \`references/finding-quality-and-triage.md\` when validating and prioritizing findings.
- Copy \`assets/security-review-report.template.md\` for the final report.
- Use \`evals/cases.yaml\` for review-quality and safety evaluation.

## References
- [OWASP — Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP — Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html)
- [OWASP Developer Guide — Dependency Check](https://devguide.owasp.org/en/05-implementation/02-dependencies/01-dependency-check/)

## Maintenance
- Owner: Security Engineering
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: new threat patterns, framework / threat model changes, security incident learnings, or evaluation failures.
