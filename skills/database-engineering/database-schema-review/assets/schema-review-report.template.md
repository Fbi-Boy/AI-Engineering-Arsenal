# Database Schema Review — [Database / Change]

> **Status:** Review draft  
> **Date:** YYYY-MM-DD  
> **DBMS / version:** [Engine / version / unknown]  
> **Scope:** [Schema, tables, migrations, files inspected]  
> **Baseline:** [Commit / release / migration version]  
> **Reviewer:** [Role]

## 1. Executive summary

[Overall risk and recommended decision. State evidence limits.]

## 2. Inspection scope and evidence

| Artifact | What was inspected | Source / version | Limitation |
| --- | --- | --- | --- |
| [DDL / migration / model] | [Scope] | [Path / commit] | [Limitation] |

## 3. Findings by severity

| ID | Severity | Object / location | Evidence | Impact | Recommendation | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| DB-001 | High / Medium / Low / Info | [Table / column / migration] | [Observed fact] | [Consequence] | [Action] | Confirmed / Potential |

## 4. Integrity and domain rules

- Primary / candidate keys: [Assessment]
- Foreign keys and relationships: [Assessment]
- Unique / not-null / check constraints: [Assessment]
- Referential actions: [Assessment]
- Tenant / ownership boundaries: [Assessment]

## 5. Type and normalization review

[Precision, range, collation, temporal semantics, repeating groups, partial/transitive dependencies, snapshots, denormalization.]

## 6. Index and query review

| Query pattern | Current supporting index | Evidence / EXPLAIN | Finding | Recommendation |
| --- | --- | --- | --- | --- |
| [Filter / join / sort] | [Index / none] | [Plan / unavailable] | [Observation] | [Action] |

## 7. Security and data governance

[Privilege, sensitive columns, secrets, audit, encryption, retention, deletion, masking, backups.]

## 8. Migration and deployment risk

[Locking, backfill, compatibility, rollout order, backup / restore, rollback / forward fix, monitoring.]

## 9. Recommended actions

| Order | Action | Finding IDs | Owner / role | Verification |
| --- | --- | --- | --- | --- |
| 1 | [Action] | DB-001 | [Role / TBD] | [Evidence] |

## 10. Release recommendation

- **Block:** unresolved critical / high risk.
- **Fix before release:** material findings remain.
- **Accept with follow-up:** bounded lower-risk findings have owners.
- **Informational:** no release-blocking findings in the inspected scope.

**Recommendation and rationale:** [Text]

> This is a review of the stated artifacts and evidence only. No SQL, migration, or production database operation was executed.
