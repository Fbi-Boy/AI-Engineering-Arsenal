# Frontend Change Patterns

## Inspect the app before choosing a pattern

Identify the actual framework, version, routing system, styling approach, form library, state strategy, API client, and test runner. Do not assume React, Vue, Angular, Svelte, or a CSS framework merely because the task is frontend work.

## Component boundaries

Good component boundaries often follow:
- Reusable visual primitives with stable behavior.
- Domain-specific components that own a coherent piece of UI.
- Page / route components that compose feature-level content.
- Shared layout or navigation that is consistent across routes.

Avoid:
- One component that owns unrelated flows.
- A component for every trivial text wrapper.
- Hidden coupling through global mutable state.
- Passing large unrelated prop objects through many layers.

## State ownership

Choose state based on its lifetime and scope:
- Local UI state for temporary interactions.
- URL state for navigable / shareable filters and tabs where appropriate.
- Server state for data fetched from an API, with invalidation / freshness rules.
- Shared application state only when multiple areas genuinely need it.

Do not copy server data into multiple unrelated local stores without a consistency strategy. Derive values where possible rather than storing duplicates.

## Forms and validation

A robust form typically needs:
1. Semantic form, labels, input types, and instructions.
2. Client-side validation for quick feedback.
3. Server-side validation as the trust boundary.
4. Pending state and duplicate-submit protection.
5. Field-level and form-level error messages.
6. Success confirmation and recovery from transient failure.
7. Accessible focus and error announcement behavior.

Do not place client-side secrets in form code or rely on client checks for policy enforcement.

## API integration

- Follow the contract and generated / shared types if the project has them.
- Distinguish loading, success, empty, and error responses.
- Cancel or ignore stale requests when the route or query changes.
- Do not automatically retry unsafe writes.
- Minimize response data retained in client memory.
- Use a central error mapping pattern if one already exists.

## Dependency choices

Before adding a dependency, establish:
- Required capability not provided by the framework or existing code.
- Maintenance and security status.
- Bundle / runtime cost.
- Type / framework compatibility.
- Licensing and project policy.
- Whether a small local utility is safer and simpler.

A dependency should solve a concrete requirement, not just match personal preference.

## Change scope

Prefer a coherent vertical slice with tests. Avoid unrelated folder restructuring, global formatting, or design-system replacement unless separately requested.
