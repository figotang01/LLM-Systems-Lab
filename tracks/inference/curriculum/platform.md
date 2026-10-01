# Kubernetes, routing and platform operation

[Curriculum](../../../teaching/CURRICULUM.md) · [Teaching contract](../../../teaching/CONTRACT.md) · [Roadmap](../../../docs/execution/roadmap.md)

This guide groups existing module blueprints. Read only the module assigned by your current task. Module IDs, hours, objectives, exercises and exit gates are unchanged; HTML and runnable labs remain planned except the existing orientation.

Use the teaching contract for independent oracles, numerical/state examples, the explain/trace/predict/implement/measure rubric and one-week/one-month retrieval checks. Task briefs own implementation acceptance and authorship.

- [16 — Kubernetes from request path to reconciliation (A + G)](#module-16)
- [17 — Gateway routing and the Go scorer (G)](#module-17)
- [18 — KV tiers, adapters and cold start (G)](#module-18)
- [19 — Scaling, overload and failures (G)](#module-19)

<a id="module-16"></a>
## 16 — Kubernetes from request path to reconciliation (A + G)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 20 baseline h: A foundations 12 + G local lab 8. Hours are owned by the roadmap.

**Concept prerequisites:** [00](foundations.md#module-00). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

Study foundations before deployment; this module is not gated on completing 01–15.

### Teaching blueprint

- **Objectives:** operate pods/services/controllers and debug deployment/resource lifecycle as a newcomer.
- **Slides 1–10:** desired vs observed state, reconciliation, pod/deployment/service/DNS. **11–22:** image/runtime, requests/limits, GPU device allocation, liveness/readiness/startup. **23–38:** selectors, Helm/Kustomize, namespaces/RBAC, termination/drain and observing events.
- **Code:** supplied kind/simulator/Helm baseline; learner changes readiness/resource policy and diagnoses intentionally wrong labels and insufficient GPU requests.
- **Experiment/exit:** explain why an alive pod is not necessarily ready; follow one request through service endpoints. No multi-node cluster administration prerequisite.

### December storyboard sequence

Reconciliation → pods/services → readiness/resources → selectors/RBAC → deployment diagnosis. Split into 12 hours of foundations and an 8-hour simulator deployment lab.

### Implementation connections

- [FND-04](../tasks/model.md#fnd-04) — Kubernetes foundations; Operate + Explain.
- [PLT-01](../tasks/platform.md#plt-01) — Local gateway and simulator deployment; Operate.

**Design context:** [routing-platform](../design/routing-platform.md).

<a id="module-17"></a>
## 17 — Gateway routing and the Go scorer (G)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 12 baseline December h (G); real GPU continuation in January. Hours are owned by the roadmap.

**Concept prerequisites:** [16](platform.md#module-16), [03](foundations.md#module-03). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** implement one explainable locality/load score and integrate its real contract.
- **Slides 1–10:** gateway vs EPP vs model server, InferencePool and request metadata. **11–22:** locality estimates, queue delay, imbalance guard, session affinity and stale statistics. **23–36:** Go function/tests, normalization, fallback, plugin integration and counterexamples.
- **Code:** supply EPP version glue and chart; learner scoring logic and tests. Avoid programming a second standalone HTTP proxy given your PennCloud background.
- **Experiment/exit:** two equivalent replicas, skewed popularity and restarted worker; show when cache affinity overloads one worker.
- **References:** Gateway architecture, protocol and llm-d supported guide.

### December storyboard sequence

Gateway/EPP boundaries → endpoint observations → locality/load trade-off → stale metrics → policy tests → adapter integration. Demonstrate decisions across two simulated replicas.

### Implementation connections

- [SRV-02](../tasks/gpu-serving.md#srv-02) — Metrics, observability and backend contract; Modify + Operate.
- [PLT-01](../tasks/platform.md#plt-01) — Local gateway and simulator deployment; Operate.
- [PLT-02](../tasks/platform.md#plt-02) — Go locality/load scorer; Build + Integrate.
- [PLT-03](../tasks/platform.md#plt-03) — Real GPU replicas and backend contracts; Operate.

**Design context:** [routing-platform](../design/routing-platform.md), [serving](../design/serving.md).

<a id="module-18"></a>
## 18 — KV tiers, adapters and cold start (G)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** Within G January allocation; no additional hours. Hours are owned by the roadmap.

**Concept prerequisites:** [17](platform.md#module-17). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** compare recompute/restore costs and distinguish weight, KV and adapter residency.
- **Slides 1–10:** HBM/host/storage state; bytes/bandwidth lower bounds and overlap. **11–22:** LMCache lifecycle, HiCache alternative, tool gaps/TTL trade-offs. **23–34:** S-LoRA/Punica, adapter identities, weights/download/load/graph warmup.
- **Code:** supplied offload/LoRA deployment; learner cache-capacity perturbation and restore/recompute cost analysis.
- **Experiment/exit:** two adapters do not share incompatible KV; offload benchmark reports transfer and recompute, not just cache hit rate.

### Implementation connections

- [PLT-04](../tasks/platform.md#plt-04) — KV tiers, two adapters and cold start; Operate + Build analysis.

**Design context:** [routing-platform](../design/routing-platform.md).

<a id="module-19"></a>
## 19 — Scaling, overload and failures (G)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** Within G January allocation; no additional hours. Hours are owned by the roadmap.

**Concept prerequisites:** [17](platform.md#module-17). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** design a measured control policy and trace abort/retry semantics.
- **Slides 1–10:** HPA/KEDA, queue signals, hysteresis/stabilization, missing metrics. **11–22:** cold start and capacity ceilings, admission/deadlines, load shedding/fairness. **23–36:** kill/drain/OOM/slow pod, pre-stream retry vs partial stream error, client cancellation and cleanup.
- **Code:** supplied manifests, failure injector and dashboards; learner scaling thresholds, fallback and outcome assertions.
- **Experiment/exit:** scale one-to-two on existing GPU capacity, record readiness/SLO failures; no claim of cloud node autoscaling.

### Implementation connections

- [PLT-05](../tasks/platform.md#plt-05) — Scaling, overload and failure diagnosis; Operate + Build policy.

**Design context:** [routing-platform](../design/routing-platform.md).
