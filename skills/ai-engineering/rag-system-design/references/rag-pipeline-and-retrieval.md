# RAG Pipeline and Retrieval Design

## Lifecycle stages
1. Source discovery and authorization.
2. Fetch, parse, normalize, and validate.
3. Split or preserve semantic document structure.
4. Enrich metadata and retain source identity / version.
5. Embed and index with lexical or structured representations as appropriate.
6. Retrieve candidate passages using permission-aware filters.
7. Rerank, deduplicate, and assemble bounded context.
8. Generate an answer with evidence references.
9. Evaluate and monitor the pipeline.
10. Update, re-index, expire, and delete derived content.

Track ingestion failures separately from retrieval misses. A document that failed to parse is not evidence that the corpus does not contain the answer.

## Chunking
Choose boundaries based on source structure:
- Headings and section hierarchy for prose and manuals.
- Function, class, or symbol boundaries for code.
- Rows, headers, and captions for tables.
- Page, slide, timestamp, or region references for scanned / visual sources.
- Parent-child chunk links when a small retrieval unit needs larger context.

Measure the effect of chunk size and overlap. Large chunks may dilute matching; tiny chunks may lose context. Do not copy defaults from a provider without evaluation.

## Retrieval strategies
- **Lexical:** precise identifiers, names, error strings, and exact terms.
- **Dense / semantic:** paraphrases and conceptually related queries.
- **Hybrid:** combine lexical and semantic candidates when both matter.
- **Metadata filters:** constrain by tenant, permission, source type, status, date, or product version.
- **Structured query:** use an authoritative database or API for structured facts.
- **Reranking:** re-order candidates using a more expensive relevance model or task-aware scorer.

The best strategy depends on actual query / corpus distribution. Compare recall, precision, relevance, answer quality, and latency.

## Context assembly
- Remove duplicate or near-duplicate passages.
- Preserve document, section, page, and version provenance.
- Order evidence to support the requested answer.
- Stay within a measured context budget.
- Clearly delimit evidence as source material, not executable instructions.
- Include contradictory evidence when it materially affects the result.
- Avoid adding irrelevant passages simply to fill a top-k quota.

## Lifecycle and freshness
Use stable source identifiers and document versions. Define incremental indexing, deletion propagation, reprocessing after parser / embedding changes, rollback, backfill, and stale-index monitoring. Treat eventual consistency explicitly: a source deletion may not immediately remove every derived copy.
