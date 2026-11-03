# Authorization Policy and Action Risk

## Control concepts
- **Authentication:** establishes the identity of the user or service.
- **Authorization:** determines whether that identity may perform an operation on a resource under current policy.
- **Consent:** communicates and records the user's understanding / agreement for a defined data or service use where applicable.
- **Approval:** an authorized person explicitly accepts a proposed action requiring human review.
- **Execution enforcement:** trusted code re-checks policy and action constraints immediately before the side effect.
- **Audit:** records the request, policy / approval decision, execution attempt, and outcome.

These concepts are related but not interchangeable.

## Risk inventory
Consider:
- Confidentiality / integrity / availability impact.
- Data classification and number of affected records.
- External visibility or notifications.
- Financial cost or transaction.
- Reversibility and recovery options.
- Target scope (local, project, tenant, account, public, production).
- Privilege required and blast radius.
- Whether the action can be duplicated by retry.

Use qualitative tiers when no approved numerical methodology exists. Document policy owner and exception path.

## Policy model
A policy decision may depend on subject, action, resource, environment, attributes, time, and context. Use the organization's established RBAC / ABAC or policy engine. Do not invent role names or treat a UI feature flag as authorization.

Enforce a policy decision at the service / tool boundary. Re-check object ownership, tenant, environment, and resource version rather than trusting model-supplied identifiers.

## Typical approval tiers
- Read-only actions may run within existing access.
- Reversible local changes may require review based on data sensitivity and user policy.
- External writes, repository changes, messages, public posts, infrastructure changes, and user-record edits require scoped permission and approval where defined.
- Destructive, financial, credential, production, or irreversible actions require strong controls, independent approval, and a recovery plan where policy requires.

The actual classification must follow the product's risk framework and owner decisions, not this generic example.

## Deny-by-default cases
Deny when actor is unknown, target is outside scope, policy denies, approval is missing / stale, resource version changed, approval authority is invalid, or enforcement cannot run.
