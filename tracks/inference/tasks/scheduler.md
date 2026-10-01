# Scheduler and lifecycle — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="sch-01"></a>
## SCH-01 — Request lifecycle and virtual execution fixtures

**Status:** planned. **Package:** E. **Milestone:** CP2.

**Requirement/design:** [SCH-1](../design/scheduler.md#sch-1) / [RUN-1](../design/model-runtime.md#run-1) — [canonical design](../design/scheduler.md). **Learning mode:** Build. **Authorship target:** learner-authored lifecycle; virtual clock/fake executor supplied.

**Dependencies:** [FND-01](model.md#fnd-01).

**Teaching:** [07](../curriculum/runtime.md#module-07), including the [four-request worked oracle](../curriculum/runtime.md#scheduler-worked-trace).

**Planned change boundary:** `src/inferstack/engine/scheduling/state.py`, `src/inferstack/engine/runtime/coordinator.py`, `src/inferstack/backends/fake/executor.py`, `tests/scheduler/test_lifecycle.py`

**Work:**

- [ ] Define waiting/active/terminal transitions and independent computed/sampled/emitted counters.
- [ ] Hand-trace four requests over six iterations, then express the sequence with a deterministic virtual clock and supplied logical executor.

**Validation / acceptance:**

- [ ] Expected transitions and output order match the independent hand trace.
- [ ] Terminal intent and in-flight ownership remain distinct; duplicate completion/cancel events cannot double-commit output.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="sch-02"></a>
## SCH-02 — Static and continuous batching

**Status:** planned. **Package:** E. **Milestone:** CP2.

**Requirement/design:** [SCH-2](../design/scheduler.md#sch-2) — [canonical design](../design/scheduler.md). **Learning mode:** Build. **Authorship target:** learner-authored policy.

**Dependencies:** [SCH-01](scheduler.md#sch-01), [KV-01](memory-cache.md#kv-01).

**Teaching:** [07](../curriculum/runtime.md#module-07).

**Planned change boundary:** `src/inferstack/engine/scheduling/policy.py`, `tests/scheduler/test_batching.py`

**Work:**

- [ ] Implement static baseline then token-budget admission/backfill using StepPlan and stable request snapshots.
- [ ] Resolve/document the initial ordering and queue-bound policy in OQ-04; keep selection separate from page reservation and execution.

**Validation / acceptance:**

- [ ] Same arrivals show correct request/token accounting under both policies, including no-capacity and no-progress cases.
- [ ] No plan exceeds budget; failed reservation cannot leave partially applied admission state.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="sch-03"></a>
## SCH-03 — Chunked prefill

**Status:** planned. **Package:** E. **Milestone:** CP2.

**Requirement/design:** [SCH-3](../design/scheduler.md#sch-3) — [canonical design](../design/scheduler.md). **Learning mode:** Build. **Authorship target:** learner-authored.

**Dependencies:** [SCH-02](scheduler.md#sch-02), [KV-02](memory-cache.md#kv-02).

**Teaching:** [08](../curriculum/runtime.md#module-08).

**Planned change boundary:** `src/inferstack/engine/scheduling/chunking.py`, `tests/scheduler/test_chunking.py`

**Work:**

- [ ] Pack partial prefill and decode work while preserving causal positions, page tails and per-request progress.
- [ ] Add a long-prompt-amid-decodes fixture and a bounded chunk-size comparison; record chosen chunk policy.

**Validation / acceptance:**

- [ ] Chunked/unchunked teacher-forced execution passes the numerical oracle.
- [ ] Report TTFT/ITL and waiting-time effects with separately counted scheduled/computed/output tokens.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="sch-04"></a>
## SCH-04 — Recompute preemption and safe cancellation

**Status:** planned. **Package:** E. **Milestone:** CP2.

**Requirement/design:** [SCH-3](../design/scheduler.md#sch-3) / [SCH-4](../design/scheduler.md#sch-4) — [canonical design](../design/scheduler.md). **Learning mode:** Build. **Authorship target:** learner-authored.

**Dependencies:** [SCH-03](scheduler.md#sch-03), [KV-02](memory-cache.md#kv-02), [MOD-04](model.md#mod-04).

**Teaching:** [08](../curriculum/runtime.md#module-08).

**Planned change boundary:** `src/inferstack/engine/scheduling/preemption.py`, `src/inferstack/engine/runtime/lifecycle.py`, `tests/scheduler/test_preemption_cancel.py`

**Work:**

- [ ] Define victim/recovery policy and replay committed token IDs to rebuild KV without re-sampling/re-emitting.
- [ ] Handle cancellation/deadline before reservation, after launch and after completion; retain in-flight leases until safe.

**Validation / acceptance:**

- [ ] Preempt/resume matches unpreempted sequence semantics under numerical checks.
- [ ] Exhaustion, shared prefixes and duplicate cancels leave no leaked/double-freed pages; emitted output is not duplicated.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="sch-05"></a>
## SCH-05 — Cache-aware scheduling with fairness guard

**Status:** planned. **Package:** E. **Milestone:** CP2.

**Requirement/design:** [SCH-4](../design/scheduler.md#sch-4) / [CACHE-2](../design/kv-cache.md#cache-2) — [canonical design](../design/scheduler.md). **Learning mode:** Build. **Authorship target:** learner-authored; comparison plotting supplied.

**Dependencies:** [SCH-04](scheduler.md#sch-04), [KV-04](memory-cache.md#kv-04).

**Teaching:** [10](../curriculum/prefix-caching.md#module-10).

**Planned change boundary:** `src/inferstack/engine/scheduling/fairness.py`, `tests/scheduler/test_fairness.py`

**Work:**

- [ ] Integrate prefix acquisition into coordinator planning and add a documented aging safeguard before LPM/cache-aware order.
- [ ] Run index-only and policy-only ablations separately; retain queue bounds and cancel semantics.

**Validation / acceptance:**

- [ ] A long-wait request progresses under repeated short arrivals according to the declared safeguard.
- [ ] Compare reused tokens, waiting times, recomputation and TTFT under matched resources; no hidden index/policy confounding.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
