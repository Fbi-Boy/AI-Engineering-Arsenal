# Relational Schema Integrity Review

## Keys
- Every entity table has an appropriate primary key.
- Candidate keys and business uniqueness rules are enforced where required.
- Surrogate keys are not treated as substitutes for business uniqueness.
- Composite keys match the real identity of the record over its lifecycle.

## Relationships
- Foreign keys reference a valid candidate / primary key.
- Parent and child column types are compatible.
- Nullability matches optionality.
- Delete and update actions match the domain ownership rule.
- Cross-tenant references cannot violate tenant boundaries.
- Junction / associative tables have a duplicate-prevention constraint when required.

## Data types
- Decimal precision / scale is appropriate for measured or monetary values.
- Integer range is sufficient for identifier and count growth.
- Date, time, timezone, and timestamp semantics are explicit.
- Character set and collation match comparison and uniqueness rules.
- Text and binary fields have justified size / usage.
- Sensitive credentials are not stored in plaintext.

## Constraints
- NOT NULL reflects required domain facts.
- UNIQUE reflects actual uniqueness rules.
- CHECK reflects enforceable domain predicates supported by the engine.
- DEFAULT values are valid and do not conceal missing required input.
- Generated / computed columns have deterministic and compatible definitions.
- Constraint names and error handling are maintainable.

## Normalization
- Repeating groups and multi-valued columns are understood.
- Partial and transitive dependencies are reviewed.
- Denormalized data has a source of truth and update strategy.
- Historical snapshots are distinguished from accidental duplicate facts.
- JSON / array fields are justified by access and integrity needs.

## Indexes
- Indexes support known query predicates, joins, ordering, and uniqueness.
- Composite column order is supported by actual query patterns.
- Redundant indexes are identified only with evidence.
- Write and storage overhead is considered.
- Plans or benchmarks support performance claims.

## Evidence limitations

A DDL-only review cannot prove:
- Actual query latency at production scale.
- Real index usage.
- Correctness of business policy.
- Completeness of all data consumers.
- Safety of a migration under an unknown deployment pattern.

Mark these as evidence gaps and define what to inspect next.
