# Agent implementation roadmap

[Overview](README.md) · [Design](RUNTIME.md) · [Learning design](LEARNING.md) · [Curriculum](CURRICULUM.md) · [Shared hours](../../docs/execution/roadmap.md)

Status: all AGT tasks are **planned**. This document owns agent task status, sequence and acceptance; the shared roadmap owns the sole effort ledger. Source paths are planned, not files delivered by this restructuring. Legacy APP/AG IDs are aliases for retained requirements within these tasks, not duplicate work items.

## Milestones

| Window | Learning target | Implementation target |
|---|---|---|
| October–November 2026 | Foundations, retrieval, tools, context, evaluation; begin training theory | Start AGT-01/02 now, alongside inference; harness as progress permits |
| December 2026 | First pass through most/all published CMU topics, including four training blocks | Working RAG gate; separate knowledge and implementation status for every later topic |
| January–February 2027 | Durable engineering and model adaptation | Original full pilot/live-quality gate targets January; runtime/domain/SFT work advances by dependencies |
| March–April 2027 | Advanced RL, systems, search and research synthesis | Real agentic RL and RL systems, remaining capability experiments, capstone |
| Before May graduation | Defense and reproduction | Close required evidence or explicitly record remaining work |

Inference remains the priority. These dates are targets, not a claim that 20 hours/week completes the expanded scope. Latest approval allows agent implementation dates to move; the earlier December MCP/AG gates are retained requirements with flexible timing, not deleted work. Required concepts are never silently relabeled optional. Review actual pace after RAG and the authored harness.

## Selecting work and handing it off

Start AGT-01. Thereafter select the earliest planned task whose dependency artifacts have evidence. AGT-03's core/tool setup may start after AGT-01; its docs_search integration/completion additionally requires AGT-02. Evaluation design and safety begin in AGT-01–03, before AGT-04/06 completion. Start AGT-14's proposal/split/protocol work after AGT-04 and before optimization/training; its listed prerequisites govern final completion, not permission to plan the study. Teaching theory may precede code dependencies, especially RL mathematics.

For each task read its design, teaching unit and [ownership rules](../../docs/engineering/ownership.md). The normal handoff contains prerequisites, permitted change boundary, supplied fixtures, independent oracle, hardware class, scope exclusions, planned commands (clearly unvalidated), artifact types and expected explanation. Create only needed files under `tracks/agents/`; production code never imports teaching reference solutions.

Completion records must contain paths/commit or checksums, authorship, exact executed commands, environment/model/data revisions, raw artifacts, independent results, limitations and learner explanation. Until such a record exists, the status stays planned/in progress. Tests and path names in this document are acceptance specifications, not implemented tests. No GPU/API expense occurs merely because a task is documented.

## Task index

| Task | Increment | Main dependencies |
|---|---|---|
| [AGT-01](#agt-01) | Workspace and logical contracts | None |
| [AGT-02](#agt-02) | Versioned RAG baseline | [01](#agt-01) |
| [AGT-03](#agt-03) | MCP tools and learner-authored harness | [01](#agt-01), [02](#agt-02) |
| [AGT-04](#agt-04) | Evaluation, trajectories and original pilot completion | [02](#agt-02), [03](#agt-03) |
| [AGT-05](#agt-05) | Context compaction, memory and skills | [03](#agt-03), [04](#agt-04) |
| [AGT-06](#agt-06) | Durable agent service and observability | [03](#agt-03), [04](#agt-04), [05](#agt-05) |
| [AGT-07](#agt-07) | Planning and deep research | [04](#agt-04), [05](#agt-05), [06](#agt-06) |
| [AGT-08](#agt-08) | Coding, computer use and OpenHands | [04](#agt-04), [05](#agt-05), [06](#agt-06) |
| [AGT-09](#agt-09) | Human and multi-agent interaction | [06](#agt-06), [07](#agt-07), [08](#agt-08) |
| [AGT-10](#agt-10) | Critics, search and prompt optimization | [04](#agt-04), [07](#agt-07), [08](#agt-08) |
| [AGT-11](#agt-11) | Training data, retrieval adaptation and SFT | [04](#agt-04), [05](#agt-05) |
| [AGT-12](#agt-12) | Multi-turn agentic RL | [04](#agt-04), [11](#agt-11) |
| [AGT-13](#agt-13) | RL systems and production rollout investigation | [12](#agt-12) |
| [AGT-14](#agt-14) | Agent research capstone and reproduction | [01](#agt-01), [02](#agt-02), [03](#agt-03), [04](#agt-04), [05](#agt-05), [06](#agt-06), [07](#agt-07), [08](#agt-08), [09](#agt-09), [10](#agt-10), [11](#agt-11), [12](#agt-12), [13](#agt-13) |

## Task briefs

<a id="agt-01"></a>
### AGT-01 — Workspace and logical contracts

**Status:** planned. **Milestone:** October start.

**Dependencies:** None. **Design:** [owning boundary](RUNTIME.md#logical-interfaces). **Teaching:** [AT-00](CURRICULUM.md#at-00).

**Ownership:** Build contracts and fixture semantics; supplied example service, dashboard, loaders and launch plumbing.

**Planned change boundary:** `contracts/core.py`, `fixtures/workspace/`, `tests/test_contracts.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Version one engineering workspace spanning docs, source, issue/dashboard state and operational records. Keep independent verifier inputs outside the agent-accessible environment; label synthetic measurements.
- [ ] Define CPU-importable task/evidence/model/tool/environment/run contracts with field documentation, pre/postconditions and explicit unfinished boundaries. Specify reset/snapshot isolation and capability checks.
- [ ] Record separate application/training environment pins and a local setup path that needs no GPU, Kubernetes or inference package. Reuse the starter artifact convention rather than duplicating it.

**Independent acceptance:**

- [ ] Two resets reproduce the same fixture state without leaking writes across runs; a private expected answer cannot appear in the agent observation.
- [ ] Contract fixtures reject invalid identity/capability combinations and distinguish unknown tool outcome from failure. Record actual setup commands only after implementation.

**Completion evidence:** pending; use the common record above.

### AGT-01 startup sequence

Use [the handoff procedure](../../docs/HANDOFF.md) and [first workspace slice](RUNTIME.md#first-workspace-slice). These substeps refine the existing task and retain its ownership; supplied fixture-service code is not learner-authored agent logic.

1. **Explain and adopt a seed:** trace documentation → SQL/source evidence → diagnosis → independent verification. Use the proposed unit-conversion fixture or record a bounded alternative under OQ-08. Separate an observed metric from the claim it supports.
2. **Version and isolate:** create fixture manifests and two resettable namespaces. Put gold labels and verifier implementation outside agent-visible files; specify a public task projection. Record source rights and synthetic-data labels.
3. **Materialize contracts:** implement only the first task/evidence/model/tool/environment/run records and their validation. Define completed/failed/unknown tool outcomes without pretending a checkpoint controls external effects. Keep model transport fake/deterministic for these contract checks.
4. **Reproduce CPU setup:** add the minimal agent package/test configuration; prove imports and resets work independently of inferstack, CUDA, Kubernetes and training libraries. Document exact commands and the expected reset/projection checks.

**Teach-back:** compute the seed's 300-versus-30 ms discrepancy, identify the evidence needed to explain it, and show which private fields never enter model context. **Next ready work:** AGT-02; AGT-03's core setup may begin as already specified. The full 30-question/15-task pilot belongs to the later owning tasks.

<a id="app-01"></a>
<a id="agt-02"></a>
### AGT-02 — Versioned RAG baseline

**Status:** planned. **Milestone:** December RAG gate. **Retained IDs:** APP-01.

**Dependencies:** [AGT-01](#agt-01). **Design:** [owning boundary](RUNTIME.md#knowledge-pipeline). **Teaching:** [AT-01](CURRICULUM.md#at-01), [AT-04](CURRICULUM.md#at-04).

**Ownership:** Modify supplied ingestion/store/embedding/reranker plumbing; Build retrieval/prompt experiments.

**Planned change boundary:** `knowledge/pipeline.py`, `tests/test_retrieval.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Retain Qdrant, fixed corpus/chunk/model revisions, BM25+dense, RRF, reranker off/on and learner chunk/prompt-layout changes; explain pgvector as the comparison.
- [ ] Start the 30 human-checked RAG questions with at least one-third held out; version evidence labels. Define evaluation before tuning and record stage timings/exact prompt identity.
- [ ] Handle changed/deleted documents, missing evidence, access filtering, citations and abstention. Produce initial December ablations; complete the broader original pilot in AGT-04.

**Independent acceptance:**

- [ ] A clean index build reproduces evidence identity; re-ingestion does not duplicate live chunks and deletion invalidates stale references.
- [ ] Report dense/hybrid and reranker results, one retrieval failure and one generation failure. Human checks and real endpoint behavior remain distinguishable from fixtures.

**Completion evidence:** pending; use the common record above.

<a id="app-02"></a>
<a id="ag-1a"></a>
<a id="agt-03"></a>
### AGT-03 — MCP tools and learner-authored harness

**Status:** planned. **Milestone:** December as progress allows; engineering gate. **Retained IDs:** APP-02, AG-1a.

**Dependencies:** [AGT-01](#agt-01), [AGT-02](#agt-02). **Design:** [owning boundary](RUNTIME.md#harness-and-tool-lifecycle). **Teaching:** [AT-02](CURRICULUM.md#at-02).

**Ownership:** Operate/Modify supplied thin baseline, then Build the loop; client/MCP/runner plumbing supplied.

**Planned change boundary:** `runtime/harness.py`, `tools/mcp.py`, `tests/test_harness.py`, `tests/test_tools.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Operate docs_search, read-only benchmark SQL and constrained execution; add step/token/time limits, structured-output/schema versus semantic checks, result caching and timeout/error behavior.
- [ ] Preserve AG-1a: write decision/action/observation control over supplied interfaces, with linked tool calls and explicit terminal reasons; do not replace the authored loop with only a framework invocation.
- [ ] Run the inference-analysis exercise over docs and benchmark records without provisioning or deployment tools. Add programmatic composition and independent-call concurrency with shared budgets.
- [ ] Use deterministic fixtures for logic, then run the authored loop on an actual open model endpoint. Record capability failures honestly.

**Independent acceptance:**

- [ ] Normal, recoverable-error and exhausted-budget trajectories preserve action/result linkage; unknown tools, malformed arguments, duplicate IDs and network denial are covered.
- [ ] Read-only SQL and sandbox permissions are enforced outside prompt text; a timeout can remain unknown. No unbounded retries or unsafe parallel dependencies.

**Completion evidence:** pending; use the common record above.

<a id="app-03"></a>
<a id="app-04"></a>
<a id="ag-1c"></a>
<a id="agt-04"></a>
### AGT-04 — Evaluation, trajectories and original pilot completion

**Status:** planned. **Milestone:** January quality target; evaluation begins in AGT-02. **Retained IDs:** APP-03, APP-04, AG-1c.

**Dependencies:** [AGT-02](#agt-02), [AGT-03](#agt-03). **Design:** [owning boundary](LEARNING.md#evaluation-architecture). **Teaching:** [AT-04](CURRICULUM.md#at-04).

**Ownership:** Build verifier/trace semantics; supplied collector and fixture shell.

**Planned change boundary:** `evaluation/runner.py`, `evaluation/verifiers.py`, `runtime/trajectory.py`, `tests/test_evaluation.py`, `tests/test_trajectory.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Preserve APP-03: version session/request/parent IDs, exact prompts or reconstructible token identities, tool/think gaps, all revisions, outcomes and live/replay mode; retain roughly 50 varied sessions with explicit reset/reuse.
- [ ] Complete the 30-question/15-task pilot, at least one-third held out, retrieval/answer ablations, live quality/tool checks and uncertainty. Grow toward 100/30 only when human review fits.
- [ ] Preserve AG-1c: label correct output, wrong aggregate and unsupported performance claim; demonstrate weak-verifier false acceptance, improve an independent check and document a remaining limitation.
- [ ] Separate runtime transcripts, training trajectories and performance export. Version the SessionTrace export without requiring BEN-04 to exist; calibrate any supplementary fixed model judge.

**Independent acceptance:**

- [ ] Dependency reconstruction and template/prompt changes are detectable; old fixtures remain readable with additive compaction metadata. Repeated load is not reported as diversity.
- [ ] Private verifier checks disagree with at least one plausible wrong output; report observed false-positive/negative causes and retrieval/tool/session failures.
- [ ] Live branching is evaluated as live behavior; transcript replay and AG teaching fixtures cannot substitute for full pilot completion.

**Completion evidence:** pending; use the common record above.

<a id="ag-1b"></a>
<a id="agt-05"></a>
### AGT-05 — Context compaction, memory and skills

**Status:** planned. **Milestone:** Engineering gate. **Retained IDs:** AG-1b.

**Dependencies:** [AGT-03](#agt-03), [AGT-04](#agt-04). **Design:** [owning boundary](RUNTIME.md#context-memory-and-skills). **Teaching:** [AT-03](CURRICULUM.md#at-03).

**Ownership:** Build context/memory policy; supplied deterministic summary and storage adapters.

**Planned change boundary:** `runtime/context.py`, `runtime/memory.py`, `runtime/skills.py`, `tests/test_context_memory.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Preserve AG-1b: compact older complete interactions, retain task/constraints and recent complete action/result pairs, and keep the unchanged full trajectory.
- [ ] Record compaction events, active token counts, tokenizer/template revisions and before/after prompt/prefix identity; validate deterministic fixtures before one bounded live comparison.
- [ ] Add episodic/factual/procedural memory with provenance, conflict correction, namespace isolation and retirement/deletion; compare memory off/on and over-retrieval failures.
- [ ] Implement skill discovery/progressive disclosure plus authored and induced skill admission/test/repair; generated code receives normal execution permissions.

**Independent acceptance:**

- [ ] A delayed-dependency continuation catches lost constraints/broken tool pairs. Explain token-volume, prefix-reuse and task-quality tradeoffs without an assumed speedup.
- [ ] Stale/conflicting/unauthorized memory is detected; a failed skill is rejected or retired and does not leak across workspaces.

**Completion evidence:** pending; use the common record above.

<a id="agt-06"></a>
### AGT-06 — Durable agent service and observability

**Status:** planned. **Milestone:** January–February target.

**Dependencies:** [AGT-03](#agt-03), [AGT-04](#agt-04), [AGT-05](#agt-05). **Design:** [owning boundary](RUNTIME.md#durable-service-interaction-and-observability). **Teaching:** [AT-07](CURRICULUM.md#at-07), [AT-08](CURRICULUM.md#at-08), [AT-09](CURRICULUM.md#at-09).

**Ownership:** Build recovery/permission policies; Modify/Operate LangGraph; supplied UI, DB and telemetry adapters.

**Planned change boundary:** `integrations/langgraph.py`, `runtime/recovery.py`, `tools/permissions.py`, `service/api.py`, `tests/test_recovery.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Integrate the existing primitives with LangGraph persistence; use one authoritative run state and persistent tool-attempt records. Resolve the local backend in OQ-15 (SQLite is proposed); PostgreSQL is an alternative if needed, not a second mandatory deployment.
- [ ] Expose CLI and minimal API/UI for progress, clarification/approval, cancellation/resumption and artifacts. Bind approval to the actual action/target/arguments.
- [ ] Add OpenTelemetry/Phoenix spans, latency/cost origin, redaction and failure diagnosis. Keep credentials separate from generated code and teach remote MCP auth boundaries.
- [ ] Run injection and permission tests; document the supplied sandbox's limits and cleanup behavior.

**Independent acceptance:**

- [ ] Crash after side effect/before checkpoint does not cause blind duplicate execution; reconcile or expose unknown outcome.
- [ ] Cancel, stale approval, resumed budgets, disconnected streaming and secret-redaction cases behave according to documented contracts.
- [ ] Trace one failed task through retrieval/model/tool/evaluator stages; do not confuse transport interruption with intentional task cancellation.

**Completion evidence:** pending; use the common record above.

<a id="agt-07"></a>
### AGT-07 — Planning and deep research

**Status:** planned. **Milestone:** Spring capabilities.

**Dependencies:** [AGT-04](#agt-04), [AGT-05](#agt-05), [AGT-06](#agt-06). **Design:** [owning boundary](RUNTIME.md#domain-capabilities-and-alternatives). **Teaching:** [AT-05](CURRICULUM.md#at-05).

**Ownership:** Build planning/retrieval policy; supplied search/corpus connectors.

**Planned change boundary:** `runtime/planning.py`, `tests/test_research.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Represent task dependencies and separate planning from execution; replan after failure or changed evidence while retaining budgets and provenance.
- [ ] Add iterative search, query refinement, source assessment, conflicting-evidence synthesis and citation verification; use versioned corpora for reproducible comparisons.
- [ ] Compare reactive versus planned/research behavior under declared call/time/token budgets, including a task where planning adds cost without benefit.

**Independent acceptance:**

- [ ] A task with an invalidated premise triggers replanning rather than an unsupported conclusion.
- [ ] Independent evidence checks detect fabricated citations and unsupported comparisons; report accuracy, stopping behavior and total cost.

**Completion evidence:** pending; use the common record above.

<a id="agt-08"></a>
### AGT-08 — Coding, computer use and OpenHands

**Status:** planned. **Milestone:** Spring capabilities.

**Dependencies:** [AGT-04](#agt-04), [AGT-05](#agt-05), [AGT-06](#agt-06). **Design:** [owning boundary](RUNTIME.md#domain-capabilities-and-alternatives). **Teaching:** [AT-06](CURRICULUM.md#at-06), [AT-07](CURRICULUM.md#at-07).

**Ownership:** Build task/verifier logic; Modify/Operate OpenHands; supplied worktrees/browser environment.

**Planned change boundary:** `tools/workspace.py`, `tools/browser.py`, `integrations/openhands.py`, `tests/test_domain_tasks.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Implement localize–edit–verify on a resettable workspace; preserve trusted tests and add independent checks for regressions and weakened-test shortcuts.
- [ ] Add DOM/accessibility and screenshot-based observations/actions on the local dashboard; assess static grounding separately from final environment success.
- [ ] Operate OpenHands on the same tasks, trace source/tool dispatch, and substantively modify one tool or skill; compare behavior with the authored harness.
- [ ] Include executable bug/task construction, non-functional checks, test-generation/CI-repair examples and data exercises for coding/GUI training.

**Independent acceptance:**

- [ ] A patch satisfies hidden behavior checks and preserves existing behavior; modifying tests alone cannot pass.
- [ ] A browser task is checked using application state outside the agent. Failed reset/grounding and plausible-but-wrong screenshots remain failures.
- [ ] Record a real OpenHands run and the modification/regression evidence; no full framework reimplementation.

**Completion evidence:** pending; use the common record above.

<a id="agt-09"></a>
### AGT-09 — Human and multi-agent interaction

**Status:** planned. **Milestone:** Spring capabilities.

**Dependencies:** [AGT-06](#agt-06), [AGT-07](#agt-07), [AGT-08](#agt-08). **Design:** [owning boundary](RUNTIME.md#domain-capabilities-and-alternatives). **Teaching:** [AT-09](CURRICULUM.md#at-09).

**Ownership:** Build bounded delegation and interaction policy; supplied A2A/transport/UI shells.

**Planned change boundary:** `runtime/delegation.py`, `integrations/a2a.py`, `tests/test_interaction.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Implement clarification, approval/correction and understandable progress; test stale user decisions and cancellation during delegated work.
- [ ] Create a bounded collaborative workflow and A2A handoff, with dependency-aware communication, shared aggregate budgets and isolated agent state.
- [ ] Compare with a single agent at declared aggregate cost; analyze communication failure, disagreement and a task where collaboration is unnecessary.
- [ ] Write a future-of-work task analysis measuring supervision/review effort and failure costs, not just automated output volume.

**Independent acceptance:**

- [ ] No subagent silently exceeds the parent's permissions or spend limit; failed handoffs and conflicting results are surfaced.
- [ ] Independent task verification remains authoritative despite agent consensus; report human intervention and total resource cost.

**Completion evidence:** pending; use the common record above.

<a id="agt-10"></a>
### AGT-10 — Critics, search and prompt optimization

**Status:** planned. **Milestone:** Spring experiments.

**Dependencies:** [AGT-04](#agt-04), [AGT-07](#agt-07), [AGT-08](#agt-08). **Design:** [owning boundary](LEARNING.md#prompt-critic-and-search-improvement). **Teaching:** [AT-10](CURRICULUM.md#at-10).

**Ownership:** Build critic/search reasoning and independent checks; Modify/Operate DSPy.

**Planned change boundary:** `runtime/search.py`, `learning/optimization.py`, `evaluation/critics.py`, `tests/test_search.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Implement candidate ranking and bounded tree search with snapshots/rollback; compare beam/best-first/MCTS mechanisms and best-of-N against reactive execution.
- [ ] Distinguish evidence rerankers, answer/trajectory critics, process rewards and RL value; calibrate critic decisions and demonstrate a selection failure.
- [ ] Run one DSPy optimization using training/development data and a fixed call/cost allowance; retain sealed test cases.

**Independent acceptance:**

- [ ] Search branches do not repeat irreversible actions or corrupt shared state; limits and failed candidates count toward cost.
- [ ] Compare success and selection bias under declared budgets; do not call a different toolset/model an isolated search improvement.

**Completion evidence:** pending; use the common record above.

<a id="agt-11"></a>
### AGT-11 — Training data, retrieval adaptation and SFT

**Status:** planned. **Milestone:** January–February target.

**Dependencies:** [AGT-04](#agt-04), [AGT-05](#agt-05). **Design:** [owning boundary](LEARNING.md#training-data-and-sft). **Teaching:** [AT-11](CURRICULUM.md#at-11).

**Ownership:** Build data/masks/evaluation; Modify/Operate supplied Transformers/PEFT/TRL infrastructure.

**Planned change boundary:** `learning/data.py`, `learning/sft.py`, `learning/retriever.py`, `tests/test_training_data.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Freeze task-family splits, curate and audit teacher/self trajectories, failures and filtering decisions; preserve source/provenance and prevent evaluation leakage.
- [ ] Fine-tune a small bi-encoder on audited positive/hard-negative evidence pairs and compare to its frozen baseline.
- [ ] Verify exact chat templates, assistant/tool masks, end markers, padding and packing boundaries with independent examples; overfit a tiny diagnostic set.
- [ ] Run real small-model LoRA SFT, save checkpoints and evaluate in the target harness including recovery and regressions. Teach code/GUI/long-context data construction, exposure bias and distillation.

**Independent acceptance:**

- [ ] An observation-inclusive or shifted mask fails the oracle; held-out task labels cannot enter training.
- [ ] Checkpoint, dataset/configuration hashes, learning curves and independently verified harness outcomes are recorded; lower training loss alone does not close the task. Use development cases for iterative selection; final sealed held-out comparison is required in AGT-14.

**Completion evidence:** pending; use the common record above.

<a id="agt-12"></a>
### AGT-12 — Multi-turn agentic RL

**Status:** planned. **Milestone:** Required spring training gate.

**Dependencies:** [AGT-04](#agt-04), [AGT-11](#agt-11). **Design:** [owning boundary](LEARNING.md#rl-objectives-and-practical-training). **Teaching:** [AT-12](CURRICULUM.md#at-12), [AT-13](CURRICULUM.md#at-13).

**Ownership:** Build objective/reward reasoning; Modify/Operate maintained trainer and isolated environments.

**Planned change boundary:** `learning/objectives.py`, `learning/rl.py`, `learning/rewards.py`, `tests/test_objectives_rewards.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Implement exact small REINFORCE, baseline/advantage, GAE, PPO and GRPO checks; compare DrGRPO, DAPO, GSPO, CISPO and course importance-weighting approaches through numerical/source exercises.
- [ ] Run real multi-turn tool-using training, initially in TRL; group equivalent task starts with distinct sampling, preserve context/policy identity, and save a trained checkpoint.
- [ ] Demonstrate verifier false negatives/positives and reward hacking; compare trusted outcome reward with auxiliary/process reward behavior.
- [ ] Study expert iteration, exploration collapse, curricula, reference KL/entropy and off/on-policy distillation; compare held-out base/SFT/RL behavior with fixed harness.

**Independent acceptance:**

- [ ] Independent gradient/mask tests cover negative advantage, clipping and zero-variance groups; tool observations never become policy targets.
- [ ] Training includes actions conditioned on intervening tool results; a single-turn formatting reward cannot close this task.
- [ ] Report reward versus independent task success, environment failures/truncation, cost, checkpoint and actual GPU evidence; a negative result is acceptable. Development feedback may guide iteration; the final held-out comparison follows the frozen AGT-14 protocol.

**Completion evidence:** pending; use the common record above.

<a id="agt-13"></a>
### AGT-13 — RL systems and production rollout investigation

**Status:** planned. **Milestone:** Required spring systems gate.

**Dependencies:** [AGT-12](#agt-12). **Design:** [owning boundary](LEARNING.md#rl-systems). **Teaching:** [AT-14](CURRICULUM.md#at-14).

**Ownership:** Modify supplied training loop; Operate verl/SGLang; Explain memory/parallelism and alternatives.

**Planned change boundary:** `integrations/verl.py`, `learning/rollouts.py`, `tests/test_rollout_identity.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Preserve B2: tiny autograd/training-loop modification, optimizer-memory accounting, DP/FSDP/ZeRO, SFT/RLHF/GRPO, distillation and verl/Miles/slime weight-version investigation.
- [ ] Operate a bounded verl/SGLang multi-turn run after a compatibility smoke; investigate learner/rollout placement, publication/synchronization, stragglers and utilization.
- [ ] Compare synchronous version-pinned dataflow with supported asynchronous/stale-policy mechanisms; distinguish async tool calls from async learning.
- [ ] Perform checkpoint/recovery and train-inference log-probability/template checks. Plan a short two-GPU exercise when supported, logging shared rental allocation once.

**Independent acceptance:**

- [ ] Trace one trajectory from task through policy version, reward, batch, update and next rollout; stale/mismatched identity is detected.
- [ ] Record a real operated RL run and bottleneck evidence. An unavailable backend leaves the operation pending rather than upgrading a source reading to a deployment.

**Completion evidence:** pending; use the common record above.

<a id="agt-14"></a>
### AGT-14 — Agent research capstone and reproduction

**Status:** planned. **Milestone:** Before May graduation.

**Dependencies:** [AGT-01](#agt-01), [AGT-02](#agt-02), [AGT-03](#agt-03), [AGT-04](#agt-04), [AGT-05](#agt-05), [AGT-06](#agt-06), [AGT-07](#agt-07), [AGT-08](#agt-08), [AGT-09](#agt-09), [AGT-10](#agt-10), [AGT-11](#agt-11), [AGT-12](#agt-12), [AGT-13](#agt-13). **Design:** [owning boundary](LEARNING.md#independent-agent-capstone). **Teaching:** [AT-15](CURRICULUM.md#at-15).

**Ownership:** Build controlled study and report; Explain/defend; supplied collection/plot/poster shells.

**Planned change boundary:** `experiments/capstone/`, `tests/test_reproduction.py` relative to the agent package or its tests/fixtures/experiments as shown in the [code map](../../docs/system/code-map.md#agent-track).

**Work:**

- [ ] Deliver CMU-equivalent proposal and progress review; preregister the diagnosis study, model/harness/task revisions, primary metric, budgets and independent quality constraints.
- [ ] Compare base, prompt-optimized, SFT and SFT-plus-RL; apply fixed RAG only to answer-only tasks. Keep memory/search/multi-agent comparisons separate.
- [ ] Complete both guest-topic exercises when materials publish, poster/demo, final report and technical defense; perform a clean reproduction and retain raw failed attempts.
- [ ] Record any unfinished requirement explicitly; the optional inference trace/report connection is not a joint-capstone gate.

**Independent acceptance:**

- [ ] Another implementer can reproduce the selected bounded experiment from pinned inputs and commands, including failures, cost and uncertainty.
- [ ] Every required course/task evidence row is accounted for; simulated/operated and supplied/learner-authored claims remain separate.

**Completion evidence:** pending; use the common record above.

## Gate interpretation

RAG acceptance requires reproducible indexing/revisions, dense/hybrid and reranker ablations, evidence/abstention, initial human checks/held-out cases, stage cost/latency and explained retrieval/generation failures. AGT-04 closes the full original pilot and live-agent quality continuation; it does not depend on BEN-04.

Engineering acceptance adds malformed calls, limits, cancellation/duplicates, unknown side effects/recovery, context preservation, memory isolation, independent patch/browser checks and adversarial permission tests. Learning acceptance requires real SFT and multi-turn RL checkpoints plus held-out outcomes, masks/reward oracles and rollout/model/template provenance. The capstone cannot mark all training complete based on illustrative examples.
