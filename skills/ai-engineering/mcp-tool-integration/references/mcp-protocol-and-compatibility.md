# MCP Protocol and Compatibility

## Protocol surface
MCP implementations commonly involve:
- **Base protocol:** structured messages and request / response patterns.
- **Tools:** operations an AI application may invoke.
- **Resources:** data exposed by a server.
- **Prompts:** reusable prompt templates or workflows.
- **Client features:** capabilities such as elicitation or sampling when supported.
- **Transport:** delivery mechanism for messages and connection lifecycle.
- **Authorization:** transport- and deployment-specific access control.

The specification evolves. Record the exact dated protocol version and consult its normative requirements. Do not assume an older initialization handshake, session behavior, capability discovery, or task model remains identical in newer revisions.

## Version pinning
Record:
- MCP spec version.
- Client and server implementation versions.
- SDK / library and runtime versions.
- Supported optional capabilities and extensions.
- Transport and authentication mode.
- Required compatibility range and upgrade owner.

Upgrade by checking breaking changes, conformance requirements, schema behavior, authorization, lifecycle, and interoperability tests. Do not infer conformance from package version alone.

## Tool schema design
- Use stable names that describe a narrow operation.
- Describe intended use and out-of-scope behavior.
- Validate types, ranges, lengths, enums, object structure, and semantic constraints.
- Define structured outputs and predictable error states.
- Bound output size and execution time.
- Include side-effect information for client presentation and policy decisions.
- Review schema changes as security-relevant changes.

## Transport selection
Choose transport based on deployment, trust, and operational needs. Local stdio integration executes a process under the host's security boundary; remote HTTP integration introduces network, TLS, origin, authentication, and token-scope requirements. Validate behavior against the pinned specification rather than copying transport assumptions from another revision.

## Interoperability tests
Test compatible and incompatible versions, capability discovery, missing optional features, malformed messages, invalid schemas, cancellation, disconnect, timeout, authentication denial, and server restart. Record exact client / server versions and transcripts with secrets redacted.
