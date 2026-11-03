# Routing Confidence and Composition

## Confidence model
- **High:** one available skill clearly owns the requested outcome and output.
- **Medium:** the best route is likely, but an input gap or adjacent skill boundary needs confirmation.
- **Low:** candidate skills overlap or the requested goal is underspecified; ask one material question.

Confidence is about routing evidence, not whether the specialist will succeed.

## Candidate comparison
Compare trigger fit, in-scope tasks, exclusions, required inputs, output contract, runtime availability, safety constraints, and lifecycle owner. A name or keyword match is insufficient.

## When to compose
Compose multiple skills when:
- Distinct artifacts are required.
- A downstream skill depends on a validated upstream artifact.
- Independent specialist work provides measurable quality or risk benefit.
- An independent review role is intentionally required.

Do not compose:
- Multiple skills that repeat the same task.
- A reviewer and author simultaneously on one artifact when independent review is required.
- Tools / skills that are unavailable in the runtime.
- Stages whose inputs or approvals are not ready.

## Handoff quality
State the exact artifact, version, required fields, owner, dependencies, acceptance criteria, and what is explicitly out of scope. Avoid passing unnecessary private data or conversation history.

## Escalation
Ask the user when the choice affects externally visible behavior, data model, security posture, cost, irreversible action, or acceptance ownership. For nonmaterial ambiguity, record a reversible assumption and proceed.
