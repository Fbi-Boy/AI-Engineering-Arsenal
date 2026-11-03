# Orchestration Lifecycle

## Lifecycle overview
1. **Intake:** define user outcome, scope, constraints, and completion evidence.
2. **Discover:** inspect catalog, active runtime capabilities, and existing project artifacts.
3. **Route:** select one or more skills with rationale and ownership.
4. **Plan:** build a dependency graph with inputs, outputs, acceptance, risk, and stop conditions.
5. **Authorize:** establish which actions can run and which require approval.
6. **Execute:** dispatch bounded tasks and collect versioned artifacts.
7. **Validate:** inspect each handoff and cross-skill consistency.
8. **Recover:** handle retries, partial completion, cancellation, and change impact.
9. **Close:** produce evidence-backed status and next actions.

## Dependency graph
Use a directed acyclic graph for ordinary work. A dependency edge A → B means B cannot begin until A's required artifact is validated. If a workflow contains a legitimate loop (for example, implementation → tests → correction), represent it as an explicit bounded iteration with a retry / exit limit instead of hiding an unbounded cycle.

## Scheduling rules
- Run independent read-only research in parallel when scope and evidence do not conflict.
- Serialize shared-file writes or any operations that rely on a prior result.
- Do not parallelize migrations, production writes, shared resource mutations, or actions whose order affects correctness without an explicit concurrency design.
- Respect model, tool, API, rate, cost, and human-review limits.
- Do not create unnecessary specialist agents for trivial transformations.

## State transitions
Use explicit statuses:
- pending: identified but not eligible to start.
- ready: inputs and dependencies are validated.
- running: work is currently executing.
- awaiting_approval: a specific action requires an owner decision.
- blocked: required input, permission, or dependency is unavailable.
- completed: output exists and meets its acceptance criteria.
- failed: execution ended unsuccessfully.
- cancelled: owner or policy stopped the step.

A terminal state must not silently transition back to running. Reopening requires a new, recorded decision.

## Change management
When scope changes:
1. Record the changed requirement and source.
2. Determine affected steps and artifacts.
3. Mark stale dependent evidence invalid.
4. Re-run only affected planning, implementation, or verification steps.
5. Preserve unaffected, still-valid outputs with version information.

## Recovery
Resume from the last validated checkpoint. Reconcile uncertain external side effects by querying a trusted source or idempotency record before retry. A timeout is not proof that an action failed.

## Integration gates
Before completing the parent workflow, compare artifacts for agreement across requirement IDs, API schemas, database constraints, implementation behavior, tests, security controls, release requirements, and documentation. Report unresolved contradictions rather than silently making a design decision.
