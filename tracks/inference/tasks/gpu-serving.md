# GPU execution and serving — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="gpu-01"></a>
## GPU-01 — Online softmax and direct paged backend

**Status:** planned. **Package:** F. **Milestone:** CP2.

**Requirement/design:** [GPU-1](../design/gpu-execution.md#gpu-1) — [canonical design](../design/gpu-execution.md). **Learning mode:** Modify + Integrate. **Authorship target:** learner metadata/softmax work; backend wrapper supplied.

**Dependencies:** [FND-03](model.md#fnd-03), [KV-02](memory-cache.md#kv-02), [MOD-02](model.md#mod-02).

**Teaching:** [11](../curriculum/gpu-serving.md#module-11).

**Planned change boundary:** `src/inferstack/backends/flashinfer/attention.py`, `src/inferstack/backends/flashinfer/executor.py`, `tests/gpu/test_paged_backend.py`

**Work:**

- [ ] Complete the tiled forward accumulator/rescaling exercise and explain split-KV.
- [ ] Adapt logical metadata to pinned FlashInfer prefill/decode layout; smoke-test dtype, page size, GQA, tails and workspace compatibility before sweeps.

**Validation / acceptance:**

- [ ] Tiny FP32 reference and GPU tolerance suite pass, including page-crossing and invalid-layout fixtures.
- [ ] Actual direct paged reads are demonstrated on recorded hardware; no gathered-reference throughput claim.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="gpu-02"></a>
## GPU-02 — Triton normalization and CUDA C++ modification

**Status:** planned. **Package:** F. **Milestone:** CP2.

**Requirement/design:** [GPU-2](../design/gpu-execution.md#gpu-2) — [canonical design](../design/gpu-execution.md). **Learning mode:** Build + Modify. **Authorship target:** learner Triton; learner-modified supplied CUDA baseline.

**Dependencies:** [FND-03](model.md#fnd-03), [MOD-01](model.md#mod-01).

**Teaching:** [12](../curriculum/gpu-serving.md#module-12).

**Planned change boundary:** `src/inferstack/backends/kernels/rmsnorm.py`, `src/inferstack/backends/kernels/rmsnorm.cu`, `src/inferstack/backends/kernels/bindings.cpp`, `tests/gpu/test_normalization.py`

**Work:**

- [ ] Author one RMSNorm or fused residual/RMSNorm kernel and change the supplied CUDA counterpart/launch parameters.
- [ ] Benchmark eager PyTorch, torch.compile and both kernels after warmup, explaining fusion bytes and reduction/accumulation.

**Validation / acceptance:**

- [ ] Independent tail/dtype/epsilon checks pass before timing.
- [ ] Report bandwidth/latency with synchronization and shape context; separate authorship and modified scaffolding.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="gpu-03"></a>
## GPU-03 — Graph buffers, buckets and bounded overlap

**Status:** planned. **Package:** F. **Milestone:** CP2.

**Requirement/design:** [GPU-3](../design/gpu-execution.md#gpu-3) — [canonical design](../design/gpu-execution.md). **Learning mode:** Modify. **Authorship target:** learner-modified; lifecycle/stream shell supplied.

**Dependencies:** [GPU-01](gpu-serving.md#gpu-01).

**Teaching:** [13](../curriculum/gpu-serving.md#module-13).

**Planned change boundary:** `src/inferstack/backends/cuda_graphs/runner.py`, `tests/gpu/test_graphs.py`

**Work:**

- [ ] Define stable buffer refresh, capture/replay/invalidation and bucket padding; fallback to eager for unsupported combinations.
- [ ] Use streams/events in a bounded overlap exercise without expanding the required runtime to a full asynchronous pipeline.

**Validation / acceptance:**

- [ ] Eager/graph numeric checks pass; stale inputs and dummy live-KV writes are detected.
- [ ] Account for graph memory and show when padding/capture overhead can lose.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="srv-01"></a>
## SRV-01 — HTTP/SSE and cancellation integration

**Status:** planned. **Package:** F. **Milestone:** CP2.

**Requirement/design:** [SRV-1](../design/serving.md#srv-1) / [SRV-2](../design/serving.md#srv-2) / [RUN-1](../design/model-runtime.md#run-1) — [canonical design](../design/serving.md). **Learning mode:** Modify + Build lifecycle. **Authorship target:** learner lifecycle; transport/tokenization supplied.

**Dependencies:** [SCH-05](scheduler.md#sch-05), [GPU-01](gpu-serving.md#gpu-01).

**Teaching:** [13](../curriculum/gpu-serving.md#module-13).

**Planned change boundary:** `src/inferstack/serving/http.py`, `src/inferstack/serving/events.py`, `tests/serving/test_stream_lifecycle.py`

**Work:**

- [ ] Document and implement the bounded API capability contract through supplied HTTP/SSE code.
- [ ] Propagate disconnect/deadline/cancel to the coordinator; support finish/error/usage semantics and reject unsupported fields.

**Validation / acceptance:**

- [ ] One-token, empty metadata, normal finish, partial stream failure and disconnect fixtures yield correct outcomes/cleanup.
- [ ] Transport cannot free pages directly or invent exact token timestamps from chunks.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="gpu-04"></a>
## GPU-04 — End-to-end profile and baseline gap

**Status:** planned. **Package:** F. **Milestone:** CP2.

**Requirement/design:** [GPU-4](../design/gpu-execution.md#gpu-4) — [canonical design](../design/gpu-execution.md). **Learning mode:** Operate + Explain. **Authorship target:** learner analysis; profiler/report plumbing supplied.

**Dependencies:** [GPU-02](gpu-serving.md#gpu-02), [GPU-03](gpu-serving.md#gpu-03), [SRV-01](gpu-serving.md#srv-01), [BEN-03](benchmark.md#ben-03).

**Teaching:** [13](../curriculum/gpu-serving.md#module-13).

**Planned change boundary:** `src/inferstack/backends/profiling.py`

**Work:**

- [ ] Integrate the selected kernel and graph path; inspect Nsight Systems launch gaps and Nsight Compute for one kernel.
- [ ] Run same-model custom-runtime versus production baseline with matched settings and profiler-free headline timing.

**Validation / acceptance:**

- [ ] Raw runs and annotated profiles explain at least one measured gap or negative result.
- [ ] No mandatory performance percentage; microkernel speedup is not reported as unmeasured end-to-end gain.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="srv-02"></a>
## SRV-02 — Metrics, observability and backend contract

**Status:** planned. **Package:** B / F / G. **Milestone:** CP2; January gateway/replica integration is PLT-03.

**Requirement/design:** [SRV-3](../design/serving.md#srv-3) — [canonical design](../design/serving.md). **Learning mode:** Modify + Operate. **Authorship target:** learner semantics; dashboards/SDK adapters supplied.

**Dependencies:** [SRV-01](gpu-serving.md#srv-01), [BEN-03](benchmark.md#ben-03).

**Teaching:** [03](../curriculum/foundations.md#module-03), [13](../curriculum/gpu-serving.md#module-13), [17](../curriculum/platform.md#module-17).

**Planned change boundary:** `src/inferstack/serving/metrics.py`, `deploy/observability/collectors.yaml`, `tests/serving/test_backend_contract.py`

**Work:**

- [ ] Normalize units/labels/capabilities for selected servers and record actual metric freshness and meaning.
- [ ] Modify one dashboard query and explain one OpenTelemetry trace; contract-test streams/disconnects and the pinned model-server adapter.

**Validation / acceptance:**

- [ ] Known metric fixtures expose unit/name mismatches; queue, utilization and locality are not conflated.
- [ ] Real-backend contract status is recorded per engine; simulator conformance alone cannot establish it.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
