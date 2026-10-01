# Shared execution roadmap and effort ledger

[Overview](../../PROJECT_PLAN.md) · [Inference tasks](../../tracks/inference/tasks/README.md) · [Agent tasks](../../tracks/agents/ROADMAP.md) · [Curriculum](../../teaching/CURRICULUM.md)

Canonical owner of total learner effort, sequencing targets and milestone boundaries. Task briefs own implementation status; system documents own behavior. Both tracks start now, with inference prioritized. Runtime/application/training milestones remain planned.

## Preserved approved baseline — 528 hours

These allocations remain intact as the historical September 29 approval. Ownership migration does not charge existing work twice. Package C includes inference replay as well as agent work; J includes the moved four-hour B2 capsule. Do not label all C/J hours agent-only or subtract them from the project total.

| Package | Purpose | Baseline hours | Before December checkpoint | January–April |
|---|---|---:|---:|---:|
| A | Numerical, GPU, Kubernetes foundations | 32 | 32 | 0 |
| B | Measurement and production baselines | 34 | 34 | 0 |
| C | RAG/MCP workloads and evaluation | 34 | 20 | 14 |
| D | Dense runtime and paged memory | 72 | 72 | 0 |
| E | Scheduling and both prefix caches | 54 | 54 | 0 |
| F | GPU execution and serving integration | 54 | 54 | 0 |
| G | Platform and routing | 72 | 20 | 52 |
| H | Speculation, quantization, collectives/EP, P/D | 54 | 0 | 54 |
| I | Capstone study | 36 | 0 | 36 |
| J | Bridges, reproduction, release/contribution | 54 | 0 | 54 |
| Baseline | All original allocations | **496** | **286** | **210** |
| PF-1–PF-4 | Production-source development | **24** | **24** | **0** |
| AG-1a–AG-1c | CMU-informed agent extension | **8** | **8** | **0** |
| Combined | Preserved pre-expansion baseline | **528** | **318** | **210** |

The PF supplement stays 8/4/8/4 hours and retains every source/patch/defense requirement. AG stays 2/3/3, on top of module 15's 12 original December hours. Module 14 retains eight original December hours. Original January pilot/evaluation remains required. B2 stays approximately four hours inside J and is independently completable from supplied fixtures; expanded training is additional.

<a id="agent-expansion"></a>
## Approved agent expansion — 280–400 additional hours

| Additional work beyond retained baseline | Low | High |
|---|---:|---:|
| Deeper RAG, data lifecycle, retrieval adaptation | 20 | 40 |
| Durable execution, memory, tools, safety, frameworks | 40 | 60 |
| Research/coding/GUI capabilities, interaction, search | 50 | 70 |
| Evaluation and optimization beyond the baseline | 30 | 40 |
| SFT, agentic RL and RL systems beyond B2 | 110 | 150 |
| Research project, guest-topic exercises, reproduction | 30 | 40 |
| **Additional total** | **280** | **400** |
| **Project total including preserved 528** | **808** | **928** |

These are provisional learner estimates including study, exercises, coding, tests and experiments, not estimates of a tutor's HTML/scaffold authoring time. AT unit/task counts do not multiply the ledger. New shared long-context explanation is included in this expansion, not funded by reducing the original B3 capsule. Re-estimate after working RAG and the authored harness; record revisions explicitly. AI assistance does not remove understanding, debugging and independent-validation gates.

The historical December/spring split of 318/210 is preserved accounting, **not the current total or a new fixed expanded-period allocation**. Latest approval prioritizes broad agent knowledge and working RAG in December, permits remaining agent implementation in spring, and allows milestone dates to move with progress. Earlier December MCP/AG implementation gates stay required at flexible timing. No inference/PF task or original evaluation requirement is silently removed.

## Current parallel execution targets

| Window | Inference & Serving | RAG & AI Agents |
|---|---|---|
| October–November 2026 | Foundations, early measurement/production baselines, dense/paged runtime, scheduling/cache work | AGT-01/02 start now; foundations/retrieval/tools/evaluation study and initial training theory |
| December 2026 | CP2, standalone replay fixtures, local gateway/Go scorer, PF source work | Working RAG gate; first pass through most/all published CMU topics including all four training blocks; other implementation progresses as feasible |
| January–February 2027 | Real replicas, offload/scaling/reliability; advanced H labs | Original full pilot/live-quality gate targets January; durable service, memory/domain tasks and SFT |
| March–April 2027 | Independent routing capstone, bridges, reproduction and release | Required multi-turn agentic RL, RL systems, search/interaction experiments, independent agent capstone |
| Before May graduation | Reproduction/defense and remaining original work | Close required evidence, poster/report/demo/defense; record any unfinished work honestly |

The original inference late-April catch-up/recruiting buffer remains a planning preference; do not assume the expanded agent workload fits inside it without an explicit scheduling revision. At 808–928 estimated hours this is substantially more than a 20-hour/week project through graduation. Use actual progress to choose dates, retain scope, and preserve the compute reserve.

## Gate definitions

- **CP1:** valid client metric fixtures and both production-engine baselines, with raw errors/configurations; early model work proceeds alongside.
- **CP2:** correct real paged GPU runtime, scheduler/both caches, Triton/CUDA, graphs/profiles, serving lifecycle and measured same-model comparison.
- **Inference December:** CP2 plus standalone BEN-04 fixture/replay evidence, local simulated gateway/Go scorer and PF artifacts. Agent application completion is not a prerequisite.
- **Agent December:** AGT-02 working RAG, source/model revisions, initial checked/held-out evaluation, dense/hybrid and reranker ablations, evidence/abstention, stage cost/latency and explained failures.
- **CP3:** physical two-replica GPU platform, offload, scaling on existing capacity, failure/cleanup evidence and runbooks. Original application quality is now the separate **AGT-04 quality gate**, target January.
- **H gate:** original supported advanced operations plus mathematical/reference exercises and explicit unsupported configurations; no full custom-engine advanced integration required.
- **Inference CP4/release:** unchanged controlled routing study, all original bridge exercises (including standalone B2), clean reproduction/report/demo and prepared upstream contribution with tests; merge timing is external.
- **Agent engineering/learning/research gates:** AGT-03–14 evidence, including real SFT and multi-turn RL checkpoints, operated RL system, full course exercises and independent research artifacts. Numerical/source work does not replace required operation.

## Learning and dependency order

Inference: diagnostic → single request/early measurement → contiguous KV → paged ownership → scheduling/chunking/preemption → hash/radix → direct paged attention/kernels/graphs → replay fixtures/routing → real platform → advanced labs → capstone/release. Teach GPU memory before kernels and Kubernetes reconciliation/readiness before deployment.

Agents: task/fixture contracts → RAG and early evaluation → tools/authored loop → quality/trajectory gate → memory/durability → capability experiments, with SFT → agentic RL → RL systems as a later branch. Theory may precede its full implementation; full course mapping lives in the agent curriculum. Each track has its own ready task and can make progress without the other.

## Preserved inference implementation waves

These preserve the earlier skeleton's handoff sequence. Wave numbers are not the project CP1–CP4 gate names. They add no hours.

| Wave | Exit evidence / owning tasks |
|---|---|
| 0 — Contracts and handoff | Typed CPU-importable contracts and explicit unfinished methods ([FND-01](../../tracks/inference/tasks/model.md#fnd-01)); briefs/blueprints now delivered, runnable contracts still planned |
| 1 — Measurement and model | Valid observations and both baselines, single-request model and contiguous-cache correctness (BEN-01–03, MOD-01/02); baseline evidence closes CP1 |
| 2 — Memory and scheduling | Paged ownership, chunking/preemption/cancellation and both indexes under CPU-driven checks (KV-01–04, SCH-01–05) |
| 3 — GPU integration | Direct paged backend, kernel/graph work, streaming and measured comparison (GPU/SRV tasks); closes CP2 |
| 4 — Workloads and routing | Standalone fixture replay plus local gateway/scorer (BEN-04, PLT-01/02); agent capture/evaluation progresses independently |
| 5 — December handoff | Reproduction instructions, evidence inventory, explicit January backlog and known limits, plus PF evidence; agent evidence has its own gate |

Model/paging tasks begin in the early learning window and feed CP2; they are not extra preconditions for the original CP1 production-baseline gate. BEN-04 and SRV-02 close inference December/CP2 acceptance; PLT-03 owns real-platform continuation. Agent APP-01/04 now resolve to independent AGT-02/04 gates. A December successor therefore does not wait for January work.

## Recovery without dropping concepts

Review after two weeks, RAG completion, authored harness completion and time-box overruns. Reduce duplicate packaging and redundant configurations first; use attributed supplied code with substantive modification/debugging checks for lower-value plumbing. Preserve every required concept, correctness/quality gate and actual-operation requirement. Record date changes; a hardware-unavailable explanation remains studied, not operated. Maintain one main implementation increment per active track and prioritize inference when capacity conflicts.

<details>
<summary>Historical baseline calendar — preserved for provenance, superseded by parallel targets above</summary>

| Window | Original allocation and gate |
|---|---|
| Oct 5–18, 2026 | A 32 + B 20 = 52 h; diagnostic, GPU/Kubernetes foundations, initial baseline |
| Oct 19–Nov 8 | B 14 + D 64 = 78 h; CP1 and model/paging development |
| Nov 9–29 | D 8 + E 54 + F foundations 16 = 78 h; most engine fundamentals before December |
| Nov 30–Dec 13 | F 38 + C 14 = 52 h; CP2 GPU runtime and initial workload path |
| Dec 14–20 | C 6 + G 20 = 26 h; trace validation and local simulator/gateway/Go demo |
| Across the fall window | Additional PF 24 + AG 8 = 32 h, following the dependency order below |
| Dec 21–Jan 3 | Break retained |
| Jan 4–31, 2027 | C 14 + G 52 = 66 h; CP3: full pilot evaluation, GPU replicas, tiers, scaling, reliability |
| Feb 1–28 | H 54 h; advanced labs |
| Mar 1–14 | I 36 h; CP4 capstone |
| Mar 15–Apr 11 | J 54 h; bridge capsules, reproduction and release |
| Apr 12–May graduation | Reserved catch-up/recruiting/graduation buffer; no new core scope |

The original 318/11 ≈ 29 hours/week estimate applied to that fall schedule only. Its AG/PF tasks were additive then; the further agent expansion is now explicitly budgeted above. The older 440–560-hour uncertainty range is historical, not a current forecast.

</details>
