# Acceptance Criteria Quality Checklist

## Testability

- Is there a clear pass/fail observation?
- Can a reviewer identify the actor, context, action, and result?
- Is the expected evidence named?
- Are thresholds measurable and sourced?

## Scope and relevance

- Does each criterion support the stated requirement or story?
- Is the criterion about externally observable behavior?
- Is it within the agreed scope?
- Could it be split without losing meaning?

## Clarity and consistency

- Does it use consistent domain language?
- Does it avoid vague adjectives and subjective judgments?
- Does it avoid combining unrelated obligations?
- Does it agree with other requirements, policies, and system states?

## Scenario coverage

- Primary successful path.
- Important alternate path.
- Invalid or missing input.
- Boundary conditions.
- Authentication and authorization.
- Dependency or service failure.
- State changes, retries, and duplicate requests.
- Relevant privacy, security, accessibility, performance, and operational behavior.

Not every item is applicable to every story. Record why a category is excluded when the risk warrants it.

## Difference from Definition of Done

| Acceptance criteria | Definition of Done |
| --- | --- |
| Specific to a story, feature, or requirement. | Shared across work items or product increments. |
| Defines the behavior or result expected by a stakeholder. | Defines the team's minimum quality and completion practices. |
| May describe an individual scenario. | Often includes testing, review, documentation, and release readiness. |
| Changes with the item. | Changes through a team-level agreement. |

A story can satisfy its acceptance criteria but still fail the team's DoD, for example when required code review or regression testing is incomplete.

## Approval discipline

- Mark criteria Draft or Proposed until the appropriate owner confirms them.
- Record who owns unresolved business rules.
- Do not mark a requirement Accepted merely because a test has been written.
- Do not claim test execution from a test plan alone.
