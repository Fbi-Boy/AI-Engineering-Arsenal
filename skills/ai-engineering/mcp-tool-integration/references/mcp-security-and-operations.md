# MCP Security and Operations

## Authorization and credentials
- Apply least privilege for each server and tool.
- Use narrow scopes and separate credentials between servers.
- Validate token audience and scope at the MCP server and downstream resource.
- Do not forward client tokens blindly to another API.
- Store access and refresh credentials in approved secure storage.
- Redact tokens and sensitive arguments from logs.
- Use the authorization flow required by the pinned transport / specification.

## Consent and side effects
Before connecting an untrusted local server, show its source, executable, exact command, arguments, and permissions. Obtain explicit consent before launch. For sensitive tool calls, display the exact target and relevant arguments and require approval. Approval does not replace server-side authorization.

## Schema and result trust
- Inspect tool descriptions, input / output schemas, annotations, and changes.
- Treat descriptions as potential prompt-injection inputs.
- Validate tool arguments before execution.
- Validate and sanitize tool results before returning them to a model.
- Do not allow returned text to change trusted instructions, access policy, or approval state.
- Validate URLs, file paths, identifiers, and shell-sensitive input at the application boundary.

## Local server isolation
Constrain filesystem paths, network access, process identity, environment variables, child processes, and resource limits. Do not run a local server with the user's entire host authority by default.

## Remote server operations
Use TLS, validate origins and tokens, enforce rate limits, bound output, monitor failures, and document data retention. Keep health, audit, and user-data paths separate where possible.

## Incident response
If a tool is compromised or a credential leaked, disable / revoke the affected integration, invalidate credentials through the owner, preserve sanitized audit evidence, review schema changes and downstream calls, and re-enable only after an authorized security review.
