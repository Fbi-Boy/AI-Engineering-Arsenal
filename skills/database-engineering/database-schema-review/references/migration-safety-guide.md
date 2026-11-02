# Database Migration Safety Guide

## Classify the migration
- Additive: adds nullable columns, tables, or compatible indexes.
- Compatible transformation: data is backfilled or application behavior changes without immediate removal of old structures.
- Contracting: removes or renames old structures after all consumers have migrated.
- Destructive: drops, truncates, overwrites, or irreversibly transforms data.
- Data correction: changes existing values according to a rule that must be verified.

The same DDL may have different risk on different engines and versions.

## Expand-and-contract pattern

For a compatibility-sensitive change:
1. **Expand:** add the new structure without removing the old one.
2. Deploy code that can safely read / write the transition state.
3. **Backfill:** migrate existing data in bounded, observable batches.
4. Validate counts, constraints, and application behavior.
5. Switch readers and writers to the new structure.
6. Monitor for a defined period.
7. **Contract:** remove obsolete structures only after old code and consumers are gone.

Do not use this sequence blindly; transactional guarantees, replication, and application topology may change the safe order.

## Pre-deployment questions
- What is the table size and growth rate?
- Does the operation scan or rewrite the table?
- What lock level and duration should be expected on this engine/version?
- Can it run transactionally?
- Will replicas or CDC consumers lag?
- Can old and new application versions run simultaneously?
- Is the backfill restartable and idempotent?
- Is there a backup and restore point that has been tested?
- What is the rollback or forward-fix strategy?
- How will success and partial failure be detected?

## Backfill design
- Use bounded batches and checkpoints.
- Make the operation restartable.
- Avoid long transactions where they cause bloat, locks, or resource pressure.
- Record progress and failure counts.
- Validate the migrated values against explicit invariants.
- Prevent application writes from reintroducing inconsistent state during the backfill.

## Rollback discipline

Rollback may be impossible after data is transformed or dropped. Before describing a rollback:
- Verify whether old data still exists.
- Confirm that down migrations preserve information.
- Consider application-version compatibility.
- Test restore / replay procedures in a non-production environment.
- Document conditions that require a forward fix instead.

## Release gate

For high-risk migrations, require:
- Reviewed migration and SQL plan.
- Production-like rehearsal.
- Backup / restore evidence.
- Lock and duration estimate grounded in the target engine.
- Monitoring and abort criteria.
- Owner and communication / maintenance plan.

This checklist is a planning aid, not an instruction to execute a production migration.
