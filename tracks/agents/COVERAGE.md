# Agent scope coverage and migration

[Overview](README.md) · [Tasks](ROADMAP.md) · [Curriculum](CURRICULUM.md) · [Original scope ledger](../../docs/archive/scope-map.md)

This is a traceability ledger, not a competing plan. Every required row has a canonical lesson, task and artifact. Mapping a topic does not mark its implementation complete. Research snapshot: **2026-09-30**, based on the public [CMU 11-768 syllabus](https://www.cmu-agents.com/), released lecture decks/assignments and the [primary-source catalog](../../docs/references/README.md#agent-track-research).

## Full course schedule mapping

All teaching rows are required. Breaks/project sessions remain visible for completeness but do not invent technical topics. Dates identify the source course, not this project's deadlines.

| CMU slot / date | Published topic or session | Canonical lesson | Task / required artifact |
|---|---|---|---|
| 1a · Aug 25 | Overview: what is an agent? | [AT-00](CURRICULUM.md#at-00) | [AGT-01](ROADMAP.md#agt-01): model/harness/environment state trace |
| 1b · Aug 27 | Tool use | [AT-02](CURRICULUM.md#at-02) | [AGT-03](ROADMAP.md#agt-03): authored loop, protocols, failures |
| 2a · Sep 1 | Long-context management | [AT-03](CURRICULUM.md#at-03), [canonical model concepts](../inference/curriculum/advanced.md#long-context-foundations) | [AGT-05](ROADMAP.md#agt-05): continuation/preservation and serving-tradeoff evidence |
| 2b · Sep 3 | Skills and memory | [AT-03](CURRICULUM.md#at-03) | [AGT-05](ROADMAP.md#agt-05): memory/skill lifecycle and harmful-retrieval case |
| 3a · Sep 8 | Planning, task decomposition, coordination | [AT-05](CURRICULUM.md#at-05) | [AGT-07](ROADMAP.md#agt-07): dependency plan/replanning comparison |
| 3b · Sep 10 | Coding agents | [AT-06](CURRICULUM.md#at-06) | [AGT-08](ROADMAP.md#agt-08): independently verified repair and task construction |
| 4a · Sep 15 | Computer-use agents | [AT-06](CURRICULUM.md#at-06) | [AGT-08](ROADMAP.md#agt-08): grounded GUI actions and end-state verifier |
| 4b · Sep 17 | Training 1: SFT | [AT-11](CURRICULUM.md#at-11) | [AGT-11](ROADMAP.md#agt-11): data/mask checks, real checkpoint and evaluation |
| 5a · Sep 22 | Training 2: RL basics | [AT-12](CURRICULUM.md#at-12) | [AGT-12](ROADMAP.md#agt-12): exact gradient/advantage examples |
| 5b · Sep 24 | Deep research agents | [AT-05](CURRICULUM.md#at-05), [AT-01](CURRICULUM.md#at-01) | [AGT-07](ROADMAP.md#agt-07): iterative retrieval and verified synthesis |
| 6a · Sep 29 | Training 3: advanced RL algorithms | [AT-13](CURRICULUM.md#at-13) | [AGT-12](ROADMAP.md#agt-12): algorithm comparisons, reward attack, real multi-turn RL |
| 6b · Oct 1 | Training 4: RL systems | [AT-14](CURRICULUM.md#at-14) | [AGT-13](ROADMAP.md#agt-13): operated rollout/learner and version/recovery evidence |
| 7a · Oct 6 | Sandboxing and credential management | [AT-08](CURRICULUM.md#at-08) | [AGT-03](ROADMAP.md#agt-03), [AGT-06](ROADMAP.md#agt-06): enforced permissions/credential boundaries |
| 7b · Oct 8 | OpenHands | [AT-07](CURRICULUM.md#at-07) | [AGT-08](ROADMAP.md#agt-08): source map, operation and substantive modification |
| 8a · Oct 13 | Fall break | No new topic | No assignment invented |
| 8b · Oct 15 | Fall break | No new topic | No assignment invented |
| 9a · Oct 20 | LangGraph | [AT-07](CURRICULUM.md#at-07) | [AGT-06](ROADMAP.md#agt-06): durable integration and recovery |
| 9b · Oct 22 | Observability and monitoring | [AT-08](CURRICULUM.md#at-08) | [AGT-06](ROADMAP.md#agt-06): task-to-stage diagnosis, cost/redaction |
| 10a · Oct 27 | Agents and the future of work | [AT-09](CURRICULUM.md#at-09) | [AGT-09](ROADMAP.md#agt-09): measured supervision/workflow analysis |
| 10b · Oct 29 | Multi-agent interaction | [AT-09](CURRICULUM.md#at-09) | [AGT-09](ROADMAP.md#agt-09): bounded handoff and single-agent comparison |
| 11a · Nov 3 | Project hours | [AT-15](CURRICULUM.md#at-15) | [AGT-14](ROADMAP.md#agt-14): proposal/progress feedback |
| 11b · Nov 5 | Project hours | [AT-15](CURRICULUM.md#at-15) | [AGT-14](ROADMAP.md#agt-14): experiment-design review |
| 12a · Nov 10 | Human-agent interaction | [AT-09](CURRICULUM.md#at-09) | [AGT-09](ROADMAP.md#agt-09): clarification/correction/approval evidence |
| 12b · Nov 12 | Reranking and critic models | [AT-10](CURRICULUM.md#at-10) | [AGT-10](ROADMAP.md#agt-10): independent ranking/critic calibration |
| 13a · Nov 17 | Tree search | [AT-10](CURRICULUM.md#at-10) | [AGT-10](ROADMAP.md#agt-10): bounded branching/rollback and compute comparison |
| 13b · Nov 19 | Guest: Karthik Narasimhan; topic not captured in review | [AT-15](CURRICULUM.md#at-15) | [AGT-14](ROADMAP.md#agt-14): required topic exercise; verify current materials |
| 14a · Nov 24 | Guest: Sasha Rush; topic not captured in review | [AT-15](CURRICULUM.md#at-15) | [AGT-14](ROADMAP.md#agt-14): required topic exercise; verify current materials |
| 14b · Nov 26 | Thanksgiving | No new topic | No assignment invented |
| 15a · Dec 1 | Poster presentations | [AT-15](CURRICULUM.md#at-15) | [AGT-14](ROADMAP.md#agt-14): poster/demo |
| 15b · Dec 3 | Poster presentations | [AT-15](CURRICULUM.md#at-15) | [AGT-14](ROADMAP.md#agt-14): defense/final report and limitations |

## Assignment and learning-objective preservation

| Source objective | Integrated implementation | Evidence |
|---|---|---|
| Implement an agent over an open model | AGT-03, AT-02 | Learner-written loop plus actual open-model endpoint run |
| Design multistep evaluations | AGT-04, AT-04 | Private outcomes, failure taxonomy, calibrated judge and protected split |
| Train agents | AGT-11/12/13, AT-11–14 | Real SFT and multi-turn RL checkpoints and operated RL system |
| Reason about safety/reliability | AGT-03/06/09, AT-08/09 | Permission, credential, recovery and interaction tests |
| Pursue an open research question | AGT-14, AT-15 | Proposal, check-in, controlled experiment, poster and final report |
| Assignment 1: reusable harness, coding tools/skills, compaction, another tool domain, programmatic calls | AGT-03/05/08 | Same loop reused across analysis/code/browser domains; task/constraint preservation and tool composition |
| Assignment 2: validator, task creation, trajectory/artifact evidence and error analysis | AGT-04 | Wrong data/aggregate, wrong artifact/presentation, execution failure and evaluator false acceptance; confusion/MCC analysis where suitable |
| Assignment 3: agent training procedures | AGT-11–13 | Required training objectives above; assignment-specific details not captured; verify current materials |
| Half-semester research project | AGT-14 | Individual adaptation of proposal/check-in/poster/report; original CMU team/grading rules are not project requirements |

User selected **integrated labs**, not separately completing all original course applications. Preserve substantive objectives and attributed methods; do not publish restricted official solutions or claim original assignment completion from adapted exercises.

## Original requirements and stable aliases

| Previous requirement | Canonical owner | Preserved content |
|---|---|---|
| APP-1 / APP-01 / module 14 / C.1–C.4 | [Runtime APP-1](RUNTIME.md#app-1), [AGT-02](ROADMAP.md#app-01), [AT-01](CURRICULUM.md#module-14) | Versioned corpus/Qdrant, embeddings/BM25, RRF, reranking, prompt/layout, evidence metrics and pgvector comparison |
| APP-2 / APP-02 / module 15 / C.5 | [Runtime APP-2](RUNTIME.md#app-2), [AGT-03](ROADMAP.md#app-02), [AT-02](CURRICULUM.md#module-15) | MCP, three original tools, limits, structured output/XGrammar concepts, tool-result caching, semantic failures and restricted-runner limits |
| APP-3 / APP-03 / C.6 | [Runtime APP-3](RUNTIME.md#app-3), [AGT-04](ROADMAP.md#app-03) | Exact input/revision identity, parent IDs/tool gaps, mode/outcomes, compatible compaction metadata and ~50 varied sessions |
| APP-04 / original January evaluation | [AGT-04](ROADMAP.md#app-04), [AL-1](LEARNING.md#al-1) | 30 RAG questions/15 tasks, one-third held out, live quality, ablations, human-calibrated judges and uncertainty; 100/30 expansion when review fits |
| AG-1a / two added hours | [AGT-03](ROADMAP.md#ag-1a), [AT-02](CURRICULUM.md#at-02) | Authored loop, normal/recoverable/budget trajectories and additional inference-analysis exercise |
| AG-1b / three added hours | [AGT-05](ROADMAP.md#ag-1b), [AT-03](CURRICULUM.md#at-03) | Task/constraint/tool-pair preservation, full trajectory, identity changes and bounded live compaction comparison |
| AG-1c / three added hours | [AGT-04](ROADMAP.md#ag-1c), [AT-04](CURRICULUM.md#at-04) | Correct/wrong/unsupported outputs, weak-verifier failure, improved independent check and residual limit |
| APP-4 / AG supplement teaching | [Runtime APP-4](RUNTIME.md#app-4), [retained storyboard](CURRICULUM.md#module-ag-1) | Original 2/3/3 hours and all exercise exits; full course is separately funded expansion |
| C.7 / BEN-04 / module 15 replay | [BEN-04](../inference/tasks/benchmark.md#ben-04), [replay lesson](../inference/curriculum/foundations.md#module-15-replay) | Three measurement modes, DAG/delays, live versus fixed content, failed dependent accounting |
| B2 / J bridge | [Standalone B2](CURRICULUM.md#module-b2), [AGT-13](ROADMAP.md#agt-13) | Original ~4 hours, optimizer state, tiny training-loop modification, DP/FSDP/ZeRO, SFT/RLHF/GRPO, verl/Miles/slime versions and distillation |
| I.6 live quality check | [AGT-04](ROADMAP.md#agt-04), [agent capstone](LEARNING.md#independent-agent-capstone) | Required small live-agent quality/tool check; optional report exchange with inference capstone |
| ADV-02 quality dependency | [ADV-02](../inference/tasks/advanced-release.md#adv-02) | Independent frozen inference quality fixtures; agent quality remains required under AGT-04 |
| All inference/PF/H–J requirements | [Original scope map](../../docs/archive/scope-map.md) | Every original numerical/ownership/runtime/platform/advanced/source-development and release requirement remains |

Legacy anchors resolve in the new owners. Historical package accounting is preserved at **528 hours**; moving requirements does not charge them again. Package C remains a historical mixed package (including BEN-04); do not call all its hours agent-only. New requirements add **280–400 hours**, with one [central ledger](../../docs/execution/roadmap.md#agent-expansion).

Explicit changes from older restrictions: the eight-hour AG supplement is no longer the limit of agent scope; the full CMU curriculum, SFT, multi-turn agentic RL and RL systems are required additions. B2's small exercise stays independently completable for inference learners. Original December agent implementation dates become flexible under the latest approval; January pilot completion remains a target and required gate. No task is erased to fund these changes.

## System boundary and independence audit

| Boundary | Rule / acceptance |
|---|---|
| Agent install/tests | CPU application checks do not import inferstack, CUDA, Kubernetes or the training environment |
| Inference install/tests | Core/bench/platform checks do not import agent_lab or require a live agent application |
| Model endpoint | Any declared-capable endpoint; support checks are explicit. Raw rendered-text serving need not support the agent tool API |
| Trace exchange | Agents export versioned SessionTrace; inference can start with self-contained supplied fixtures |
| Evaluation | Live task quality belongs to agents; inference replay proves timing/dependency behavior, not model task success |
| Training serving | verl may use production SGLang independently of completing this repository's inference track |
| Shared concepts | Canonical model/cache/parallelism explanations are linked; agent study does not imply a duplicate engine lab |
| Capstones | Two independent experiments; optional shared endpoints/artifacts, no compulsory integrated system |

Removed dependency edges: APP-01→BEN-03, APP-03→BEN-01, APP-04→BEN-04, BEN-04→APP-03, ADV-02→APP-04 and REL-02→APP-04. Replace input dependencies with explicit self-contained fixture/contract requirements, not missing validation. Recheck both task graphs after future edits.

## Industry skill and evidence map

| Research signal | Required project evidence | Owner |
|---|---|---|
| SDE lifecycle/traceable agent services | Contracts, meaningful tests, durable state, operations/runbooks, source modification | AGT-01/03/06/08 |
| Retrieval/generation under latency constraints | Labeled retrieval/evidence quality, ablations, stage/session cost and latency | AGT-02/04/07 |
| Conversation evaluation and statistics | Task/family splits, uncertainty, judge calibration, failure attribution | AGT-04/10/14 |
| Verified data/model improvement | Audited trajectories, SFT/RL, independent outcomes and reproducible releases | AGT-11–14 |
| Human feedback and interoperability | Clarification/approval, MCP/A2A, shared budgets, framework comparisons | AGT-03/06/09 |

Use the [sampled primary job descriptions](../../docs/references/README.md#agent-track-research) as skill evidence, not a promise of currently open roles, new-graduate eligibility or equivalent production experience.

<a id="course-update-rule"></a>
## Course update rule and unresolved external details

The earlier September 30 review recorded lecture decks 01–11. Detailed later decks, guest-lecture topics and the Assignment 3 brief were not captured. This is a limitation of the recorded review, not proof that those materials are currently unpublished. A later check could retrieve the official course overview but could not independently confirm the full material-release list. Recheck the official course links when authoring those units; do not invent missing topics or assignment requirements.

Known syllabus topics can be taught now using their primary readings and framework documentation. Course-specific alignment remains pending review where the original materials have not been inspected; this does not block the rest of the track.

Before authoring an affected lesson, check the official syllabus/materials, record date/source/revision, and add its substantive objectives to the existing unit/task. Compare coverage against the full published lecture and assignment content; preserve additions instead of silently substituting a selected excerpt. If a new topic changes scope materially, record the delta and estimate; continue independent work. A missing release stays explicitly pending external material and cannot be marked completed.

Software/model/hardware pins and actual capability/fit require task-level smoke tests. Remaining choices live in the [open-question register](../../docs/engineering/open-questions.md); neither unavailable future materials nor version pins block this documentation handoff.
