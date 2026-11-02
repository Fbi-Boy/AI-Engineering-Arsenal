# API Contract Review Checklist

## Scope and modeling
- [ ] API purpose, boundary, consumers, and trust zones are stated.
- [ ] Resource names describe stable domain concepts.
- [ ] Operations are not a thin exposure of database tables or internal methods.
- [ ] Ownership and lifecycle behavior are documented.
- [ ] Nested resource depth and resource identity are unambiguous.

## HTTP semantics
- [ ] Method choice matches the operation's semantics.
- [ ] GET and HEAD have no state-changing side effects.
- [ ] PUT / DELETE idempotency expectations are documented.
- [ ] POST / PATCH retry behavior is explicit.
- [ ] Success, empty success, validation, not-found, conflict, and dependency errors are covered.
- [ ] Status codes are not used inconsistently for identical error situations.

## Schema quality
- [ ] Required vs optional and nullable vs absent are distinguished.
- [ ] Type, format, bounds, length, enum, and pattern constraints are explicit.
- [ ] Request schemas exclude server-managed fields.
- [ ] Response schemas omit sensitive or unauthorized properties.
- [ ] Examples use synthetic values and match schemas.
- [ ] Date/time, currency, locale, and identifier formats are explicit when relevant.

## Client experience
- [ ] Pagination is bounded and has stable ordering.
- [ ] Filtering / sorting fields are allowlisted and documented.
- [ ] Error codes are stable and actionable.
- [ ] Correlation identifiers and retry guidance are provided where useful.
- [ ] Versioning and deprecation policy are clear.
- [ ] Breaking changes have a migration plan.

## Contract tooling
- [ ] OpenAPI version is compatible with the target toolchain.
- [ ] operationId values are unique and stable.
- [ ] Reusable schemas / responses resolve correctly.
- [ ] Security declarations match actual operation requirements.
- [ ] Examples are valid against schemas.
- [ ] Generated clients or contract tests are reviewed where appropriate.
- [ ] Implementation and documentation drift is considered.
