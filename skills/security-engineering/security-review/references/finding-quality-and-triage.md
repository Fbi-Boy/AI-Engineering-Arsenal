# Finding Quality and Triage

## A finding must be actionable
A useful finding explains:
1. What is wrong and where.
2. Which input, identity, or state can reach it.
3. What preconditions are required.
4. How the behavior can be triggered.
5. Which security property or asset is affected.
6. Why the severity is appropriate.
7. How to remediate and verify the correction.

Avoid vague statements such as "security could be improved" without a concrete path.

## Severity dimensions
Consider:
- Impact: confidentiality, integrity, availability, privilege, financial, or safety effect.
- Exploitability: complexity, required access, user interaction, and reliability.
- Exposure: internet-facing, authenticated-only, internal, or build-time.
- Reachability: whether the relevant path is active and attacker controlled.
- Compensating controls: rate limits, segmentation, approval gates, monitoring, or other verified mitigations.

Use the organization's policy when available. If no policy exists, use a provisional qualitative rating and state that it is not a formal risk acceptance.

## Evidence confidence
- **Confirmed:** code / configuration and reachable path support the issue.
- **Likely:** strong indicators exist but runtime or deployment evidence is missing.
- **Needs validation:** plausible concern requiring additional context.
- **False positive:** evidence disproves the concern; document why.

## Triage guidance
- Consolidate duplicate findings with the same root cause.
- Separate distinct attack paths even when they share a vulnerable helper.
- Prioritize exploitable paths that cross trust boundaries or affect high-value assets.
- Do not lower severity just because a patch is small.
- Do not raise severity based only on a tool's default label.
- Re-review the corrected path and add a regression test where practical.
- Record accepted residual risk with its authorized owner and expiry / revisit condition.
