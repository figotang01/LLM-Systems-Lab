# Routing and serving platform

[Documentation index](../../../README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Task index](../tasks/README.md)

Status: planned system design; named source paths are reserved in the code map and will be created during implementation.

## Requirements

| ID | Requirement | Goal / evidence |
|---|---|---|
| <a id="route-1"></a>ROUTE-1 | Pure Go scoring with queue/load, estimated reuse, affinity, health and freshness | [G3](../../../PROJECT_PLAN.md#g3); deterministic ranking and fallback tests |
| <a id="route-2"></a>ROUTE-2 | Compare equivalent replicas within a pool under controlled policy/workload changes | [G2](../../../PROJECT_PLAN.md#g2)/[G5](../../../PROJECT_PLAN.md#g5); matched routing experiments |
| <a id="plat-1"></a>PLAT-1 | Reproduce a local simulator gateway and later a real two-GPU pool | [G3](../../../PROJECT_PLAN.md#g3); deployment/contract evidence |
| <a id="plat-2"></a>PLAT-2 | Diagnose readiness, capacity, offload, adapter identity, overload and failures | [G3](../../../PROJECT_PLAN.md#g3); January controlled lifecycle experiments |

## Architecture and December boundary

Client → supported Gateway API implementation → InferencePool/EPP → selected model-server endpoint. The EPP adapter translates endpoint/request observations into a pure Go scoring function; it owns integration state, not the inference engine scheduler. Supply chart/API-registration glue and choose one supported packaging/deployment path.

December: kind plus llm-d-inference-sim replicas, actual streams/metrics contract checks, custom scorer and failure fixtures. These HTTP replicas are separate from the runtime's FakeExecutor and virtual-clock tests. Their configured TTFT/cache behavior is illustrative, not GPU evidence.

January: two equivalent replicas of one model/engine on available GPUs; swap engines sequentially. Embeddings/reranking/tools stay on CPU where feasible. A rental must actually support the required Kubernetes/driver/transport privileges. If it does not, document the alternate platform environment rather than silently claim a Kubernetes GPU deployment.

## Routing policy

Inputs: queue estimate, estimated reusable tokens, session affinity, health/readiness, timestamp and endpoint identity. Output: score/ranking plus reasons suitable for inspection. Exact normalization, queue guard and freshness thresholds are OQ-06; do not hard-code untested constants as approved architecture.

Exclude unready endpoints. Bound the extra queueing allowed for affinity. If locality is unknown, fall back to load selection; if all load observations are stale, round-robin among healthy candidates; if none are eligible, surface an explicit unavailable outcome. Deterministic tie behavior belongs in the policy tests.

December locality uses bounded request history and is explicitly approximate. Do not derive prefix residency from KV-utilization percentage. Invalidate endpoint-local estimates after restart using the selected identity/epoch contract; pod identity alone may not capture every container restart. A real cache-event index remains later work, not an implicit December dependency.

## Platform lifecycle and later labs

Teach desired/observed state, reconciliation, namespaces/RBAC, selectors, DNS/services, readiness/liveness/startup, resources and GPU device allocation. A live pod is not necessarily ready to serve loaded weights. Helm/Kustomize alternatives are discussed; operate one. Inspect events to diagnose wrong labels and unavailable requested resources.

January adds LMCache or a compatible primary host-memory offloader, with HiCache/native alternatives inspected; measure restore versus recompute under limited capacity. Use two compatible LoRA adapters with cache-key separation, residency and loading exercises; no adapter-training dependency. Keep cold start stages—image/weights/load/graphs/cache warming—observable.

Operate KEDA or HPA scaling from one to two replicas on existing GPU capacity, inspecting the alternative. No cloud-node autoscaler implementation. Learner policy covers overload/admission, fairness, missing metrics and stabilization. Test kill/drain, overload, OOM/slow-worker cases as feasible, disconnects, cold-cache recovery, and resource cleanup. Preserve pre-stream versus partial-stream failure behavior; never automatically replay emitted tokens or side-effecting tools.

## Validation and implementation boundaries

[Platform tasks](../tasks/platform.md) sequence local deployment, scorer, actual GPU pool, tiers/adapters, and scaling/failure work. [Serving contracts](serving.md) own wire/metric compatibility; [capstone](../CAPSTONE.md) owns the routing study. Prometheus/Grafana, DCGM and OpenTelemetry/Tempo-or-Jaeger are supplied configurations with learner diagnosis/modification requirements.

Acceptance separates local simulation evidence from real GPU evidence and from untested multi-node fault tolerance. Record exact versions, units, backend parser contracts, resource limits, routing reasons, failure outcomes and commands. The local demo cannot close CP3; the later controlled two-GPU deployment cannot justify thousand-GPU experience.
