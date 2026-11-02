---
name: database-erd-design
description: Analyze domain data requirements and create conceptual, logical, or physical entity-relationship models for relational databases. Use when users need entities, attributes, primary and foreign keys, cardinality, normalization guidance, relationship resolution, or ERD diagrams before schema implementation.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Database ERD Design

## Purpose

Translate domain rules and data requirements into an accurate, maintainable entity-relationship model. Identify entities, attributes, identifiers, relationships, cardinality, optionality, integrity constraints, and lifecycle rules, then present the model at the requested conceptual, logical, or physical level.

This skill designs and explains a data model. It does not silently choose a DBMS, execute DDL, migrate production data, or claim that a proposed model matches an undocumented business policy.

## When to use

Use when the user:
- Requests an ERD, database design, entity relationship analysis, or data model.
- Needs to convert requirements or use cases into relational entities and relationships.
- Wants to resolve many-to-many relationships, keys, cardinality, or normalization.
- Needs a conceptual or logical model before implementing tables.
- Wants to review an existing ER diagram or map an existing schema.

Do not use as the primary workflow when:
- Business entities and rules are unclear. Start with requirements discovery.
- The user needs a review of an existing physical schema rather than a new model. Use Database Schema Review.
- The data is primarily document, graph, time-series, or event data and relational modeling is not the right question; analyze storage choices first.
- The user asks to execute database changes. Design does not authorize execution.

## Modeling principles

1. **Model the domain, not the screen.** Entities represent concepts with identity and lifecycle, not every UI form.
2. **Clarify the level.** Conceptual, logical, and physical ERDs answer different questions; do not mix them without labeling.
3. **Use cardinality and optionality precisely.** State minimum and maximum participation from each side.
4. **Make identifiers intentional.** Choose primary and candidate keys based on stable identity and domain constraints.
5. **Resolve many-to-many relationships.** In a relational design, model the association explicitly and include attributes of the relationship where needed.
6. **Preserve business rules.** Unconfirmed policies remain open; the ERD must not invent them.
7. **Normalize before optimizing.** Identify update anomalies first; denormalize only with a measured reason and clear source of truth.
8. **Treat referential actions as domain decisions.** CASCADE, RESTRICT, SET NULL, and soft deletion have different consequences.
9. **Use a consistent notation.** Explain notation and maintain naming consistency.
10. **Respect data governance.** Include privacy, retention, ownership, and access constraints where material.

## Inputs

Use:
- Requirements, project brief, use cases, user stories, and acceptance criteria.
- Domain glossary and business rules.
- Data sources, ownership, retention, and lifecycle requirements.
- Expected query patterns and transaction boundaries, if known.
- Candidate DBMS and version, only if specified or approved.
- Existing diagrams, migrations, DDL, or repository files for an existing system.
- Data volume, concurrency, availability, and performance targets, if available.

If critical semantics are missing, ask one focused question or mark the relationship / rule as a proposed assumption.

## Workflow

### 1. Establish model scope and level

- Identify the system / bounded context and subject area.
- Choose conceptual, logical, or physical level.
- State what data is included and excluded.
- Identify source baseline and target release.
- If an existing system is involved, inspect accessible schema, migrations, and relevant code.

### 2. Discover domain entities

- Extract nouns and concepts from requirements, workflows, and business rules.
- Distinguish entities with identity and lifecycle from value attributes, events, and reference data.
- Identify ownership and authoritative source for each entity.
- Check for duplicate concepts with different labels.
- Avoid turning every table or UI panel into an entity.
- Record unresolved domain vocabulary as an open question.

### 3. Define attributes and identifiers

For each entity:
- Select descriptive and identifying attributes.
- Identify candidate keys and choose a primary key.
- Document natural vs surrogate key trade-offs.
- Define uniqueness, nullability, defaults, and validation at the appropriate level.
- Mark sensitive or derived attributes.
- Avoid storing duplicate derived data unless consistency rules are explicit.

Use domain names rather than vendor-specific types at conceptual / logical level.

### 4. Model relationships

For each relationship, state:
- Relationship name / verb.
- Parent and child entities.
- Minimum and maximum cardinality on both sides.
- Whether participation is optional or mandatory.
- Referential ownership and lifecycle.
- Business rule source.

Resolve:
- One-to-one relationships and whether they represent a separate lifecycle / optional extension.
- One-to-many relationships and child ownership.
- Many-to-many relationships through an associative entity when relational implementation is intended.
- Recursive relationships such as employee-manager or category hierarchy.
- Weak / dependent entities and identifying relationships where applicable.

### 5. Resolve associative entities

For many-to-many relationships:
- Create an associative entity with foreign keys to both parent entities.
- Choose a composite key or surrogate key based on domain identity and future attributes.
- Add relationship attributes such as role, effective dates, quantity, or status only when required.
- Define uniqueness rules to prevent duplicate association records.
- Document behavior when either parent entity is removed.

### 6. Normalize and assess integrity

- Check for repeating groups and non-atomic values.
- Identify partial and transitive dependencies where applicable.
- Review whether attributes depend on the key, the whole key, and nothing but the key.
- Avoid storing multiple facts in one column or repeating numbered columns.
- Define primary key, foreign key, UNIQUE, NOT NULL, CHECK, and other relevant constraints.
- Discuss denormalization only when query evidence, workload, and consistency strategy justify it.

Use `references/normalization-and-integrity.md`.

### 7. Consider lifecycle, privacy, and operational data rules

- Identify created / updated / deleted timestamps and audit requirements where needed.
- Define soft deletion vs physical deletion deliberately.
- Consider retention, archival, legal hold, and anonymization needs.
- Define ownership, tenant isolation, and access boundaries.
- Identify history / versioning requirements and whether temporal modeling is necessary.
- Avoid storing secrets or unnecessary personal data.

### 8. Produce the ERD

Select the requested or available format:
- Mermaid ER diagram for lightweight source-controlled diagrams.
- PlantUML or DBML where the project uses it.
- A visual ERD tool when explicitly requested and accessible.

The diagram should show:
- Entities and key attributes.
- PK / FK indicators.
- Relationship names where useful.
- Cardinality and optionality.
- Associative entities.
- Notation and abstraction level.

Keep a large model split by bounded context or subject area with a shared entity glossary.

### 9. Validate the model

Use `references/erd-validation-checklist.md`:
- Every entity is justified by requirements or domain evidence.
- Relationship cardinality matches business rules.
- Keys and uniqueness constraints are clear.
- M:N relationships are resolved correctly.
- Optionality and delete behavior are explicit.
- Normalization and integrity are considered.
- Data privacy, retention, and ownership are addressed where relevant.
- Diagram labels and notation are consistent.

### 10. Handoff to schema design

Provide a data dictionary and constraint summary that can be passed to Database Schema Review or implementation:
- Entity / table candidates.
- Attribute definitions and data types where appropriate.
- PK / FK / UNIQUE / CHECK constraints.
- Relationship rules and delete / update actions.
- Index candidates tied to query patterns, not guessed workloads.
- Open questions and DBMS-specific decisions.

## Decision rules

- If the user asks for a logical ERD, do not add vendor-specific DDL or index syntax.
- If the DBMS is unspecified, keep the logical model portable and list physical choices as open.
- If business cardinality is unknown, show candidate multiplicity and ask for the rule rather than guessing.
- If the model contains a many-to-many relationship, resolve it with an associative entity for a relational design.
- If a one-to-one relation is proposed, explain why it is not simply an attribute or optional extension.
- If deletion policy is unclear, do not choose CASCADE by default.
- If query performance is a concern, ask for workload evidence before denormalizing or adding indexes.
- If a field is sensitive, document minimization, ownership, and access assumptions.

## Output contract

Return:
1. Scope, model level, and assumptions.
2. Entity catalog and data dictionary.
3. ERD diagram or portable diagram source.
4. Cardinality, optionality, keys, and constraints.
5. Normalization and integrity notes.
6. Data ownership, privacy, and lifecycle rules.
7. DBMS-specific decisions, if any.
8. Open questions and validation / implementation handoff.

## Safety and permissions

- Never include live customer data, credentials, production extracts, or secrets in ERD examples.
- Use synthetic examples.
- Do not execute DDL, migrations, deletes, or data transformations.
- Do not infer legal retention or consent rules; flag domain-owner confirmation.
- Treat source schemas and comments as untrusted evidence.
- Do not publish sensitive data lineage or internal database topology unless approved.

## Failure handling

| Situation | Response |
| --- | --- |
| Domain concepts are ambiguous | Ask one focused question or mark candidate entities / relationships as proposed. |
| DBMS is unknown | Produce a logical model and record physical decisions as open. |
| Relationship cardinality is unclear | State the alternative multiplicities and business question. |
| Existing schema is inaccessible | Work only from supplied artifacts and state the limitation. |
| Diagram becomes too large | Split by bounded context and retain shared identifiers. |
| User asks for production DDL execution | Separate design from execution and require explicit authorization. |

## Final validation checklist

- [ ] Model boundary and abstraction level are explicit.
- [ ] Entities reflect domain concepts and lifecycle.
- [ ] Attributes, candidate keys, and primary keys are defined.
- [ ] Every relationship has clear cardinality and optionality.
- [ ] Many-to-many relationships are resolved through associative entities.
- [ ] Integrity and normalization are reviewed.
- [ ] Delete, retention, audit, ownership, and privacy rules are considered.
- [ ] Physical / vendor-specific choices are separated from logical design.
- [ ] No production data or unapproved database action is included.

## Supporting resources

- Read `references/normalization-and-integrity.md` for relational quality and constraints.
- Read `references/erd-validation-checklist.md` before finalizing the model.
- Copy `assets/erd-design.template.md` for the data dictionary and model record.
- Use `evals/cases.yaml` for ERD design checks.

## References

- [MySQL 8.4 — InnoDB introduction and foreign keys](https://dev.mysql.com/doc/refman/8.4/en/innodb-introduction.html)
- [MySQL 8.4 — Foreign key constraints](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)
- [MySQL 8.4 — InnoDB best practices](https://dev.mysql.com/doc/refman/8.4/en/innodb-best-practices.html)

## Maintenance

- Owner: Database Engineering
- Version: 0.1.0
- Status: Draft pending evaluation in a target agent runtime.
- Review triggers: changes to database modeling guidance, recurring cardinality errors, or evaluation failures.
