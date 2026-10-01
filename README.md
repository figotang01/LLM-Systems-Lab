# LLM Systems Lab

[GitHub repository](https://github.com/figotang01/LLM-Systems-Lab) · [Agent entry instructions](AGENTS.md) · [Teaching/implementation handoff](docs/HANDOFF.md)

One learning repository, two independently usable tracks. **Runtime and agent implementations are planned.** Existing runnable artifacts are the supplied experiment/budget and documentation-checking utilities with their tests, plus one historical HTML orientation lesson.

## Choose your track

| Track | What you build and learn | Start here |
|---|---|---|
| **Inference & Serving** | Correct runtime, attention/KV/scheduling, GPU execution, SGLang/vLLM, routing and serving experiments | [Inference entrance](tracks/inference/README.md) → [FND-01](tracks/inference/tasks/model.md#fnd-01) |
| **RAG & AI Agents** | Engineering assistant, retrieval, tools, memory, evaluation, human interaction, SFT and agentic RL | [Agent entrance](tracks/agents/README.md) → [AGT-01](tracks/agents/ROADMAP.md#agt-01) |

Both tracks start now; inference receives priority. December targets working RAG and broad agent knowledge alongside inference milestones. Full published **CMU 11-768 coverage and real agentic RL are required**, with later implementation continuing through spring 2027. Neither track requires completing the other; endpoint/trace exchange is optional.

## Read only what you need

| Your question | Canonical document |
|---|---|
| What is the whole project? | [PROJECT_PLAN.md](PROJECT_PLAN.md) — latest umbrella scope |
| What happens when, and how much work? | [Shared roadmap](docs/execution/roadmap.md) — preserved 528-hour baseline plus 280–400 hours of new scope |
| What do I study next? | [Curriculum entrance](teaching/CURRICULUM.md) — choose a track/current unit |
| What is implemented? | [Status and validation](docs/VALIDATION.md) |
| How do I hand a task to a coding agent? | [Handoff guide](docs/HANDOFF.md) — modes, first tasks, evidence and resumption |
| What runs locally, and what costs money? | [Resources](docs/execution/resources.md) — $500–700 combined planning range |

FND-01 and AGT-01 are independently ready for initial CPU/fixture work; neither requires a paid resource.

## Workspace map

| Location | Purpose |
|---|---|
| tracks/inference/ | Inference architecture, designs, tasks, curriculum, correctness/measurement and capstone |
| tracks/agents/ | Six canonical documents: overview, runtime, learning, roadmap, curriculum, coverage |
| docs/system/ | Shared endpoint/trace contracts and the single planned code inventory |
| docs/engineering/, docs/execution/ | Shared ownership/decisions and effort/resources |
| teaching/ | Shared teaching contract, curriculum entrance and delivered lesson artifacts |
| starter/, tools/, tests/ | Supplied experiment utility, documentation checks and their tests |
| docs/references/ | One reference catalog with research provenance |
| docs/archive/ | Historical plans/scope audits; normally skip |

Each track owns its detailed content; `docs/` owns shared guidance. Inference uses several subsystem files while agents use six consolidated documents because their content has different granularity. The distinction is file organization, not learning depth. Cross-links and short summaries do not introduce competing design owners.

Résumé files are kept outside this repository; project bullets are provided in conversation.

No empty source-file forest is recreated. Planned names and responsibilities live in the [code map](docs/system/code-map.md); create files when their task starts. Runtime code, training, runnable labs and new HTML remain deferred.

Existing local checks:

    python3 tools/check_docs.py
    python3 -m unittest discover -s tests -v
    python3 starter/experiment.py budget starter/budget.example.json

The starter example budget is historical, not the current combined ledger. The GitHub CPU workflow is supplied configuration; its hosted result remains unverified until a run exists. The declared remote is linked above; this local folder has not been initialized or pushed as a Git checkout.

For a new session, ask: “Read AGENTS.md and prepare the FND-01 lesson,” or “Read AGENTS.md and implement AGT-01.” The [handoff guide](docs/HANDOFF.md#choose-the-mode-from-the-request) explains the different deliverables.

<details>
<summary>Detailed navigation and source-of-truth rules</summary>

## System view

Inference: [architecture/contracts](tracks/inference/ARCHITECTURE.md), [model/runtime](tracks/inference/design/model-runtime.md), [KV/cache](tracks/inference/design/kv-cache.md), [scheduler](tracks/inference/design/scheduler.md), [GPU](tracks/inference/design/gpu-execution.md), [serving](tracks/inference/design/serving.md), [routing/platform](tracks/inference/design/routing-platform.md), [advanced labs](tracks/inference/design/advanced-labs.md).

Agents: [runtime/knowledge](tracks/agents/RUNTIME.md), [evaluation/training/capstone](tracks/agents/LEARNING.md), [course/migration coverage](tracks/agents/COVERAGE.md).

## Execution view

[Shared roadmap](docs/execution/roadmap.md) owns effort and scheduling. [Inference tasks](tracks/inference/tasks/README.md) and [agent tasks](tracks/agents/ROADMAP.md) own implementation status, dependencies and acceptance. [Curriculum](teaching/CURRICULUM.md) links to canonical lessons; [teaching contract](teaching/CONTRACT.md) owns delivery standards.

[Ownership/status](docs/engineering/ownership.md), [correctness](tracks/inference/engineering/correctness.md), [performance measurement/replay](tracks/inference/engineering/measurement.md), [open decisions](docs/engineering/open-questions.md), [references](docs/references/README.md), [inference capstone](tracks/inference/CAPSTONE.md), [original requirement ledger](docs/archive/scope-map.md).

## Source-of-truth rules

Overview → requirement/design → task → independent acceptance/evidence → milestone. Link to the owner instead of copying a competing plan. Knowledge coverage, authored/supplied code, implementation and operation are separate statuses. The historical 318/210-hour split is preserved accounting, not a claim that the expanded project still totals 528 hours.

The [archive](docs/archive/README.md) preserves earlier evolution. Old names, scope limits, prices and deadlines do not supersede current approval. Existing orientation HTML reflects the older baseline; use the current roadmap for scheduling.

</details>
