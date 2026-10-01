# Foundations and model execution — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="fnd-01"></a>
## FND-01 — Environment and minimal logical contracts

**Status:** planned. **Package:** A. **Milestone:** CP1.

**Requirement/design:** [RUN-1](../design/model-runtime.md#run-1) / [MODEL-1](../design/model-runtime.md#model-1) — [canonical design](../ARCHITECTURE.md). **Learning mode:** Modify + Explain. **Authorship target:** learner-modified; environment and interface plumbing supplied.

**Dependencies:** none; first implementation task.

**Teaching:** [00](../curriculum/foundations.md#module-00), [01](../curriculum/foundations.md#module-01).

**Planned change boundary:** `src/inferstack/contracts/model.py`, `src/inferstack/contracts/requests.py`, `src/inferstack/contracts/execution.py`, `src/inferstack/contracts/observations.py`, `environments/compatibility.md`

**Work:**

- [ ] Define CPU-only request/model/step/observation records from the architecture contract. Document typed signatures, fields, preconditions and postconditions; unfinished methods raise NotImplementedError instead of returning plausible outputs. Keep imports independent of GPU/gateway SDKs.
- [ ] Document separate CPU/custom-GPU/production-image/Go environments; pin the first tested set after a smoke test. Preserve starter bundle/CLI behavior and add CPU CI when runnable code exists; GPU, weight-download and Kubernetes checks require explicit selection.

**Validation / acceptance:**

- [ ] Core contracts import with no CUDA or downloaded weights. Unsupported model/schema states are explicit.
- [ ] Existing eight starter tests pass; one bundle records supplied configuration and no fabricated provenance. Version-sensitive choices are recorded or visibly pending.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

### FND-01 startup sequence

Use [the handoff procedure](../../../docs/HANDOFF.md) and [first contract slice](../ARCHITECTURE.md#first-contract-slice). These substeps refine the existing task; they add no hours or new curriculum gate.

1. **Explain and select:** read the existing starter and trace R0's computed/sampled/emitted counts from the design fixture. Identify one owner for each mutable state. Record local Python/OS and choose the first isolated CPU dependency set; do not assume the author's current interpreter is the ML stack's supported version.
2. **Materialize contracts:** create the named contract files and minimal package metadata. Document field units, identity and validation behavior. Use a plain CPU representation for prepared-step metadata; unfinished execution interfaces fail explicitly.
3. **Check boundaries:** add independent valid/invalid record cases, serialization/identity checks where persistence is intended, and an import check that needs no model weights or GPU SDK. Keep actual scheduler/allocation behavior for SCH/KV tasks.
4. **Reproduce:** run the existing starter tests and the new contract checks, create one clearly labeled fixture bundle, and write the actual environment/commands in the evidence record. The supplied documentation CI does not replace these new checks.

**Teach-back:** explain the difference between a request contract, authoritative runtime state and an observation; predict how the R0 trace changes after output emission. **Next ready work:** FND-02 or SCH-01, selected by the requested learning path. Understanding remains unassessed until the learner demonstrates it.

<a id="fnd-02"></a>
## FND-02 — Numerical diagnostic and independent oracle

**Status:** planned. **Package:** A. **Milestone:** CP1.

**Requirement/design:** [MODEL-1](../design/model-runtime.md#model-1) / [MODEL-2](../design/model-runtime.md#model-2) — [canonical design](../design/model-runtime.md). **Learning mode:** Build. **Authorship target:** learner-authored; tiny fixtures supplied.

**Dependencies:** [FND-01](model.md#fnd-01).

**Teaching:** [01](../curriculum/foundations.md#module-01).

**Planned change boundary:** `tests/model/test_numerics.py`

**Work:**

- [ ] Diagnose tensor broadcasting and Python async behavior; trace five-token prefill and three decode steps with shapes, causal positions, GQA mapping, RoPE and QK norm.
- [ ] Compare stable/naive softmax and cache append; repair a shifted-position fixture. Use explicit configured head dimension.

**Validation / acceptance:**

- [ ] Hand-computed/tiny FP32 expected values detect the deliberately broken case.
- [ ] Explain tolerance, dtype effects and greedy near ties without treating plausible generated text as proof.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="fnd-03"></a>
## FND-03 — GPU execution foundations

**Status:** planned. **Package:** A. **Milestone:** CP2.

**Requirement/design:** [GPU-2](../design/gpu-execution.md#gpu-2) / [GPU-4](../design/gpu-execution.md#gpu-4) — [canonical design](../design/gpu-execution.md). **Learning mode:** Modify + Explain. **Authorship target:** learner-modified; CUDA build/examples supplied.

**Dependencies:** [FND-01](model.md#fnd-01).

**Teaching:** [02](../curriculum/foundations.md#module-02).

**Planned change boundary:** `src/inferstack/backends/kernels/foundations.cu`

**Work:**

- [ ] Use supplied vector/reduction fixtures to change indexing and repair a race; map grid/block/warp and Triton program IDs.
- [ ] Explain coalescing, shared/register/global memory, barriers, streams/events and completed-device timing.

**Validation / acceptance:**

- [ ] Predict a bounds/coalescing/synchronization failure and demonstrate the repair in the supported environment.
- [ ] Separate enqueue time from completion; annotate a tiny execution trace and record real GPU versus reference-only status.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="fnd-04"></a>
## FND-04 — Kubernetes foundations

**Status:** planned. **Package:** A. **Milestone:** December.

**Requirement/design:** [PLAT-1](../design/routing-platform.md#plat-1) — [canonical design](../design/routing-platform.md). **Learning mode:** Operate + Explain. **Authorship target:** learner-operated; local manifests supplied.

**Dependencies:** [FND-01](model.md#fnd-01).

**Teaching:** [16](../curriculum/platform.md#module-16).

**Planned change boundary:** `deploy/local/foundation.yaml`

**Work:**

- [ ] Trace desired/observed state through pod/deployment/service, selectors/DNS, readiness/startup/liveness and resources.
- [ ] Inspect namespace/RBAC and GPU allocation contracts; diagnose supplied wrong-label and insufficient-resource fixtures.

**Validation / acceptance:**

- [ ] Explain why a live pod is not necessarily ready and follow a request to endpoints.
- [ ] Record events and corrected configuration; do not claim GPU operation from a local kind exercise.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="mod-01"></a>
## MOD-01 — Dense model operations and loader boundary

**Status:** planned. **Package:** D. **Milestone:** CP2 (early reference/ownership work).

**Requirement/design:** [MODEL-1](../design/model-runtime.md#model-1) — [canonical design](../design/model-runtime.md). **Learning mode:** Build + Modify. **Authorship target:** learner-authored math; loader/tokenizer supplied.

**Dependencies:** [FND-02](model.md#fnd-02).

**Teaching:** [04](../curriculum/runtime.md#module-04).

**Planned change boundary:** `src/inferstack/engine/model/decoder.py`, `src/inferstack/serving/model_loader.py`

**Work:**

- [ ] Implement embeddings/projections, RMSNorm, GQA, RoPE/QK norm, SwiGLU and output projection for the same tiny supported model revision used in BEN-03.
- [ ] Map supplied weights/config/tokenizer/template, validate shapes/tied weights, and reject unsupported model forms.

**Validation / acceptance:**

- [ ] Per-layer fixed-input comparisons isolate shape/position/normalization errors against an independent reference.
- [ ] Record exact model/config revision and explained mismatch; no arbitrary checkpoint-generalization claim.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="mod-02"></a>
## MOD-02 — Contiguous KV prefill and incremental decode

**Status:** planned. **Package:** D. **Milestone:** CP2 (early reference/ownership work).

**Requirement/design:** [MODEL-2](../design/model-runtime.md#model-2) / [RUN-1](../design/model-runtime.md#run-1) — [canonical design](../design/model-runtime.md). **Learning mode:** Build. **Authorship target:** learner-authored.

**Dependencies:** [MOD-01](model.md#mod-01).

**Teaching:** [04](../curriculum/runtime.md#module-04).

**Planned change boundary:** `src/inferstack/engine/model/attention.py`, `src/inferstack/backends/torch_reference/executor.py`

**Work:**

- [ ] Implement readable uncached and contiguous-cache paths with explicit causal positions and cache writes.
- [ ] Expose prepared-step execution without allowing executor code to own request cancellation or free pages.

**Validation / acceptance:**

- [ ] Teacher-forced logits agree across uncached and cached prefill/decode under documented tolerances.
- [ ] A shifted position/mask fixture fails; output counters distinguish sampled/emitted tokens from computed KV.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="mod-03"></a>
## MOD-03 — Memory accounting

**Status:** planned. **Package:** D. **Milestone:** CP2 (early reference/ownership work).

**Requirement/design:** [MODEL-3](../design/model-runtime.md#model-3) — [canonical design](../design/model-runtime.md). **Learning mode:** Build. **Authorship target:** learner-authored accounting; memory collector supplied.

**Dependencies:** [MOD-01](model.md#mod-01).

**Teaching:** [05](../curriculum/runtime.md#module-05).

**Planned change boundary:** `src/inferstack/engine/memory/accounting.py`

**Work:**

- [ ] Compute dense KV bytes from config and dtype; keep weight, KV, activation/workspace, reserve and graph allocations distinct.
- [ ] Use config fixtures for MHA/MQA/GQA and explain MLA/hybrid/MoE exceptions; compare prediction with measured allocations.

**Validation / acceptance:**

- [ ] Recover the approved tiny-model example only when its actual configuration matches.
- [ ] Unsupported architecture assumptions are rejected/labeled and measured memory differences are explained.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="mod-04"></a>
## MOD-04 — Sampling and determinism exercise

**Status:** planned. **Package:** D. **Milestone:** CP2.

**Requirement/design:** [MODEL-3](../design/model-runtime.md#model-3) — [canonical design](../design/model-runtime.md). **Learning mode:** Build + Explain. **Authorship target:** learner-authored small sampler; generation glue supplied.

**Dependencies:** [MOD-02](model.md#mod-02).

**Teaching:** [01](../curriculum/foundations.md#module-01), [04](../curriculum/runtime.md#module-04).

**Planned change boundary:** `src/inferstack/engine/model/sampling.py`

**Work:**

- [ ] Implement a bounded temperature/top-p sampling exercise with tiny distributions and greedy baseline.
- [ ] Explain min-p, RNG state, near ties and batch-dependent numerical order without expanding the public serving API implicitly.

**Validation / acceptance:**

- [ ] Small exact categorical cases and repeated-seed experiments check the intended distribution/limits.
- [ ] Document why equal seeds across kernels are not a universal semantic-equivalence test.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
