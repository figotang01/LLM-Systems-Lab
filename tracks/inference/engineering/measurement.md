# Measurement and replay methodology

Supports [G2 — measurement](../../../PROJECT_PLAN.md#g2) and [G5 — reproducible conclusions](../../../PROJECT_PLAN.md#g5).

## Requirements

| ID | Requirement | Validation |
|---|---|---|
| <a id="meas-1"></a>MEAS-1 | Preserve event origin, timing/count semantics and all offered outcomes | Synthetic timing, overload and failure fixtures; explicit token versus chunk observations |
| <a id="meas-2"></a>MEAS-2 | Compare controlled configurations with raw evidence, provenance and uncertainty | Matched production baselines, same-engine ablations and reproducible run bundles |
| <a id="meas-3"></a>MEAS-3 | Distinguish replay modes and enforce declared causal dependencies | Parent-DAG, delay and failure fixtures; separate live task-quality evaluation |

### Timing and load

Record `scheduled_arrival`, `dispatch`, `first_content`, `last_content`, `finish`, error/cancel status, session/parent IDs, emitted token count and chunk events on a monotonic clock. Retain empty/metadata events for diagnosis but do not treat them as generated content.

| Metric | Definition / qualification |
|---|---|
| Dispatch lag | dispatch − scheduled arrival; a client bottleneck must be visible |
| Client TTFT | first content − dispatch; includes network/server queue/prefill |
| Offered-arrival TTFT | first content − scheduled arrival; report separately for open-loop tests |
| TPOT | (last token − first token)/(N−1), undefined for N<2; state timestamp/count source |
| Chunk latency | Gaps between content-bearing SSE chunks; **not automatically per-token ITL** |
| E2E | finish − dispatch; also retain arrival-to-finish when studying offered load |
| SLO goodput | Count of successful requests meeting ALL their individual thresholds / measured seconds |
| Attainment | SLO-successful requests / all offered requests; include failures/timeouts/rejections |
| Session goodput | Completed sessions satisfying the declared session contract / measured seconds |
| Cost | Total billed resources / successful output or sessions; distinguish steady-state and total experimental cost |

AIPerf distinguishes aggregate latency metrics and inter-chunk observations; match its exact definition/version when cross-checking. If the backend emits multi-token chunks, a client cannot reconstruct exact individual token times. Report approximate normalized latency with that limitation or instrument token events server-side. [AIPerf metrics](https://docs.nvidia.com/aiperf/reference/ai-perf-metrics-reference)

For example, a 95th-percentile TTFT below 1 s and a 95th-percentile TPOT below 50 ms do not establish that 95% of requests meet both. Define per-request thresholds first, then aggregate. A one-token response has no TPOT; use TTFT/E2E plus an explicit eligibility rule.

Open-loop arrivals must not wait for previous completions. If a concurrency/safety cap is reached, record offered requests and drops/delay rather than quietly becoming closed-loop. Closed-loop tests remain useful, but answer a different question. Use Little's law only for a stable interval with matching definitions of in-flight work, arrival/completion rate and latency.

### Three replay modes

| Mode | Timing and content | Valid use |
|---|---|---|
| **Fixed-arrival request replay** | Recorded complete prompts and intended timestamps; fresh outputs may differ | Server load/locality study; may violate original within-session dependencies, so no live session-latency claim |
| **Dependency-aware transcript replay** | Each child waits for required parents + recorded tool/think delay; recorded next prompt is preserved | Controlled session scheduling study, conditional on fixed transcript and tool behavior |
| **Live agent execution** | New outputs determine tool arguments, next prompts and branching | Task quality, real behavior and full end-to-end validation; less repeatable load |

`max_tokens` is normally a cap, not a length guarantee. `ignore_eos`/minimum-output settings are backend-specific, stop conditions may differ, and identical lengths do not reproduce content/control flow. Preserve exact rendered prompt/token identity when studying cache reuse; same messages can tokenize differently with another chat template. AIPerf's verbatim replay similarly does not automatically feed new responses into recorded subsequent prompts. [Replay behavior](https://docs.nvidia.com/aiperf/tutorials/datasets-inputs/inputs-json-replay)

### Experimental rigor

- Separate warm-cache, cold-cache and cold-start experiments. Reset caches between paired runs as declared; repeated transcripts can create artificial reuse.
- Freeze model/tokenizer/template/precision/context/output settings, total available memory, topology and offered workload. Use same-engine ablations for causal mechanism claims.
- Start with three pilot repetitions; report variability. More repetitions are required when uncertainty is material. Three observations do not magically yield precise confidence intervals.
- Bootstrap whole sessions or runs where observations are dependent; do not pretend tokens within one session are independent samples. Do not average p99s into a global p99.
- With only 100 observations, p99 depends on about one upper-tail observation. Choose duration/sample count for the tail claim; with small task sets report broad uncertainty, not tiny accuracy deltas.
- Randomize or interleave configuration order; record throttling, warmup, cache state and co-tenancy. Separate profiler overhead from headline results.
- Hold out RAG/agent tasks from tuning and quantization calibration. Performance replay output is not a quality evaluation.
- Freeze one primary hypothesis and one main metric; add a small interaction test where mechanisms interact. Do not run every feature combination.

## Interfaces and ownership

The client records RequestObservation; server execution instrumentation emits ServingEvent. Retain clock domain and origin alongside timestamps. Latency calculations subtract timestamps from the same monotonic clock; trace correlation across processes is not permission to subtract arbitrary raw monotonic values.

ArrivalSchedule owns intended open-loop arrival independently of request completion. A transport concurrency cap records dropped/delayed offers explicitly. The event parser retains content/metadata/error/finish distinctions; metric aggregation never infers exact token timestamps from multi-token chunks.

SessionTrace capture/export belongs to the agent track; replay eligibility and standalone supplied fixtures belong to inference bench. Both use the [track contract](../../../docs/system/track-contracts.md#track-boundary), without a mandatory application dependency. Validate parent existence, acyclic dependencies, required completions, and tool/think delays before dispatch. A parent failure has an explicit dependent-session outcome rather than quietly omitting its children from offered-work accounting. The concrete serialized trace contract is planned and must preserve fixture compatibility when optional compaction metadata is added.

For dependency-aware replay, report offered sessions, causally eligible model requests, dispatched requests, and blocked/skipped descendants separately. A child that never becomes eligible is not a request rejected by the model server. Its parent/session failure still belongs in session attainment and completion accounting. Fix these eligibility rules before comparing policies; reporting only successful sessions can hide a policy that drops its slowest work.

Prepared bundles use the existing starter utility; benchmark code writes observations and analysis to the supplied directory. Retain raw artifacts referenced by hashes, because the utility does not copy them automatically or discover complete GPU provenance.

## Acceptance and task connections

[BEN-01–BEN-04](../tasks/benchmark.md) implement event semantics, load, production baselines and replay. [APP-03](../../agents/ROADMAP.md#app-03) captures provenance/dependencies. [REL-02](../tasks/advanced-release.md#rel-02) consumes these contracts for the capstone. Report source/count provenance for every timing metric and explain any discrepancy against the pinned AIPerf/vLLM benchmark definitions.

## Distinguish the three replay purposes

This document owns fixed-arrival and dependency-aware **performance transcript replay**. Agent checkpoint recovery is execution resumption with side-effect reconciliation; training rollout reuse concerns behavior-policy likelihood and data provenance. Neither inherits a correctness claim from successful performance replay. Live task/quality and training statistics are owned by the [agent learning design](../../agents/LEARNING.md). Shared metric names must still retain their origin, clock domain and denominator.
