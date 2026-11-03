# Performance Measurement and Profiling

## Workload model
Describe user journeys, request / job mix, arrival rate, concurrency, burst behavior, payload and result sizes, read/write ratio, cache hit / miss, dependency topology, and runtime / host limits. A benchmark without workload context may be fast but irrelevant.

## Metrics
- **Latency:** p50, p95, p99, maximum where meaningful; separate success and failure paths.
- **Traffic / throughput:** requests, jobs, queries, or transactions per unit time.
- **Errors:** explicit failures, timeouts, partial failures, and incorrect outcomes.
- **Saturation:** CPU, memory, disk / network I/O, pools, queues, and quotas.
- **Cost:** compute time, storage, tokens, external calls, and infrastructure spend.

Use histograms or distributions for latency; averages can conceal tail behavior.

## Profiling by suspected bottleneck
- CPU: sampling profiles, flame graphs, hot paths, algorithmic complexity.
- Memory: allocation profiles, heap snapshots, leaks, retention.
- I/O: disk / network wait, filesystem, database round trips.
- Database: query plans, index use, lock waits, cardinality, N+1 patterns.
- Distributed requests: traces, span duration, queue time, dependency breakdown.
- Frontend: browser timeline, long tasks, rendering, assets, layout and script costs.

## Hypothesis workflow
1. State a falsifiable hypothesis.
2. Identify the metric and expected direction.
3. Capture a controlled baseline.
4. Change one material factor where feasible.
5. Re-run the same workload.
6. Compare distribution, errors, and resource effects.
7. Keep or revert according to evidence.

A faster component does not necessarily improve the end-to-end critical path. A cache can reduce compute while increasing memory, staleness, or invalidation risk.
