# InferLab design review

Reviewed 2026-09-28 against the complete 1,233-line v2 plan and selected primary resources. [Current plan](../PROJECT_PLAN.md) · [Original, unchanged](archive/PROJECT_PLAN_v2.md)

## Judgment

**The project has a good intellectual core and more than enough inference-system coverage. The original learning curve and completion contract were too aggressive.** The correction is to distinguish what you implement, modify, operate and explain, while retaining all topics and tools in the curriculum.

Your follow-up makes the path clearer: Python/PyTorch/transformers are familiar; CUDA and Kubernetes are new; PennOS and PennCloud provide relevant systems experience. Aim for engine fundamentals by Nov 29, a working GPU runtime and first platform path by Dec 20, and full completion in April before May graduation. This needs about 26 h/week in fall under the revised estimate; “20+” cannot silently be treated as unlimited time.

These hour estimates are engineering judgments, not figures established by a course syllabus. AI assistance can reduce typing and boilerplate substantially. The original plan already relied on compact reference implementations, so it would be double-counting to both remove boilerplate and assume a second uniform 2× acceleration across learning, testing and experiments.

## What v2 gets right

1. The same workload, runtime and fleet measurements connect the layers into one project.
2. Paged memory, prefix reuse and cache indexing are distinguished correctly rather than called the same optimization.
3. Both allocator invariants and ablations are first-class artifacts.
4. Mac development plus short GPU sessions fits the hardware constraint.
5. RAG and agents justify realistic traffic instead of becoming an unrelated chatbot portfolio item.
6. Early artifacts, honest skill claims and negative-result write-ups are good completion mechanisms.

The original project is already far beyond a toy if those principles survive. Adding more frameworks would contribute less than making the existing correctness and measurement contracts rigorous.

## Changes needed and why

| Priority | v2 location / issue | Revised decision |
|---|---|---|
| Critical | §8 Step 3.5 schedules CUDA learning, FlashAttention homework, paged-backend integration, graphs, multiple Triton kernels and CUDA C++ in one week | Separate GPU fundamentals, attention integration, one authored kernel and supplied graph/CUDA glue; budget F at 54 h |
| Critical | §2 “cut order” drops entire concepts when behind | Keep each concept; reduce custom integration, duplicate stacks and sweep size |
| Critical | §4.4 fixed lengths presented as making agents reproducible | Separate fixed-arrival replay, dependency-aware transcript replay and live agents; different claims for each |
| Critical | §10 per-token timing assumed from SSE | Retain chunk events/count sources; exact token timestamps require backend support/instrumentation |
| Critical | §1/§8 universal identical greedy-output gates | Structural exactness, teacher-forced numeric comparison, margin-aware greedy diagnostics and distribution tests |
| Critical | §5 budget unclear about GPU-hours vs multi-GPU node-hours | Explicit counts, topology, per-node billing, setup/idle hours and contingency |
| High | §4.4 three vLLM metric names imply full gateway compatibility | Contract test the pinned gateway/EPP, units, labels, errors, streaming and locality input |
| High | §8 platform compares “routing” across three separate engines | Route between equivalent replicas within a pool; swap engines sequentially for controlled comparisons |
| High | §6.6 tree branching implies radix superiority | Both indexes represent shared prefixes; hold memory/page size/eviction/scheduler constant before attribution |
| High | §8 Phase 2 expects substantial dataset creation plus application build in two weeks | Supplied app baseline; modest human-checked pilot; grow diversity later |
| High | §8 goodput example uses marginal p95 SLOs | Define per-request pass/fail and aggregate; marginal percentiles do not establish joint attainment |
| High | §8 P/D can be compared to too few colocated GPUs | Primary comparison uses equal total GPUs/cost; include two colocated replicas |
| High | §8 TP/EP/MoE assumes model fits and combination exists | Preflight total weight+KV memory and supported parallel configuration; separate small collective lab from production run |
| High | §8 scaling on a fixed GPU node | Teach replica scaling on pre-existing capacity; node provisioning is a separate layer |
| Medium | §7 course warm-ups are “absorbed,” measured in days despite part-time schedule | Bound selected exercises in learner hours; full assignments optional |
| Medium | §7.4 course grading weights treated as effort ratios | Grades are not work estimates; budget writing explicitly |
| Medium | §7.5 “no course covers” and “new work” claims | Do not claim exhaustive syllabus coverage or research novelty without evidence |
| Medium | §5 RTX A6000 grouped as Ada/Hopper | Correct to Ampere; RTX 6000 Ada is different |
| Medium | §8 three merged upstream PRs required | Require a well-supported contribution artifact/submission; merge is external |
| Medium | §3 primarily senior job advertisements inform scope | Treat them as an ecosystem map, not a new-grad minimum checklist; do not require staff-scale ownership |
| Medium | §1/§8 strict “never fork/no copied code” | Preserve learner ownership of key mechanisms; allow attributed licensed scaffolds, isolate course solutions according to policy |

## Technical refinements beyond the schedule

### Memory and correctness

The dense KV formula in v2 is useful and its 0.6B worked value is consistent with the inspected Qwen configuration: `2 × 28 × 8 × 128 × 2 = 114,688` bytes/token = 112 KiB; at 32,768 tokens that is 3.5 GiB. Use the checkpoint's explicit `head_dim`; it need not equal `hidden_size / num_attention_heads`. The calculator must reject or handle MLA/hybrid/sliding-window configurations explicitly rather than claim “any config.” [Qwen configuration](https://huggingface.co/Qwen/Qwen3-0.6B-Base/blob/main/config.json)

Decode being bandwidth-bound and prefill being compute-bound are useful starting hypotheses, not universal laws. Batch size, context length, launch overhead, model size and interconnect move the bottleneck. Measure arithmetic intensity and end-to-end breakdown before stating the cause.

FlashAttention preserves the attention operation mathematically while changing its evaluation order; floating-point results need not be bitwise equal. Graph capture must account for stable buffers, dummy slots, and graph/workspace memory. A faster individual kernel does not establish faster serving when scheduling or network time dominates.

The speculative-decoding expected-length formula assumes a simplified acceptance model. Real acceptance is position/workload dependent and drafting/verification have costs. Teach `min(1, p(x)/q(x))` with a normalized positive residual on rejection, then test target-distribution preservation and KV rollback. [Original speculative-decoding paper](https://arxiv.org/abs/2211.17192)

The ring all-reduce traffic is not simply the tensor size: a common ring model moves approximately `2(p−1)/p × tensor_bytes` per rank, ignoring algorithmic variants and overhead. For TP accounting name whether a quantity is logical tensor bytes, per-rank link traffic or aggregate traffic. GQA/KV head divisibility can also complicate naive KV sharding.

### Prefix reuse and workload causality

vLLM's cache key includes prefix ancestry and additional identity, and supports cache isolation. Use model/revision/adapter and trusted tenant namespace consistently; a caller-chosen arbitrary salt alone is not an authorization boundary. A prefix hash and radix tree can find the same page-aligned reusable prefixes. Structural differences alone do not prove one has higher hit rate. [vLLM cache design](https://docs.vllm.ai/en/latest/design/prefix_caching/)

App prompts may retain the same text but change token identity with template/model revision. Cached KV is not durable application state. On worker death, recomputation can recover inference while tool side effects still require separate semantics. This is a useful bridge from your PennCloud experience.

Fixed transcripts preserve a workload but do not validate answers. Dependency-aware replay should send a continuation only after its parent completions and recorded think/tool delay. The public AIPerf replay documentation explicitly distinguishes recorded message history from freshly generated outputs. [Verbatim multi-turn replay](https://docs.nvidia.com/aiperf/tutorials/datasets-inputs/inputs-json-replay)

### Serving lifecycle and fairness

Treat admission/backpressure, cancellation, deadline expiry, preemption, stream termination and cleanup as a request state machine. They are core systems learning, not optional production polish. LPM cache-aware ordering needs a wait-time bound or aging policy; report starvation/fairness as well as cache hits.

A pod can be alive but unable to serve while weights load. A gateway can observe stale queue/cache data. Retries before output and retries after streaming begins have different user-visible semantics. Reusing a tool call after timeout can duplicate side effects. These concrete cases are better learning targets than adding a second orchestration framework.

### Research scope

The capstone should establish the conditions under which prefix affinity helps or hurts multi-turn workloads under bounded resources. Continuum studies cache retention across tool gaps; XPerf studies agentic workload replay; AgentSysBench studies system costs across agents and their tools. They motivate recording tool gaps and session dependencies, but do not predict your small-model results. [Continuum](https://arxiv.org/abs/2511.02230), [XPerf](https://arxiv.org/abs/2608.20370), [AgentSysBench](https://arxiv.org/abs/2608.15127)

Abstract/landing-page inspection here establishes relevance and source identity; it is not a completed replication or an independent verification of their performance numbers. Read methods/full papers before adopting their experiment protocols. The revised project does not claim research novelty merely because it combines these ideas.

## Resource selection and reading order

Use a **spine plus references**, not eight complete courses at once. Required reading is the relevant concept/implementation section; slides supplement the original teaching deck, rather than becoming another whole course to finish.

| Order / source (checked 2026-09-28) | Use in InferLab | Assigned depth |
|---|---|---|
| [Stanford CS336](https://cs336.stanford.edu/) | PyTorch/resource accounting; GPU/Triton; inference | Diagnostic portions of lecture 2, GPU/kernel lectures and inference lecture; no full A1 prerequisite given your experience |
| [CMU ML Systems schedule](https://mlsyscourse.org/schedule) | CUDA, attention, serving, parallelism | Primary lecture spine immediately before each lab; schedule supports teaching CUDA/attention before deep serving internals |
| [CS336 systems assignment](https://github.com/stanford-cs336/assignment2-systems) | Profiling and tiled-attention exercise format | Selected subproblems; inspect current assignment and course policy before adapting |
| [MIT accelerated computing](https://accelerated-computing.academy/fall25/) | GPU memory and execution intuition | Selected introductory/tiling exercises for a CUDA newcomer |
| [MIT efficient AI, 2024 archive](https://hanlab.mit.edu/courses/2024-fall-65940) | Quantization/deployment | Quantization and deployment material, bounded lab excerpt; do not assume every future offering's files exist |
| [CMU advanced ML systems](https://www.cs.cmu.edu/~zhihaoj2/15-779/schedule.html) | Broader research paper map | Reference when a specific mechanism becomes relevant |
| [Orca](https://www.usenix.org/conference/osdi22/presentation/yu) | Iteration scheduling | Draw a scheduling example and implement it |
| [PagedAttention](https://arxiv.org/abs/2309.06180) | Memory management and sharing | Study design/invariants; original throughput numbers are historical, not your acceptance threshold |
| [SGLang paper](https://arxiv.org/abs/2312.07104) | Radix reuse and structured generation | Cache design and control-flow connection |
| [Sarathi-Serve](https://arxiv.org/abs/2403.02310) | Chunked prefill trade-offs | Work an iteration-packing example and test interference |
| [Mini-SGLang](https://github.com/sgl-project/mini-sglang) | Compact executable reference | Read the module matching the mechanism; pin a revision before relying on filenames |
| [vLLM prefix design](https://docs.vllm.ai/en/latest/design/prefix_caching/) | Prefix key, ownership, eviction | Compare with your design after writing the invariants |
| [FlashInfer attention API](https://docs.flashinfer.ai/api/attention.html) | Paged-backend integration | Pick one supported API, record shapes/layouts, test the pinned version |
| [Triton normalization tutorial](https://triton-lang.org/main/getting-started/tutorials/05-layer-norm.html) | Reduction/fusion | Adapt ideas for RMSNorm; layer norm and RMSNorm are not identical operations |
| [vLLM reproducibility](https://docs.vllm.ai/en/latest/usage/reproducibility/) | Numerical and sampling tests | Understand conditions and limits before requiring cross-run equality |
| [AIPerf metric reference](https://docs.nvidia.com/aiperf/reference/ai-perf-metrics-reference) | New resource for measurement semantics | Map each reported metric to its timestamp/count source |
| [AIPerf replay guide](https://docs.nvidia.com/aiperf/tutorials/datasets-inputs/inputs-json-replay) | New resource for replay semantics | Compare fixed content with live-agent execution |
| [Gateway Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/) | Routing contracts and control-plane responsibilities | Understand gateway, pool and endpoint picker before deploying |
| [Model-server protocol proposal](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/main/docs/proposals/003-model-server-protocol/README.md) | Contract starting point | Verify against actual released implementation; proposal alone is not conformance |
| [llm-d](https://github.com/llm-d/llm-d) | Supported deployment guides | Choose one supported routing setup; do not install all guides simultaneously |
| [LMCache](https://docs.lmcache.ai/) | Host-memory KV tier | Integration/usage for the pinned engine, plus restore/recompute experiment |
| [vLLM disaggregated prefill](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | P/D scope and connector integration | One compatible connector, two-GPU comparison |
| [vLLM quantization support](https://docs.vllm.ai/en/latest/features/quantization/) | Actual format/backend hardware constraints | Read before choosing a rental or checkpoint |
| [Speculative decoding](https://arxiv.org/abs/2211.17192) | Verifier correctness | Work exact categorical examples, then a supported serving run |
| [Continuum](https://arxiv.org/abs/2511.02230) | Session retention and tool gaps | Read methods before trying a TTL policy |
| [XPerf](https://arxiv.org/abs/2608.20370) | Agent workload replay | Methods comparison; not a second benchmark framework implementation |
| [AgentSysBench](https://arxiv.org/abs/2608.15127) | Non-LLM stages and state | Use to question whether LLM optimization improves the whole task |
| [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) | SDK/protocol boundary | Current checked spec describes stateless self-contained requests; app/tool state still needs handling |
| [Lambda instance pricing](https://lambda.ai/instances) | GPU cost scenarios | Per-GPU vs per-node rate, topology, availability and tax |
| [Runpod pricing](https://www.runpod.io/pricing) | Alternative quote source | Check current SKU, cloud tier, storage, privileges and topology before booking; no assumed cheapest-rate guarantee |
| [NVIDIA RTX A6000](https://www.nvidia.com/en-us/design-visualization/rtx-a6000/) | Correct GPU architecture identity | Avoid confusing Ampere A6000 with RTX 6000 Ada |

Additional specialized references already in v2 remain available in the archive. Not every archived URL, code path, job posting, course lab requirement or deployment combination was revalidated in this review. They are research leads until checked for the exact lesson.

## Version verification and uncertainty

The inspected [vLLM release page](https://github.com/vllm-project/vllm/releases) did show v0.30.0, dated September 22, and the specified MCP revision did exist. Therefore the original September-2026 snapshot should not be dismissed merely because it describes recent changes. Conversely, existence of releases does not establish compatibility between vLLM, SGLang, FlashInfer, llm-d, gateway charts and the MCP SDK.

No full GPU stack was installed or benchmarked during this design review. Record a compatibility set after a smoke test: OS/image digest, driver, CUDA, PyTorch, attention backend, engine commit, gateway/EPP chart versions, model and tokenizer revisions, quantization format, GPU architecture and tested command. Do not copy an untested list of independent “latest” versions into a lockfile and call it validated.

The new plan avoids promises that all hardware, exact course assignments or advanced configurations are available. When blocked by hardware, preserve the concept with a numerical/reference exercise and state the smaller claim level. No rented instance or external account action is part of this review.

## Acceptance criteria for the revised design

- **Learning curve:** new CUDA/Kubernetes ideas arrive through short worked examples before major integration; familiar OS/distributed-system material is reused.
- **Coverage:** all v2 core concepts/tools and electives have a learning mode and evidence artifact; broader ML-system gaps have bounded bridge lessons.
- **Scope:** one dense runtime, one primary fleet stack, one corpus/agent path and one capstone question. Full distributed training or wide-EP replication is not required.
- **Finishability:** fall and spring hour totals are explicit, AI responsibilities are explicit, and late-April buffer remains.
- **Teaching:** each concept has an HTML lesson contract, code handoff, exercise, error diagnosis and test/experiment gate.
- **Budget:** several hundred dollars can work on the stated small-model/two-GPU plan; long premium-GPU sweeps and training are separately budgeted extensions.
