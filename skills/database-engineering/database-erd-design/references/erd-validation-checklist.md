# ERD Validation Checklist

## Scope and semantics
- [ ] Model subject, boundary, level, and exclusions are explicit.
- [ ] Every entity is supported by a domain concept, requirement, or lifecycle.
- [ ] Entity names are singular or follow a documented repository convention.
- [ ] Domain terms and definitions are consistent.

## Attributes and identifiers
- [ ] Attribute meaning, type family, nullability, and constraints are known at the chosen model level.
- [ ] Primary key exists for every physical table.
- [ ] Candidate / alternate keys and uniqueness are considered.
- [ ] Derived and duplicated values have a justified consistency rule.
- [ ] Sensitive attributes are minimized and access-controlled.

## Relationships
- [ ] Relationship names express business meaning.
- [ ] Minimum and maximum cardinality are stated on both ends.
- [ ] Optionality matches the domain rule.
- [ ] M:N relationships are resolved for relational implementation.
- [ ] Self-references and weak entities are modeled intentionally.
- [ ] Referential actions match ownership and deletion policy.

## Normalization and integrity
- [ ] Repeating groups and non-atomic facts are reviewed.
- [ ] Partial and transitive dependencies are considered.
- [ ] UNIQUE, NOT NULL, CHECK, and FK constraints are identified.
- [ ] Data anomalies from update / delete / insert are considered.
- [ ] Denormalization has workload evidence and consistency strategy.

## Lifecycle and operational concerns
- [ ] Audit and history needs are considered.
- [ ] Retention, archival, and deletion are not guessed.
- [ ] Tenant and ownership boundaries are explicit when relevant.
- [ ] Index candidates are tied to actual query patterns or labeled provisional.
- [ ] Model is split into understandable views if large.

## Diagram quality
- [ ] Notation and symbols are identified.
- [ ] PK / FK and optionality are visible.
- [ ] Cross-context references are clearly shown.
- [ ] No sensitive production sample data is present.
- [ ] Diagram and data dictionary tell the same story.
