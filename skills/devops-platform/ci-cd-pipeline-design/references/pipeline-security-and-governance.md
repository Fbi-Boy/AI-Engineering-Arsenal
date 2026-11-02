# Pipeline Security and Governance

## Workflow identity and permissions
- Set explicit minimum GITHUB_TOKEN or platform permissions.
- Give write permissions only to the job that requires them.
- Separate untrusted pull-request validation from release and deployment identities.
- Avoid privileged triggers that check out and execute attacker-controlled code.
- Use short-lived federated identities such as OIDC where supported and approved.

## Third-party actions and dependencies
- Prefer trusted official actions or reviewed reusable workflows.
- Pin actions to full-length commit SHAs or use an approved immutable workflow dependency lockfile.
- Review the action source, permissions, maintainer identity, and transitive behavior.
- Upgrade pins through a reviewed process; do not invent SHAs or pin to a fork without verification.
- Use lockfiles and integrity verification for application dependencies.

## Secrets
- Do not store secrets in repository source, workflow literals, command-line arguments, or logs.
- Use separate credentials per environment and narrow scopes.
- Do not expose privileged deployment secrets to pull-request jobs or untrusted forks.
- Masking is not a substitute for avoiding secret output.
- Rotate a compromised credential through the authorized secret owner; do not print it in a workflow log.

## Event payloads and shell safety
- Treat branch names, titles, labels, comments, paths, and other event fields as untrusted.
- Avoid direct expression interpolation into shell scripts.
- Pass values as environment variables and validate them before use.
- Do not use a privileged pull_request_target workflow to execute untrusted checked-out code.
- Validate file paths and artifact names before using them in commands.

## Environment protection
Use platform protection rules to:
- Limit which branches can deploy.
- Require designated reviewers for sensitive environments.
- Separate environment secrets.
- Prevent overlapping deploy jobs.
- Record deployment history and approvals.

## Supply-chain evidence
Where practical, produce an SBOM and build provenance. Provenance records how an artifact was produced; it does not by itself prove that the source code is secure or that the artifact is safe to deploy.

## Governance
Document workflow owners, required checks, approval authority, exception process, emergency path, and review frequency. Changes to permissions, secrets, or release triggers require focused review.
