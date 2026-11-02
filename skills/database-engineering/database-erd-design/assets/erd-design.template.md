# Entity-Relationship Design — [Domain / System]

> **Status:** Proposed  
> **Model level:** Conceptual / Logical / Physical  
> **Version:** 0.1  
> **Date:** YYYY-MM-DD  
> **Target DBMS / version:** [Known / TBD]  
> **Source baseline:** [Requirements / use cases / commit / TBD]

## 1. Scope and assumptions

**Subject / boundary:** [Domain or bounded context]

**Included:** [Data concepts]

**Excluded:** [Out-of-scope concepts]

**Assumptions and open rules:** [Clearly label each]

## 2. Entity catalog

| Entity | Purpose / business meaning | Owner / source of truth | Lifecycle | Sensitivity |
| --- | --- | --- | --- | --- |
| [Entity] | [Definition] | [System / role] | [State changes] | [Classification / TBD] |

## 3. Attribute dictionary

| Entity | Attribute | Meaning | Key role | Type / domain | Nullability | Constraints |
| --- | --- | --- | --- | --- | --- | --- |
| [Entity] | [Attribute] | [Definition] | PK / FK / UK / — | [Logical type] | Required / Optional | [Rule] |

## 4. Relationship catalog

| Relationship | From | To | Cardinality | Optionality | Business rule / source |
| --- | --- | --- | --- | --- | --- |
| [Verb] | [Entity A] | [Entity B] | [1:N / 0..1 / etc.] | [Mandatory / optional] | [Evidence] |

## 5. ERD diagram

[Insert Mermaid / PlantUML / DBML / visual ERD source. Identify the notation and model level.]

## 6. Associative entities

| Associative entity | Parent references | Key strategy | Relationship attributes | Uniqueness rule |
| --- | --- | --- | --- | --- |
| [Entity] | [FKs] | [Composite / surrogate] | [Attributes] | [Constraint] |

## 7. Integrity and normalization

- Primary / candidate keys: [Summary]
- Foreign keys: [Summary]
- UNIQUE / NOT NULL / CHECK constraints: [Summary]
- Normalization review: [1NF / 2NF / 3NF considerations]
- Denormalization decisions and evidence: [None / details]

## 8. Lifecycle, privacy, and operations

[Audit, history, retention, deletion, anonymization, tenant boundaries, indexing candidates, query patterns.]

## 9. Open questions and decisions

| ID | Question / decision | Impact | Owner | Status |
| --- | --- | --- | --- | --- |
| Q-001 | [Question] | [Impact] | [Role / TBD] | Open |

## 10. Handoff

[DBMS-specific DDL needs, migration / review tasks, tests, and acceptance checks.]

> This is a proposed model. It does not authorize DDL execution, data migration, or production changes.
