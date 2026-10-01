# InferStack: December codebase and teaching skeleton

Recorded 2026-09-29 from the first detailed skeleton approved in the planning conversation. This is the baseline blueprint, preserved in full below; the later condensed restatement does not supersede it. All paths, stubs, storyboards, and runtime deliverables described below are **planned**, unless explicitly identified as already delivered. This documentation pass does not create source stubs or HTML lessons.

Read alongside the authoritative [project plan](../PROJECT_PLAN.md), existing [teaching curriculum](../teaching/CURRICULUM.md), and [append-only supplements](PLAN_ADDITIONS.md). The baseline's 286 December hours remain intact; the supplements add 32 hours, giving 318 December hours and 528 overall. Existing InferLab names in older files are retained to preserve their contents; InferStack is the current project name.

---

## 1. Deliverable and scope

Create a **blueprint plus thin interface stubs** for the December project. Supply lesson storyboards and bounded implementation assignments that you or another agent can complete independently.

The skeleton pass will produce architecture, contracts, directory structure, task descriptions, and acceptance criteria. It will **not implement the inference engine, integrations, benchmark algorithms, or HTML lessons**.

Preserve the existing December target:

- A correct dense-model runtime with paged KV memory, continuous batching, chunked prefill, recompute preemption, and both prefix indexes.
- FlashInfer integration, one authored Triton kernel, a modified CUDA C++ kernel, CUDA Graphs, and profiling.
- Comparable vLLM/SGLang baselines and trustworthy measurement.
- Initial RAG/MCP traces and replay.
- A local Kubernetes gateway with simulated replicas and a custom Go routing scorer.

January–May features receive documented extension boundaries, without unused implementation stubs.

**Defaults:** InferStack branding; Python for runtime, measurement, and workloads; CUDA C++/Triton for kernel work; Go for routing; one dense Qwen3 model family; one model per runtime process. Preserve the existing estimate of **286 learner hours through December 20**, including lessons, coding, debugging, and experiments.

## 2. Codebase architecture

### Repository structure

Use one installable Python package with a `src` layout. Keep Go and deployment assets outside that package.

```text
PROJECT_PLAN.md                  Authoritative scope, schedule, completion gates
README.md                        Project overview and shortest working paths

src/inferstack/
  contracts/                     Requests, state, execution plans, events, protocols
  engine/
    model/                       Dense transformer operations and sampling
    memory/                      Page allocation, ownership, mappings, accounting
    scheduling/                  Admission, batching, chunking, preemption
    prefix/                      Shared interface; hash and radix implementations
    runtime/                     Request lifecycle and execution coordination
  backends/
    fake/                        Deterministic logical executor
    torch_reference/             Readable numerical execution path
    flashinfer/                  Direct paged attention adapter
    cuda_graphs/                 Capture, buffers, buckets, replay
    kernels/                     Triton implementation and CUDA extension
  serving/                       HTTP/SSE, tokenizer/loading adapters, metrics
  bench/                         Arrivals, observations, metrics, replay, reporting
  workloads/                     RAG path, thin MCP agent, trace capture

routing/
  scorer/                        Independent Go policy and tests
  epp/                           Version-specific endpoint-picker integration

deploy/
  local/                         kind, gateway, simulated replicas
  engines/                       Separate vLLM and SGLang launch configurations
  observability/                 Prometheus/Grafana and trace configuration

configs/                         Small, named, reproducible experiment profiles
environments/                    Separate dependency sets and compatibility records
tests/                           Contract, unit, integration, and GPU tests

teaching/
  catalog.yaml                   Module IDs, prerequisites, hours, ownership, status
  modules/<id>/
    README.md                    Learning objectives and implementation assignment
    storyboard.md                Sequenced teaching content
    reading.md                   Required sections and pinned source references
    fixtures/                    Small deterministic examples, when implemented
    reference/                   Isolated annotated solutions, when supplied
  slides/                        Existing lesson 00; later HTML delivery

docs/
  architecture/                  Boundaries, lifecycle diagrams, design decisions
  handoff/                       Dependency order, compatibility, evidence checklist
  archive/                       Historical plans

starter/                         Preserve existing artifact/budget utility
results/                         Generated experiment bundles; no invented results
```

Create directories only when they contain a contract, explanatory document, or useful stub. Do not populate the repository with empty advanced-feature packages.

### Dependency rules

The dependency direction is:

```text
HTTP / workloads / benchmark clients
                 ↓
         runtime coordinator
                 ↓
       scheduler + memory + prefix
                 ↓
          execution interface
                 ↓
  fake / PyTorch / FlashInfer + graphs
```

- Core state, allocator metadata, and scheduling logic must import without CUDA, FlashInfer, Kubernetes, or model downloads.
- Backend-specific tensors, workspaces, and vendor APIs remain behind adapters.
- The benchmark communicates with serving endpoints; it must not import scheduler internals to calculate client latency.
- The Go scorer must be testable without Kubernetes. Its EPP wrapper translates external objects into the scorer’s own inputs.
- Teaching modules import the main implementation. Small exercises illustrate mechanisms; they must not become separate full runtimes.
- Production code must never import teaching reference solutions.
- Preserve the starter utility as the bundle creator. Benchmark commands accept an existing output directory rather than duplicating its artifact-management logic.

### Minimum contracts to freeze

Define these contracts before assigning implementation tasks:

| Contract | Responsibility |
|---|---|
| `ModelSpec` / `CacheIdentity` | Model/tokenizer revisions, architecture dimensions, KV representation, adapter identity, and namespace |
| `GenerationRequest` / `RequestState` | Input tokens, generation limits, lifecycle, computed-token count, emitted tokens, and termination reason |
| `BlockPool` / `BlockLease` | Reserve, share, copy-on-write, retain, release, and inspect page ownership |
| `PrefixIndex` | Match, acquire reusable blocks, publish completed prefixes, release references, and evict |
| `Scheduler` / `StepPlan` | Select work under token and memory budgets; describe prefill/decode positions and preemption decisions |
| `Executor` / `StepResult` | Execute a prepared step and return completion information without owning request lifecycle |
| `ServingEvent` / `RequestObservation` | Separate server execution events from client timing observations |
| `SessionTrace` / `ReplayPolicy` | Preserve prompts, parent dependencies, tool delays, and replay mode |
| Go `RoutingPolicy` | Rank eligible endpoints using load, estimated reuse, affinity, and metric freshness |

Stubs contain typed signatures, field documentation, preconditions, postconditions, and explicit `NotImplementedError` bodies. They must not return fabricated outputs.

### Ownership and correctness decisions

These rules prevent the most expensive integration mistakes:

1. **One coordinator owns state mutation.** HTTP handlers submit requests and cancellations; they never free KV pages or modify scheduling queues directly.
2. **Separate planned, computed, and emitted tokens.** A sampled token may already have been emitted while its KV has not yet been computed. Recompute preemption preserves the existing token sequence and resumes computation without re-emitting or re-sampling prior output.
3. **Plan, reserve, execute, commit.** The scheduler proposes work; the coordinator reserves resources, executes it, and commits completed state. Failed reservations do not leave partial ownership changes.
4. **Cancellation respects in-flight execution.** Mark cancellation immediately, suppress subsequent output, and reclaim pages only when the relevant GPU work can no longer access them. Start with one execution step in flight.
5. **Both prefix indexes share one ownership model.** Use the same page pool, page size, reusable-token rules, and eviction eligibility. Compare indexing independently of scheduling policy.
6. **Publish only completed, immutable full pages.** Request-local partial tails remain writable under copy-on-write rules. For a full-prompt cache hit, recompute the necessary final position to obtain logits; cached KV alone does not provide the next-token distribution.
7. **Keep physical layouts inside backend boundaries.** FlashInfer receives translated page metadata; its wrapper types must not become the public scheduler API. Its documented paged prefill/decode interfaces support this adapter boundary. [FlashInfer attention API](https://docs.flashinfer.ai/api/attention.html)

### Serving, measurement, and routing boundaries

**Serving:** support a documented subset of completions/chat completions, streaming, usage, finish reasons, errors, and cancellation. Greedy generation is the integration baseline; basic sampling remains a separate model exercise. Reject unsupported options explicitly. Full tool-call formatting and structured-output integration belong to the production-engine workload path.

**Measurement:** retain offered arrival, dispatch, first/last content, completion, failures, and count sources. Compute durations within a declared clock domain. Treat SSE chunk gaps separately from token timing. Report both successful-request latency and outcomes over all offered requests.

**Replay:** implement fixed-arrival replay and dependency-aware transcript replay as separate policies. Live agent execution generates traces and evaluates behavior; replay does not substitute for task-quality evaluation.

**Routing:** deploy one Gateway/EPP implementation. Use the existing llm-d inference simulator for HTTP replicas rather than building another simulated server; it already provides configurable cache behavior and metrics. Keep it distinct from the logical executor used in scheduler tests. [llm-d simulator](https://github.com/llm-d/llm-d-inference-sim/blob/main/docs/kv-cache.md)

The custom Go policy will:

- Exclude unready endpoints.
- Prefer fresh load information and bound the extra queueing allowed for affinity.
- Use explicitly estimated prefix locality and session affinity.
- Fall back to load-based selection when locality is unavailable, and round-robin among healthy endpoints when all load metrics are stale.
- Invalidate endpoint-local history after restart.
- Return decision reasons for inspection.

The EPP integration remains a thin adapter because endpoint selection and gateway forwarding have distinct responsibilities. [Gateway architecture](https://gateway-api-inference-extension.sigs.k8s.io/)

December locality estimates will use bounded request history, explicitly labeled approximate. A real cache-event index belongs to the later platform work.

## 3. Teaching scope and storyboards

### Standard lesson structure

Every storyboard specifies this sequence:

1. **Prerequisite check:** a short diagnostic and the required earlier artifacts.
2. **Concrete problem:** one request, workload, or failure that motivates the topic.
3. **State trace:** diagrams and a hand-worked example before implementation.
4. **Mechanism:** equations, dimensions, units, ownership, and assumptions.
5. **Code walkthrough:** the exact production module and relevant external reference.
6. **Failure investigation:** two misconceptions and one deliberately broken fixture.
7. **Learner assignment:** implementation boundaries, supplied code, and independent oracle.
8. **Experiment and explanation:** a bounded comparison, expected questions, and an exit demonstration.

Specify each diagram’s states and each numerical example’s inputs and expected reasoning. Leave prose expansion, visual styling, and HTML construction to the lesson-writing agent.

Retain the existing offline HTML requirements: keyboard navigation, reading/print views, expandable notes and answers, accessible controls, and no required CDN.

### December module map

Hours below partition the existing 286-hour budget; they are not additional assignments.

| Module | Hours | Storyboard progression and required evidence |
|---|---:|---|
| **01 · Tensor and numerical diagnostic** | 8 | Attention shapes → GQA mapping → positions/RoPE → cached versus uncached execution → numerical discrepancies. Produce a teacher-forced comparison and diagnose a shifted-position fixture. |
| **02 · GPU execution foundations** | 12 | Threads/warps → memory hierarchy → indexing/coalescing → synchronization → streams/events → timing. Modify supplied examples and explain an asynchronous timing error. |
| **03 · Serving measurement** | 34 | Request timeline → streaming observations → open/closed-loop load → failure accounting → SLO goodput → matched baselines. Produce validated metric calculations and vLLM/SGLang baseline bundles. |
| **04 · Dense runtime** | 30 | Request walkthrough → RMSNorm/GQA/RoPE/QK norm/SwiGLU → contiguous KV → prefill/decode → sampling. Implement model operations and compare layer outputs against an independent reference. |
| **05 · Memory accounting** | 8 | Weight/KV formulas → live versus reserved memory → workspace/graphs → fragmentation → model fit. Produce predictions and measured allocation breakdowns. |
| **06 · Paged ownership** | 34 | Logical-to-physical mapping → allocation → append/share/fork → copy-on-write → exhaustion/release. Implement the pool and gathered oracle; demonstrate conservation under randomized transitions. |
| **07 · Iteration scheduling** | 16 | Static batching → request states → token budgets → admission/backfill → fairness. Trace a small workload manually and reproduce it with the logical executor. |
| **08 · Chunking and lifecycle** | 14 | Long-prefill interference → chunk packing → recompute preemption → cancellation races → deferred cleanup. Demonstrate correct continuation and no page leaks. |
| **09 · Hash prefix cache** | 10 | Prefix ancestry → identity → immutable pages → ownership/eviction → full-hit logits. Implement reuse and show isolation misses and cold/warm behavior. |
| **10 · Radix prefix cache** | 14 | Compressed edges → match/split/insert → locks → eviction → fair comparison. Implement the same prefix contract and isolate index effects from policy effects. |
| **11 · GPU attention** | 20 | Attention IO → online softmax → tiled accumulation → causal boundaries → paged layouts → FlashInfer adapter. Complete the numerical exercise and validate direct paged reads. |
| **12 · Triton and CUDA C++** | 18 | RMSNorm → reduction/masking → accumulation dtype → CUDA equivalent → fusion/launch parameters → roofline. Author one Triton kernel, modify the CUDA version, and compare correctness and timing. |
| **13 · Graphs and profiling** | 16 | Launch gaps → static buffers → capture/replay → bucket padding → stream dependencies → end-to-end impact. Integrate graph execution and HTTP transport; produce correctness checks and annotated profiles. |
| **14 · Initial RAG workload** | 8 | Corpus/chunk identity → dense/BM25 retrieval → RRF/reranking → prompt construction → stage timing. Adapt the supplied pipeline and capture a small trace pilot. Full retrieval/answer-quality ablations continue in January. |
| **15 · MCP and replay** | 12 | Thin agent loop → tool/schema failures → budgets → trace dependencies → transcript replay versus live execution. Capture deterministic tool scenarios and validate child-dispatch timing. Broader task evaluation continues in January. |
| **16 · Kubernetes foundations and local lab** | 20 | Reconciliation → pods/services → readiness/resources → selectors/RBAC → deployment diagnosis. Split into 12 hours of foundations and an 8-hour simulator deployment lab. |
| **17 · Gateway and Go scorer** | 12 | Gateway/EPP boundaries → endpoint observations → locality/load trade-off → stale metrics → policy tests → adapter integration. Demonstrate decisions across two simulated replicas. |
| **Total** | **286** | |

Lesson 00 remains the delivered orientation. Teach Kubernetes foundations before the deployment lab; begin production-engine measurement before optimizing the custom engine.

### Learner and agent responsibilities

**Learner-owned mechanisms:** numerical reasoning, allocator ownership, scheduling, cache indexes, metric definitions, Triton kernel, routing policy, experimental interpretation.

**Agent-supplied or adapted infrastructure:** checkpoint mapping, tokenizer plumbing, HTTP/SSE transport, CUDA build setup, graph lifecycle shell, deployment manifests, dashboards, RAG/MCP wrappers, plotting, and artifact formatting.

Every supplied component includes one modification task and one failure explanation. Reference solutions stay available but separate from the normal implementation path.

## 4. Handoff structure and execution order

Each module assignment must contain:

- Prerequisites and exact modules it may modify.
- Public contracts it must preserve.
- A bounded implementation checklist.
- Supplied fixtures and independent correctness oracles.
- Required commands, hardware class, and expected artifact types.
- Explicit exclusions and remaining January work.
- Completion evidence and ownership attribution.

Use these implementation waves:

| Wave | Deliverable and gate |
|---|---|
| **0 · Skeleton** | Importable contracts, module briefs, storyboards, dependency boundaries, and documented unfinished components. No inference claims. |
| **1 · Measurement and model** | Valid timing fixtures, both production baselines, single-request model, contiguous-cache correctness. |
| **2 · Memory and scheduling** | Paged allocation, continuous batching, chunking, preemption, cancellation, and both prefix indexes under CPU-driven tests. |
| **3 · GPU integration** | FlashInfer path, Triton/CUDA exercise, graph execution, streaming service, and measured comparisons. |
| **4 · Workloads and routing** | Initial RAG/MCP traces, replay validation, local Kubernetes replicas, and integrated Go scorer. |
| **5 · December checkpoint** | Reproduction instructions, evidence inventory, known limitations, and explicit January backlog. |

A later agent receives one assignment plus its contracts and prerequisites, rather than repeatedly ingesting the entire planning archive.

### Environment and later-extension decisions

- Separate CPU development, custom GPU runtime, production-engine images, and Go/platform dependencies.
- Record tested dependency sets after smoke tests; do not call independently selected “latest” versions compatible.
- Make lightweight CPU checks the default. GPU, model-download, and Kubernetes checks require explicit selection.
- Keep experiments sequential on the 16 GB Mac and rented GPU; do not require the complete stack to run simultaneously.

Reserve these future boundaries without implementing them:

| Later topic | December boundary that enables it |
|---|---|
| Quantization | Model loading and kernel/backend selection |
| Speculative decoding | Token commitment and KV rollback semantics |
| Distributed execution / TP / EP | Executor boundary; December remains single-device |
| KV offload | Explicit memory ownership and transfer completion |
| Autoscaling and real GPU replicas | Endpoint observations, deployment profiles, readiness |
| P/D disaggregation | Documented prefill/decode state and ownership; no premature transfer framework |

## 5. Acceptance and validation

### Skeleton acceptance

- Core contracts import on the Mac without CUDA or downloaded weights.
- Existing starter tests and CLI behavior remain intact.
- Stub methods fail explicitly; no fake successful inference or benchmark output.
- Every December module maps to code ownership, a storyboard, a lab, and evidence.
- The module-hour total remains 286.
- Lesson references resolve to planned or existing targets with status clearly identified.
- Active documentation uses InferStack; archived material remains historical.
- January features are identified as future work rather than appearing complete.

### Implementation acceptance specified for later agents

- **Numerical:** uncached/cached, contiguous/paged, chunked/unchunked, and recompute/resume comparisons.
- **Ownership:** shared tails, exhaustion, repeated cancellation, eviction while referenced, and cleanup after in-flight completion.
- **GPU:** page boundaries, unusual tensor tails, graph padding, eager/graph equivalence, and profiler-free timing runs.
- **Measurement:** multi-token chunks, one-token outputs, delayed dispatch, timeout/rejection accounting, and dependent-session replay.
- **Routing:** equal-load ties, overloaded affinity target, stale observations, worker restart, and no healthy endpoints.
- **Teaching:** one complete offline lesson can be authored from its storyboard without inventing the mechanism, examples, or lab requirements.

No throughput target or positive speedup is required. December completion requires correct behavior, reproducible measurements, and explanations that connect the implementation to the observed result.

---

## Append-only supplement cross-reference

The approved [production-framework and CMU agent supplements](PLAN_ADDITIONS.md) add 32 learner hours to this baseline. All baseline contracts, tasks, hours, and spring topics above remain. The append-only preservation instruction takes precedence over the earlier branding-cleanup acceptance item: existing files are not rewritten just to replace InferLab with InferStack. Source stubs and per-module storyboards remain future deliverables; this file records their specification only.
