# Inference & Serving

[LLM Systems Lab](../../README.md) · [Umbrella scope](../../PROJECT_PLAN.md) · [Shared roadmap](../../docs/execution/roadmap.md)

Status: runtime/platform implementation remains planned. Start [FND-01](tasks/model.md#fnd-01), then follow existing dependencies. The planned inferstack Python namespace remains an internal component name; the umbrella is LLM Systems Lab.

## What this track owns

Build the correct dense runtime, paged KV, scheduler/chunking/preemption, both hash/radix caches, GPU backend, Triton/CUDA kernel and graphs. Operate vLLM/SGLang, investigate production source (deeper SGLang), build Go routing policy, operate Kubernetes/gateway/replicas, and complete the original advanced labs and routing study.

No original inference, PF, advanced or release requirement is removed. The [baseline scope ledger](../../docs/archive/scope-map.md) remains mapped. Application/training ownership moves to agents; standalone performance replay stays here.

## Reading path

This folder now owns the full inference documentation: `ARCHITECTURE.md`, `design/`, `tasks/`, `curriculum/`, `engineering/` and `CAPSTONE.md`. Shared procedures, budget and cross-track contracts remain in `docs/`. Read [the handoff guide](../../docs/HANDOFF.md) when starting or resuming implementation.

| Need | Document |
|---|---|
| System/contracts | [Architecture](ARCHITECTURE.md) |
| Next increment | [Task index](tasks/README.md) |
| Current lesson | [Curriculum entrance](../../teaching/CURRICULUM.md) → this track’s `curriculum/` guide |
| Planned source responsibilities | [Code map](../../docs/system/code-map.md) |
| Measurement/causal replay | [Measurement contract](engineering/measurement.md) |
| Final experiment | [Routing capstone](CAPSTONE.md) |

A scheduler task needs its task brief, scheduler design and runtime lesson, not the entire agent curriculum.

## Independent execution

Inference environments do not depend on agent_lab. BEN-04 consumes supplied self-contained versioned session fixtures; live agent exports are optional. Quantization has its own frozen quality set. The capstone retains the 36-run routing study; the original live-agent quality check is required under agent evaluation and can be linked as a separate report.

The original B2 training bridge remains independently completable through the [canonical four-hour capsule](../agents/CURRICULUM.md#module-b2), without waiting for full SFT/RL. Canonical attention/cache lessons also support agent learners without requiring this engine implementation. [Track boundary](../../docs/system/track-contracts.md#track-boundary)

## First increment

[FND-01 startup sequence](tasks/model.md#fnd-01-startup-sequence) specifies the first CPU contract slice, teaching trace and independent checks. Future source remains in the approved `src/inferstack/`, `routing/` and `deploy/` boundaries; moving documentation does not change those package boundaries.
