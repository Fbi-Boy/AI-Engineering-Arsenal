# Benchmarking and Load-Test Safety

## Experiment design
- Use a dedicated environment with production-like topology where feasible.
- Pin application and dependency versions.
- Record hardware / container limits and runtime configuration.
- Include warm-up, steady state, and cooldown when relevant.
- Repeat runs and report sample count and variability.
- Control background work, noisy neighbors, network, and cache state.
- Change one major variable at a time where possible.
- Verify output correctness, not only speed.
- Preserve exact commands and raw measurements safely.

## Load profiles
- **Baseline:** expected ordinary demand.
- **Load:** target operating volume.
- **Stress:** beyond expected capacity, in a controlled environment only.
- **Spike:** abrupt increase and recovery.
- **Soak:** long-duration accumulation and degradation.
- **Concurrency:** competing operations on shared resources.

Do not infer capacity from one request or one concurrency level.

## Stop conditions
Before testing, define maximum rate, concurrency, duration, resource use, error rate, and owner contact. Stop when target instability or shared-system impact appears.

## Production safety
Default to a dedicated performance environment. Production tests require explicit authorization, known blast radius, rate limits, monitoring, stop control, stakeholder notification, and a defined window. Do not run resource-exhaustion tests against production as an informal experiment.

## Evidence
Report environment differences, tool overhead, confidence, and untested scaling dimensions. Do not present local laptop benchmarks as production capacity claims.
