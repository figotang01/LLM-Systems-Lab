# InferLab HTML teaching and code curriculum

[Execution plan](../PROJECT_PLAN.md) · [Design review and checked resources](../docs/PLAN_REVIEW.md) · [Open lesson 00](slides/00-orientation.html)

## Teaching contract

Audience: experienced Python/PyTorch/transformer user with C/C++ OS and distributed-systems projects, new to CUDA and Kubernetes. Teach GPU execution and Kubernetes explicitly; use PennOS scheduling/ownership and PennCloud failure/routing experience as bridges. Skip rebuilding HTTP, durable KV or an autodiff framework as prerequisites.

**Delivered now:** lesson 00 and the dependency-free [starter utility](../starter/README.md). **Planned:** modules 01–24 and bridge capsules B1–B6, their exercise scaffolds and reference solutions. This document specifies those deliverables; links to code under future module paths are path specifications, not existing files. Do not mistake a syllabus for completed courseware.

Delivery order matches the accelerated calendar: 00–13 for fall engine learning; 14–17 for December applications/first gateway; deeper 18–19 in January; 20–23 in February; 24 and bridges in March/April. Teach the conceptual overview of advanced topics early without turning it into a prerequisite for the engine.

A full technical module normally consists of 25–40 slides plus expandable notes, a 45–75-minute teaching session, 1–2 hours of small exercises and the project lab assigned in the master plan. Larger topics split into sessions A/B. This is **inside** the package budgets, not extra homework. Lesson 00 is an orientation/reference deck, not a substitute for the deep modules.

Each module must contain:

1. Three to five observable learning objectives and a short prerequisite check.
2. A concrete request or failure that motivates the mechanism.
3. A visual state trace before abstract equations or production code.
4. Equations with units, tensor shapes, assumptions and a worked numerical example.
5. A minimal readable implementation and mapping to a pinned production reference.
6. At least two misconception/debugging examples and a deliberately broken fixture.
7. “Predict before running” questions with revealable answers; notes explain why wrong answers fail.
8. A scaffolded learner task, independent correctness oracle, one bounded experiment and an exit explanation.
9. Exact source links, tested software/hardware, and an explicit limit on what the lesson demonstrates.

**Notes:** include reasoning, intermediate steps, edge cases and what to inspect in code. Do not hide essential explanation exclusively in a spoken lecture. A learner must be able to study offline with no instructor.

**HTML:** plain HTML/CSS/JS, no required CDN, keyboard next/previous and direct slide selection, URL anchors, reading view, print styles, expandable notes/answers, accessible labels, responsive code blocks and high contrast. Use inline SVG/CSS state diagrams and small interactive simulators. Synthetic animations/calculators must say “illustrative”; performance plots must link to real raw data. Do not invent benchmark graphs.

**Code tree for later delivery:**

```text
teaching/modules/<id>/
  README.md          objectives, environment, run commands, ownership, time box
  scaffold/          working transport/build/plumbing; learner TODOs clearly marked
  exercises/         only the mechanism under study
  fixtures/          deterministic inputs and independent expected results
  tests/             correctness/state invariants; no perf assertion on a laptop
  reference/         complete annotated solution, opened when useful
  experiments/       fixed small sweep + collection recipe + expected qualitative questions
  reading.md         paper sections and pinned source symbols
teaching/slides/<id>.html
```

The AI tutor first supplies explanation, then code assistance. After understanding, ask it to implement your stated design, review its diff, and run independent checks. Request a walkthrough of any line you cannot explain. Rebuild a small part without the agent at each exit gate. Supplied reference code is clearly credited and never silently described as your independent implementation.

## Module blueprints

### 00 — Project map and measurement foundations (delivered)

- **Objectives:** define the project’s one central question, choose implementation ownership, distinguish timing/replay modes, and calculate KV/cost units.
- **Deck:** project identity → OS/distributed-systems analogies → fall/spring calendar → build/modify/operate/explain → request lifetime → prefill/decode → KV math and interactive capacity → physical pages/prefix identity → metric timeline and goodput → chunk-vs-token and replay modes → numerical correctness → GPU budget → AI workflow → first lab/quiz.
- **Code:** `starter/experiment.py`; inspect `budget()` and `create_bundle()`; supplied artifact support, not a benchmark implementation.
- **Exit:** compute 112 KiB/token, explain why two GPUs for three hours is six GPU-hours, and identify why fixed-length agent replay cannot validate task quality.

### 01 — Tensor and numerical diagnostic (package A)

- **Objectives:** trace attention dimensions and causal positions, identify where KV is reused, distinguish numerical and semantic failures.
- **Slides 1–8:** one five-token prompt; embeddings/QKV shapes; GQA head mapping; RoPE positions and QK norm. **9–18:** stable softmax, masks, prefill vs one-token decode, teacher-forced comparison. **19–28:** dtype error, argmax ties, sampling vs greedy and debugging examples.
- **Code:** supplied tiny model/config/weight fixtures; learner attention/cache append exercise. Use explicit head dimension, not a guessed `hidden_size/heads` value.
- **Experiment/exit:** compare uncached and incremental logits; catch a deliberately shifted RoPE position. Budget ~8 h refresher/diagnostic given your background; no full CS336 A1.
- **References:** CS336 resource accounting; model config and the archived v2 transformer references.

### 02 — GPU execution for a systems programmer (A + F)

- **Objectives:** explain grids/blocks/warps, memory hierarchy, coalescing, synchronization and asynchronous host behavior.
- **Slides 1–10:** CPU process/thread analogy and its limits; SIMT; global/shared/register memory. **11–20:** index mapping, bounds, coalescing, barriers, races. **21–34:** launch overhead, streams/events, host/device copies, arithmetic intensity, roofline and correct timing.
- **Code:** supplied CUDA/PyTorch-extension build setup and vector-add/reduction examples; learner changes indexing and fixes a race. Triton program IDs compared with CUDA blocks.
- **Experiment/exit:** predict a noncoalesced access pattern and a missing synchronization bug; distinguish enqueue time from completed device work. Use one tiny GPU session, not a training workload.
- **References:** CMU CUDA lectures; selected MIT accelerated-computing introductions. Budget ~12 h GPU foundations within A, deeper work in F.

### 03 — Measuring a serving system (B)

- **Objectives:** implement open/closed-loop load and trustworthy latency/goodput; recognize coordinated omission and client saturation.
- **Slides 1–10:** queue timeline, intended arrival vs dispatch, first useful content, completion/errors. **11–22:** SSE chunks, TPOT edge cases, SLO conjunction, throughput vs goodput, Little’s law. **23–36:** cache warmup, load sweeps, repeats, dependent observations and confidence intervals.
- **Code:** supply HTTP/SSE parser, fixtures, artifact/plot plumbing; learner `ArrivalSchedule`, `RequestObservation`, `aggregate_slo()` and saturation detection.
- **Experiment/exit:** recover known synthetic timings, count timeout/drop failures, cross-check one production run with AIPerf. A client dispatch cap must not silently alter the offered workload.
- **References:** AIPerf metric reference and arrival/replay docs; CS336 profiling problems.

### 04 — A single-request dense runtime (D)

- **Objectives:** implement the decoder path and cache state while using a supplied checkpoint loader.
- **Slides 1–8:** full request trace and model architecture. **9–22:** RMSNorm, RoPE, QK norm, GQA, SwiGLU, output projection and sampling. **23–34:** weight shapes/tied embeddings, prefill/decode interface, logits inspection and reference comparisons.
- **Code:** supplied safetensors/name mapping/tokenizer/CLI; learner model operations and cache writes. Support one dense revision first.
- **Experiment/exit:** fixed-token per-layer comparisons and a small greedy suite; explain one mismatch from tensor shape or position rather than chasing generated text.

### 05 — Memory accounting and cache lifetime (D)

- **Objectives:** distinguish live KV, reserved capacity, weights, activations and graph/workspace allocation.
- **Slides 1–10:** KV formula, bytes/units, context/concurrency trade-off; MHA/MQA/GQA. **11–20:** allocator-reserved vs live tensors, peak measurement, fragmentation, model fit. **21–28:** MLA/hybrid exceptions, MoE active-vs-resident weights.
- **Code:** learner config-aware dense `kv_calculator`; supplied config fixtures and device-memory collection.
- **Experiment/exit:** predict and measure context-length memory; reject unsupported hybrid configs with a clear explanation. No claim to support all architectures.

### 06 — Paged ownership, refcounts and copy-on-write (D)

- **Objectives:** implement pool/tables/mappings with precise ownership and read-path correctness.
- **Slides 1–10:** OS virtual-memory analogy; logical token → logical page → physical page/slot. **11–22:** allocate/append/fork/share/free and partial-page copy-on-write. **23–36:** property/state-machine tests, capacity, reference gather vs direct paged read.
- **Code:** supply fixtures/state visualizer; learner block pool, block tables, writes and gathered attention oracle. Inject exhaustion and stale page IDs.
- **Experiment/exit:** randomized transitions conserve pages and preserve output; demonstrate the shared-tail bug before fixing it.
- **References:** PagedAttention; compact reference engines. The OS analogy does not imply hardware page faults or general-purpose virtual memory.

### 07 — Iteration scheduling and continuous batching (E)

- **Objectives:** translate PennOS queue/scheduler ideas into token-level serving work and resource constraints.
- **Slides 1–8:** static batch inefficiency with uneven output lengths. **9–20:** waiting/running/finished states, token budgets, backfill, admission. **21–30:** virtual time vs real executor, compute vs memory constraints, fairness.
- **Code:** supplied virtual clock/FakeExecutor; learner scheduling policy and state transitions. Never use simulator wall-clock speed as GPU throughput.
- **Experiment/exit:** manually trace four requests across six iterations; compare static/continuous on the same arrival sequence.
- **References:** Orca and CMU serving lecture.

### 08 — Chunked prefill, preemption and cancellation (E)

- **Objectives:** bound decode interference, recover from memory pressure and clean up every request exit path.
- **Slides 1–10:** long prefill interrupts decodes; token-budget packing. **11–22:** partial-prefill positions, recompute vs swap cost, victim/aging policy. **23–36:** disconnect/timeout races, in-flight GPU work and idempotent release.
- **Code:** learner chunk packing/recompute state machine; supplied adversarial schedules including cancellation immediately before/after a step finishes.
- **Experiment/exit:** one long prompt amid decodes; report TTFT/ITL trade-off and recomputed tokens. Correct output and no leak after cancel/resume.
- **References:** Sarathi-Serve; production scheduler selected code.

### 09 — Block-hash prefix reuse (E)

- **Objectives:** derive complete cache identity and evict only safe blocks.
- **Slides 1–10:** full-block prefix chain and ancestry; model/adapter/tenant identities. **11–20:** cache ownership vs active references, LRU queue, full-prompt hit/logit issue. **21–30:** hash collision assumptions, isolation boundaries and cold/warm tests.
- **Code:** learner chained key/lookup/eviction; supplied reused-prefix fixtures and cache visualization.
- **Experiment/exit:** same block under a different parent must miss; new adapter/namespace must miss; quantify reused tokens, not just request hits.
- **Reference:** vLLM automatic-prefix-cache design.

### 10 — Radix cache and fair cache-aware scheduling (E)

- **Objectives:** implement compressed edges, splitting, locks and eviction; isolate indexing from policy effects.
- **Slides 1–10:** draw SYS+A+X / SYS+A+Y / SYS+B+Z. **11–24:** partial-edge match, split/insert, lock propagation, leaf eviction, page alignment. **25–36:** fair comparison with block hashes, LPM/aging, lookup cost and fairness.
- **Code:** learner radix operations over the SAME pool; supplied printer and adversarial split/evict sequence. Use a provided reference if the full implementation threatens the December gate, then modify/debug it.
- **Experiment/exit:** cache-policy comparison with matched resources; explain why branching alone does not guarantee radix superiority.
- **References:** SGLang paper and Mini-SGLang.

### 11 — Online softmax and paged GPU attention (F)

- **Objectives:** derive streaming softmax accumulation and connect algorithm/layout to the attention backend.
- **Slides 1–12:** attention IO cost; running maximum and denominator; rescale old accumulator when max increases. **13–24:** tiled forward, causal boundaries, numerical tests and split-KV decode. **25–38:** paged layouts, last-page length, GQA, plan/run workspace and backend compatibility.
- **Code:** supplied partial tiled forward and FlashInfer wrapper; learner completes accumulator update and paged metadata adapter.
- **Experiment/exit:** compare against tiny FP32 reference then GPU tolerance; trace a sequence crossing a page boundary. Full optimized FlashAttention implementation is an extension.
- **References:** FlashAttention papers, FlashInfer API, selected CS336 systems exercise.

### 12 — Triton and CUDA C++ through one useful kernel (F)

- **Objectives:** write normalization, explain fusion and recognize bandwidth/occupancy limits.
- **Slides 1–10:** RMSNorm equation, reduction, epsilon and accumulation dtype. **11–22:** Triton program mapping/masking; CUDA warp/block version; launch configuration. **23–36:** fusion bytes saved, roofline, eager/compile comparisons, shape/dtype tests.
- **Code:** learner Triton kernel; supplied CUDA baseline and extension build, learner substantive change and comparison. CUDA is retained without making build-system debugging the main assignment.
- **Experiment/exit:** correct tails and dtypes, microbenchmark with warmup and device synchronization; check if the engine gets faster.
- **Reference:** Triton layer-normalization tutorial, adapted with the RMSNorm distinction explained.

### 13 — Graph capture, overlap and profiling (F)

- **Objectives:** interpret CPU/GPU timelines; safely manage graph buffers; understand streams/events.
- **Slides 1–10:** host launches, GPU idle gaps, Amdahl’s law. **11–24:** capture/replay, static addresses, bucket padding, dummy KV writes, invalidation. **25–36:** event dependencies, next-batch preparation, Nsight Systems vs Compute and profiler overhead.
- **Code:** supplied graph lifecycle and profiler scripts; learner buffer updates/bucket policy; bounded overlap example rather than a mandatory fully async engine.
- **Experiment/exit:** eager-vs-graph across batch sizes with equal math; explain when padding or graph memory loses.

### 14 — RAG as a measured pipeline (C, December then January)

- **Objectives:** assess retrieval quality, context construction and latency rather than just build a demo.
- **Slides 1–10:** corpus versions, chunks and evidence labels. **11–22:** embeddings/BM25, RRF, vector-store choice, reranker, prompt identity. **23–34:** recall/MRR, citation support, held-out evaluation, stage timing and judge calibration.
- **Code:** supplied ingest/Qdrant/embedding/reranking/service plumbing; learner chunk/RRF/prompt ablations. Explain pgvector alternative without another required migration.
- **Experiment/exit:** hand-check a small held-out set, show one retrieval failure and one generation failure; preserve exact corpus/prompt revisions in traces.

### 15 — MCP agents and causally valid replay (C)

- **Objectives:** distinguish tool syntax from semantic correctness and preserve session dependencies in measurements.
- **Slides 1–10:** thin agent loop, budgets, JSON/schema constraints, parsers and tool failures. **11–22:** MCP SDK boundary, docs/SQL/execution tools, state vs stateless requests, trace spans. **23–38:** three replay modes, delays/parent DAG, content vs length, live task checks and tool-result caching.
- **Code:** supplied app/MCP wrappers and restricted tool runner; learner policy, parent dependency scheduling and evaluation fixtures. No general-purpose sandbox implementation.
- **Experiment/exit:** intentionally delay a tool; verify child dispatch; contrast fixed transcript vs fresh-output control flow. Explain why post-timeout tool retries need care.
- **References:** checked MCP specification; AIPerf replay; XPerf/AgentSysBench methods before capstone.

### 16 — Kubernetes from request path to reconciliation (A + G)

- **Objectives:** operate pods/services/controllers and debug deployment/resource lifecycle as a newcomer.
- **Slides 1–10:** desired vs observed state, reconciliation, pod/deployment/service/DNS. **11–22:** image/runtime, requests/limits, GPU device allocation, liveness/readiness/startup. **23–38:** selectors, Helm/Kustomize, namespaces/RBAC, termination/drain and observing events.
- **Code:** supplied kind/simulator/Helm baseline; learner changes readiness/resource policy and diagnoses intentionally wrong labels and insufficient GPU requests.
- **Experiment/exit:** explain why an alive pod is not necessarily ready; follow one request through service endpoints. No multi-node cluster administration prerequisite.

### 17 — Gateway routing and the Go scorer (G)

- **Objectives:** implement one explainable locality/load score and integrate its real contract.
- **Slides 1–10:** gateway vs EPP vs model server, InferencePool and request metadata. **11–22:** locality estimates, queue delay, imbalance guard, session affinity and stale statistics. **23–36:** Go function/tests, normalization, fallback, plugin integration and counterexamples.
- **Code:** supply EPP version glue and chart; learner scoring logic and tests. Avoid programming a second standalone HTTP proxy given your PennCloud background.
- **Experiment/exit:** two equivalent replicas, skewed popularity and restarted worker; show when cache affinity overloads one worker.
- **References:** Gateway architecture, protocol and llm-d supported guide.

### 18 — KV tiers, adapters and cold start (G)

- **Objectives:** compare recompute/restore costs and distinguish weight, KV and adapter residency.
- **Slides 1–10:** HBM/host/storage state; bytes/bandwidth lower bounds and overlap. **11–22:** LMCache lifecycle, HiCache alternative, tool gaps/TTL trade-offs. **23–34:** S-LoRA/Punica, adapter identities, weights/download/load/graph warmup.
- **Code:** supplied offload/LoRA deployment; learner cache-capacity perturbation and restore/recompute cost analysis.
- **Experiment/exit:** two adapters do not share incompatible KV; offload benchmark reports transfer and recompute, not just cache hit rate.

### 19 — Scaling, overload and failures (G)

- **Objectives:** design a measured control policy and trace abort/retry semantics.
- **Slides 1–10:** HPA/KEDA, queue signals, hysteresis/stabilization, missing metrics. **11–22:** cold start and capacity ceilings, admission/deadlines, load shedding/fairness. **23–36:** kill/drain/OOM/slow pod, pre-stream retry vs partial stream error, client cancellation and cleanup.
- **Code:** supplied manifests, failure injector and dashboards; learner scaling thresholds, fallback and outcome assertions.
- **Experiment/exit:** scale one-to-two on existing GPU capacity, record readiness/SLO failures; no claim of cloud node autoscaling.

### 20 — Speculation as an exact probabilistic algorithm (H)

- **Objectives:** prove the acceptance rule, understand proposer economics and preserve cache state.
- **Slides 1–12:** sequential decoding, draft/verify, exact categorical example, acceptance and residual distribution. **13–24:** bonus token, rejection rollback, EOS, greedy vs stochastic equivalence. **25–38:** n-gram, draft-target, EAGLE/MTP/DFlash families; load-dependent break-even.
- **Code:** learner small verifier/ngram proposal; supplied draft-worker plumbing and supported serving recipe. Explain SpecForge/drafter training without requiring it.
- **Experiment/exit:** exact small probability checks, statistical output check, then off/on at low/high load. Do not compare same-seed trajectories as the correctness proof.

### 21 — Quantization with quality gates (H)

- **Objectives:** distinguish storage formats, compute kernels and error controls.
- **Slides 1–10:** scales/zero points, symmetric/asymmetric, channel/group granularity, error. **11–24:** GPTQ/AWQ/SmoothQuant, calibration and leakage, W4A16 vs W8A8 and KV quantization. **25–38:** FP8/FP4 variants and hardware support, dequant overhead, quality-memory-latency Pareto.
- **Code:** learner groupwise INT8 reference; supplied LLM Compressor/evaluation scripts and fixed calibration/held-out split.
- **Experiment/exit:** one real compressed checkpoint plus a KV precision ablation; unsupported formats get a numerical exercise and a clearly limited claim.
- **References:** MIT efficient-AI quantization/deployment, vLLM support matrix, papers in v2.

### 22 — Collectives, TP and expert parallelism (H)

- **Objectives:** derive row/column shards, communication bytes and MoE dispatch/combine; compare with training parallelism.
- **Session A:** DP/PP/TP, FSDP/ZeRO memory bridge, rank groups, NCCL/MPI, ring traffic, two-rank algebra, shard loading and GQA caveats. **Session B:** MoE total/active parameters, expert routing/skew, all-to-all, DP-attention, DeepEP/EPLB and topology.
- **Code:** supplied launchers/sharded loader; learner two-rank linear/transformer block and toy expert dispatcher; production TP/EP configuration only when supported.
- **Experiment/exit:** TP=1 vs 2 at equal model/settings with topology recorded; explain a slowdown. Tiny MoE lab remains possible when production EP is unavailable.

### 23 — Disaggregated prefill/decode (H)

- **Objectives:** account for transfer and compare capacity fairly.
- **Slides 1–10:** interference and separate SLOs, P:D ratio. **11–22:** KV layout/transport, NIXL/Mooncake, staging/overlap, ownership and failure. **23–34:** transfer/recompute model, break-even conditions, equal-GPU baselines and queueing.
- **Code:** supplied transport/connector/routers and transfer driver; learner analytical model plus validation from measured bandwidth.
- **Experiment/exit:** 1P1D vs two colocated replicas; no claimed advantage that merely comes from giving one system an extra GPU.

### 24 — Capstone, statistical argument and reproduction (I + J)

- **Objectives:** make a bounded causal claim with trustworthy uncertainty and honest provenance.
- **Slides 1–10:** hypothesis, primary metric, workload/popularity/dependency design. **11–22:** paired configurations, whole-session resampling, tails, errors and cost. **23–36:** explain profiles, falsify alternative causes, negative results, version/artifact bundle and portfolio claim levels.
- **Code:** supplied plot/report template; learner experiment design, analysis and interpretation. Start with 36 primary runs, not a huge Cartesian product.
- **Exit:** a stranger can reproduce one main figure; oral defense connects routing, queue, KV and session behavior. No required positive result or upstream merge.

## Bridge capsules B1–B6 (J, approximately four learner hours each)

Each gets 10–18 slides, an annotated code/profile artifact, one modification/calculation and a teach-back. Hardware-unavailable capsules use supplied traces/numerical examples and are labeled studied; no fabricated GPU measurement.

| ID | Content and supplied code | Learner evidence |
|---|---|---|
| B1 advanced kernels/compilers | Tiled matmul, tensor cores, warp specialization, FlashAttention generations, TVM/TIRx and mega-kernel annotated examples | Modify tile parameter; compare IO/occupancy predictions to one profile |
| B2 training and rollout systems | Tiny autograd/training step; DP/FSDP/ZeRO memory; SFT/RLHF/GRPO; verl/Miles/slime weight-version/rollout trace; distillation | Optimizer-state calculation; identify stale-weight/train-inference mismatch; modify small supplied loop |
| B3 nonstandard attention | MLA latent, sliding window, hybrid recurrent/Gated DeltaNet/Mamba state examples | Checkpoint/restore a tiny recurrence; explain prefix reuse constraints and state size |
| B4 multimodal | Supplied VLM encoder/prefill/decode example, image identity and encoder-cache trace | Identify encoder vs language cost and an invalid image-cache hit |
| B5 alternative accelerators | Local MLX example, vllm-metal architecture, supplied JAX/TPU layout sample | Run local code and compare layouts; separate Mac performance from NVIDIA results |
| B6 routing languages and control planes | Supplied small Rust load selector; SGLang gateway/Dynamo/KServe map; DRA, KAI/Grove examples | Modify Rust selection/tie handling; explain who allocates GPUs, picks an endpoint and moves KV |

Data/model lifecycle, SQL, IaC and evaluation provenance recur in 03/14/16/24: version corpus and artifacts, inspect a provisioning configuration, test train/calibration/eval split integrity. They do not become another full platform build.

## Code assistance priorities

| Provide complete code | Keep learner ownership |
|---|---|
| Experiment directories, manifest/report formatting, plot styling | Measurement definitions and causal interpretation |
| HTTP/SSE transport, API schema adapters, tokenizer/weight loading | Request lifetime/cancellation and model math |
| RAG service/MCP wrappers/vector-store setup | Retrieval ablation, prompt identity, eval and agent policy |
| CUDA extension build, GPU provisioning/collection, distributed launch | One kernel, collective algebra and profile explanation |
| Graph capture shell and FlashInfer binding scaffolds | Buffer/state invariants, shape metadata and safe padding |
| Helm, dashboards, EPP registration, offload/P/D launch recipes | Routing score, failure/scaling policy and controlled experiments |

Give complete assistance code with explanations, not opaque generated files. For version-sensitive components, use the exact dependency set tested for the lesson, include a local smoke test and disclose whether validation used real GPUs. Use a clean environment and a tiny model before larger runs.

## Lesson acceptance rubric

Score each dimension 0 (cannot), 1 (with notes), 2 (independent): explain; trace state/shapes; predict failure; implement/modify; design/interpret measurement. Advance at 8/10 with no zero in correctness. If a module stalls, use a reference and repeat a smaller variation; do not silently skip the concept.

Check understanding again one week and one month later with a five-minute reconstruction or oral explanation. At each milestone, identify one limitation you can defend. This is the guard against AI-generated code creating the appearance of mastery without the ability to reason about it.

## Append-only teaching supplements — approved 2026-09-29

All preceding modules **00–24**, bridges **B1–B6**, objectives, exercises, references, code-assistance rules, and acceptance gates remain intact. The [complete December skeleton](../docs/DECEMBER_SKELETON.md) preserves the earlier detailed structure; the [supplement specification](../docs/PLAN_ADDITIONS.md) supplies additional assignments and storyboards. These entries are planned teaching scope, not delivered slides or completed code.

### PF-1–PF-4 — production-framework development (24 added hours)

| ID | Added hours | Attach to | Added teaching/evidence |
|---|---:|---|---|
| PF-1 | 8 | 03 and 06–10 | SGLang request, cache, and cancellation walkthrough with pinned source links and observed runtime state |
| PF-2 | 4 | 03 and PF-1 | vLLM V1 request-path and responsibility comparison; preserve all original vLLM operation and study |
| PF-3 | 8 | PF-1 and relevant mechanism lesson | Bounded SGLang patch, reproduction, focused regression coverage, and measured or state-based validation |
| PF-4 | 4 | December engine/GPU checkpoint | Two technical walkthrough/practice sessions with initial answers, corrections, and remaining gaps |
| **Total** | **24** | | |

Use the existing lesson format: motivating request/failure → state trace → source inspection → learner task → independent check → experiment/explanation. Follow the detailed handoff and acceptance rules in the supplement. SGLang is the deeper source-study target **within this added track**, not a replacement for any baseline vLLM/SGLang work. An upstream merge is not the December gate.

### AG-1 — CMU 11-768 agent-development extension (8 added hours)

Add to module 15's original **12 December hours**, giving **20 December hours** for that module plus its extension. Do not rewrite its existing tasks or reduce its January continuation. Preserve module 14, MCP tools and SDK work, step/token/time budgets, structured-output/XGrammar concepts, all trace/replay modes, and held-out evaluation.

- **AG-1a, 2 h:** implement a small decision/action/observation loop over supplied transport/tools; explain termination, tool-call linkage, recoverable errors, and budget exhaustion.
- **AG-1b, 3 h:** implement and inspect context compaction; preserve task constraints and complete recent tool interactions; retain full trajectories and record changed prompt/token identity.
- **AG-1c, 3 h:** challenge an evaluator with plausible wrong outputs, diagnose its mistakes, and improve a check without treating a judge as ground truth.

Use an additional inference-analysis agent over the existing documentation, read-only benchmark SQL, and constrained execution tools. Its teaching fixtures and full acceptance criteria are in [the supplement](../docs/PLAN_ADDITIONS.md). It supplements the original workloads and does not replace January quality evaluation.

References: [CMU 11-768](https://www.cmu-agents.com/), [Assignment 1: agent harness](https://github.com/cmu-agents/assignment-1/blob/main/ASSIGNMENT.md), and [Assignment 2: agent evaluation](https://github.com/cmu-agents/assignment-2/blob/main/ASSIGNMENT.md). Adapt selected methods with provenance; completing the entire course or its hosted deployments is not a new requirement.

### Combined accounting and delivery boundary

Baseline December modules retain **286 h**. PF-1–PF-4 add **24 h** and AG-1 adds **8 h**: **318 h through December**, plus unchanged **210 h January–April**, giving **528 h overall**. Record the supplements separately in the future catalog; do not count AG-1 both as an added task and as a rewritten 20-hour baseline module. New source stubs, individual lesson files, experiments, and HTML slides remain deferred.
