# Relational Normalization and Integrity Notes

This guide is DBMS-neutral unless a vendor-specific behavior is explicitly identified. Physical behavior must be checked against the target database engine and version.

## Normalization review

### First Normal Form (1NF)

A relation should represent atomic values at the chosen domain level and avoid repeating groups or numbered columns that encode a variable-length list.

Review for:
- Comma-separated IDs or values in one field.
- Columns such as phone_1, phone_2, phone_3 when the number is unbounded.
- Multiple independent facts stored in one attribute.

Not every JSON or array column is inherently wrong. Choose it only when the domain semantics, query needs, and DBMS support justify treating the value as one attribute.

### Second Normal Form (2NF)

A non-key attribute should depend on the whole candidate key, not only part of a composite key. This matters especially in associative relations with composite identifiers.

Example: if an Enrollment key is (student_id, course_id), a student_name depends on student_id, not on the entire enrollment key, and belongs to Student rather than Enrollment.

### Third Normal Form (3NF)

Non-key attributes should not depend transitively on a candidate key through another non-key attribute.

Example: if a Course row stores department_id and department_name, the department name depends on department_id. Store department attributes with the Department entity and reference it from Course, unless a deliberate snapshot / historical rule applies.

Normalization is a tool for reducing update anomalies, not a prohibition on every repeated or denormalized value.

## Keys and constraints

- **Primary key:** chosen identifier for a row; should be stable and unique.
- **Candidate key:** any minimal attribute set that uniquely identifies a row.
- **Foreign key:** enforces a relationship to a referenced key where supported and enabled.
- **UNIQUE:** enforces uniqueness beyond the primary key.
- **NOT NULL:** requires a value.
- **CHECK:** enforces a row-level predicate where supported.
- **DEFAULT:** supplies a value when the insert omits it; it does not necessarily validate every business rule.
- **Exclusion / temporal constraints:** use where the engine supports them and the domain requires them.

A foreign key can preserve referential integrity, but it does not by itself enforce all domain authorization or lifecycle rules.

## Referential actions

| Action | Typical consequence | Questions before selecting |
| --- | --- | --- |
| RESTRICT / NO ACTION | Prevents deletion or key change when dependents exist, subject to engine semantics. | Should a parent be retained while child records exist? |
| CASCADE | Propagates parent update / delete to dependent rows. | Are child rows truly owned and disposable with the parent? |
| SET NULL | Clears the child reference. | Is the relationship optional and is null meaningful? |
| SET DEFAULT | Sets a configured default where supported. | Does the default preserve domain meaning? |

Do not select CASCADE merely because it makes test cleanup convenient. Verify exact engine semantics and timing of constraint checks.

## Many-to-many relationships

Use an associative relation when each entity can be associated with many instances of another entity. Its key may be:
- Composite, such as (student_id, course_id), when the pair is unique for its whole lifetime.
- Surrogate plus a unique constraint on the natural pair, when the relationship has independent identity, lifecycle, or history.

If the relation can happen multiple times over time, add a period, attempt number, or other domain discriminator; do not assume the pair alone is unique.

## Temporal and historical data

Before updating a record in place, ask whether the domain needs to preserve:
- Who changed it and when.
- Previous values.
- Effective dates vs transaction timestamps.
- Approval or audit history.
- Reversibility and correction records.

Use history tables, event records, or temporal features only where requirements justify them.

## Denormalization

Consider denormalization only when:
1. A measured query or workload problem exists.
2. The normalized source of truth is identified.
3. Update propagation or refresh behavior is defined.
4. Staleness and consistency trade-offs are acceptable.
5. There is a verification / monitoring plan.

A cache, materialized view, summary table, or search index may be more appropriate than duplicating transactional state.

## Engine-specific note

MySQL InnoDB and other relational engines implement index and referential-integrity behavior with engine-specific details. For example, InnoDB documents foreign-key constraints and indexes required for relationship checks. Always verify the selected engine's exact data types, collation, indexing, deferred constraint support, and delete/update semantics.

Sources:
- [MySQL InnoDB introduction](https://dev.mysql.com/doc/refman/8.4/en/innodb-introduction.html)
- [MySQL foreign key constraints](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)
- [MySQL InnoDB best practices](https://dev.mysql.com/doc/refman/8.4/en/innodb-best-practices.html)
