# Acceptance Criteria Writing Patterns

Choose a format that makes the expected behavior easiest to understand and verify.

## Checklist criteria

Use concise checklist statements when the behavior is straightforward.

Example:
- [ ] A signed-in student can view only their own attendance records.
- [ ] The page shows an empty state when no records exist.
- [ ] An unavailable service produces a clear retry message without exposing internal error details.

Avoid vague criteria such as "the page works correctly".

## Given / When / Then

Use this form when a behavior depends on context and an action.

```text
Given [known initial context]
When [an actor performs an action]
Then [observable expected result]
```

Example:
- Given a student is signed in and has an attendance record for the selected course,
- When the student opens the attendance page,
- Then the page displays the matching record and its recorded status.

Keep each scenario focused on one behavior. Do not pack many unrelated outcomes into a single Then clause.

## Decision tables

Use a table when multiple conditions combine to determine an outcome.

| Actor role | Record owner | Record status | Expected action |
| --- | --- | --- | --- |
| Student | Same student | Finalized | View only |
| Student | Different student | Any | Access denied |
| Authorized staff | Any in assigned scope | Pending | Review permitted |
| Unauthenticated | Any | Any | Sign-in required |

These rows are examples only. Confirm actual access policy with the responsible owner.

## Boundary criteria

For numeric or length boundaries, state:
- Boundary value.
- Below-boundary behavior.
- At-boundary behavior.
- Above-boundary behavior.
- Validation message or outcome.

Do not invent a boundary value. Use the requirement or label the proposed value for confirmation.

## Quality-attribute criteria

A quality criterion needs a defined operating context and verification method.

Weak: "The API must be fast."

Better structure:
- Under [defined workload],
- the [named operation] must complete within [approved threshold],
- measured at [measurement point],
- using [test method / environment].

If any parameter is missing, identify it as an open question. Do not fill it with an arbitrary industry number.

## Negative and failure paths

Consider invalid input, unavailable dependencies, expired sessions, permission denial, retries, duplicates, and partial failures where relevant. Describe what the user can observe and what data or state must remain unchanged.

## Language guide

Prefer:
- "The system displays..."
- "The user can..."
- "The request is rejected when..."
- "No record is created unless..."
- "The result contains..."

Avoid:
- "Should be nice..."
- "Works properly..."
- "Fast enough..."
- "Secure by default..." without a defined behavior or assurance method.
