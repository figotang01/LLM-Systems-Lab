# Orientation, foundations and measurement

[Curriculum](../../../teaching/CURRICULUM.md) · [Teaching contract](../../../teaching/CONTRACT.md) · [Roadmap](../../../docs/execution/roadmap.md)

This guide groups existing module blueprints. Read only the module assigned by your current task. Module IDs, hours, objectives, exercises and exit gates are unchanged; HTML and runnable labs remain planned except the existing orientation.

Use the teaching contract for independent oracles, numerical/state examples, the explain/trace/predict/implement/measure rubric and one-week/one-month retrieval checks. Task briefs own implementation acceptance and authorship.

- [00 — Project map and measurement foundations (delivered)](#module-00)
- [01 — Tensor and numerical diagnostic (package A)](#module-01)
- [02 — GPU execution for a systems programmer (A + F)](#module-02)
- [03 — Measuring a serving system (B)](#module-03)

<a id="module-00"></a>
## 00 — Project map and measurement foundations (delivered)

**Status:** Delivered supplied orientation HTML; linked runtime exercises remain planned.

**Allocation:** Delivered orientation; no additional learner budget. Hours are owned by the roadmap.

**Concept prerequisites:** none. The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** define the project’s one central question, choose implementation ownership, distinguish timing/replay modes, and calculate KV/cost units.
- **Deck:** project identity → OS/distributed-systems analogies → fall/spring calendar → build/modify/operate/explain → request lifetime → prefill/decode → KV math and interactive capacity → physical pages/prefix identity → metric timeline and goodput → chunk-vs-token and replay modes → numerical correctness → GPU budget → AI workflow → first lab/quiz.
- **Code:** `starter/experiment.py`; inspect `budget()` and `create_bundle()`; supplied artifact support, not a benchmark implementation.
- **Exit:** compute 112 KiB/token, explain why two GPUs for three hours is six GPU-hours, and identify why fixed-length agent replay cannot validate task quality.

### Implementation connections

- [FND-01](../tasks/model.md#fnd-01) — Environment and minimal logical contracts; Modify + Explain.

**Design context:** [architecture](../ARCHITECTURE.md).

<a id="module-01"></a>
## 01 — Tensor and numerical diagnostic (package A)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 8 baseline h (A). Hours are owned by the roadmap.

**Concept prerequisites:** [00](foundations.md#module-00). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** trace attention dimensions and causal positions, identify where KV is reused, distinguish numerical and semantic failures.
- **Slides 1–8:** one five-token prompt; embeddings/QKV shapes; GQA head mapping; RoPE positions and QK norm. **9–18:** stable softmax, masks, prefill vs one-token decode, teacher-forced comparison. **19–28:** dtype error, argmax ties, sampling vs greedy and debugging examples.
- **Code:** supplied tiny model/config/weight fixtures; learner attention/cache append exercise. Use explicit head dimension, not a guessed `hidden_size/heads` value.
- **Experiment/exit:** compare uncached and incremental logits; catch a deliberately shifted RoPE position. Budget ~8 h refresher/diagnostic given your background; no full CS336 A1.
- **References:** CS336 resource accounting; model config and the archived v2 transformer references.

### December storyboard sequence

Attention shapes → GQA mapping → positions/RoPE → cached versus uncached execution → numerical discrepancies. Produce a teacher-forced comparison and diagnose a shifted-position fixture.

### Implementation connections

- [FND-01](../tasks/model.md#fnd-01) — Environment and minimal logical contracts; Modify + Explain.
- [FND-02](../tasks/model.md#fnd-02) — Numerical diagnostic and independent oracle; Build.
- [MOD-04](../tasks/model.md#mod-04) — Sampling and determinism exercise; Build + Explain.

**Design context:** [model-runtime](../design/model-runtime.md), [architecture](../ARCHITECTURE.md).

<a id="module-02"></a>
## 02 — GPU execution for a systems programmer (A + F)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 12 baseline h (A). Hours are owned by the roadmap.

**Concept prerequisites:** [01](foundations.md#module-01). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** explain grids/blocks/warps, memory hierarchy, coalescing, synchronization and asynchronous host behavior.
- **Slides 1–10:** CPU process/thread analogy and its limits; SIMT; global/shared/register memory. **11–20:** index mapping, bounds, coalescing, barriers, races. **21–34:** launch overhead, streams/events, host/device copies, arithmetic intensity, roofline and correct timing.
- **Code:** supplied CUDA/PyTorch-extension build setup and vector-add/reduction examples; learner changes indexing and fixes a race. Triton program IDs compared with CUDA blocks.
- **Experiment/exit:** predict a noncoalesced access pattern and a missing synchronization bug; distinguish enqueue time from completed device work. Use one tiny GPU session, not a training workload.
- **References:** CMU CUDA lectures; selected MIT accelerated-computing introductions. Budget ~12 h GPU foundations within A, deeper work in F.

### December storyboard sequence

Threads/warps → memory hierarchy → indexing/coalescing → synchronization → streams/events → timing. Modify supplied examples and explain an asynchronous timing error.

### Implementation connections

- [FND-03](../tasks/model.md#fnd-03) — GPU execution foundations; Modify + Explain.

**Design context:** [gpu-execution](../design/gpu-execution.md).

<a id="module-03"></a>
## 03 — Measuring a serving system (B)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 34 baseline h (B). Hours are owned by the roadmap.

**Concept prerequisites:** [00](foundations.md#module-00), [01](foundations.md#module-01). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** implement open/closed-loop load and trustworthy latency/goodput; recognize coordinated omission and client saturation.
- **Slides 1–10:** queue timeline, intended arrival vs dispatch, first useful content, completion/errors. **11–22:** SSE chunks, TPOT edge cases, SLO conjunction, throughput vs goodput, Little’s law. **23–36:** cache warmup, load sweeps, repeats, dependent observations and confidence intervals.
- **Code:** supply HTTP/SSE parser, fixtures, artifact/plot plumbing; learner `ArrivalSchedule`, `RequestObservation`, `aggregate_slo()` and saturation detection.
- **Experiment/exit:** recover known synthetic timings, count timeout/drop failures, cross-check one production run with AIPerf. A client dispatch cap must not silently alter the offered workload.
- **References:** AIPerf metric reference and arrival/replay docs; CS336 profiling problems.

<a id="metrics-worked-fixture"></a>
### Worked metric oracle for BEN-01

Use this synthetic one-second window `[0,1)` with all four requests offered and resolved inside it. All timestamps are seconds from one client clock. The fixture supplies exact first/last token events; real SSE chunks may support only approximate normalized timing, which must be labeled separately.

| Request | Scheduled | Dispatch | First token | Last token | Finish | Output count / outcome |
|---|---:|---:|---:|---:|---:|---|
| A | 0.00 | 0.00 | 0.10 | 0.30 | 0.31 | 5 / success |
| B | 0.05 | 0.20 | 0.25 | 0.25 | 0.26 | 1 / success |
| C | 0.10 | 0.10 | — | — | 0.60 | 0 / timeout |
| D | 0.10 | 0.10 | 0.35 | 0.55 | 0.56 | 3 / success |

Declare dispatch-based TTFT ≤0.20 s, TPOT ≤0.08 s when N≥2, and dispatch-to-finish E2E ≤0.50 s. For a one-token success, TPOT is ineligible rather than zero; TTFT/E2E still apply. A and B pass all eligible thresholds; D fails TTFT/TPOT and C fails completion. SLO attainment is `2/4 = 50%`; SLO goodput is `2/1 = 2 requests/s`. Successful-request throughput is 3 requests/s, a different metric.

Independent calculations: A TTFT=0.10, TPOT=(0.30−0.10)/4=0.05; B dispatch lag=0.15, client TTFT=0.05, offered-arrival TTFT=0.20; D TTFT=0.25 and TPOT=0.10. E2E values for A/B/D are 0.31/0.06/0.46. A timeout is never dropped from the offered denominator.

Broken variants: omit C (false attainment 2/3); report B's TPOT as zero (incorrect eligibility); call A's multi-token SSE chunk gaps exact token ITL after changing the event source; replace scheduled arrival with dispatch (hide B's client lag). Assertions should use explicit tolerances for floating-point arithmetic while keeping counts/outcomes exact. Timing definitions remain canonical in the [measurement contract](../engineering/measurement.md).

### December storyboard sequence

Request timeline → streaming observations → open/closed-loop load → failure accounting → SLO goodput → matched baselines. Produce validated metric calculations and vLLM/SGLang baseline bundles.

### Implementation connections

- [SRV-02](../tasks/gpu-serving.md#srv-02) — Metrics, observability and backend contract; Modify + Operate.
- [BEN-01](../tasks/benchmark.md#ben-01) — Streaming observations and metric definitions; Build.
- [BEN-02](../tasks/benchmark.md#ben-02) — Open-loop and closed-loop load; Build.
- [BEN-03](../tasks/benchmark.md#ben-03) — Matched vLLM and SGLang baselines; Operate both.

**Design context:** [serving](../design/serving.md), [measurement](../engineering/measurement.md).

<a id="module-15-replay"></a>
## Module 15 — performance replay portion (relocated)

Status: blueprint; executable lab/HTML planned. This retains the original module-15 replay work within package C, not a new charge. Agent loop/tool/live-quality teaching is now [AT-02/04](../../agents/CURRICULUM.md#module-15).

**Objectives:** preserve session dependencies; distinguish fixed-arrival transcript replay, dependency-aware transcript replay and live-agent execution. Fixed recorded prompts cannot validate fresh-output control flow. Token-count approximations and max_tokens do not guarantee the recorded output length.

**Preserved storyboard, formerly slides 23–38:** three modes → tool/think gaps → parent DAG → prompt content versus length → delayed child eligibility → failures/blocked descendants → contrast live branching. Inspect AIPerf replay, XPerf and AgentSysBench methods from the central references before capstone interpretation.

**Worked state trace:** parent completion at virtual time 20 plus recorded tool delay 10 makes its child eligible no earlier than 30. Contrast a fixed intended arrival at 5, then fail a required parent and show the explicit blocked-child/session outcome. Use a virtual clock, not sleeping tests.

**Code/ownership:** learner parent-dependency scheduling, supplied HTTP/fixture transport. [BEN-04](../tasks/benchmark.md#ben-04) consumes standalone SessionTrace fixtures under the [measurement contract](../engineering/measurement.md), never requiring the agent application.

**Exit:** intentionally delay a tool, verify child dispatch, reject missing parents/cycles, retain failure denominators, and explain fixed transcript versus fresh live behavior. Agent [AGT-04](../../agents/ROADMAP.md#agt-04) separately preserves original pilot/live evaluation.
