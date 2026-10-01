# Measurement and replay — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="ben-01"></a>
## BEN-01 — Streaming observations and metric definitions

**Status:** planned. **Package:** B. **Milestone:** CP1.

**Requirement/design:** [MEAS-1](../engineering/measurement.md#meas-1) — [canonical design](../engineering/measurement.md). **Learning mode:** Build. **Authorship target:** learner metrics; parser/artifacts supplied.

**Dependencies:** [FND-01](model.md#fnd-01).

**Teaching:** [03](../curriculum/foundations.md#module-03), including the [independent metric fixture](../curriculum/foundations.md#metrics-worked-fixture).

**Planned change boundary:** `src/inferstack/bench/observations.py`, `src/inferstack/bench/metrics.py`, `tests/bench/test_metrics.py`

**Work:**

- [ ] Record scheduled arrival, dispatch, content/chunk events, finish/errors and count provenance on a client monotonic clock.
- [ ] Implement latency, per-request SLO conjunction, attainment and goodput; preserve all offered outcomes.

**Validation / acceptance:**

- [ ] Synthetic event fixtures recover known timings, count drops/errors, and handle N<2 TPOT explicitly.
- [ ] Chunk gaps are not labeled exact ITL unless token-level timing exists; no unrelated clock subtraction.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="ben-02"></a>
## BEN-02 — Open-loop and closed-loop load

**Status:** planned. **Package:** B. **Milestone:** CP1.

**Requirement/design:** [MEAS-1](../engineering/measurement.md#meas-1) / [MEAS-2](../engineering/measurement.md#meas-2) — [canonical design](../engineering/measurement.md). **Learning mode:** Build. **Authorship target:** learner arrival/runner policy; HTTP plumbing supplied.

**Dependencies:** [BEN-01](benchmark.md#ben-01).

**Teaching:** [03](../curriculum/foundations.md#module-03).

**Planned change boundary:** `src/inferstack/bench/arrivals.py`, `src/inferstack/bench/runner.py`, `tests/bench/test_arrivals.py`

**Work:**

- [ ] Implement offered arrivals independently of completions and a separate closed-loop concurrency mode.
- [ ] Detect client dispatch lag/saturation; record cap-induced drop/delay rather than silently changing offered load.

**Validation / acceptance:**

- [ ] Virtual-clock fixtures preserve intended arrivals during slow responses.
- [ ] Timeout/rejection/cancellation denominators remain correct under overload.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="ben-03"></a>
## BEN-03 — Matched vLLM and SGLang baselines

**Status:** planned. **Package:** B. **Milestone:** CP1.

**Requirement/design:** [MEAS-2](../engineering/measurement.md#meas-2) — [canonical design](../engineering/measurement.md). **Learning mode:** Operate both. **Authorship target:** learner-operated; launch/config/plot scaffolds supplied.

**Dependencies:** [BEN-02](benchmark.md#ben-02).

**Teaching:** [03](../curriculum/foundations.md#module-03).

**Planned change boundary:** `deploy/engines/vllm.yaml`, `deploy/engines/sglang.yaml`, `configs/baseline.yaml`

**Work:**

- [ ] Run one tiny dense revision on both servers, then one larger fitting model; match tokenizer/template/precision/context/generation settings.
- [ ] Use three load points, two workload shapes, cache-off baseline and one prefix ablation. Cross-check a matched run with vllm bench serve and AIPerf.
- [ ] Read one profiler trace, modify a supplied dashboard and publish a short baseline report linking observations to an explained bottleneck.

**Validation / acceptance:**

- [ ] Bundles contain raw failures, definitions, environment and one explained finding.
- [ ] Metric discrepancies are explained by exact definition/version; no latest-version compatibility or positive speedup assumption.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="ben-04"></a>
## BEN-04 — Dependency-aware and fixed-arrival replay

**Status:** planned. **Package:** C (preserved historical accounting). **Milestone:** inference December; PLT-03 owns later deployment, and agent AGT-04 independently owns live quality.

**Requirement/design:** [MEAS-3](../engineering/measurement.md#meas-3) / [APP-3](../../agents/RUNTIME.md#app-3) — [canonical design](../engineering/measurement.md). **Learning mode:** Build. **Authorship target:** learner replay policy; transport supplied.

**Dependencies:** [BEN-02](benchmark.md#ben-02). Use self-contained supplied versioned SessionTrace fixtures under the [track contract](../../../docs/system/track-contracts.md#track-boundary); agent APP-03 exports are optional inputs, not a prerequisite.

**Teaching:** [15 — replay](../curriculum/foundations.md#module-15-replay).

**Planned change boundary:** `src/inferstack/bench/replay.py`, `tests/bench/test_replay.py`

**Work:**

- [ ] Implement separate replay modes and validate parent DAG, prompts, delays and outcome policy. Provide independently usable, versioned fixture sessions so tests and the routing study do not require a live agent application.
- [ ] Preserve recorded next prompts for transcript replay; retain live-agent branching as a different execution mode.

**Validation / acceptance:**

- [ ] Child dispatch waits for required parents plus recorded delays; cycles/missing parents are rejected.
- [ ] Parent failures remain visible in session accounting; distinguish blocked descendants from eligible/dispatched model requests. max_tokens is not treated as an output-length guarantee.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
