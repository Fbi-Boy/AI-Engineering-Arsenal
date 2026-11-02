# Task Sizing and Dependency Guidance

## Signs that an item is too large

Consider splitting a work item when:
- It includes several distinct user outcomes.
- It cannot be completed or demonstrated within the team's normal planning horizon.
- Acceptance checks cover unrelated behaviors.
- It contains multiple independent integrations or large unknowns.
- Reviewers cannot understand the scope in one focused review.

Use the team's agreed threshold. A rule of thumb from an external guide is not a universal limit for every team.

## Signs that an item is too small

Consider combining items when:
- They have no independent value or verification.
- They are always completed together by the same role.
- The extra tracking costs more than the clarity it provides.
- The breakdown is merely a list of coding keystrokes.

## Estimation

Estimates are forecasts, not promises.

- Prefer the team's established method: relative points, t-shirt sizes, ideal days, or another calibrated approach.
- Do not convert story points into hours unless the team has a defined and defensible method.
- Consider complexity, effort, uncertainty, and dependencies.
- Record the rationale when an estimate is highly uncertain.
- Re-estimate when scope, context, or technical evidence changes.
- Do not use estimates or velocity to rank individual developers.

When context is insufficient, use:
- `Not estimated` — insufficient information.
- `Spike needed` — discovery is required.
- A broad range — only when the user explicitly asks and the uncertainty is explained.

## Dependency types

| Type | Example | Planning treatment |
| --- | --- | --- |
| Technical | API contract must exist before client integration. | Show predecessor and verify contract readiness. |
| Data / environment | Test dataset or environment is unavailable. | Record prerequisite and owner. |
| External party | Identity provider team must provision a client. | Track as an external dependency. |
| Decision | Attendance correction policy is unsettled. | Create a decision item; do not assume policy. |
| Validation gate | Security review is required before release. | Make the gate explicit in the delivery sequence. |

Distinguish:
- **Blocking dependency:** work cannot responsibly proceed until it is satisfied.
- **Non-blocking relationship:** work can proceed with a documented assumption or parallel path.
- **Suggested order:** a preferred sequence, not a hard dependency.

## Risk-aware sequencing

Prioritize learning and risk reduction when:
- An integration or platform is unfamiliar.
- Data migration is difficult to reverse.
- Security or privacy implications are material.
- A key requirement has not been validated.
- A critical dependency is outside the team's control.

Do not place all testing or security at the end. Include verification throughout each slice.
