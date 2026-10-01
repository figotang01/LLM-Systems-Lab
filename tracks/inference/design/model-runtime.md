# Dense model execution and runtime coordination

[Documentation index](../../../README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Task index](../tasks/README.md)

Status: planned system design; named source paths are reserved in the code map and will be created during implementation.

## Requirements

| ID | Requirement | Goal / validation |
|---|---|---|
| <a id="model-1"></a>MODEL-1 | Implement one fixed dense Qwen3 revision with explicit dimensions, RoPE, GQA, QK norm, RMSNorm and SwiGLU | [G1](../../../PROJECT_PLAN.md#g1); per-layer independent reference |
| <a id="model-2"></a>MODEL-2 | Uncached, contiguous-cache and paged execution preserve intended positions/masks and teacher-forced logits within justified tolerance | [G1](../../../PROJECT_PLAN.md#g1); numerical contract |
| <a id="model-3"></a>MODEL-3 | Explain sampling and predict weight/KV/workspace memory separately | [G4](../../../PROJECT_PLAN.md#g4); exact small examples and measured allocation |
| <a id="run-1"></a>RUN-1 | Coordinator owns request progression, committed output and safe resource cleanup | [G1](../../../PROJECT_PLAN.md#g1); lifecycle/state tests |

## Responsibilities and interfaces

The supplied loader maps checkpoint names, tokenizer/chat template and config into ModelSpec and parameters. Learner model code owns the math and cache writes; it must not guess head dimension from hidden size when config supplies it. Restrict the initial path to supported dense attention; reject or explicitly classify hybrid/MLA/sliding-window configurations.

Model operations accept token positions and execution/cache metadata. Separate projection/normalization/MLP math from the attention backend. A readable uncached/contiguous implementation precedes the gathered paged reference. The executor runs a prepared step and reports completion; it cannot publish cache pages, cancel requests, or mutate queues on its own.

The coordinator translates validated requests into [scheduler state](scheduler.md), acquires memory, executes, and commits. Treat ModelSpec, GenerationRequest, RequestState, StepPlan, and StepResult as logical contracts until FND-01 locks minimal concrete types. No weight download is necessary for tiny synthetic parameter fixtures.

## Data and lifecycle

Trace five prompt tokens, then three incremental decode steps with explicit causal positions and GQA head mapping. Teacher-forced comparisons use identical input/output-token prefixes so sampling differences cannot hide model errors. The next sampled token is not yet necessarily represented in KV; retain separate counters for computed KV and emitted output.

Recompute reconstructs KV from the already committed prompt/output sequence. It must not re-sample or re-emit earlier tokens. A finishing/cancelled request can still hold an in-flight execution lease; terminal output status and physical reclamation are related but distinct events.

## Numerical and memory decisions

Use tiny FP32 references before lower-precision GPU tests. Diagnose masks, positions, normalization, dtype and tensor shape before blaming near-tie argmax drift. Greedy is the integration baseline; temperature/top-p and sampling/determinism remain learning exercises. Min-p and batch-invariant sampling references are retained for explanation; unsupported API controls are rejected rather than silently accepted.

For dense full attention, KV bytes = 2 × layers × KV heads × head dimension × bytes/element × cached tokens. Account for weights, workspace, activations, allocator reserve, and graph pools separately. MoE active parameters do not describe resident weight bytes. The approved tiny configuration example is 112 KiB/token; verify the actual pinned config before using it as a capacity prediction.

## Failure cases and trade-offs

- A loader mismatch is a model-identity/shape failure, not a reason to tolerate inaccurate logits.
- A shifted RoPE position can produce plausible text while violating correctness; test fixed tokens.
- Unsupported checkpoints fail early; architecture breadth is a spring bridge, not implicit model support.
- Gathered paged attention is an oracle/capacity path, not evidence of fast PagedAttention.
- Sampling distributions and greedy decisions have different validation rules. Follow [correctness](../engineering/correctness.md).

## Implementation and acceptance

[Foundation/model tasks](../tasks/model.md) build the numerical oracle, decoder path, contiguous cache, accounting, and sampling exercises. [Memory tasks](../tasks/memory-cache.md) connect paging; [GPU tasks](../tasks/gpu-serving.md) replace the reference attention path; [scheduler tasks](../tasks/scheduler.md) own lifecycle integration.

Accept when per-layer and teacher-forced checks pass on documented configurations, memory predictions explain observed allocation, unsupported model forms are explicit, and coordinator cleanup passes the lifecycle tests. Exact tolerance values and fatal GPU-context recovery remain OQ-03/OQ-12; no arbitrary universal bound is implied.
