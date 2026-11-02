# Observability Evidence for Debugging

## Logs

Useful structured log attributes may include:
- Timestamp with timezone / clock source context.
- Service / component and version.
- Severity and event name.
- Trace / span / request correlation ID.
- Non-sensitive entity or operation identifier.
- Outcome, error category, and retry attempt number.

Avoid logging:
- Passwords, access tokens, API keys, session identifiers.
- Full payment / identity data.
- Large payloads containing personal or confidential information.
- Sensitive request headers or connection strings.

Redaction should occur before logs leave the trust boundary where possible.

## Metrics

Metrics help establish scope and timing:
- Request / job rate.
- Error rate by bounded error class.
- Latency distribution, not only averages.
- Queue depth and age of oldest message.
- Resource saturation (CPU, memory, connections).
- Retry / timeout / dead-letter counts.
- Business outcome counters where privacy and cardinality allow.

Avoid high-cardinality labels such as user IDs, email addresses, raw URLs with identifiers, or arbitrary exception messages.

## Distributed traces

A trace can show timing and dependency relationships across services. Use:
- Trace and span context propagation.
- Service / operation names.
- Dependency timing and status.
- Retry / timeout spans.
- Sampling awareness.

A missing span is not proof that a call did not happen; instrumentation and sampling affect visibility.

## Correlation

Use request / trace IDs to connect:
- Client interaction.
- API handler.
- Database operation where instrumented.
- Message publication / queue handling.
- Background job and external dependency.

Do not use a trace ID as an authorization credential or expose it as sensitive data. Treat it as diagnostic metadata.

## Time and clock assumptions

For distributed systems, confirm:
- Timezone in log rendering.
- Clock synchronization and skew.
- Event time vs processing time.
- Client vs server timestamp.
- Whether the failure is tied to daylight-saving transitions or local date boundaries.

Do not compare timestamps from different systems without understanding their clocks.

## Sources

- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [Google SRE Workbook — Troubleshooting](https://sre.google/workbook/troubleshooting/)
- [Google SRE — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
