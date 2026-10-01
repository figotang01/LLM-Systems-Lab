# Serving transport and backend contracts

[Documentation index](../../../README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Task index](../tasks/README.md)

Status: planned system design; named source paths are reserved in the code map and will be created during implementation.

## Requirements

| ID | Requirement | Goal / evidence |
|---|---|---|
| <a id="srv-1"></a>SRV-1 | Documented compatible completion/chat subset with explicit rejection of unsupported options | [G3](../../../PROJECT_PLAN.md#g3); request/response fixtures |
| <a id="srv-2"></a>SRV-2 | Streaming, finish/error and disconnect/cancellation semantics reflect actual engine state | [G1](../../../PROJECT_PLAN.md#g1)/[G3](../../../PROJECT_PLAN.md#g3); transport plus lifecycle tests |
| <a id="srv-3"></a>SRV-3 | Normalize engine metrics/capabilities from tested versions | [G2](../../../PROJECT_PLAN.md#g2)/[G3](../../../PROJECT_PLAN.md#g3); backend/gateway contract tests |

## Responsibilities and request flow

Supply the HTTP/SSE server shell, schema adapters, model loader/tokenizer plumbing, and client parser. Learner work owns cancellation propagation, lifecycle integration, capability checks and metric meanings. Do not rebuild a general HTTP server after PennCloud.

The transport validates model selection and supported request fields, renders the pinned chat template, submits tokenized work to the coordinator, forwards content/usage/finish/error events, and translates client disconnect into cancellation intent. Only the coordinator releases resources. Greedy is the custom-engine integration baseline; the model lesson preserves sampling concepts separately.

The public compatibility scope includes messages/completions, streaming, usage, finish and error behavior, and cancellation. OQ-07 must define exact paths/fields/statuses before implementation. Full tool-call/grammar parity is required only on the chosen production workload path; custom runtime replay can use exact rendered text. Reject unsupported options rather than silently ignore them; engine extras such as ignore_eos require explicit capabilities.

## Stream and failure semantics

Metadata-only SSE events do not establish first generated content. Client chunks may contain multiple tokens; transport must retain events/count sources without inventing individual token timestamps. Disconnect, deadline, overload, model error, and normal completion are distinguishable outcomes. Test empty content, one-token output, partial output then failure, and cancellation races.

Retries before first output and failure after a partial stream have different semantics. Do not automatically replay already emitted tokens or side-effecting tools. Exact pre-stream retry policy is part of the platform contract, not an assumption inside the benchmark.

## Metrics and adapters

Export request/queue/cache/resource observations with units, labels, freshness and provenance. A prefix hit count, KV utilization and queue depth are not interchangeable, and three familiar vLLM metric names do not establish EPP compatibility. The platform adapter must contract-test actual selected backends, streams, disconnects and metric parsing.

Prometheus/Grafana and OpenTelemetry configuration are supplied; the learner modifies one query and explains one end-to-end trace. Choose Tempo or Jaeger and inspect the alternative. DCGM applies to real GPU operation; do not require a full monitoring cluster beside all workloads on the 16 GB Mac.

## Dependencies and acceptance

Use [SRV-01/SRV-02 and GPU tasks](../tasks/gpu-serving.md), [BEN tasks](../tasks/benchmark.md), and [platform tasks](../tasks/platform.md). Acceptance requires explicit supported API behavior, valid lifecycle/cancellation cleanup, real metric semantics, and a tested gateway/model-server combination. Follow the cross-cutting [measurement contract](../engineering/measurement.md); observational clock domains must remain explicit.
