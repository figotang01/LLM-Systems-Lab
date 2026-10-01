# Advanced labs, capstone and release — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="adv-01"></a>
## ADV-01 — Speculation verifier and supported proposer

**Status:** planned. **Package:** H. **Milestone:** Advanced labs.

**Requirement/design:** [ADV-1](../design/advanced-labs.md#adv-1) — [canonical design](../design/advanced-labs.md). **Learning mode:** Build + Operate + Explain. **Authorship target:** learner math/verifier; proposer integration supplied.

**Dependencies:** [GPU-04](gpu-serving.md#gpu-04), [BEN-03](benchmark.md#ben-03).

**Teaching:** [20](../curriculum/advanced.md#module-20).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Derive acceptance/residual and bonus-token behavior, implement small verifier/n-gram proposal and cache rollback fixtures.
- [ ] Run one supported production proposer off/on at low/high load; explain EAGLE-3/MTP/DFlash and SpecForge alternatives.

**Validation / acceptance:**

- [ ] Exact categorical and statistical checks plus EOS/rejection rollback invariants.
- [ ] Load-dependent result with environment/support map; no required drafter training or full-engine integration.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="adv-02"></a>
## ADV-02 — Quantization with quality gates

**Status:** planned. **Package:** H. **Milestone:** Advanced labs.

**Requirement/design:** [ADV-2](../design/advanced-labs.md#adv-2) — [canonical design](../design/advanced-labs.md). **Learning mode:** Build + Operate. **Authorship target:** learner math/interpretation; conversion/evaluator plumbing supplied.

**Dependencies:** [GPU-04](gpu-serving.md#gpu-04). Freeze an inference-owned quality set with independent labels/oracles and the supported lm-eval/structured-output checks; do not require the agent application. Full live workload quality remains required under agent AGT-04.

**Teaching:** [21](../curriculum/advanced.md#module-21).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Implement groupwise INT8 reference and calibration/held-out checks; inspect GPTQ/AWQ/SmoothQuant and supported kernel formats.
- [ ] Run one compressed checkpoint plus KV precision ablation; preserve FP8/W4A16 and FP4 numerical learning when hardware is unavailable.

**Validation / acceptance:**

- [ ] Quality/memory/latency trade-off with declared gates, formats and actual hardware.
- [ ] Unsupported throughput is not fabricated; held-out data never becomes calibration data.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="adv-03"></a>
## ADV-03 — Collectives, tensor and expert parallelism

**Status:** planned. **Package:** H. **Milestone:** Advanced labs.

**Requirement/design:** [ADV-3](../design/advanced-labs.md#adv-3) — [canonical design](../design/advanced-labs.md). **Learning mode:** Build + Modify + Operate. **Authorship target:** learner algebra/dispatch; distributed launch/shards supplied.

**Dependencies:** [GPU-04](gpu-serving.md#gpu-04), [PLT-03](platform.md#plt-03).

**Teaching:** [22](../curriculum/advanced.md#module-22).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Complete two-rank row/column linear or block exercise and traffic/memory calculation; profile collectives.
- [ ] Modify token dispatch/combine and skew fixtures, operate TP=2 and supported EP; explain DP-attention, DeepEP/EPLB and training-parallel alternatives.

**Validation / acceptance:**

- [ ] Numerical agreement with single-rank reference and recorded topology/communication overhead.
- [ ] MoE fit uses total weights; unsupported EP remains explicitly limited, with conceptual artifact retained.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="adv-04"></a>
## ADV-04 — Prefill/decode transfer and fair comparison

**Status:** planned. **Package:** H. **Milestone:** Advanced labs.

**Requirement/design:** [ADV-4](../design/advanced-labs.md#adv-4) — [canonical design](../design/advanced-labs.md). **Learning mode:** Operate + Build analysis. **Authorship target:** learner cost model; connector/transport recipes supplied.

**Dependencies:** [PLT-03](platform.md#plt-03), [GPU-04](gpu-serving.md#gpu-04).

**Teaching:** [23](../curriculum/advanced.md#module-23).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Run transfer benchmark and one supported NIXL/Mooncake-style path; inspect the alternative.
- [ ] Compare 1P1D with two colocated replicas at equal total GPUs/cost, including layout/ownership/failure and bandwidth assumptions.

**Validation / acceptance:**

- [ ] Measured transfer/recompute break-even and matched-load latency/goodput results.
- [ ] No extra-GPU advantage disguised as architectural gain; unsupported transport is recorded.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="rel-01"></a>
## REL-01 — Six bridge capsules and lifecycle breadth

**Status:** planned. **Package:** J. **Milestone:** Release.

**Requirement/design:** [ADV-1](../design/advanced-labs.md#adv-1) / [ADV-2](../design/advanced-labs.md#adv-2) / [ADV-3](../design/advanced-labs.md#adv-3) / [ADV-4](../design/advanced-labs.md#adv-4) — [canonical design](../design/advanced-labs.md). **Learning mode:** Modify + Explain; Operate where specified. **Authorship target:** learner exercises; annotated reference/profile artifacts supplied.

**Dependencies:** [GPU-04](gpu-serving.md#gpu-04).

**Teaching:** [B1](../curriculum/advanced.md#module-b1), [B2](../../agents/CURRICULUM.md#module-b2), [B3](../curriculum/advanced.md#module-b3), [B4](../curriculum/advanced.md#module-b4), [B5](../curriculum/advanced.md#module-b5), [B6](../curriculum/advanced.md#module-b6).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Complete B1–B6 at their stated bounded depth; retain all optional deeper paths without requiring them.
- [ ] Connect corpus/model/artifact versioning, SQL, leakage and cloud/IaC exercises to preceding work rather than creating another platform.

**Validation / acceptance:**

- [ ] Six artifacts with modifications/calculations and teach-backs; local MLX run where specified.
- [ ] Hardware-unavailable references remain studied, not measured accelerator runs.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="rel-02"></a>
## REL-02 — Capstone experiment and report

**Status:** planned. **Package:** I. **Milestone:** CP4.

**Requirement/design:** [ROUTE-2](../design/routing-platform.md#route-2) / [MEAS-2](../engineering/measurement.md#meas-2) / [MEAS-3](../engineering/measurement.md#meas-3) — [canonical design](../CAPSTONE.md). **Learning mode:** Build experiments + Explain. **Authorship target:** learner hypothesis/analysis; report/plot scaffolds supplied.

**Dependencies:** [PLT-04](platform.md#plt-04), [PLT-05](platform.md#plt-05), [BEN-04](benchmark.md#ben-04). Consume versioned supplied workload fixtures; agent exports/reports may supplement them without becoming an implementation prerequisite.

**Teaching:** [24](../curriculum/advanced.md#module-24).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Pre-register p95 session completion and the 36-run primary matrix with held-out sessions and explicit SLO/cache/resource controls.
- [ ] Run dependency-aware replay, a skew/staleness stress case and limited optional interactions only after sound main results. The original live-quality subset is required under [AGT-04](../../agents/ROADMAP.md#agt-04); attach its separate report when available without making it an inference completion dependency.

**Validation / acceptance:**

- [ ] Raw bundles, four useful figures, uncertainty and trace/profile-supported interpretation reproduce.
- [ ] Negative results accepted; simulator and product-wide comparisons do not establish hash/radix causal effects.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="rel-03"></a>
## REL-03 — Clean reproduction, regression policy and release

**Status:** planned. **Package:** J. **Milestone:** Release.

**Requirement/design:** [RUN-1](../design/model-runtime.md#run-1) / [MEAS-2](../engineering/measurement.md#meas-2) — [canonical design](../../../docs/engineering/ownership.md). **Learning mode:** Build policies + Explain. **Authorship target:** learner reproduction/contribution; CI/report/provision templates supplied.

**Dependencies:** [REL-01](advanced-release.md#rel-01), [REL-02](advanced-release.md#rel-02), [PF-4](framework.md#pf-4), [ADV-01](advanced-release.md#adv-01), [ADV-02](advanced-release.md#adv-02), [ADV-03](advanced-release.md#adv-03), [ADV-04](advanced-release.md#adv-04).

**Teaching:** [24](../curriculum/advanced.md#module-24).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Reproduce on a clean environment; implement on-demand GPU regression decisions with effect-size/repeated-confirmation policy.
- [ ] Prepare one coherent README/design/report/four-page summary/demo and upstream contribution with reproduction/tests; derive website/blog material rather than duplicate reporting.

**Validation / acceptance:**

- [ ] A stranger reproduces a main figure; exact exceptions, tested hardware, authorship and limits are visible.
- [ ] Final oral walkthrough explains one request, failure and negative result; merge timing is not a gate.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
