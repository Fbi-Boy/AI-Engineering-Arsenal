# Practical Debugging Workflow

## Observe before changing

Capture:
- Exact expected and actual behavior.
- First known failure time and last known good state.
- Application / dependency versions and commit.
- Request or event shape, with sensitive values removed.
- Environment, feature flags, and relevant configuration.
- Frequency, affected users, and business impact.
- Trace / correlation IDs.

Do not replace missing evidence with a guess.

## Reproduce minimally

- Build the smallest input and environment that trigger the failure.
- Use deterministic test data.
- Remove unrelated services / variables only when safe and relevant.
- Record each reproduction attempt and result.
- Keep one variable fixed while testing another.

A failure that cannot be reproduced can still be investigated, but conclusions must reflect the evidence limit.

## Hypothesis matrix

| Hypothesis | Supporting evidence | Evidence against | Safe discriminating test | Result |
| --- | --- | --- | --- | --- |
| [Cause A] | [Signal] | [Counter-signal] | [Test] | Open |

Prefer tests that distinguish two competing hypotheses rather than simply repeat the failure.

## Compare working and failing cases

Compare:
- Input values and shape.
- User / role / tenant context.
- Database state and record history.
- Environment / config / feature flags.
- Build and dependency versions.
- Call order / concurrency / timing.
- External dependency response.
- Cache and browser state.

Change one factor at a time when possible.

## Trace causal chain

Follow:
1. Triggering actor / job / event.
2. Request parsing and validation.
3. Authentication / authorization.
4. Domain logic and state transition.
5. Persistence and transaction.
6. External integration / queue / worker.
7. Response, notification, or visible symptom.

Look for the earliest point where observed state diverges from expected state.

## Root cause language

Use careful distinctions:
- "Confirmed root cause" only when evidence establishes the causal mechanism.
- "Likely cause" when evidence is strong but a key confirmation is missing.
- "Hypothesis" when it is plausible but not yet discriminated.
- "Contributing factor" for a condition that increases likelihood or impact.
- "Detection gap" for missing test, alert, telemetry, or operational control.

Avoid "the developer forgot" or other blame-oriented explanations. Focus on systems, assumptions, and controls.

## Regression prevention

A useful regression test should:
- Reproduce the triggering condition.
- Fail against the faulty behavior.
- Pass after the correction.
- Assert a user-visible or domain invariant.
- Avoid dependence on real external services where a controlled contract / integration test suffices.

## Regression boundary

When a change range is known and repository history is accessible:
- Identify the last known good and first known bad refs.
- Compare changed files and dependency updates.
- Use binary search / bisect only in a safe working copy and when builds / tests are reproducible.
- Avoid rewriting shared branch history or changing the user's branch without permission.
