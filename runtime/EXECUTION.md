# Workflow executor v0.1

## Scope

The executor runs a ready `WorkflowPlan` synchronously and sequentially through
Python handlers explicitly registered by the application, keyed by the selected
skill name. It never loads or interprets `SKILL.md` as executable code and does
not dynamically import modules, invoke shell commands, or discover plugins.

## Execution contract

Call `execute_workflow(plan, handlers, approval=...)` with:
- a planner result whose status is `ready`;
- a mapping from skill names to trusted Python callables;
- an `ExecutionApproval` containing a non-empty approver label and reason.

The approval object is a caller attestation, **not authentication**. The runtime
does not verify identity, role, policy, or permission. Applications must enforce
their own approval and authorization controls before constructing it. This API
gate is defense-in-depth against accidental invocation, not a security boundary.

Preflight validates the plan ordering and dependency references and verifies
that every selected skill has a registered handler before invoking any handler.
A preflight failure leaves every task pending and starts none.

## State and failure behavior

Task event states are `pending`, `running`, `completed`, `failed`, and
`blocked`. Events preserve the transition history for this run.

Tasks run in the planner's topological execution order. A task whose dependency
did not complete is marked blocked. A handler exception marks that task failed;
independent tasks continue, while dependents are blocked. The overall result is
`completed`, `failed`, or `blocked`. Missing approval yields
`awaiting_approval`; invalid plans or missing handlers yield `not_started`.

A handler receives task metadata and a read-only mapping of completed dependency
outputs. Outputs remain in memory and are not persisted. The runtime does not
retry, timeout, cancel, parallelize, serialize outputs, or roll back side effects.

## Safety and limitations

Registered handlers are trusted application code and may perform arbitrary
actions. Do not register untrusted skill content as a handler. The runtime
cannot sandbox Python callables. The approval attestation is not an authorization
system. Browser/local tool permissions, durable state, policy checks, audit
storage, retries, cancellation, and safe concurrency are future layers.
