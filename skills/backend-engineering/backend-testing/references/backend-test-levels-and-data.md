# Backend Test Levels and Data Strategy

## Test level selection
- **Unit:** deterministic domain rules, validation functions, mapping, and state transitions.
- **Service / component:** one service with collaborators controlled at its external boundaries.
- **Database integration:** migrations, constraints, isolation, transactions, locking, queries, and ORM behavior against a real isolated database.
- **API / contract:** request and response schemas, status behavior, authentication contract, error format, and event compatibility.
- **System / end-to-end:** a small set of important workflows across real application boundaries.
- **Operational:** health checks, recovery behavior, queue replay, backup / restore, and observability when explicitly in scope.

A test double is not equivalent to a real database or provider. State exactly which boundary is real and which is simulated.

## Data lifecycle
- Generate synthetic records and stable identifiers.
- Scope each test to its own transaction, schema, tenant, or unique namespace.
- Reset state deterministically and verify cleanup after failures.
- Do not rely on execution order or shared seed records that another test may mutate.
- Keep passwords, tokens, personal data, and provider credentials out of fixtures and logs.
- Use approved masked data only when synthetic data cannot represent the required behavior.

## Database confidence
Use database integration tests for:
- Unique, foreign-key, check, and not-null constraints.
- Transaction commit and rollback.
- Isolation and concurrent updates.
- Query behavior and important index / pagination assumptions.
- Migration forward and, where supported, rollback behavior.

An in-memory fake can help unit tests but may have different SQL, locking, null, collation, or isolation semantics.

## Integration contract
Test provider adapters with:
- Valid success responses.
- Authentication / permission failure.
- Rate limit and timeout.
- Malformed or unexpected payload.
- Duplicate callback or event.
- Partial success and retry behavior.

Use a provider sandbox for actual integration confidence. A stubbed unit test proves only the logic configured in the stub.
