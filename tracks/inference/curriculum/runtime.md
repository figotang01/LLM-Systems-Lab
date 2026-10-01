# Model execution, memory and scheduling

[Curriculum](../../../teaching/CURRICULUM.md) · [Teaching contract](../../../teaching/CONTRACT.md) · [Roadmap](../../../docs/execution/roadmap.md)

This guide groups existing module blueprints. Read only the module assigned by your current task. Module IDs, hours, objectives, exercises and exit gates are unchanged; HTML and runnable labs remain planned except the existing orientation.

Use the teaching contract for independent oracles, numerical/state examples, the explain/trace/predict/implement/measure rubric and one-week/one-month retrieval checks. Task briefs own implementation acceptance and authorship.

- [04 — A single-request dense runtime (D)](#module-04)
- [05 — Memory accounting and cache lifetime (D)](#module-05)
- [06 — Paged ownership, refcounts and copy-on-write (D)](#module-06)
- [07 — Iteration scheduling and continuous batching (E)](#module-07)
- [08 — Chunked prefill, preemption and cancellation (E)](#module-08)

<a id="module-04"></a>
## 04 — A single-request dense runtime (D)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 30 baseline h (D). Hours are owned by the roadmap.

**Concept prerequisites:** [01](foundations.md#module-01). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** implement the decoder path and cache state while using a supplied checkpoint loader.
- **Slides 1–8:** full request trace and model architecture. **9–22:** RMSNorm, RoPE, QK norm, GQA, SwiGLU, output projection and sampling. **23–34:** weight shapes/tied embeddings, prefill/decode interface, logits inspection and reference comparisons.
- **Code:** supplied safetensors/name mapping/tokenizer/CLI; learner model operations and cache writes. Support one dense revision first.
- **Experiment/exit:** fixed-token per-layer comparisons and a small greedy suite; explain one mismatch from tensor shape or position rather than chasing generated text.

### December storyboard sequence

Request walkthrough → RMSNorm/GQA/RoPE/QK norm/SwiGLU → contiguous KV → prefill/decode → sampling. Implement model operations and compare layer outputs against an independent reference.

### Implementation connections

- [MOD-01](../tasks/model.md#mod-01) — Dense model operations and loader boundary; Build + Modify.
- [MOD-02](../tasks/model.md#mod-02) — Contiguous KV prefill and incremental decode; Build.
- [MOD-04](../tasks/model.md#mod-04) — Sampling and determinism exercise; Build + Explain.

**Design context:** [model-runtime](../design/model-runtime.md).

<a id="module-05"></a>
## 05 — Memory accounting and cache lifetime (D)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 8 baseline h (D). Hours are owned by the roadmap.

**Concept prerequisites:** [04](runtime.md#module-04). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** distinguish live KV, reserved capacity, weights, activations and graph/workspace allocation.
- **Slides 1–10:** KV formula, bytes/units, context/concurrency trade-off; MHA/MQA/GQA. **11–20:** allocator-reserved vs live tensors, peak measurement, fragmentation, model fit. **21–28:** MLA/hybrid exceptions, MoE active-vs-resident weights.
- **Code:** learner config-aware dense `kv_calculator`; supplied config fixtures and device-memory collection.
- **Experiment/exit:** predict and measure context-length memory; reject unsupported hybrid configs with a clear explanation. No claim to support all architectures.

### December storyboard sequence

Weight/KV formulas → live versus reserved memory → workspace/graphs → fragmentation → model fit. Produce predictions and measured allocation breakdowns.

### Implementation connections

- [MOD-03](../tasks/model.md#mod-03) — Memory accounting; Build.

**Design context:** [model-runtime](../design/model-runtime.md).

<a id="module-06"></a>
## 06 — Paged ownership, refcounts and copy-on-write (D)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 34 baseline h (D). Hours are owned by the roadmap.

**Concept prerequisites:** [04](runtime.md#module-04), [05](runtime.md#module-05). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** implement pool/tables/mappings with precise ownership and read-path correctness.
- **Slides 1–10:** OS virtual-memory analogy; logical token → logical page → physical page/slot. **11–22:** allocate/append/fork/share/free and partial-page copy-on-write. **23–36:** property/state-machine tests, capacity, reference gather vs direct paged read.
- **Code:** supply fixtures/state visualizer; learner block pool, block tables, writes and gathered attention oracle. Inject exhaustion and stale page IDs.
- **Experiment/exit:** randomized transitions conserve pages and preserve output; demonstrate the shared-tail bug before fixing it.
- **References:** PagedAttention; compact reference engines. The OS analogy does not imply hardware page faults or general-purpose virtual memory.

### December storyboard sequence

Logical-to-physical mapping → allocation → append/share/fork → copy-on-write → exhaustion/release. Implement the pool and gathered oracle; demonstrate conservation under randomized transitions.

### Implementation connections

- [KV-01](../tasks/memory-cache.md#kv-01) — Pool ownership and transactional reservation; Build.
- [KV-02](../tasks/memory-cache.md#kv-02) — Page tables, writes and shared-tail copy-on-write; Build.

**Design context:** [kv-cache](../design/kv-cache.md).

<a id="module-07"></a>
## 07 — Iteration scheduling and continuous batching (E)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 16 baseline h (E). Hours are owned by the roadmap.

**Concept prerequisites:** [06](runtime.md#module-06). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** translate PennOS queue/scheduler ideas into token-level serving work and resource constraints.
- **Slides 1–8:** static batch inefficiency with uneven output lengths. **9–20:** waiting/running/finished states, token budgets, backfill, admission. **21–30:** virtual time vs real executor, compute vs memory constraints, fairness.
- **Code:** supplied virtual clock/FakeExecutor; learner scheduling policy and state transitions. Never use simulator wall-clock speed as GPU throughput.
- **Experiment/exit:** manually trace four requests across six iterations; compare static/continuous on the same arrival sequence.
- **References:** Orca and CMU serving lecture.

<a id="scheduler-worked-trace"></a>
### Worked lifecycle oracle for SCH-01/02

This supplies the original four-request/six-iteration exercise with concrete expected values. It is a logical fixture, not measured GPU performance or a frozen production scheduler policy. Use at most two active requests, FCFS backfill at iteration boundaries, enough memory and a three-input-token iteration budget. Each successful prefill or decode samples and immediately emits one output; stop at the declared output count. Symbolic outputs such as A0 are deterministic fixture IDs.

| Request | Arrival before iteration | Prompt tokens | Required output tokens |
|---|---:|---:|---:|
| A | 1 | 2 | 3 |
| B | 1 | 1 | 2 |
| C | 2 | 2 | 4 |
| D | 3 | 1 | 2 |

| Iteration | Prepared work → newly emitted outputs | Waiting after admission | Newly finished |
|---|---|---|---|
| 1 | A prefill(2) → A0; B prefill(1) → B0 | None | None |
| 2 | A decode(A0) → A1; B decode(B0) → B1 | C | B |
| 3 | A decode(A1) → A2; C prefill(2) → C0 | D | A |
| 4 | C decode(C0) → C1; D prefill(1) → D0 | None | None |
| 5 | C decode(C1) → C2; D decode(D0) → D1 | None | D |
| 6 | C decode(C2) → C3 | None | C |

Expected final `(computed, sampled, emitted)` counts: A `(4,3,3)`, B `(2,2,2)`, C `(5,4,4)`, D `(2,2,2)`. There are 13 computed input tokens and 11 emitted outputs; each last sampled output is emitted without a subsequent KV computation. Derive these counts independently before implementing the coordinator. SCH-01 can execute the fixed plan with a fake executor; SCH-02 generates the admission/backfill behavior and compares a declared static baseline using the same arrivals.

Broken variants: deliver iteration 3's completion twice (no duplicate A2 emission); cancel D after iteration 4 dispatch but before completion (no D0 emitted, retain its in-flight lease until completion); leave a queue slot empty after B finishes (the static-versus-continuous comparison must expose the idle slot). Resource reclamation uses an opaque fake lease here and the actual pool in later KV/SCH integration. Do not implement a GPU allocator as a new SCH-01 prerequisite.

### December storyboard sequence

Static batching → request states → token budgets → admission/backfill → fairness. Trace a small workload manually and reproduce it with the logical executor.

### Implementation connections

- [SCH-01](../tasks/scheduler.md#sch-01) — Request lifecycle and virtual execution fixtures; Build.
- [SCH-02](../tasks/scheduler.md#sch-02) — Static and continuous batching; Build.

**Design context:** [scheduler](../design/scheduler.md).

<a id="module-08"></a>
## 08 — Chunked prefill, preemption and cancellation (E)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 14 baseline h (E). Hours are owned by the roadmap.

**Concept prerequisites:** [07](runtime.md#module-07). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** bound decode interference, recover from memory pressure and clean up every request exit path.
- **Slides 1–10:** long prefill interrupts decodes; token-budget packing. **11–22:** partial-prefill positions, recompute vs swap cost, victim/aging policy. **23–36:** disconnect/timeout races, in-flight GPU work and idempotent release.
- **Code:** learner chunk packing/recompute state machine; supplied adversarial schedules including cancellation immediately before/after a step finishes.
- **Experiment/exit:** one long prompt amid decodes; report TTFT/ITL trade-off and recomputed tokens. Correct output and no leak after cancel/resume.
- **References:** Sarathi-Serve; production scheduler selected code.

### December storyboard sequence

Long-prefill interference → chunk packing → recompute preemption → cancellation races → deferred cleanup. Demonstrate correct continuation and no page leaks.

### Implementation connections

- [SCH-03](../tasks/scheduler.md#sch-03) — Chunked prefill; Build.
- [SCH-04](../tasks/scheduler.md#sch-04) — Recompute preemption and safe cancellation; Build.

**Design context:** [scheduler](../design/scheduler.md).
