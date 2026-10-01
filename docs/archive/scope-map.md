# Scope preservation and migration audit

[Overview](../../PROJECT_PLAN.md) · [Roadmap](../execution/roadmap.md) · [Archived originals](README.md)

This document is a traceability ledger, not another implementation plan. Canonical behavior lives in the linked designs/tasks. Source locators below refer to the archived v3 work-package bullets in order; the full original text remains in the snapshot. The approved additions are extra tasks, not replacements. No source requirement is considered implemented by being mapped here.

## A–J checklist coverage

| Original item | Short locator | Canonical implementation task(s) |
|---|---|---|
| A.1 | Diagnose tensor broadcasting, causal masks, attention shapes and Python async;… | [FND-02](../../tracks/inference/tasks/model.md#fnd-02) |
| A.2 | Trace a five-token prefill and three decode iterations on paper.… | [FND-02](../../tracks/inference/tasks/model.md#fnd-02) |
| A.3 | Compare stable vs naive softmax; implement a tiny attention reference… | [FND-02](../../tracks/inference/tasks/model.md#fnd-02), [MOD-02](../../tracks/inference/tasks/model.md#mod-02) |
| A.4 | Calculate KV bytes and weights/workspace/graphs separately; predict a memory ceiling.… | [MOD-03](../../tracks/inference/tasks/model.md#mod-03) |
| A.5 | Use the supplied starter to make an experiment bundle. Learn… | [FND-01](../../tracks/inference/tasks/model.md#fnd-01) |
| A.6 | Set up Python environment and CPU CI; pin code/model/tokenizer revisions… | [FND-01](../../tracks/inference/tasks/model.md#fnd-01) |
| B.1 | Implement metric calculations against synthetic event fixtures before real HTTP… | [BEN-01](../../tracks/inference/tasks/benchmark.md#ben-01) |
| B.2 | Use supplied HTTP/SSE plumbing; record intended arrival, dispatch, first content,… | [BEN-01](../../tracks/inference/tasks/benchmark.md#ben-01) |
| B.3 | Implement open-loop arrivals and closed-loop concurrency; detect load-generator dispatch lag.… | [BEN-02](../../tracks/inference/tasks/benchmark.md#ben-02) |
| B.4 | Run Qwen3-0.6B or 1.7B on both engines, then one larger… | [BEN-03](../../tracks/inference/tasks/benchmark.md#ben-03) |
| B.5 | Three load points, two workload shapes, caching off baseline; one… | [BEN-03](../../tracks/inference/tasks/benchmark.md#ben-03) |
| B.6 | Cross-check a matched run with vllm bench serve and AIPerf.… | [BEN-03](../../tracks/inference/tasks/benchmark.md#ben-03) |
| B.7 | Read one profiler trace and modify a supplied dashboard. Publish… | [BEN-03](../../tracks/inference/tasks/benchmark.md#ben-03) |
| C.1 | One versioned documentation corpus; supplied ingest/store/embedding/reranker plumbing.… | [APP-01](../../tracks/agents/ROADMAP.md#app-01) |
| C.2 | You implement or modify chunk selection, RRF and prompt layout;… | [APP-01](../../tracks/agents/ROADMAP.md#app-01) |
| C.3 | Start with 30 hand-checked RAG questions and 15 deterministic agent… | [APP-01](../../tracks/agents/ROADMAP.md#app-01), [APP-04](../../tracks/agents/ROADMAP.md#app-04) |
| C.4 | Measure recall@k with evidence labels, answer correctness/citation support and stage… | [APP-04](../../tracks/agents/ROADMAP.md#app-04) |
| C.5 | Run the supplied thin MCP agent; add step/token/time limits and… | [APP-02](../../tracks/agents/ROADMAP.md#app-02) |
| C.6 | Record roughly 50 varied sessions initially; repeat for load with… | [APP-03](../../tracks/agents/ROADMAP.md#app-03) |
| C.7 | Implement the replay modes in §8. Keep live task evaluation… | [BEN-04](../../tracks/inference/tasks/benchmark.md#ben-04) |
| D.1 | Start with the same tiny model revision as B; use… | [MOD-01](../../tracks/inference/tasks/model.md#mod-01) |
| D.2 | Validate uncached vs contiguous-cache prefill/decode with fixed positions and teacher-forced… | [MOD-02](../../tracks/inference/tasks/model.md#mod-02) |
| D.3 | Define request states and ownership before optimization. Build the pool,… | [KV-01](../../tracks/inference/tasks/memory-cache.md#kv-01), [KV-02](../../tracks/inference/tasks/memory-cache.md#kv-02), [SCH-01](../../tracks/inference/tasks/scheduler.md#sch-01) |
| D.4 | Test allocation/append/fork/release, shared partial-block copy-on-write, exhaustion and cancellation; assert conservation… | [KV-01](../../tracks/inference/tasks/memory-cache.md#kv-01), [KV-02](../../tracks/inference/tasks/memory-cache.md#kv-02), [SCH-04](../../tracks/inference/tasks/scheduler.md#sch-04) |
| D.5 | Compare predicted live KV bytes with allocated/reserved device memory. Explain… | [MOD-03](../../tracks/inference/tasks/model.md#mod-03) |
| D.6 | Capacity and correctness experiments only; gathered reference attention is not… | [KV-02](../../tracks/inference/tasks/memory-cache.md#kv-02) |
| E.1 | Implement static vs continuous scheduling with an injected virtual clock,… | [SCH-01](../../tracks/inference/tasks/scheduler.md#sch-01), [SCH-02](../../tracks/inference/tasks/scheduler.md#sch-02) |
| E.2 | Add token budget, chunked prefill and recompute preemption sequentially. Track… | [SCH-02](../../tracks/inference/tasks/scheduler.md#sch-02), [SCH-03](../../tracks/inference/tasks/scheduler.md#sch-03), [SCH-04](../../tracks/inference/tasks/scheduler.md#sch-04) |
| E.3 | Add idempotent cancellation/cleanup, bounded queues and a starvation safeguard before… | [SCH-04](../../tracks/inference/tasks/scheduler.md#sch-04), [SCH-05](../../tracks/inference/tasks/scheduler.md#sch-05) |
| E.4 | Implement chained block hashes with model/adaptor/tokenizer-relevant identity and tenant namespace.… | [KV-03](../../tracks/inference/tasks/memory-cache.md#kv-03) |
| E.5 | Implement radix match/insert/split/lock/evict against the same pool; compare it with… | [KV-04](../../tracks/inference/tasks/memory-cache.md#kv-04) |
| E.6 | Measure lookup overhead, reused tokens, eviction, recomputation, TTFT and waiting-time… | [KV-04](../../tracks/inference/tasks/memory-cache.md#kv-04), [SCH-05](../../tracks/inference/tasks/scheduler.md#sch-05) |
| F.1 | Study online softmax with a small numerical exercise; complete a… | [GPU-01](../../tracks/inference/tasks/gpu-serving.md#gpu-01) |
| F.2 | Integrate a pinned FlashInfer paged prefill/decode path. Test layout, dtype,… | [GPU-01](../../tracks/inference/tasks/gpu-serving.md#gpu-01) |
| F.3 | Write one Triton normalization kernel; modify the CUDA C++ reference… | [GPU-02](../../tracks/inference/tasks/gpu-serving.md#gpu-02) |
| F.4 | Modify the supplied CUDA Graph runner: stable addresses, input refresh,… | [GPU-03](../../tracks/inference/tasks/gpu-serving.md#gpu-03) |
| F.5 | Annotate Nsight Systems CPU launch gaps; use Nsight Compute on… | [GPU-04](../../tracks/inference/tasks/gpu-serving.md#gpu-04) |
| F.6 | Wrap the engine in supplied HTTP/SSE transport; implement cancellation ownership… | [SRV-01](../../tracks/inference/tasks/gpu-serving.md#srv-01), [SRV-02](../../tracks/inference/tasks/gpu-serving.md#srv-02) |
| G.1 | On kind, deploy simulator + one supported gateway/EPP pair using… | [PLT-01](../../tracks/inference/tasks/platform.md#plt-01), [FND-04](../../tracks/inference/tasks/model.md#fnd-04) |
| G.2 | Implement the Go score as a pure function first. Inputs:… | [PLT-02](../../tracks/inference/tasks/platform.md#plt-02) |
| G.3 | Test actual metrics parsing/units, routing, streams and disconnects for each… | [SRV-02](../../tracks/inference/tasks/gpu-serving.md#srv-02), [PLT-03](../../tracks/inference/tasks/platform.md#plt-03) |
| G.4 | On two GPUs, run two replicas of one model/engine, then… | [PLT-03](../../tracks/inference/tasks/platform.md#plt-03) |
| G.5 | Compare round-robin, least-queue and bounded prefix affinity. Implement stale-cache-index invalidation… | [PLT-02](../../tracks/inference/tasks/platform.md#plt-02), [PLT-03](../../tracks/inference/tasks/platform.md#plt-03) |
| G.6 | Run LMCache (or a compatible primary offloader), two LoRA adapters,… | [PLT-04](../../tracks/inference/tasks/platform.md#plt-04), [PLT-05](../../tracks/inference/tasks/platform.md#plt-05) |
| G.7 | Scale from one to two replicas on already available GPUs.… | [PLT-05](../../tracks/inference/tasks/platform.md#plt-05) |
| G.8 | Kill/drain a pod, overload the queue and disconnect a client.… | [PLT-05](../../tracks/inference/tasks/platform.md#plt-05) |
| H.1 | Speculation: implement the small rejection verifier and n-gram proposal logic;… | [ADV-01](../../tracks/inference/tasks/advanced-release.md#adv-01) |
| H.2 | Quantization: implement reference groupwise quantization, inspect calibration, run one supported… | [ADV-02](../../tracks/inference/tasks/advanced-release.md#adv-02) |
| H.3 | TP/EP: complete a two-rank linear/transformer-block lab; profile all-reduce and dispatch/combine.… | [ADV-03](../../tracks/inference/tasks/advanced-release.md#adv-03) |
| H.4 | P/D: run the supplied transfer benchmark and connector deployment. Compare… | [ADV-04](../../tracks/inference/tasks/advanced-release.md#adv-04) |
| H.5 | Record unsupported configurations explicitly. One real run is required for… | [ADV-01](../../tracks/inference/tasks/advanced-release.md#adv-01), [ADV-02](../../tracks/inference/tasks/advanced-release.md#adv-02), [ADV-03](../../tracks/inference/tasks/advanced-release.md#adv-03), [ADV-04](../../tracks/inference/tasks/advanced-release.md#adv-04) |
| I.1 | Pre-register one primary metric (p95 session completion), secondary metrics (per-turn… | [REL-02](../../tracks/inference/tasks/advanced-release.md#rel-02) |
| I.2 | Primary experiment: one production engine × three routing policies ×… | [REL-02](../../tracks/inference/tasks/advanced-release.md#rel-02) |
| I.3 | At five measured minutes/run that is three measured node-hours before… | [REL-02](../../tracks/inference/tasks/advanced-release.md#rel-02) |
| I.4 | Add one selected offload interaction and one second-engine cross-check only… | [REL-02](../../tracks/inference/tasks/advanced-release.md#rel-02) |
| I.5 | Use held-out sessions and a popularity-skew or stale-metric stress case;… | [REL-02](../../tracks/inference/tasks/advanced-release.md#rel-02) |
| I.6 | For completion-time claims use dependency-aware replay. Check a small live-agent… | [REL-02](../../tracks/inference/tasks/advanced-release.md#rel-02) owns replay; [AGT-04](../../tracks/agents/ROADMAP.md#agt-04) owns the required live quality check |
| I.7 | Write one coherent report, four useful plots and an artifact… | [REL-02](../../tracks/inference/tasks/advanced-release.md#rel-02) |
| J.1 | Six bridge capsules from §4.3 (about four hours each); include… | [REL-01](../../tracks/inference/tasks/advanced-release.md#rel-01) |
| J.2 | On-demand GPU regression test with effect-size threshold and repeated confirmation.… | [REL-03](../../tracks/inference/tasks/advanced-release.md#rel-03) |
| J.3 | Reproduce the core on a clean environment; record all exceptions… | [REL-03](../../tracks/inference/tasks/advanced-release.md#rel-03) |
| J.4 | One README, architecture note, capstone report, four-page summary, one short… | [REL-03](../../tracks/inference/tasks/advanced-release.md#rel-03) |
| J.5 | Prepare a small upstream contribution with reproduction/tests. Submission is within… | [REL-03](../../tracks/inference/tasks/advanced-release.md#rel-03) |
| J.6 | Final oral walkthrough: one request through API, scheduler, KV, GPU… | [REL-03](../../tracks/inference/tasks/advanced-release.md#rel-03) |

## Named technical coverage and learning modes

The complete original topic names and learning modes are retained here as an inventory. The owning tasks/designs specify how the concepts are learned; named alternatives do not become extra required deployments.

| Approved topic/tool coverage | Learning mode | Canonical task(s) |
|---|---|---|
| Python/PyTorch, transformer inference | Build | [MOD-01](../../tracks/inference/tasks/model.md#mod-01), [MOD-02](../../tracks/inference/tasks/model.md#mod-02) |
| KV accounting, MHA/MQA/GQA | Build | [MOD-03](../../tracks/inference/tasks/model.md#mod-03) |
| Paged KV and PagedAttention | Build + integrate | [KV-01](../../tracks/inference/tasks/memory-cache.md#kv-01), [KV-02](../../tracks/inference/tasks/memory-cache.md#kv-02), [GPU-01](../../tracks/inference/tasks/gpu-serving.md#gpu-01) |
| Continuous batching, chunked prefill, recompute preemption | Build | [SCH-02](../../tracks/inference/tasks/scheduler.md#sch-02), [SCH-03](../../tracks/inference/tasks/scheduler.md#sch-03), [SCH-04](../../tracks/inference/tasks/scheduler.md#sch-04) |
| Block-hash and radix prefix caching | Build | [KV-03](../../tracks/inference/tasks/memory-cache.md#kv-03), [KV-04](../../tracks/inference/tasks/memory-cache.md#kv-04) |
| CUDA Graphs and CPU/GPU overlap | Modify | [GPU-03](../../tracks/inference/tasks/gpu-serving.md#gpu-03) |
| Triton, CUDA C++, torch.compile, Nsight | Build + modify | [GPU-02](../../tracks/inference/tasks/gpu-serving.md#gpu-02), [GPU-04](../../tracks/inference/tasks/gpu-serving.md#gpu-04) |
| FlashAttention/Flash-Decoding/FlashInfer | Modify + integrate | [GPU-01](../../tracks/inference/tasks/gpu-serving.md#gpu-01) |
| Measurement, SLOs, trace replay | Build | [BEN-01](../../tracks/inference/tasks/benchmark.md#ben-01), [BEN-02](../../tracks/inference/tasks/benchmark.md#ben-02), [BEN-04](../../tracks/inference/tasks/benchmark.md#ben-04) |
| Go and gateway scoring | Build | [PLT-02](../../tracks/inference/tasks/platform.md#plt-02) |
| vLLM and SGLang | Operate both | [BEN-03](../../tracks/inference/tasks/benchmark.md#ben-03), [PF-1](../../tracks/inference/tasks/framework.md#pf-1), [PF-2](../../tracks/inference/tasks/framework.md#pf-2) |
| RAG, embeddings, BM25, vector DB, RRF, reranking | Modify + build experiments | [APP-01](../../tracks/agents/ROADMAP.md#app-01), [APP-04](../../tracks/agents/ROADMAP.md#app-04) |
| Agents, MCP SDK, structured output, XGrammar | Modify | [APP-02](../../tracks/agents/ROADMAP.md#app-02), [AG-1a](../../tracks/agents/ROADMAP.md#ag-1a), [AG-1b](../../tracks/agents/ROADMAP.md#ag-1b), [AG-1c](../../tracks/agents/ROADMAP.md#ag-1c) |
| Docker, kind/k3s, Kubernetes, GPU Operator/device plugin, Helm/Kustomize | Operate | [FND-04](../../tracks/inference/tasks/model.md#fnd-04), [PLT-01](../../tracks/inference/tasks/platform.md#plt-01), [PLT-03](../../tracks/inference/tasks/platform.md#plt-03) |
| Gateway API Inference Extension, llm-d | Operate + build scorer | [PLT-02](../../tracks/inference/tasks/platform.md#plt-02), [PLT-03](../../tracks/inference/tasks/platform.md#plt-03) |
| Prometheus, Grafana, DCGM, OpenTelemetry, Jaeger/Tempo | Operate + modify | [SRV-02](../../tracks/inference/tasks/gpu-serving.md#srv-02) |
| KEDA/HPA, cold start, admission, fairness, drain | Operate + build policy | [PLT-05](../../tracks/inference/tasks/platform.md#plt-05) |
| LMCache and HiCache / native offload | Operate primary, inspect alternative | [PLT-04](../../tracks/inference/tasks/platform.md#plt-04) |
| Multi-LoRA, S-LoRA/Punica | Operate | [PLT-04](../../tracks/inference/tasks/platform.md#plt-04) |
| Speculative draft-target and n-gram | Build small verifier + operate | [ADV-01](../../tracks/inference/tasks/advanced-release.md#adv-01) |
| EAGLE-3, MTP, DFlash, SpecForge/distillation | Operate one supported family; explain others | [ADV-01](../../tracks/inference/tasks/advanced-release.md#adv-01) |
| INT8, GPTQ/AWQ/SmoothQuant, FP8, W4A16, FP8 KV, NVFP4/MXFP4; LLM Compressor, lm-eval | Build math + operate | [ADV-02](../../tracks/inference/tasks/advanced-release.md#adv-02) |
| TP, DP, PP, FSDP/ZeRO, context parallelism; NCCL/MPI | Build small TP block + operate | [ADV-03](../../tracks/inference/tasks/advanced-release.md#adv-03) |
| MoE/EP, DP-attention, all-to-all, DeepEP/EPLB | Modify + operate if compatible | [ADV-03](../../tracks/inference/tasks/advanced-release.md#adv-03) |
| P/D disaggregation, NIXL/Mooncake | Operate + build cost analysis | [ADV-04](../../tracks/inference/tasks/advanced-release.md#adv-04) |
| Reliability, CI, cost, reproducibility | Build policies + use scaffolds | [REL-03](../../tracks/inference/tasks/advanced-release.md#rel-03) |

## Teaching, bridges and supplemental coverage

All module 00–24 blueprint bodies have been moved intact into the eight topic guides, with navigation and task connections added. The [curriculum](../../teaching/CURRICULUM.md) indexes them. [The teaching contract](../../teaching/CONTRACT.md) preserves the lesson/HTML/notes/ownership/rubric requirements. Full source stubs, detailed executable fixtures and HTML lessons remain future work.

All B1–B6 topic/evidence rows remain in bridge sections in the advanced topic guide and [advanced scope](../../tracks/inference/design/advanced-labs.md). Data/model lifecycle, SQL, held-out leakage, artifacts and cloud/IaC remain cross-cutting learning requirements. v2 E1–E6 deeper expansions remain optional under their corresponding bridges; none is silently converted to a mandatory semester-sized extension or erased.

PF-1/PF-2/PF-3/PF-4 retain 8/4/8/4 hours and full source/patch/defense handoffs in [framework tasks](../../tracks/inference/tasks/framework.md) and their teaching modules. AG-1a/AG-1b/AG-1c retain 2/3/3 added hours and their full loop/context/evaluator exercises in [workload tasks](../../tracks/agents/ROADMAP.md). The original MCP, tools, budgets, structured output, trace/replay and January evaluation remain. No baseline hours were reassigned.

## Design decisions retained from earlier revisions

The earlier detailed skeleton's nine logical interfaces are consolidated in [architecture](../../tracks/inference/ARCHITECTURE.md#logical-interfaces). Its seven ownership decisions are preserved at their canonical engineering boundaries:

| Preserved skeleton rule | Current owner |
|---|---|
| One coordinator mutates request state | [Runtime coordination](../../tracks/inference/design/model-runtime.md#responsibilities-and-interfaces) |
| Planned/computed/emitted tokens remain distinct | [Request lifecycle](../../tracks/inference/design/model-runtime.md#data-and-lifecycle) |
| Plan/reserve/execute/commit with reservation rollback | [Scheduler transaction](../../tracks/inference/design/scheduler.md#iteration-transaction) |
| Cancellation respects outstanding device work | [Scheduler lifecycle](../../tracks/inference/design/scheduler.md#preemption-and-edge-cases), [page lifetime](../../tracks/inference/design/kv-cache.md#page-lifecycle-and-invariants) |
| Both indexes use the same ownership/comparison contract | [Prefix contract](../../tracks/inference/design/kv-cache.md#responsibilities-and-interface) |
| Publish completed immutable full pages; compute final-hit logits safely | [Reuse rules](../../tracks/inference/design/kv-cache.md#identity-and-reuse) |
| Physical layouts stay behind the backend interface | [GPU boundary](../../tracks/inference/design/gpu-execution.md#backend-boundary) |

Its 01–17 storyboard sequences now live in the corresponding teaching blueprints; its waves 0–5 live in the roadmap. Typed signatures, preconditions/postconditions, explicit unfinished-method failures, CPU-only imports, independent oracles and later HTML accessibility requirements remain assigned to FND-01 and the teaching contract. The planned code map does not satisfy those future implementation gates; its former comment-only files are retained in the pre-simplification ZIP.

| Historical ambiguity or superseded proposal | Current approved treatment |
|---|---|
| 286 versus 318 fall hours; 496 versus 528 total | Baseline plus additive PF/AG allocations; baseline spring remains 210. The later agent expansion adds 280–400, yielding 808–928 overall |
| InferLab versus InferStack | LLM Systems Lab is the current umbrella; InferStack/src/inferstack remain valid inference-engine names. Preserve historical names in archives and unchanged supplied artifacts |
| Root engine/adapters/bench/apps paths versus src package | Approved December skeleton's src/inferstack boundaries; Go and deployment separate; logical responsibilities preserved |
| Gathered paged reference called fast PagedAttention | Real direct paged backend required for the performance claim |
| Universal greedy/bitwise equality | Exact structural invariants, teacher-forced tolerance checks, near-tie diagnostics and distribution-specific sampling tests |
| Fixed transcript treated as live agent evaluation | Three explicit replay/execution modes and separate task-quality checks |
| SSE chunks treated as exact token events | Keep count/timestamp source and chunk-versus-token distinction |
| Marginal percentiles treated as joint SLO attainment | Per-request threshold conjunction, all-offered failure accounting |
| Cache utilization treated as known prefix residency | Explicit locality source or approximate history; stale-state handling |
| Radix assumed better merely because prompts branch | Same pool/policy comparison before index/policy attribution |
| All engines/fleet stacks running simultaneously | Equivalent replica pool, sequential stack comparisons, bounded hardware |
| Full CUDA/attention assignments, two custom kernels, every advanced feature inside own engine | Approved selected attention lab, one authored Triton kernel plus CUDA modification, bounded guided advanced labs; optional deeper material retained |
| Multiple adapters trained by learner / production multi-node fleet | Two supplied compatible adapters and bounded local/two-GPU studies; no adapter-training dependency |
| 1P1D compared against one colocated GPU | Equal total GPU/cost comparisons |
| Merge count, novelty, positive speedup as graduation gates | Reproduction, explanation and contribution artifact; outcomes honestly reported |
| Old v2 cut order drops topics | Preserve topics; reduce repeated packaging/integration/sweep breadth before explicit schedule changes |

The older v2 examples/readings remain in the archive and preserved reference inventory. Their expired dates, unsafe equivalence assumptions, stale API details, elective expansion estimates and superseded implementation demands do not override the later approved decisions. This is consolidation of those decisions, not a new reduction in scope.

## Source-of-truth and audit limits

The approved two-track expansion relocates APP-01–04, AG-1a/b/c and teaching modules 14/15/AG-1/B2 to [agent owners](../../tracks/agents/COVERAGE.md#original-requirements-and-stable-aliases), preserving legacy anchors. BEN-04 and module 15's replay segment stay with inference. B2's original small bridge remains independently completable; substantive SFT/agentic RL/RL systems are now required additional agent work. The expanded course ledger covers the full CMU syllabus without replacing this original 64-item A–J and 26-topic ledger.

Byte-identical snapshots permit direct comparison. This ledger maps every A–J checkbox, approved topic row, teaching module, bridge and supplement; links then lead to acceptance criteria and milestone. Automated checks verify counts, links, dependency cycles, planned code paths and retained originals. A link/count check is not proof of technical implementation or of external software compatibility; those remain future evidence gates.
