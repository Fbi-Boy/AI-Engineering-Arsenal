# RAG Security and Evaluation

## Security controls
- Apply tenant and document authorization in the trusted retrieval service before returning passages.
- Never rely on the language model to enforce ACLs.
- Treat document text, OCR output, metadata, filenames, and search snippets as untrusted.
- Defend against indirect prompt injection by separating instructions from retrieved data and restricting tool authority.
- Prevent retrieval filters from being overwritten by user / model query parameters.
- Keep source URLs and citations subject to the same access checks as content.
- Redact secrets and personal data from traces, examples, and evaluation artifacts.
- Define retention and deletion for raw documents, chunks, embeddings, caches, and backups.

## Evaluation layers
### Ingestion quality
- Correct file extraction, structure preservation, metadata, version, and deletion behavior.
- Coverage of supported formats, languages, tables, images, and code.

### Retrieval quality
- Recall@k and precision@k against relevant labeled passages.
- Mean reciprocal rank or nDCG when rank ordering matters.
- Filter correctness and cross-tenant isolation.
- Coverage of exact identifiers, paraphrases, multi-hop queries, and unanswerable questions.

### Answer quality
- Correctness against authoritative references.
- Faithfulness / groundedness in retrieved context.
- Citation correctness and citation coverage.
- Completeness, relevance, uncertainty, and abstention behavior.
- Safe handling of conflicts, stale documents, and prompt injection.

## Evaluation hygiene
- Use real representative query distributions only where approved; otherwise use reviewed synthetic examples.
- Record dataset provenance, annotation instructions, reviewer agreement, and version.
- Calibrate automated / model graders against human-labeled examples.
- Inspect examples where retrieval and answer scores disagree.
- Test ACL negative cases explicitly; a fluent answer does not prove authorized retrieval.
- Keep model, prompt, index, embedding, chunking, and ranker versions with each result.

## Observability
Capture stage duration, candidate counts, filters, retrieval scores, token budget, model use, citation identifiers, and outcome signals without logging restricted text or credentials. Apply sampling, access control, and retention limits to traces.
