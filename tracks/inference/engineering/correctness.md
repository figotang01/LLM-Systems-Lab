# Inference correctness and shared evidence principles

1. **Exact structural invariants:** blocks conserved, no negative refcounts, no double release/use-after-free, no cross-namespace reuse, correct page tails/positions/masks, eventual cleanup after abort or preemption.
2. **Numerical oracle:** tiny FP32 cases first; compare layer outputs and teacher-forced logits on identical input token sequences. Specify dtype-dependent absolute/relative tolerances from the actual backend, not a universal arbitrary threshold.
3. **Greedy smoke tests:** fixed model/backend/batch configuration with stable argmax margins. On divergence inspect logits and top-two margins; numeric drift can change an argmax near a tie. Never dismiss large systematic differences as “floating point.”
4. **Semantic transformations:** cache on/off, chunked/unchunked and recompute/resume use controlled fixtures and numerical comparisons. Randomized scheduler/cache tests must exercise state transitions, not only final text.
5. **Sampling/speculation:** test acceptance/residual math on exact small distributions and empirically across seeds, plus rollback/cache invariants. Equal distributions do not require identical random trajectories.
6. **Quantization:** tolerate intended numeric changes only with predeclared held-out task-quality criteria and uncertainty.

vLLM explicitly limits reproducibility guarantees to particular settings, hardware and versions; “identical greedy tokens across all kernels and batch sizes” is not a defensible universal gate. [Reproducibility documentation](https://docs.vllm.ai/en/latest/usage/reproducibility/)

## Evidence tiers

| Tier | Appropriate evidence | Does not establish |
|---|---|---|
| CPU logic | Fake executor, virtual clock, randomized allocator/scheduler/cache transitions | GPU performance or backend compatibility |
| Tiny numerical | Independent FP32 attention/model oracle; fixed positions and teacher-forced tokens | Universal greedy equality across kernels/hardware |
| GPU integration | Real paged reads, kernel/graph checks, dtype/shape suite with environment provenance | Multi-node production reliability |
| Transport/platform | Streams, disconnects, metrics and readiness tests; later physical replica runs | Real GPU results from configured simulator delays |
| Task quality | Held-out labeled tasks, evidence checks and inspected live trajectories | Agent success from fixed-transcript replay |

## Test ownership and failure policy

Fixtures must not repeat the same implementation mistake as the learner code. Prefer independently computed small expected values, hand-traced schedules, unrelated reference formulations, and state-machine invariants. Randomized tests should retain seeds and minimized failing sequences.

Every implementation task defines acceptance and expected artifact types. Bind tests to stable task/requirement IDs rather than copying specifications into several documents. Tests themselves are planned until executable assertions exist; placeholder filenames do not constitute coverage. A failed check remains recorded, not converted to passed because another environment succeeded.

Record exact model/template/code versions, dtype, hardware, tolerances and their justification. Diagnose systematic discrepancies before accepting tolerance changes. Fatal device errors require explicit safe-lifetime handling; do not assume a host exception synchronizes GPU work.

No mandatory benchmark speedup, fixed percentage of vLLM performance, or upstream merge. For regression performance gates, choose an effect-size threshold from pilots and require repeated confirmation; run GPU checks on demand rather than paid nightly defaults.

[Task index](../tasks/README.md) · [Measurement](measurement.md) · [Status](../../../docs/VALIDATION.md)

## Agent-specific validation owner

Independent oracles, honest evidence tiers and no invented performance apply to both tracks. Agent lifecycle/permission/memory invariants live in [runtime design](../../agents/RUNTIME.md#correctness-and-acceptance); task verifiers, masks/rewards, SFT/RL and held-out comparisons live in [learning design](../../agents/LEARNING.md). Keep those requirements canonical rather than treating inference numerical checks as an agent-quality gate.
