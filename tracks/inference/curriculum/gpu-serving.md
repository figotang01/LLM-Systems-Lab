# GPU execution, kernels and serving

[Curriculum](../../../teaching/CURRICULUM.md) · [Teaching contract](../../../teaching/CONTRACT.md) · [Roadmap](../../../docs/execution/roadmap.md)

This guide groups existing module blueprints. Read only the module assigned by your current task. Module IDs, hours, objectives, exercises and exit gates are unchanged; HTML and runnable labs remain planned except the existing orientation.

Use the teaching contract for independent oracles, numerical/state examples, the explain/trace/predict/implement/measure rubric and one-week/one-month retrieval checks. Task briefs own implementation acceptance and authorship.

- [11 — Online softmax and paged GPU attention (F)](#module-11)
- [12 — Triton and CUDA C++ through one useful kernel (F)](#module-12)
- [13 — Graph capture, overlap and profiling (F)](#module-13)

<a id="module-11"></a>
## 11 — Online softmax and paged GPU attention (F)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 20 baseline h (F). Hours are owned by the roadmap.

**Concept prerequisites:** [02](foundations.md#module-02), [06](runtime.md#module-06). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** derive streaming softmax accumulation and connect algorithm/layout to the attention backend.
- **Slides 1–12:** attention IO cost; running maximum and denominator; rescale old accumulator when max increases. **13–24:** tiled forward, causal boundaries, numerical tests and split-KV decode. **25–38:** paged layouts, last-page length, GQA, plan/run workspace and backend compatibility.
- **Code:** supplied partial tiled forward and FlashInfer wrapper; learner completes accumulator update and paged metadata adapter.
- **Experiment/exit:** compare against tiny FP32 reference then GPU tolerance; trace a sequence crossing a page boundary. Full optimized FlashAttention implementation is an extension.
- **References:** FlashAttention papers, FlashInfer API, selected CS336 systems exercise.

### December storyboard sequence

Attention IO → online softmax → tiled accumulation → causal boundaries → paged layouts → FlashInfer adapter. Complete the numerical exercise and validate direct paged reads.

### Implementation connections

- [GPU-01](../tasks/gpu-serving.md#gpu-01) — Online softmax and direct paged backend; Modify + Integrate.

**Design context:** [gpu-execution](../design/gpu-execution.md).

<a id="module-12"></a>
## 12 — Triton and CUDA C++ through one useful kernel (F)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 18 baseline h (F). Hours are owned by the roadmap.

**Concept prerequisites:** [02](foundations.md#module-02), [04](runtime.md#module-04). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** write normalization, explain fusion and recognize bandwidth/occupancy limits.
- **Slides 1–10:** RMSNorm equation, reduction, epsilon and accumulation dtype. **11–22:** Triton program mapping/masking; CUDA warp/block version; launch configuration. **23–36:** fusion bytes saved, roofline, eager/compile comparisons, shape/dtype tests.
- **Code:** learner Triton kernel; supplied CUDA baseline and extension build, learner substantive change and comparison. CUDA is retained without making build-system debugging the main assignment.
- **Experiment/exit:** correct tails and dtypes, microbenchmark with warmup and device synchronization; check if the engine gets faster.
- **Reference:** Triton layer-normalization tutorial, adapted with the RMSNorm distinction explained.

### December storyboard sequence

RMSNorm → reduction/masking → accumulation dtype → CUDA equivalent → fusion/launch parameters → roofline. Author one Triton kernel, modify the CUDA version, and compare correctness and timing.

### Implementation connections

- [GPU-02](../tasks/gpu-serving.md#gpu-02) — Triton normalization and CUDA C++ modification; Build + Modify.

**Design context:** [gpu-execution](../design/gpu-execution.md).

<a id="module-13"></a>
## 13 — Graph capture, overlap and profiling (F)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 16 baseline h (F). Hours are owned by the roadmap.

**Concept prerequisites:** [11](gpu-serving.md#module-11), [12](gpu-serving.md#module-12). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** interpret CPU/GPU timelines; safely manage graph buffers; understand streams/events.
- **Slides 1–10:** host launches, GPU idle gaps, Amdahl’s law. **11–24:** capture/replay, static addresses, bucket padding, dummy KV writes, invalidation. **25–36:** event dependencies, next-batch preparation, Nsight Systems vs Compute and profiler overhead.
- **Code:** supplied graph lifecycle and profiler scripts; learner buffer updates/bucket policy; bounded overlap example rather than a mandatory fully async engine.
- **Experiment/exit:** eager-vs-graph across batch sizes with equal math; explain when padding or graph memory loses.

### December storyboard sequence

Launch gaps → static buffers → capture/replay → bucket padding → stream dependencies → end-to-end impact. Integrate graph execution and HTTP transport; produce correctness checks and annotated profiles.

### Implementation connections

- [GPU-03](../tasks/gpu-serving.md#gpu-03) — Graph buffers, buckets and bounded overlap; Modify.
- [SRV-01](../tasks/gpu-serving.md#srv-01) — HTTP/SSE and cancellation integration; Modify + Build lifecycle.
- [GPU-04](../tasks/gpu-serving.md#gpu-04) — End-to-end profile and baseline gap; Operate + Explain.
- [SRV-02](../tasks/gpu-serving.md#srv-02) — Metrics, observability and backend contract; Modify + Operate.

**Design context:** [gpu-execution](../design/gpu-execution.md), [serving](../design/serving.md).
