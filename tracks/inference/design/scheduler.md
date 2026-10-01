# Scheduling, preemption, and cancellation

[Documentation index](../../../README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Task index](../tasks/README.md)

Status: planned system design; named source paths are reserved in the code map and will be created during implementation.

## Requirements

| ID | Requirement | Goal / evidence |
|---|---|---|
| <a id="sch-1"></a>SCH-1 | Explicit lifecycle and deterministic CPU execution model | [G1](../../../PROJECT_PLAN.md#g1); hand-traced state fixtures |
| <a id="sch-2"></a>SCH-2 | Static/continuous scheduling under compute and memory budgets | [G1](../../../PROJECT_PLAN.md#g1)/[G2](../../../PROJECT_PLAN.md#g2); matched arrival workloads |
| <a id="sch-3"></a>SCH-3 | Chunked prefill and recompute preemption preserve sequence semantics | [G1](../../../PROJECT_PLAN.md#g1); transformation oracles |
| <a id="sch-4"></a>SCH-4 | Cancellation, bounds and aging avoid resource leaks and starvation | [G1](../../../PROJECT_PLAN.md#g1)/[G3](../../../PROJECT_PLAN.md#g3); adversarial lifecycle/fairness fixtures |

## State and control ownership

The runtime coordinator owns requests and applies transitions. Scheduling policy reads state and produces a StepPlan: selected token ranges, prefill/decode work, requested reservations, and proposed preemption actions. A policy must not execute kernels or free pages while selecting candidates.

Logical lifecycle: waiting → admitted/active → finished, cancelled, or failed. Active requests may be partly prefilling, decoding, or waiting to recompute. In-flight work is a lease/completion concern, not permission to overwrite terminal output status. Exact enum names are a contract-task detail; these behaviors are approved requirements.

Track prompt length, computed KV prefix length, already sampled/emitted output, scheduled/completed token counts, wait age, cancellation/deadline intent, page ownership, and execution completion. These distinguish generated output from work that has merely been proposed or enqueued.

## Iteration transaction

1. Drain request/cancel/completion events at a defined boundary; establish a stable candidate snapshot.
2. Propose work within token and memory limits, accounting for prefix reuse and valid positions.
3. Reserve pages/COW and prepare metadata. If capacity is insufficient, leave rejected work consistent; apply a safe recompute-preemption plan or defer admission.
4. Execute at most one step in flight in the baseline. Retain all resources referenced by the step.
5. On successful completion, reconcile cancellation/deadline intents received while work was in flight before publishing output. Commit eligible progress/cache pages and dispatch content only for requests still allowed to emit.
6. Release finished/cancelled state after safe completion; queue any remaining continuation without re-emission.

This ordering is the baseline transaction boundary. Exact asynchronous APIs and fatal-device recovery are OQ-12; a task cannot treat an exception as proof that the GPU has stopped using memory.

## Batching and fairness

Start with static batches, then continuous iteration-level admission/backfill. The token budget is work per iteration, not output length or memory capacity; report each separately. Long prefill must be chunkable so it does not monopolize decode service. Compute and memory pressure can bind at different times.

Queue bounds, idempotent cancellation, and an aging/starvation safeguard precede optional LPM ordering. FCFS/decode-sensitive packing, queue thresholds, chunk sizes, victim policy and aging bounds are proposed implementation choices, explicitly unresolved in OQ-04. Implement one documented baseline before sweeping parameters; do not silently select an exotic policy.

## Preemption and edge cases

Recompute preemption discards eligible active KV ownership and later rebuilds from the prompt plus committed generated IDs. It preserves the output prefix and RNG progression; earlier tokens are neither re-sampled nor re-emitted. Swapping is a later offload comparison, not required for December preemption.

Required cases: arrival during an iteration; zero usable capacity; final partial prefill chunk; full cache hit requiring final logits; cancellation before reservation, after launch and after completion; duplicate cancel; request expiry; preempting a shared prefix; no progress under a too-small budget; starvation risk under repeated short arrivals.

## Simulation and validation

Use a virtual clock and a logical FakeExecutor to test ordering and accounting deterministically. A discrete-event model may estimate scheduling behavior. The local HTTP inference simulator is a separate platform dependency; neither simulator's wall-clock throughput is GPU evidence.

[Scheduler tasks](../tasks/scheduler.md) specify the sequence and cases. Numerical acceptance is in [correctness](../engineering/correctness.md); measurement is in [measurement](../engineering/measurement.md). Accept only when random/adversarial lifecycle transitions conserve resources, chunk/recompute preserve outputs under the numerical contract, and experiments report TTFT/ITL versus recomputation and wait-time fairness. A faster average cannot excuse a leaking or starving request.
