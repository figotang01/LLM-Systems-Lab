# LLM Systems Lab — curriculum entrance

[Overview](../PROJECT_PLAN.md) · [Documentation index](../README.md) · [Roadmap and hours](../docs/execution/roadmap.md) · [Teaching delivery contract](CONTRACT.md)

This is the shared navigation view. Inference topic guides and the sixteen-unit agent curriculum own teaching blueprints; task briefs own implementation steps/evidence. Only [lesson 00](slides/00-orientation.html) is delivered as HTML. The topic guides contain blueprints, not completed lessons or runnable exercises. Lesson 00 retains its original baseline calendar; the shared roadmap owns the historical 528-hour baseline and the expanded 808–928-hour estimate.

## Choose a teaching track

The original numbered modules remain traceable inside these guides. Their required content is preserved; the AT units add the full agent scope. Separate module directories will be created only when runnable exercises or HTML authoring need them.

| Guide | Modules |
|---|---|
| [Foundations and measurement](../tracks/inference/curriculum/foundations.md) | 00–03 |
| [Model, memory and scheduling](../tracks/inference/curriculum/runtime.md) | 04–08 |
| [Prefix caching](../tracks/inference/curriculum/prefix-caching.md) | 09–10 |
| [GPU execution and serving](../tracks/inference/curriculum/gpu-serving.md) | 11–13 |
| [Full agent curriculum](../tracks/agents/CURRICULUM.md) | AT-00–15, retained 14–15 application work, AG-1 and B2 |
| [Performance replay](../tracks/inference/curriculum/foundations.md#module-15-replay) | Original module-15 replay portion; inference owner |
| [Platform and routing](../tracks/inference/curriculum/platform.md) | 16–19 |
| [Production-framework development](../tracks/inference/curriculum/frameworks.md) | PF-1–PF-4 |
| [Advanced labs, bridges and capstone](../tracks/inference/curriculum/advanced.md) | 20–24, B1 and B3–B6; B2 links to the agent owner |

## Core modules

Inference 00–13 support fall engine learning and 16–17 the December gateway. Agent AT units run in parallel now; December targets working RAG and broad knowledge, with later implementation continuing through spring. Module 16 foundations are learned before deployment, not after every prior module. Original workload evaluation retains a January target under agent AGT-04; inference 18–19 platform completion targets January; 20–23 are February; 24 and bridges are March/April. Exact task prerequisites live in the task briefs. Existing 01–17 baseline allocations sum to 286; PF and AG remain separate additions.

| Module | Teaching scope | Allocation |
|---|---|---|
| [00](../tracks/inference/curriculum/foundations.md#module-00) | Project map and measurement foundations (delivered) | Delivered orientation; no additional learner budget |
| [01](../tracks/inference/curriculum/foundations.md#module-01) | Tensor and numerical diagnostic (package A) | 8 baseline h (A) |
| [02](../tracks/inference/curriculum/foundations.md#module-02) | GPU execution for a systems programmer (A + F) | 12 baseline h (A) |
| [03](../tracks/inference/curriculum/foundations.md#module-03) | Measuring a serving system (B) | 34 baseline h (B) |
| [04](../tracks/inference/curriculum/runtime.md#module-04) | A single-request dense runtime (D) | 30 baseline h (D) |
| [05](../tracks/inference/curriculum/runtime.md#module-05) | Memory accounting and cache lifetime (D) | 8 baseline h (D) |
| [06](../tracks/inference/curriculum/runtime.md#module-06) | Paged ownership, refcounts and copy-on-write (D) | 34 baseline h (D) |
| [07](../tracks/inference/curriculum/runtime.md#module-07) | Iteration scheduling and continuous batching (E) | 16 baseline h (E) |
| [08](../tracks/inference/curriculum/runtime.md#module-08) | Chunked prefill, preemption and cancellation (E) | 14 baseline h (E) |
| [09](../tracks/inference/curriculum/prefix-caching.md#module-09) | Block-hash prefix reuse (E) | 10 baseline h (E) |
| [10](../tracks/inference/curriculum/prefix-caching.md#module-10) | Radix cache and fair cache-aware scheduling (E) | 14 baseline h (E) |
| [11](../tracks/inference/curriculum/gpu-serving.md#module-11) | Online softmax and paged GPU attention (F) | 20 baseline h (F) |
| [12](../tracks/inference/curriculum/gpu-serving.md#module-12) | Triton and CUDA C++ through one useful kernel (F) | 18 baseline h (F) |
| [13](../tracks/inference/curriculum/gpu-serving.md#module-13) | Graph capture, overlap and profiling (F) | 16 baseline h (F) |
| [14](../tracks/agents/CURRICULUM.md#module-14) | RAG as a measured pipeline (C, December then January) | 8 baseline December h, remaining C evaluation in January |
| [15 application](../tracks/agents/CURRICULUM.md#module-15) / [15 replay](../tracks/inference/curriculum/foundations.md#module-15-replay) | MCP agents and causally valid replay (C), with distinct owners | 12 baseline December h across both portions + separate AG-1 8 h; remaining C evaluation in January |
| [16](../tracks/inference/curriculum/platform.md#module-16) | Kubernetes from request path to reconciliation (A + G) | 20 baseline h: A foundations 12 + G local lab 8 |
| [17](../tracks/inference/curriculum/platform.md#module-17) | Gateway routing and the Go scorer (G) | 12 baseline December h (G); real GPU continuation in January |
| [18](../tracks/inference/curriculum/platform.md#module-18) | KV tiers, adapters and cold start (G) | Within G January allocation; no additional hours |
| [19](../tracks/inference/curriculum/platform.md#module-19) | Scaling, overload and failures (G) | Within G January allocation; no additional hours |
| [20](../tracks/inference/curriculum/advanced.md#module-20) | Speculation as an exact probabilistic algorithm (H) | Within H 54 h (~10 h speculation) |
| [21](../tracks/inference/curriculum/advanced.md#module-21) | Quantization with quality gates (H) | Within H 54 h (~12 h quantization) |
| [22](../tracks/inference/curriculum/advanced.md#module-22) | Collectives, TP and expert parallelism (H) | Within H 54 h (~12 h collectives/EP) |
| [23](../tracks/inference/curriculum/advanced.md#module-23) | Disaggregated prefill/decode (H) | Within H 54 h (~12 h P/D) |
| [24](../tracks/inference/curriculum/advanced.md#module-24) | Capstone, statistical argument and reproduction (I + J) | Within I/J; no additional hours |

## Production-framework and agent development

- [PF-1](../tracks/inference/curriculum/frameworks.md#module-pf-1): SGLang source and runtime-state walkthrough, 8 added hours.
- [PF-2](../tracks/inference/curriculum/frameworks.md#module-pf-2): vLLM V1 architectural comparison, 4 added hours.
- [PF-3](../tracks/inference/curriculum/frameworks.md#module-pf-3): Bounded SGLang change and regression, 8 added hours.
- [PF-4](../tracks/inference/curriculum/frameworks.md#module-pf-4): Technical defense and interview practice, 4 added hours.
- [AG-1](../tracks/agents/CURRICULUM.md#module-ag-1): harness, context compaction and evaluator failures, 8 added hours. All baseline module-15 tasks remain.

## Bridge capsules

- [B1 — advanced kernels/compilers](../tracks/inference/curriculum/advanced.md#module-b1): required bounded capsule within J; optional depth is recorded in [advanced scope](../tracks/inference/design/advanced-labs.md).
- [B2 — training and rollout systems](../tracks/agents/CURRICULUM.md#module-b2): original independently completable four-hour J capsule; full agent SFT/RL/RL systems are now required additional scope.
- [B3 — nonstandard attention](../tracks/inference/curriculum/advanced.md#module-b3): required bounded capsule within J; optional depth is recorded in [advanced scope](../tracks/inference/design/advanced-labs.md).
- [B4 — multimodal](../tracks/inference/curriculum/advanced.md#module-b4): required bounded capsule within J; optional depth is recorded in [advanced scope](../tracks/inference/design/advanced-labs.md).
- [B5 — alternative accelerators](../tracks/inference/curriculum/advanced.md#module-b5): required bounded capsule within J; optional depth is recorded in [advanced scope](../tracks/inference/design/advanced-labs.md).
- [B6 — routing languages and control planes](../tracks/inference/curriculum/advanced.md#module-b6): required bounded capsule within J; optional depth is recorded in [advanced scope](../tracks/inference/design/advanced-labs.md).

## Authoring and ownership

Follow the teaching contract for offline HTML, notes, worked state/numerical examples, exercises, independent oracles, debugging, experiments and retrieval practice. Keep assistance/reference code attributable and separate; use the production package as the integration target. No curriculum item is removed merely because it becomes a supplied-code modification or hardware-unavailable explanation.

## Agent knowledge versus implementation

Use [AT-00–15](../tracks/agents/CURRICULUM.md) for the complete CMU course and integrated assignment objectives. The [coverage map](../tracks/agents/COVERAGE.md) includes every lecture and pending guest/training material. Passing a teaching exit is distinct from real SFT/RL operation. B2 and shared attention/cache concepts are learned once; links do not introduce cross-track runtime dependencies.
