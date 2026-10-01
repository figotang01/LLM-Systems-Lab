# LLM Systems Lab — project overview

Canonical umbrella scope, updated **2026-09-30**. [Start here](README.md) · [Shared roadmap](docs/execution/roadmap.md) · [Current status](docs/VALIDATION.md)

## Motivation and background

Build a defensible understanding of both how LLMs execute efficiently and how useful agent applications are engineered, evaluated and trained. The learner knows Python/PyTorch/transformers and has PennOS/PennCloud systems experience; CUDA and Kubernetes need explicit teaching. Supplied transport, loaders, deployment plumbing and UI avoid rebuilding familiar infrastructure while preserving mechanism ownership and independent checks.

## Goals and non-goals

| Goal | Outcome | Evidence |
|---|---|---|
| <a id="g1"></a>G1 — Correct inference | Dense Qwen3 runtime, paged KV, scheduling, both prefix indexes, real GPU attention | Numerical oracles, ownership/lifecycle tests and GPU results |
| <a id="g2"></a>G2 — Measurable performance | Operate vLLM/SGLang and explain runtime/kernel gaps fairly | Raw observations, profiles, controlled ablations |
| <a id="g3"></a>G3 — Serving and useful workloads | Small routing platform and independently usable RAG/agent application | Replay correctness, local/later two-GPU serving, independently checked application outcomes |
| <a id="g4"></a>G4 — Transferable engineering | Build mechanisms; modify/operate frameworks; complete the full published CMU agent syllabus | Learner explanations, Triton/CUDA work, SGLang patch, durable/tool/interaction exercises |
| <a id="g5"></a>G5 — Reproducible conclusions | Independent inference-routing and agent-improvement studies | Reports, raw artifacts, negative results and limits |
| <a id="g6"></a>G6 — Agent learning | Curate trajectories and train/evaluate small agents | Real SFT/multi-turn RL checkpoints; rollout/learner correctness and independent success metrics |

No large-model pretraining, general hardened sandbox, multi-node GPU fleet, universal numerical identity, guaranteed speedup or upstream merge is required. Full agent-course concepts remain required even where research-scale reproductions use bounded worked exercises. SFT, multi-turn agentic RL and RL-system operation are required practical milestones.

## What we are building

Two independent systems share documentation conventions and may exchange endpoints/artifacts:

- **Inference & Serving:** custom runtime → GPU backend → serving/benchmarking → routing platform → independent routing study.
- **RAG & AI Agents:** engineering workspace → retrieval/tools/runtime → independent evaluation → SFT/RL improvement → independent agent study.

The inference runtime, production engines and gateway retain their approved design. Agent development uses any declared-capable model endpoint and does not wait for the custom engine. Inference benchmarks use standalone supplied workload fixtures when agent exports are unavailable. No compulsory joint application or evaluation experiment is introduced.

## Tracks and major decisions

| Track | Scope | Canonical entrance |
|---|---|---|
| Inference & Serving | Model/attention, paged ownership, scheduler, hash/radix, Triton/CUDA/graphs, serving metrics, vLLM/SGLang, Go/Kubernetes, speculation/quantization/TP/EP/P/D and bridges | [Inference](tracks/inference/README.md) |
| RAG & AI Agents | Retrieval/evidence, MCP/tools, context/memory/skills, durable workflow, research/code/GUI, human/multi-agent interaction, evaluation/search/optimization, SFT/RL/RL systems | [Agents](tracks/agents/README.md) |

Use one engineering workspace with docs, code, issues, SQL records and a local dashboard. Supply the fixture service and ordinary plumbing; retain learner ownership of policies, invariants, verifiers, training data/objectives and interpretation. Preserve the original inference-analysis agent as a required exercise.

Keep one authoritative implementation per mechanism. Attention/KV/serving theory is canonical in inference lessons; the agent curriculum links to it without a duplicate engine lab. Agent memory concerns semantic/episodic/procedural state; agent search and inference token scheduling remain separate systems. [Boundary contract](docs/system/track-contracts.md#track-boundary)

Build a small agent loop before LangGraph integration; operate and modify OpenHands. Use Qdrant with the pgvector comparison, MCP/A2A, DSPy, OpenTelemetry/Phoenix, Transformers/PEFT/TRL and verl/SGLang at assigned depths. Alternatives teach different abstractions without multiplying full applications. [Agent runtime design](tracks/agents/RUNTIME.md) · [Learning design](tracks/agents/LEARNING.md)

## Execution and success

Graduation is May 2027. Start both tracks now, prioritize inference, and target broad agent knowledge plus working RAG in December. Agent implementation dates may move with observed progress; all required topics remain tracked. [Full CMU/assignment coverage](tracks/agents/COVERAGE.md)

| Gate | Required outcome |
|---|---|
| Inference CP1/CP2 | Trustworthy baselines; correct real paged GPU runtime, scheduling/caches, kernels/graphs and explained comparisons |
| Inference December | CP2, standalone replay fixtures, local gateway/Go scorer and PF source-development evidence |
| Agent December | Versioned RAG, initial checked/held-out questions, dense/hybrid/reranker ablations, evidence/abstention and stage cost/latency |
| January targets | Inference two-replica/platform continuation; independently, complete original workload pilot and live quality checks |
| Agent spring | Durable runtime, capabilities, real SFT/multi-turn RL, RL systems and full course exercises |
| Capstones/release | Separate studies, clean reproduction, report/poster/demo/defense and honest authorship |

Preserve the historical **528-hour baseline** (318 through December, 210 January–April). Expansion adds **280–400 hours**, for **808–928 total**; moving content adds no hours. New effort is not silently funded by shrinking inference tasks. Actual capacity and AI assistance determine pacing, not which concepts disappear. [Sole effort ledger](docs/execution/roadmap.md)

## Resources, status and reading path

Use the M4/16 GB Mac for bounded local work, isolated environments and short prepared GPU sessions. Confirmed combined planning range: **$500–700**, with a $600 working allocation. RL rollouts and repeated search/judging add substantial cost; bound model/run size without marking unfinished practical work as completed study. [Resources](docs/execution/resources.md)

Delivered: documentation/teaching blueprints, agent handoff instructions, supplied experiment/documentation utilities with tests, CPU CI configuration and one historical orientation HTML. No implemented inference runtime, agent application or training result is claimed. Create source files at task start; planned responsibilities live in the [code map](docs/system/code-map.md).

Read overview → chosen track → one task → linked design/lesson. Shared [ownership](docs/engineering/ownership.md) and [teaching](teaching/CONTRACT.md) rules retain Build/Modify/Operate/Explain. [Open questions](docs/engineering/open-questions.md) record course materials needing availability checks and compatibility decisions; [archives](docs/archive/README.md) are historical.
