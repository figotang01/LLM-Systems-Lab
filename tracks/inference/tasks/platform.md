# Routing and platform — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="plt-01"></a>
## PLT-01 — Local gateway and simulator deployment

**Status:** planned. **Package:** G. **Milestone:** December.

**Requirement/design:** [PLAT-1](../design/routing-platform.md#plat-1) — [canonical design](../design/routing-platform.md). **Learning mode:** Operate. **Authorship target:** learner-operated; manifests/chart glue supplied.

**Dependencies:** [FND-04](model.md#fnd-04).

**Teaching:** [16](../curriculum/platform.md#module-16), [17](../curriculum/platform.md#module-17).

**Planned change boundary:** `deploy/local/kind.yaml`, `deploy/local/gateway.yaml`, `deploy/local/simulators.yaml`

**Work:**

- [ ] Choose and pin one supported Gateway/EPP pair and packaging path; deploy llm-d HTTP simulator replicas on kind.
- [ ] Trace request routing, metrics, streams and disconnects; diagnose readiness and labels.

**Validation / acceptance:**

- [ ] Document successful local routing and errors under known fixtures.
- [ ] Label all simulator timings synthetic; actual GPU fleet completion remains PLT-03.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="plt-02"></a>
## PLT-02 — Go locality/load scorer

**Status:** planned. **Package:** G. **Milestone:** December.

**Requirement/design:** [ROUTE-1](../design/routing-platform.md#route-1) / [ROUTE-2](../design/routing-platform.md#route-2) — [canonical design](../design/routing-platform.md). **Learning mode:** Build + Integrate. **Authorship target:** learner Go policy; EPP registration supplied.

**Dependencies:** [PLT-01](platform.md#plt-01), [BEN-01](benchmark.md#ben-01).

**Teaching:** [17](../curriculum/platform.md#module-17).

**Planned change boundary:** `routing/scorer/policy.go`, `routing/scorer/policy_test.go`, `routing/epp/adapter.go`

**Work:**

- [ ] Implement pure ranking over queue/reuse/affinity/health/staleness; document guard/normalization/tie settings before coding.
- [ ] Integrate provided EPP shell, bounded request-history locality, restart invalidation and fallback reasons.

**Validation / acceptance:**

- [ ] Equal-load, overloaded-affinity, missing/stale metrics, restart and no-healthy-endpoint fixtures pass.
- [ ] Show simulated cache-affinity overload counterexample and explain estimated versus actual residency.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="plt-03"></a>
## PLT-03 — Real GPU replicas and backend contracts

**Status:** planned. **Package:** G. **Milestone:** CP3.

**Requirement/design:** [PLAT-1](../design/routing-platform.md#plat-1) / [ROUTE-2](../design/routing-platform.md#route-2) — [canonical design](../design/routing-platform.md). **Learning mode:** Operate. **Authorship target:** learner-operated; launch/provision recipes supplied.

**Dependencies:** [PLT-02](platform.md#plt-02), [SRV-02](gpu-serving.md#srv-02), [BEN-04](benchmark.md#ben-04).

**Teaching:** [17](../curriculum/platform.md#module-17).

**Planned change boundary:** `deploy/gpu/replicas.yaml`

**Work:**

- [ ] Run two equivalent replicas of one engine/model, then swap engines sequentially; keep CPU tools separate where feasible.
- [ ] Record GPU topology/host privilege compatibility and compare round-robin, least-queue and bounded prefix affinity on real traces.

**Validation / acceptance:**

- [ ] Actual backend metrics/stream contracts and routing outcomes are verified per engine.
- [ ] Same offered workload/resources, real GPU evidence and cold-cache restart observations are retained; no multi-node fault-tolerance claim.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="plt-04"></a>
## PLT-04 — KV tiers, two adapters and cold start

**Status:** planned. **Package:** G. **Milestone:** CP3.

**Requirement/design:** [PLAT-2](../design/routing-platform.md#plat-2) — [canonical design](../design/routing-platform.md). **Learning mode:** Operate + Build analysis. **Authorship target:** learner analysis; offload/adapter recipes supplied.

**Dependencies:** [PLT-03](platform.md#plt-03).

**Teaching:** [18](../curriculum/platform.md#module-18).

**Planned change boundary:** `deploy/gpu/offload-adapters.yaml`

**Work:**

- [ ] Operate one compatible host-memory offloader and inspect LMCache/HiCache/native alternatives.
- [ ] Use two compatible LoRA adapters; measure residency, identity separation, restore/recompute crossover and cold-start stages.

**Validation / acceptance:**

- [ ] Incompatible adapter identities cannot reuse KV; offload report includes transfer/recompute costs and occupancy.
- [ ] No adapter-training dependency or remote-storage fleet is introduced.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="plt-05"></a>
## PLT-05 — Scaling, overload and failure diagnosis

**Status:** planned. **Package:** G. **Milestone:** CP3.

**Requirement/design:** [PLAT-2](../design/routing-platform.md#plat-2) — [canonical design](../design/routing-platform.md). **Learning mode:** Operate + Build policy. **Authorship target:** learner policy; autoscale/failure tools supplied.

**Dependencies:** [PLT-03](platform.md#plt-03).

**Teaching:** [19](../curriculum/platform.md#module-19).

**Planned change boundary:** `deploy/gpu/scaling.yaml`, `tests/platform/test_outcomes.py`

**Work:**

- [ ] Operate KEDA or HPA on existing capacity and inspect the alternative; define queue signal, stabilization and missing-metric behavior.
- [ ] Scale one-to-two and test overload/kill/drain/disconnect, OOM/slow-worker cases where feasible; distinguish pre-stream retry from partial-stream failure.

**Validation / acceptance:**

- [ ] Record readiness/cold-cache recovery, SLO failures, resource cleanup and explicit client outcomes.
- [ ] No emitted-token/tool replay or cloud-node autoscaler claim; write deploy/scale/TTFT-debug runbooks.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
