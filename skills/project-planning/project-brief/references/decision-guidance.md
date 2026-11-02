# Assumptions, Options, Decisions, and Approval

These labels prevent a draft brief from turning uncertain ideas into false commitments.

## Classification

| Label | Meaning | Example |
| --- | --- | --- |
| Fact | Supported by supplied evidence or an observed source. | "The current application has no self-service password reset." |
| Assumption | Believed to be true but not yet confirmed. | "Most students can access campus email." |
| Constraint | A mandatory boundary imposed by an authorized source. | "The service must use the existing identity provider." |
| Preference | A favored direction that can still change. | "The team prefers a web-first experience." |
| Option | One candidate among multiple possible approaches. | "Use a managed database or operate the existing database cluster." |
| Proposal | A recommended course of action awaiting a decision. | "Prototype the authentication flow before full implementation." |
| Decision | A choice made by an authorized decision-maker. | "The product owner selected the managed database option." |
| Approval | Explicit authorization by the responsible authority. | "The sponsor approved the discovery budget on YYYY-MM-DD." |

Do not upgrade a label without evidence. A technology mentioned in a conversation is not automatically a constraint or approved architecture.

## Record decision ownership

For each material decision, capture:
- Decision to be made.
- Options and meaningful trade-offs.
- Person or role authorized to decide.
- Information needed.
- Consequence of delaying the decision.
- Current state: Open, Proposed, Decided, or Approved where relevant.
- Evidence or record of the decision.

A recommendation from the assistant is not a stakeholder decision.

## Handle disagreement

When two stakeholders disagree:
1. Preserve each position in neutral language.
2. Identify the policy, user, cost, security, or operational impact.
3. Identify who has authority to resolve the conflict.
4. Present viable options only when supported.
5. Keep the item open until a decision is recorded.

Never merge conflicting positions into a made-up consensus.

## Escalation triggers

Recommend qualified review when the brief involves:
- Sensitive personal data or cross-border data handling.
- Payments, financial records, identity proofing, or access control.
- Safety-critical, health, legal, or regulated workflows.
- High availability or recovery commitments.
- Contracts, procurement, licensing, or vendor commitments.
- Material migration or production cutover risk.

The brief should identify the review dependency; it should not claim that the project is compliant or safe merely because the risk is documented.
