# RAG & AI Agents

[LLM Systems Lab](../../README.md) · [Project scope](../../PROJECT_PLAN.md) · [Current status](../../docs/VALIDATION.md)

Status: approved design and teaching blueprints; application, training runs, exercises and HTML lessons are **planned**. Start with [AGT-01](ROADMAP.md#agt-01) and its [startup sequence](ROADMAP.md#agt-01-startup-sequence); use the shared [handoff guide](../../docs/HANDOFF.md). No inference implementation is a prerequisite.

## What we are building

An engineering workspace assistant that retrieves evidence, investigates issues, uses tools, proposes and verifies fixes, and improves through evaluated trajectories and training. One versioned workspace supplies documentation, source code, issues, operational SQL records and a local issue dashboard. The example service/dashboard and environment-launching plumbing are supplied; the learner owns agent mechanisms and interpretation.

| Task family | Example | Independent success evidence |
|---|---|---|
| Documentation | Explain an API across versions | Supported answer and correct source locations |
| Investigation | Diagnose a regression from docs and SQL | Correct diagnosis, query and reproducible calculation |
| Research | Compare fixes using several sources | Evidence-backed synthesis that handles disagreement |
| Coding | Localize and repair a seeded bug | Patch passes hidden behavior checks and preserves existing tests |
| Computer use | Investigate/update an issue in the local dashboard | Application state verified independently of screenshots or agent claims |
| Collaboration | Delegate, clarify and obtain approval | Correct handoff, permission boundary and final artifact |

The existing inference-analysis exercise remains required: docs_search, read-only benchmark SQL and constrained analysis produce an evidence-backed answer without provisioning GPUs or changing deployments. Supplied/synthetic measurements must be labeled; performance claims require real experiment bundles.

Traceability: [G3](../../PROJECT_PLAN.md#g3) maps to runtime APP-1–3 and AR-1–4; [G4](../../PROJECT_PLAN.md#g4) maps to full course coverage and framework exercises; [G5](../../PROJECT_PLAN.md#g5) maps to AL-1/2/6 evaluation and research; [G6](../../PROJECT_PLAN.md#g6) maps to AL-3–5 training. The linked design requirement tables lead to tasks, independent acceptance and milestones.

## Reading path — six documents

| Document | Canonical responsibility |
|---|---|
| This overview | Application, goals, decisions and navigation |
| [Runtime design](RUNTIME.md) | Retrieval, tools, context/memory, harness, persistence, service and trace boundaries |
| [Evaluation and learning](LEARNING.md) | Task datasets, independent verification, optimization, SFT/RL and agent capstone |
| [Roadmap and tasks](ROADMAP.md) | Fourteen implementation increments, dependencies, milestones and status |
| [Curriculum](CURRICULUM.md) | Sixteen grouped teaching units, worked exercises and lesson exit checks |
| [Coverage map](COVERAGE.md) | Every CMU lecture/assignment, migrated requirement and job-skill signal |

Read only the current task and its linked design/lesson. [Shared ownership](../../docs/engineering/ownership.md), [teaching contract](../../teaching/CONTRACT.md), [resource ledger](../../docs/execution/resources.md), [reference catalog](../../docs/references/README.md) and [code map](../../docs/system/code-map.md#agent-track) remain single shared owners.

## Architecture and important decisions

Online: task → runtime → context construction → model → validated tools → observations → continuation/result. Retrieval, memory, permissions, budgets and traces support the loop.

Offline: versioned tasks/trajectories → independent evaluation → curated data → optimization/training → held-out evaluation → versioned release. Evaluation starts with the first RAG implementation.

- Build a bounded loop first, then reuse its tool/context/evaluation components in LangGraph. OpenHands receives its own operation and substantive modification exercise.
- Keep full evidence trajectories separate from model-visible context and from redacted telemetry.
- Use one Qdrant-backed retrieval implementation, retaining the pgvector comparison. Reranking retrieved evidence, scoring candidate answers, and estimating RL value are different responsibilities.
- Use maintained framework/training infrastructure; learner authorship is concentrated on policies, invariants, data, objectives, rewards and experiments.
- Require the full published CMU 11-768 syllabus, integrated harness/evaluation/training assignments and research-project outcomes. Agentic RL is required spring implementation, not an optional reading.
- Compare alternatives under declared budgets; additional agents, memory, search or training need not improve results.

## Framework depth

| Role | Selected tool and responsibility |
|---|---|
| Retrieval | Qdrant plus local BM25/RRF; pgvector comparison at the original explanatory depth |
| Minimal loop | mini-SWE-agent source reference; learner-authored bounded harness |
| Durable runtime | LangGraph: Build integration, Modify/Operate persistence and recovery |
| Coding-agent comparison | OpenHands: source walkthrough, real task run, substantive tool/skill modification |
| Harness comparison | DeepAgents: Explain context offloading/subagents; map to our interfaces |
| Interoperability | MCP: implement tool integration; A2A: bounded handoff exercise |
| Optimization | DSPy: one controlled prompt/program optimization experiment |
| Observability | OpenTelemetry/Phoenix: supplied instrumentation, learner diagnosis and metric definitions |
| Training | Transformers/PEFT/TRL: real small-model SFT and multi-turn RL |
| RL systems | verl with SGLang rollouts: operate, inspect synchronization, diagnose failures |
| Ecosystem | Google ADK and Microsoft Agent Framework: architecture/API comparison exercises |

Sources and rationale live in the [reference catalog](../../docs/references/README.md#agent-track-research). Pin compatible versions at each implementation handoff; a repository link is not a tested dependency set.

## Milestones and limits

Both tracks start now; inference receives priority. December targets broad course knowledge and the working RAG gate. Other agent implementation progresses into spring, including SFT, multi-turn agentic RL, RL systems and an independent agent capstone. [Detailed sequencing](ROADMAP.md#milestones)

The inference capstone remains separate. Any capable model endpoint can support this track; SGLang used by verl is an external training backend, not a dependency on completing the custom inference runtime. Optional endpoint/trace interoperability does not introduce a mandatory joint application.

Success requires runnable evidence and a learner explanation. Small fixtures demonstrate mechanisms; they do not establish production scale or population-level agent quality. Large-model pretraining, rebuilding a general sandbox, and implementing every comparison framework are outside the implementation scope; their relevant course mechanisms remain taught.
