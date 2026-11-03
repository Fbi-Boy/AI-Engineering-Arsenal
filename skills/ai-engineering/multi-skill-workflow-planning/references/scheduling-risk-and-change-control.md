# Scheduling, Risk, and Change Control

## Parallel work
Parallelize tasks only when:
- All prerequisites are satisfied.
- Inputs are stable and versioned.
- Output scopes do not overlap or have an explicit merge owner.
- Shared systems and environments are isolated.
- Failure / cancellation in one branch has known effects on others.

Serialize work involving shared migrations, the same mutable artifact, ordered external operations, or dependent integration state.

## Prioritization
Consider user value, risk reduction, urgency, dependency leverage, uncertainty reduction, and cost. Document the chosen method. Avoid false precision from weighted scores whose inputs are guesses.

## Risk register
Record risk, probability / impact evidence, owner, mitigation, trigger, contingency, and whether a decision or approval is required. Use qualitative ratings when numerical likelihood is unsupported.

## Change control
When scope changes:
1. Capture source and changed requirement.
2. Identify affected task nodes and artifacts.
3. Reassess dependencies, acceptance criteria, estimates, and permissions.
4. Mark stale evidence invalid.
5. Re-plan affected work and obtain renewed approval where action details change.
6. Preserve unaffected completed tasks and rationale.

## Cancellation and recovery
- Stop dependent queued work when a prerequisite is cancelled.
- Preserve validated artifacts and checkpoint references.
- Reconcile uncertain side effects before retrying.
- Define compensation or rollback owner for mutable external steps.
- Avoid restarting the entire plan when a bounded subset can safely resume.
