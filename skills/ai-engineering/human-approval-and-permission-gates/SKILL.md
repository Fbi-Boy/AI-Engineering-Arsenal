---
name: human-approval-and-permission-gates
description: Design and review authorization and human-approval controls for AI assistants and agents, including action risk classification, policy enforcement, scoped consent, approval lifecycle, revocation, and auditable decisions.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Human Approval and Permission Gates

## Purpose
Define controls that prevent an AI assistant or agent from performing actions beyond the user's authority, the application's policy, or the exact scope approved by a human. Separate authentication, authorization, policy evaluation, consent, and approval; each answers a different question.

Approval is not a substitute for authorization, and model intent is never permission.

## When to use
Use when:
- An assistant can change repositories, files, accounts, records, settings, or external systems.
- Tools perform privileged, destructive, financial, public, or irreversible operations.
- A workflow needs review pauses, approval routing, expiry, revocation, or evidence.
- Permission boundaries differ by user, tenant, project, target, or operation.

Do not use to grant access, override an organization's policy, or perform the gated action itself.

## Required inputs
Identify actor identity, roles / attributes, policy owner, resources and targets, operations, side effects, reversibility, sensitivity, execution environment, approval authorities, authentication model, audit obligations, and emergency / denial behavior. Unknown policy must remain a decision, not an assumption.

## Workflow
1. **Inventory actions.** Enumerate tools and operations, including hidden side effects and downstream calls.
2. **Classify risk.** Consider impact, reversibility, scope, sensitivity, audience, cost, and blast radius.
3. **Separate control questions.** Identify authenticated actor, current authorization, policy decision, required consent, approval authority, and runtime enforcement point.
4. **Define least-privilege policy.** Scope user / service identity to allowed action, resource, project / tenant, environment, and time.
5. **Place enforcement at the boundary.** Check policy in trusted application / tool server code immediately before the side effect; UI and prompts are not enforcement.
6. **Design approval request.** Present exact action, tool, target, arguments, expected effect, risk, reversibility, and meaningful consequences.
7. **Bind approval.** Associate the decision with an immutable action fingerprint, requester, approver, target, argument digest, policy version, timestamp, and expiry.
8. **Handle decision lifecycle.** Support pending, approved, rejected, expired, revoked, consumed, and failed states; define one-time use and duplicate submission behavior.
9. **Revalidate at execution.** Check actor identity, policy, target, current state, approval expiry / revocation, and action fingerprint again before execution.
10. **Enforce safe failure.** Fail closed when policy or approval service is unavailable for actions that require it.
11. **Record evidence.** Store decision and execution outcome separately, with redaction and retention controls.
12. **Test bypass paths.** Exercise direct tool access, altered arguments, stale approvals, role changes, retries, queued work, and cancellation.
13. **Document ownership.** Use the approval-gate template and record policy owner, reviewer roles, exceptions, and recovery.

## Design principles
- Authentication proves identity; authorization decides what that identity may do; approval is an additional human decision.
- Approval must not grant a permission the actor or organization policy does not allow.
- Bind a decision to the exact action, target, material arguments, and relevant resource version.
- Any change to target, arguments, identity, policy version, or material state invalidates the prior approval.
- Require approval at the last responsible moment, immediately before the side effect.
- Use one-time, expiring approvals for sensitive operations.
- Keep approval UI and policy engine separate from the model's proposal.
- Present concise, human-readable consequences; do not hide material effects in long JSON.
- Record who requested, who decided, what was approved, and whether the action actually ran.
- Reject self-approval where separation of duties or policy requires independent approver.
- Make cancellation, role revocation, and approval expiry disable queued actions.
- Do not equate an approval click with successful execution.

## Decision rules
- If actor identity cannot be established, deny protected actions.
- If policy denies the action, no human approval can override that denial unless a documented exception mechanism authorizes it.
- If policy requires approval, pause without running the side effect.
- If arguments or target change after approval, require a new decision.
- If an approval has expired, been revoked, or already consumed, do not reuse it.
- If authorization changes while approval is pending, re-evaluate against current policy.
- If the approval service is unavailable, fail closed for gated operations; allow only explicitly safe read-only behavior.
- If high-risk action has no named approver, mark BLOCKED.
- If multiple independent owners are required, collect each required decision and stop on any rejection.
- If action result is uncertain, reconcile before retry; the old approval is not a retry token.

## Output contract
Return:
1. Action inventory and risk classification.
2. Actor / resource / operation authorization model.
3. Policy enforcement points and failure behavior.
4. Approval request payload and human-readable presentation.
5. Approval binding, expiry, revocation, and consumption lifecycle.
6. Execution-time revalidation and idempotency design.
7. Audit evidence and privacy / retention approach.
8. Bypass / abuse test matrix.
9. Policy owners, exceptions, assumptions, and unresolved decisions.

## Safety and permissions
- Never expose tokens, credentials, or private approval links.
- Do not allow model instructions, tool descriptions, or UI state to grant permissions.
- Do not log full secrets or unnecessary personal data in approval / audit records.
- Do not approve an action on behalf of the user or approver.
- Do not execute a privileged action while approval is pending.
- Ensure cancellation and revocation propagate to queues and worker execution.
- Never create a generic reusable approval for all future actions.

## Failure handling
| Situation | Response |
| --- | --- |
| Actor identity unavailable | Deny protected action and report authentication failure. |
| Policy denies | Stop; do not present approval as a bypass. |
| Approval service unavailable | Fail closed for gated actions and preserve safe state. |
| Arguments changed | Invalidate approval and request a new decision. |
| Approval expired / revoked | Cancel action and dependent queued work. |
| Duplicate approval submission | Use idempotent decision handling; do not execute twice. |
| Execution outcome unknown | Reconcile resource state before any retry. |
| Approver is not authorized | Reject the decision and request a valid approver. |

## Validation checklist
- [ ] Authentication, authorization, consent, policy, and approval are distinct.
- [ ] All side effects and downstream operations are inventoried.
- [ ] Policy is enforced in trusted code immediately before action.
- [ ] Approval is bound to exact action / target / argument digest.
- [ ] Approval expires, can be revoked, and is consumed once.
- [ ] Current identity and policy are revalidated at execution.
- [ ] Queued actions respond to cancellation / role changes.
- [ ] Denial and service outage fail safely.
- [ ] Decision, execution attempt, and outcome are separately audited.
- [ ] Tests cover tampering, replay, stale state, and bypass attempts.

## Supporting resources
- Read `references/authorization-policy-and-risk.md` for actors, policy, action classification, and enforcement points.
- Read `references/approval-lifecycle-and-bypass-resistance.md` for fingerprint binding, expiry, revocation, replay, and tests.
- Copy `assets/approval-gate-design.template.md` for the security / approval design.
- Use `evals/cases.yaml` for approval and authorization evaluation.

## References
- [OpenAI — Guardrails and Human Review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)
- [OpenAI — Results and State](https://developers.openai.com/api/docs/guides/agents/results)
- [OWASP — Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP — Transaction Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

## Maintenance
- Owner: Security Engineering / Platform Engineering
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: policy changes, new tool types, authorization incidents, approval UX changes, or evaluation failures.
