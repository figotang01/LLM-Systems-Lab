# Inference implementation task index

[Overview](../../../PROJECT_PLAN.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Curriculum](../../../teaching/CURRICULUM.md)

## Choose a track

[Inference FND-01](model.md#fnd-01) and [agent AGT-01](../../agents/ROADMAP.md#agt-01) can start independently. The full [agent roadmap](../../agents/ROADMAP.md) owns AGT-01–14; legacy APP/AG IDs are retained aliases there, not extra duplicated tasks. This table lists inference tasks only. Legacy APP/AG aliases remain in the agent roadmap and [coverage map](../../agents/COVERAGE.md#original-requirements-and-stable-aliases). The shared [handoff guide](../../../docs/HANDOFF.md) owns teaching/implementation procedure.

## How to implement the next task

1. Pick the relevant subsystem document below and read its linked design, shared correctness/measurement rules, and teaching brief.
2. Choose the first planned task in that subsystem whose dependencies have implementation evidence. Dependencies are canonical in task briefs, not inferred from the table order.
3. If prerequisites are incomplete, name the blocked task and implement the earliest ready prerequisite instead of guessing missing APIs. For example, “next scheduler task” currently selects SCH-01, but FND-01 must be completed first.
4. Use the change boundary as the primary owned files. Extend focused tests and wire completed dependency components when integration requires it; record those additional touches. Update a shared contract and its owning design together if required; do not silently add a subsystem or settle an unresolved design choice without recording the decision. Proposed defaults and decisions are in the open-question register.
5. Run the task's meaningful independent checks, preserve failures, and record evidence/ownership. Update the one task status to in progress/blocked/implemented and link evidence. Never mark a task implemented because placeholders import or empty tests collect.

All implementation tasks start **planned**. Existing starter tooling and lesson 00 are already delivered and listed in [validation](../../../docs/VALIDATION.md). Task acceptance is a future validation specification, not a report of checks run today.

The traceability chain is goal in the overview → requirement ID in canonical design → task below → its acceptance/evidence → named milestone. Each planned code-map entry links back to its owning task. Dates/hours live only in the roadmap. New agent work is explicitly funded by the added shared-roadmap range; legacy aliases do not add charges.

## Task directory

| Task | Engineering increment | Milestone |
|---|---|---|
| [FND-01](model.md#fnd-01) | Environment and minimal logical contracts | CP1 |
| [FND-02](model.md#fnd-02) | Numerical diagnostic and independent oracle | CP1 |
| [FND-03](model.md#fnd-03) | GPU execution foundations | CP2 |
| [FND-04](model.md#fnd-04) | Kubernetes foundations | December |
| [MOD-01](model.md#mod-01) | Dense model operations and loader boundary | CP2; early reference/ownership work |
| [MOD-02](model.md#mod-02) | Contiguous KV prefill and incremental decode | CP2; early reference/ownership work |
| [MOD-03](model.md#mod-03) | Memory accounting | CP2; early reference/ownership work |
| [MOD-04](model.md#mod-04) | Sampling and determinism exercise | CP2 |
| [KV-01](memory-cache.md#kv-01) | Pool ownership and transactional reservation | CP2; early reference/ownership work |
| [KV-02](memory-cache.md#kv-02) | Page tables, writes and shared-tail copy-on-write | CP2; early reference/ownership work |
| [KV-03](memory-cache.md#kv-03) | Block-hash prefix index | CP2 |
| [KV-04](memory-cache.md#kv-04) | Radix index and controlled comparison | CP2 |
| [SCH-01](scheduler.md#sch-01) | Request lifecycle and virtual execution fixtures | CP2 |
| [SCH-02](scheduler.md#sch-02) | Static and continuous batching | CP2 |
| [SCH-03](scheduler.md#sch-03) | Chunked prefill | CP2 |
| [SCH-04](scheduler.md#sch-04) | Recompute preemption and safe cancellation | CP2 |
| [SCH-05](scheduler.md#sch-05) | Cache-aware scheduling with fairness guard | CP2 |
| [GPU-01](gpu-serving.md#gpu-01) | Online softmax and direct paged backend | CP2 |
| [GPU-02](gpu-serving.md#gpu-02) | Triton normalization and CUDA C++ modification | CP2 |
| [GPU-03](gpu-serving.md#gpu-03) | Graph buffers, buckets and bounded overlap | CP2 |
| [SRV-01](gpu-serving.md#srv-01) | HTTP/SSE and cancellation integration | CP2 |
| [GPU-04](gpu-serving.md#gpu-04) | End-to-end profile and baseline gap | CP2 |
| [SRV-02](gpu-serving.md#srv-02) | Metrics, observability and backend contract | CP2 |
| [BEN-01](benchmark.md#ben-01) | Streaming observations and metric definitions | CP1 |
| [BEN-02](benchmark.md#ben-02) | Open-loop and closed-loop load | CP1 |
| [BEN-03](benchmark.md#ben-03) | Matched vLLM and SGLang baselines | CP1 |
| [BEN-04](benchmark.md#ben-04) | Dependency-aware and fixed-arrival replay | December |
| [PLT-01](platform.md#plt-01) | Local gateway and simulator deployment | December |
| [PLT-02](platform.md#plt-02) | Go locality/load scorer | December |
| [PLT-03](platform.md#plt-03) | Real GPU replicas and backend contracts | CP3 |
| [PLT-04](platform.md#plt-04) | KV tiers, two adapters and cold start | CP3 |
| [PLT-05](platform.md#plt-05) | Scaling, overload and failure diagnosis | CP3 |
| [PF-1](framework.md#pf-1) | SGLang source and runtime-state walkthrough | December |
| [PF-2](framework.md#pf-2) | vLLM V1 architectural comparison | December |
| [PF-3](framework.md#pf-3) | Bounded SGLang change and regression | December |
| [PF-4](framework.md#pf-4) | Technical defense and interview practice | December |
| [ADV-01](advanced-release.md#adv-01) | Speculation verifier and supported proposer | Advanced labs |
| [ADV-02](advanced-release.md#adv-02) | Quantization with quality gates | Advanced labs |
| [ADV-03](advanced-release.md#adv-03) | Collectives, tensor and expert parallelism | Advanced labs |
| [ADV-04](advanced-release.md#adv-04) | Prefill/decode transfer and fair comparison | Advanced labs |
| [REL-01](advanced-release.md#rel-01) | Six bridge capsules and lifecycle breadth | Release |
| [REL-02](advanced-release.md#rel-02) | Capstone experiment and report | CP4 |
| [REL-03](advanced-release.md#rel-03) | Clean reproduction, regression policy and release | Release |

## General handoff boundary

The code map reserves names and responsibilities; source files will be created during their tasks. It defines no implemented or frozen signatures. Resolve exact interfaces during the owning first task. Keep CPU, GPU, production-engine and platform environments isolated; run paid/real-device checks only in the appropriate prepared environment. CPU fixture success never closes a GPU or operated-platform gate.
