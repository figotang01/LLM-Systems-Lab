# Production-framework development — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="pf-1"></a>
## PF-1 — SGLang source and runtime-state walkthrough

**Status:** planned. **Package:** PF (8 added h). **Milestone:** December.

**Requirement/design:** [RUN-1](../design/model-runtime.md#run-1) / [CACHE-1](../design/kv-cache.md#cache-1) / [SCH-1](../design/scheduler.md#sch-1) — [canonical design](../ARCHITECTURE.md). **Learning mode:** Explain + Operate. **Authorship target:** learner explanation; source-navigation and launch scaffolds supplied.

**Dependencies:** [BEN-03](benchmark.md#ben-03), [KV-03](memory-cache.md#kv-03), [SCH-02](scheduler.md#sch-02).

**Teaching:** [PF-1](../curriculum/frameworks.md#module-pf-1).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Pin source revision and trace cold/repeated-prefix requests through API, scheduler, cache, model execution and output.
- [ ] Inspect cancellation/ownership and map actual source to the simpler InferStack boundaries; annotate observed runtime state.

**Validation / acceptance:**

- [ ] Revision-linked call/state diagram, commands/environment and one corrected prediction.
- [ ] Source-only investigation is labeled as such; unavailable execution remains pending.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="pf-2"></a>
## PF-2 — vLLM V1 architectural comparison

**Status:** planned. **Package:** PF (4 added h). **Milestone:** December.

**Requirement/design:** [RUN-1](../design/model-runtime.md#run-1) / [CACHE-2](../design/kv-cache.md#cache-2) — [canonical design](../ARCHITECTURE.md). **Learning mode:** Explain + Operate. **Authorship target:** learner comparison.

**Dependencies:** [PF-1](framework.md#pf-1).

**Teaching:** [PF-2](../curriculum/frameworks.md#module-pf-2).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Trace the corresponding V1 API/core/worker, scheduler/KV and abort/output path.
- [ ] Document at least three responsibility/state differences at pinned revisions, distinguishing source inspection from observed behavior.

**Validation / acceptance:**

- [ ] Source-linked comparison and request walkthrough; matched settings for empirical claims.
- [ ] Explain paging versus indexing versus policy without replacing baseline vLLM/SGLang tasks.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="pf-3"></a>
## PF-3 — Bounded SGLang change and regression

**Status:** planned. **Package:** PF (8 added h). **Milestone:** December.

**Requirement/design:** [CACHE-1](../design/kv-cache.md#cache-1) / [SCH-4](../design/scheduler.md#sch-4) — [canonical design](../engineering/correctness.md). **Learning mode:** Modify. **Authorship target:** learner-modified upstream code with attribution.

**Dependencies:** [PF-1](framework.md#pf-1), [KV-04](memory-cache.md#kv-04), [SCH-04](scheduler.md#sch-04).

**Teaching:** [PF-3](../curriculum/frameworks.md#module-pf-3).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Select a prepared bounded instrumentation/bookkeeping/validation task after inspecting the relevant pinned source; no novel-bug-discovery requirement.
- [ ] Make a local patch and independent reproducer/regression or known-state instrumentation check; retain measured/state-based validation.

**Validation / acceptance:**

- [ ] Patch checksum/base commit, relevant before/after behavior, focused tests and explained limits.
- [ ] Cosmetic edits do not satisfy runtime-depth gate; upstream merge is not required and J remains allocated.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="pf-4"></a>
## PF-4 — Technical defense and interview practice

**Status:** planned. **Package:** PF (4 added h). **Milestone:** December.

**Requirement/design:** [RUN-1](../design/model-runtime.md#run-1) / [MODEL-3](../design/model-runtime.md#model-3) / [GPU-4](../design/gpu-execution.md#gpu-4) — [canonical design](../ARCHITECTURE.md). **Learning mode:** Explain. **Authorship target:** learner independent walkthrough.

**Dependencies:** [PF-2](framework.md#pf-2), [PF-3](framework.md#pf-3), [GPU-04](gpu-serving.md#gpu-04).

**Teaching:** [PF-4](../curriculum/frameworks.md#module-pf-4).

**Planned change boundary:** Pinned external source or experiment/release artifacts; no new custom-runtime subsystem is implied.

**Work:**

- [ ] Run two practice sessions including preparation/correction: lifecycle/patch, then capacity/profile/benchmark diagnosis.
- [ ] Attempt without AI/notes, then inspect source and correct mistakes; include a limitation and a negative result.

**Validation / acceptance:**

- [ ] Questions, initial answers, corrections and remaining gaps are recorded. Assemble December reproduction instructions, evidence inventory, known limits and an explicit January backlog; link existing artifacts instead of writing another plan.
- [ ] Use the teaching rubric; passing is not a claim about a specific employer interview or large-fleet expertise.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
