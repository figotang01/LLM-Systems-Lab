# Shared track boundaries

[Project overview](../../PROJECT_PLAN.md) · [Code map](code-map.md) · [Inference](../../tracks/inference/README.md) · [Agents](../../tracks/agents/README.md)

Status: approved logical interoperability boundaries; concrete schemas and adapters remain planned. This is the sole owner of endpoint/trace exchange. Track designs own their internal execution.

<a id="track-boundary"></a>
## Track boundary and optional exchange

Inference owns attention/KV/cache/scheduling/GPU/serving internals, metrics, load generation and performance replay. Agents own retrieval, semantic memory, task state, tools, live quality and model improvement. Root-level starter artifact/provenance conventions and teaching/authorship rules are shared; no common heavyweight runtime is introduced.

**Model boundary:** ordinary configured HTTP model endpoints with declared capabilities, revisions and usage/error semantics. Tool/vision support is checked by the agent adapter; the custom rendered-text endpoint is not assumed to provide every production API capability. Agents can use an external provider or independently launched production engine. Inference can benchmark supplied prompts without running agents.

**SessionTrace boundary:** preserve run/session/request/parent IDs, rendered prompts or reconstructible token IDs with model/tokenizer/template revisions, recorded tool/think delays, terminal outcomes, corpus/tool/content versions and measurement mode. Optional compaction metadata links old/new prompt identities. Exact serialization is materialized at the first owning trace task and documented here, with a schema version and old-fixture compatibility test. Both adapters implement this logical contract; neither requires the other package's runtime objects. Supplied self-contained fixtures make both task paths independently startable.

Agent APP-03/AGT-04 owns capture/export and live semantics; BEN-04 owns performance fixture validation and replay eligibility. Full training trajectories and private scoring data are not the public performance export. Exported traces never invent missing exact tokens/timestamps or hidden reasoning; sensitive fixtures require appropriate redaction/access while private reproduction artifacts preserve authorized exact inputs.

**Evidence boundary:** live task success and training rewards belong to agent evaluation; fixed transcripts establish performance/dependency behavior. The inference capstone remains independent and can link a separately produced live-quality report. The original B2 learning capsule can be studied independently of full agent implementation.

Acceptance: no mandatory inference task depends on AGT/APP completion; no mandatory agent task depends on engine/GPU/platform implementation. Independent installation/smoke checks are future task acceptance, not claimed to pass for packages that do not exist yet.
