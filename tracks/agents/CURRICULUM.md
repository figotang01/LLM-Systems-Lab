# Agent teaching curriculum

[Overview](README.md) · [Task roadmap](ROADMAP.md) · [Full coverage](COVERAGE.md) · [Shared teaching contract](../../teaching/CONTRACT.md)

Status: sixteen grouped **blueprints delivered**; their HTML, executable exercises, reference solutions and implementations remain planned. Only the existing umbrella orientation is delivered HTML. All published CMU topics and integrated assignment outcomes are required; unknown future material is tracked explicitly.

## Delivery contract

Apply the shared contract: 25–40 slides per full technical session with expandable notes; split longer units into A/B sessions rather than compressing away mechanisms. A 45–75 minute teaching session, worked exercises and project lab are included in learner estimates. Provide prerequisites, a motivating failure, state/numerical traces, annotated code, two misconceptions, a broken fixture, independent oracle, bounded experiment and teach-back. HTML is offline/self-contained with reading/print modes and accessible navigation. Synthetic timings/plots must say illustrative; measured plots link to actual artifacts.

Course-specific additions: show complete actions/observations; separate retrieval/reasoning/execution/evaluation failures; demonstrate when extra memory/planning/agents/search/training fails to help; link every lab to the owning production task; preserve Build/Modify/Operate/Explain attribution. Reconstruct a small mechanism without assistance and apply the existing 8/10, no-zero-in-correctness rubric plus one-week/one-month retrieval checks.

Concept prerequisites below order study, not entire implementation completion. In particular, RL theory can be learned in December before the spring training pipeline exists. Exact code/source revisions and commands are selected and smoke-tested when each lesson is authored. Primary readings live in the [reference catalog](../../docs/references/README.md#agent-track-research).

## Unit index

| Unit | Scope | Implementation connection |
|---|---|---|
| [AT-00](#at-00) | Agent foundations and engineering workspace | [AGT-01](ROADMAP.md#agt-01) |
| [AT-01](#at-01) | RAG, retrieval and evidence | [AGT-02](ROADMAP.md#agt-02), [AGT-04](ROADMAP.md#agt-04), [AGT-11](ROADMAP.md#agt-11) |
| [AT-02](#at-02) | Tools, protocols and the authored harness | [AGT-03](ROADMAP.md#agt-03) |
| [AT-03](#at-03) | Long context, memory and skills | [AGT-05](ROADMAP.md#agt-05) |
| [AT-04](#at-04) | Evaluation, datasets and evaluator failures | [AGT-02](ROADMAP.md#agt-02), [AGT-04](ROADMAP.md#agt-04) |
| [AT-05](#at-05) | Planning, decomposition and deep research | [AGT-07](ROADMAP.md#agt-07) |
| [AT-06](#at-06) | Coding and computer-use agents | [AGT-08](ROADMAP.md#agt-08) |
| [AT-07](#at-07) | LangGraph and OpenHands | [AGT-06](ROADMAP.md#agt-06), [AGT-08](ROADMAP.md#agt-08) |
| [AT-08](#at-08) | Safety, durable services and observability | [AGT-03](ROADMAP.md#agt-03), [AGT-06](ROADMAP.md#agt-06) |
| [AT-09](#at-09) | Human/multi-agent interaction and future of work | [AGT-09](ROADMAP.md#agt-09) |
| [AT-10](#at-10) | Critics, reranking, tree search and optimization | [AGT-10](ROADMAP.md#agt-10) |
| [AT-11](#at-11) | Data, SFT, PEFT and distillation | [AGT-11](ROADMAP.md#agt-11) |
| [AT-12](#at-12) | RL foundations for agents | [AGT-12](ROADMAP.md#agt-12) |
| [AT-13](#at-13) | Advanced agentic RL | [AGT-12](ROADMAP.md#agt-12) |
| [AT-14](#at-14) | RL systems | [AGT-13](ROADMAP.md#agt-13) |
| [AT-15](#at-15) | Guest topics, research project and defense | [AGT-14](ROADMAP.md#agt-14) |

## Unit blueprints

<a id="at-00"></a>
### AT-00 — Agent foundations and engineering workspace

**Prerequisite concepts:** Python/PyTorch and transformer familiarity; no completed inference engine. **Course mapping:** CMU 1a; project foundation.

**Objectives:** Distinguish model, harness, environment, workflow and agent; trace one task to an independently verified outcome.

**Storyboard:** User task → observations/actions → harness boundaries → workspace and verifier separation → versioned artifacts.

**Worked example / independent oracle:** Trace an investigation with docs_search then SQL: list each observed fact, action and expected artifact; identify which private expected result must never enter context.

**Failure fixtures:** A plausible final answer without a valid query; grading truth accidentally mounted in the agent workspace.

**Lab / exit evidence:** Build a task/environment contract over supplied fixtures; reconstruct one loop and defend its stop conditions. Use the [first workspace slice](RUNTIME.md#first-workspace-slice) for a concrete independent diagnosis oracle and verifier-isolation exercise.

**Task handoff:** [AGT-01](ROADMAP.md#agt-01). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="module-14"></a>
<a id="at-01"></a>
### AT-01 — RAG, retrieval and evidence

**Prerequisite concepts:** [AT-00](#at-00). **Course mapping:** Existing module 14; CMU deep-research retrieval.

**Objectives:** Explain retrieval versus generation failure; compute ranking metrics; design evidence-backed answers and controlled retrieval adaptation.

**Storyboard:** Corpus/chunk identity → dense/BM25 retrieval → RRF/reranking → prompt construction → stage timing → held-out evidence checks.

**Worked example / independent oracle:** Two candidates have rank pairs (1,3) and (2,1); compute RRF with k=60 by hand. With two relevant documents and one in the top three, recall@3=1/2. Keep MRR distinct.

**Failure fixtures:** Stale chunk after document deletion; a supported-looking answer that cites an irrelevant source; permission filtering only after exposure.

**Lab / exit evidence:** Modify chunk/RRF/prompt policies over supplied ingestion/Qdrant/embedding/reranker/service code; compare dense/hybrid and reranker off/on. Explain pgvector and inspect positive/hard-negative retrieval training data.

**Task handoff:** [AGT-02](ROADMAP.md#agt-02), [AGT-04](ROADMAP.md#agt-04), [AGT-11](ROADMAP.md#agt-11). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

**Preserved module 14 allocation/storyboard:** 8 original December hours, with remaining package C evaluation in January. Slides 1–10: corpus versions/chunks/evidence labels; 11–22: embeddings/BM25, RRF, vector-store choice, reranker and prompt identity; 23–34: recall/MRR, citation support, held-out evaluation, stage timing and judge calibration. New depth is additive and counted in the expanded ledger.

<a id="module-15"></a>
<a id="at-02"></a>
### AT-02 — Tools, protocols and the authored harness

**Prerequisite concepts:** [AT-00](#at-00), [AT-01](#at-01). **Course mapping:** CMU 1b; module 15 application portion; AG-1a.

**Objectives:** Build bounded action/observation control; distinguish schema from semantic correctness; explain tool/protocol and credential boundaries.

**Storyboard:** Thin loop → JSON/schema/parsing failures → budgets → REST/OpenAPI/MCP → linked tool observations → programmatic composition → independent concurrency → termination.

**Worked example / independent oracle:** Hand-trace two independent 100/200 ms fixture calls (serial 300 ms versus ideal concurrent 200 ms, excluding overhead), then introduce a dependency that forbids parallel dispatch. These are illustrative times.

**Failure fixtures:** Unknown tool; malformed arguments; duplicate result ID; SQL write attempt; timeout after a side effect; a retry that exceeds budget.

**Lab / exit evidence:** Operate the supplied baseline and write AG-1a's loop over the same client/tools. Produce normal, recoverable-error and exhausted-budget trajectories plus an actual open-model run.

**Task handoff:** [AGT-03](ROADMAP.md#agt-03). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

**Preserved module 15 allocation/storyboard:** 12 original December hours plus the separate AG eight hours; original January evaluation remains required. Slides 1–10: thin loop, budgets, JSON/schema constraints, parsers/tool failures; 11–22: MCP SDK, docs/SQL/execution tools, state versus protocol request semantics and trace spans. Slides 23–38's replay teaching is now owned by [module 15 replay section](../inference/curriculum/foundations.md#module-15-replay); live checks/tool-result caching remain here and in AT-04. Use the checked MCP spec, AIPerf, XPerf and AgentSysBench references. Latest approval makes implementation timing flexible; it does not erase these hours or exercises.

<a id="at-03"></a>
### AT-03 — Long context, memory and skills

**Prerequisite concepts:** [AT-02](#at-02). **Course mapping:** CMU 2a/2b; AG-1b.

**Objectives:** Distinguish working context, factual/episodic/procedural memory and KV; preserve constraints during compaction; evaluate skill lifecycle.

**Storyboard:** History growth → effective context → linked model/serving foundations → compaction as state estimation → continuation checks → memory conflict/update → skill admission/use/repair.

**Worked example / independent oracle:** Plant an early constraint and a delayed tool dependency, compact older complete interactions, then continue the task. Compare exact before/after prompt IDs and tokenizer-counted tokens; calculate repeated-history token growth.

**Failure fixtures:** Broken action/result pair; summary drift; stale or cross-namespace memory; over-retrieval; an induced skill accepted by an unreliable judge.

**Lab / exit evidence:** Build AG-1b's deterministic compactor checks followed by one bounded live comparison; implement memory/skill policy over supplied storage. Explain why fewer tokens may lose prefix reuse or quality.

**Task handoff:** [AGT-05](ROADMAP.md#agt-05). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

**Required cross-track concepts:** study [attention/context foundations](../inference/curriculum/advanced.md#long-context-foundations) and the linked numerical/cache/measurement lessons. This includes prefill/decode, effective versus advertised context, RoPE/NoPE, position interpolation/YaRN, sparse/linear/delta/latent attention, context parallelism and cache-aware layout/routing. Canonical mechanisms are taught once; this track requires understanding, not a second engine implementation.

<a id="at-04"></a>
### AT-04 — Evaluation, datasets and evaluator failures

**Prerequisite concepts:** [AT-01](#at-01), [AT-02](#at-02). **Course mapping:** CMU Assignment 2; AG-1c; original January evaluation.

**Objectives:** Design independent task verifiers; protect splits; distinguish model, retrieval, tool, environment and evaluator failures; report useful uncertainty.

**Storyboard:** Versioned tasks → family-grouped splits → trusted outcomes → trajectory evidence → weak-verifier attack → calibrated judges → statistical comparison.

**Worked example / independent oracle:** Label a correct aggregate, an incorrect aggregate and an unsupported speed claim from known records. Build a confusion table; show why one false acceptance changes the conclusion. Group repeated sessions under their task.

**Failure fixtures:** Public tests pass while behavior is wrong; judge verbosity/order bias; leaked test labels; repeated prompts counted as independent tasks; an existing file whose content is wrong.

**Lab / exit evidence:** Build AG-1c and the original 30-question/15-task pilot; preserve one-third held out and ~50 initial sessions. Adapt Assignment 2 validator/task-creation, execution/presentation failure and MCC/error-analysis methods.

**Task handoff:** [AGT-02](ROADMAP.md#agt-02), [AGT-04](ROADMAP.md#agt-04). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-05"></a>
### AT-05 — Planning, decomposition and deep research

**Prerequisite concepts:** [AT-02](#at-02), [AT-04](#at-04). **Course mapping:** CMU 3a/5b.

**Objectives:** Represent dependencies and replanning; distinguish reasoning from world-changing actions; synthesize claims with verified sources.

**Storyboard:** Reactive baseline → plan representations → planner/executor boundary → execution feedback → replan → iterative retrieval → source conflict → report verification.

**Worked example / independent oracle:** A diagnosis initially assumes version A, but SQL reveals version B. Update the dependency plan and evidence table; identify invalid conclusions and compare to a reactive run.

**Failure fixtures:** Rigid plan persists after its premise fails; citations support only part of a claim; stopping too early or endlessly searching.

**Lab / exit evidence:** Build bounded planning and research policies. Compare task success and total calls/time, including a case where planning offers no gain; inspect research retrieval/training and rubric-construction methods.

**Task handoff:** [AGT-07](ROADMAP.md#agt-07). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-06"></a>
### AT-06 — Coding and computer-use agents

**Prerequisite concepts:** [AT-02](#at-02), [AT-04](#at-04). **Course mapping:** CMU 3b/4a.

**Objectives:** Trace localize–edit–verify and GUI observe–act loops; distinguish static grounding from final outcome; construct resettable executable tasks.

**Storyboard:** Code model/pre-midtraining and infilling → behavior/pass@k evaluation → repository navigation/edit/test → task generation → DOM/accessibility/screenshots → grounded actions → end-state checks.

**Worked example / independent oracle:** Repair a seeded default-value bug where zero differs from missing/None; independent tests cover all cases. Then change a dashboard issue and verify its database state rather than the agent's description.

**Failure fixtures:** Agent edits grading tests; pass@k reported as first-attempt success; screenshot looks correct but persisted state is wrong; browser reset fails.

**Lab / exit evidence:** Modify supplied repository/browser adapters; deliver a verified patch and GUI task. Include test-generation/CI repair, non-functional constraints, code-world-model reasoning, and GUI demonstration/SFT/RL data exercises.

**Task handoff:** [AGT-08](ROADMAP.md#agt-08). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-07"></a>
### AT-07 — LangGraph and OpenHands

**Prerequisite concepts:** [AT-02](#at-02), [AT-03](#at-03), [AT-04](#at-04). **Course mapping:** CMU 7b/9a.

**Objectives:** Map own contracts into production frameworks; trace persistence/tool dispatch; explain what a framework does and does not guarantee.

**Storyboard:** Authored loop → reusable primitives → LangGraph nodes/checkpoints/interrupts → OpenHands tools/context/events → source modification → alternatives.

**Worked example / independent oracle:** Trace a run through a selected pinned source revision and crash immediately after a tool changes state. Identify what the checkpoint proves and what must be reconciled externally.

**Failure fixtures:** Two independent writable run states; context copied differently by framework adapters; checkpoint treated as exactly-once external execution.

**Lab / exit evidence:** Operate both named frameworks; modify one OpenHands tool/skill and the LangGraph integration. Compare DeepAgents, ADK and Microsoft Agent Framework APIs without building three extra products.

**Task handoff:** [AGT-06](ROADMAP.md#agt-06), [AGT-08](ROADMAP.md#agt-08). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-08"></a>
### AT-08 — Safety, durable services and observability

**Prerequisite concepts:** [AT-02](#at-02), [AT-04](#at-04). **Course mapping:** CMU 7a/9b.

**Objectives:** Enforce permissions independently of model text; scope credentials; diagnose a task through traces; recover safely from interruptions.

**Storyboard:** Threat/action boundaries → local/remote tool auth → sandbox policies → durable attempts → idempotency/unknown outcomes → telemetry/redaction → recovery.

**Worked example / independent oracle:** A tool completes but its reply is lost; enumerate what persisted and choose status lookup, idempotent reconciliation or explicit uncertainty. Bind approval to an immutable action description.

**Failure fixtures:** Retrieved prompt injection grants imaginary authority; secrets enter code sandbox/trace; cancelled run launches another action; stale approval authorizes changed parameters.

**Lab / exit evidence:** Modify supplied runner/UI/auth/telemetry adapters and author permission/recovery policy. Demonstrate failure diagnosis in Phoenix and enforce aggregate resource budgets.

**Task handoff:** [AGT-03](ROADMAP.md#agt-03), [AGT-06](ROADMAP.md#agt-06). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-09"></a>
### AT-09 — Human/multi-agent interaction and future of work

**Prerequisite concepts:** [AT-05](#at-05), [AT-07](#at-07), [AT-08](#at-08). **Course mapping:** CMU 10a/10b/12a.

**Objectives:** Design clarification/approval and bounded delegation; assess supervision costs; compare coordinated and single-agent approaches.

**Storyboard:** Task ambiguity → human clarification/correction → delegation/handoffs → protocols and budgets → disagreement/failure → measured workflow impact.

**Worked example / independent oracle:** Split investigation and verification between two roles with a single total budget; inject conflicting evidence and a delayed user correction. Account for review minutes as well as model calls.

**Failure fixtures:** Agent consensus mistaken for truth; duplicate delegated actions; approval replayed after task changes; communication overhead exceeds benefit.

**Lab / exit evidence:** Build a bounded A2A handoff and human-interaction path; compare a single-agent baseline and record automation suitability, intervention burden and limitations.

**Task handoff:** [AGT-09](ROADMAP.md#agt-09). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-10"></a>
### AT-10 — Critics, reranking, tree search and optimization

**Prerequisite concepts:** [AT-04](#at-04), [AT-05](#at-05), [AT-06](#at-06). **Course mapping:** CMU 12b/13a; industry optimization addition.

**Objectives:** Distinguish evidence rankers, answer critics, process rewards and values; reason about search selection bias and resource budgets.

**Storyboard:** Candidate generation → independent scoring → best-of-N → beam/best-first/MCTS state traces → branch rollback → DSPy optimization → held-out comparison.

**Worked example / independent oracle:** Use a hand-scored tree where the highest-looking intermediate node leads to failure. Show how greedy, beam and budgeted search select different terminal artifacts and count every expansion.

**Failure fixtures:** Critic rewards plausible wrong answer; irreversible action explored on two branches; test-set prompt optimization; reporting only successful attempts.

**Lab / exit evidence:** Build candidate/branch policy and modify supplied optimizer plumbing; run one measured DSPy experiment with a sealed test split.

**Task handoff:** [AGT-10](ROADMAP.md#agt-10). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-11"></a>
### AT-11 — Data, SFT, PEFT and distillation

**Prerequisite concepts:** [AT-03](#at-03), [AT-04](#at-04). **Course mapping:** CMU 4b; Assignment 3 objectives; expanded B2.

**Objectives:** Audit trajectory mixtures; compute masked next-token loss; explain packing/template drift and train-run mismatch; evaluate real adaptation.

**Storyboard:** Data source/teacher/filtering → typed trajectories → templates and masks → token/example weighting → packing → LoRA → harness evaluation → distillation and exposure bias.

**Worked example / independent oracle:** Render a tiny assistant/tool conversation; print each token's target/mask and independently align the shifted loss. Pack two examples and verify boundaries; deliberately train on tool observations to expose the error.

**Failure fixtures:** Teacher success contains a shortcut; source/template leakage across splits; padding/end markers mis-masked; training loss falls but tool success regresses.

**Lab / exit evidence:** Build mask/data tests, overfit a diagnostic set, run retrieval fine-tuning and real LoRA SFT, then evaluate the checkpoint. Explain code/GUI/long-context data construction and off/on-policy distillation.

**Task handoff:** [AGT-11](ROADMAP.md#agt-11). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-12"></a>
### AT-12 — RL foundations for agents

**Prerequisite concepts:** [AT-04](#at-04), [AT-11](#at-11). **Course mapping:** CMU 5a; B2 numerical prerequisite.

**Objectives:** Derive trajectory probability and policy gradients; reason about exposure bias, expert iteration, baselines and group-relative advantage.

**Storyboard:** Agent/environment trajectory → expected return → ReST/expert iteration → REINFORCE → reward-to-go → baselines/advantages → GRPO.

**Worked example / independent oracle:** For a two-action policy with p(A)=0.25 and reward(A)=1/reward(B)=0, expected return is 0.25 and its logit derivative is 0.1875. Enumerate gradients with/without an action-independent baseline.

**Failure fixtures:** Environment observations included in policy likelihood; baseline depends improperly on the selected action; all-equal rewards produce invalid normalization.

**Lab / exit evidence:** Build numerical/autograd oracles and a tiny supplied-loop modification. Explain why a good baseline reduces variance without solving all credit assignment.

**Task handoff:** [AGT-12](ROADMAP.md#agt-12). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-13"></a>
### AT-13 — Advanced agentic RL

**Prerequisite concepts:** [AT-12](#at-12). **Course mapping:** CMU 6a; required integrated Assignment 3 training.

**Objectives:** Compare credit assignment and stable updates; explain stale-policy ratios; detect verifier failure/reward hacking; run real multi-turn learning.

**Storyboard:** Value/GAE/process rewards → synchronous/asynchronous samples → importance ratios → PPO/GRPO variants → KL/entropy → curricula → distillation → independent outcomes.

**Worked example / independent oracle:** Rewards [0,1,1,0] have mean 0.5 and population SD 0.5, giving advantages [-1,1,1,-1]. Trace positive/negative-advantage PPO clipping; compare DrGRPO, DAPO, GSPO, CISPO and CTPO mechanisms.

**Failure fixtures:** Degenerate groups; collapsing exploration; overly stale data; constant-output patch exploits incomplete tests; auxiliary reward replaces task success.

**Lab / exit evidence:** Implement objective/reward fixtures and run actual multi-turn tool-conditioned model updates in TRL. Compare training reward with independently verified outcomes, including a negative outcome if observed. Iteration uses development cases; final held-out success is measured under the sealed AGT-14 protocol.

**Task handoff:** [AGT-12](ROADMAP.md#agt-12). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-14"></a>
### AT-14 — RL systems

**Prerequisite concepts:** [AT-12](#at-12), [AT-13](#at-13). **Course mapping:** CMU 6b; B2; required agent RL systems.

**Objectives:** Account for training/rollout memory; trace policy publication; distinguish async tool calls from async learning; diagnose mismatch and stragglers.

**Storyboard:** Tiny training bridge → DP/FSDP/ZeRO and placement → rollout/tools/reward/batch → learner update → weight synchronization → async/staleness → checkpoint/recovery.

**Worked example / independent oracle:** For one billion parameters, assume BF16 weights/grads (2+2 bytes), FP32 master weights (4) and two FP32 Adam moments (8): 16 GB before activations/other buffers. Change assumptions and compute shard effects; trace old versus current policy IDs.

**Failure fixtures:** Confusing parameter storage with peak memory; stale samples labeled on-policy; tokenizer/template mismatch; a cancelled rollout enters a completed batch.

**Lab / exit evidence:** Modify the B2 tiny loop, inspect verl/Miles/slime, operate a bounded verl/SGLang run, and diagnose a recorded recovery/versioning failure. Hardware-unavailable source work retains its honest evidence tier.

**Task handoff:** [AGT-13](ROADMAP.md#agt-13). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="at-15"></a>
### AT-15 — Guest topics, research project and defense

**Prerequisite concepts:** [AT-04](#at-04). **Course mapping:** CMU guest slots 13b/14a; project hours/presentations.

**Objectives:** Form an answerable agent research question; design controlled comparisons; communicate limitations and reproduce results.

**Storyboard:** Guest-topic updates → proposal → progress review → preregistration → experiment → uncertainty/failure analysis → poster/report/demo → defense.

**Worked example / independent oracle:** Explain why fixed RAG is a valid baseline for answer-only tasks but cannot perform a code-edit task. Design contrasts among base/prompt/SFT/RL without changing the harness simultaneously.

**Failure fixtures:** Confounded all-features switch; invented missing lecture topic; selective failures; statistically unsupported headline; supplied code described as independent work.

**Lab / exit evidence:** Complete both guest-topic exercises when published, proposal/check-in/poster/report, clean reproduction and oral walkthrough. Keep knowledge and implementation status separate.

**Task handoff:** [AGT-14](ROADMAP.md#agt-14). Author explanation before scaffolding/reference code; task briefs own implementation status and acceptance.

<a id="module-ag-1"></a>
## Preserved AG-1 supplement

The historical addition remains **AG-1a 2 + AG-1b 3 + AG-1c 3 = 8 hours**, separate from module 15's 12. These are retained exercises inside expanded units, not a claim that eight hours fund a full course. Original task IDs resolve in the [roadmap](ROADMAP.md); January evaluation remains a required continuation.

- **AG-1a / AT-02:** task/observations → model action → parsing → linked result → next decision → termination. Produce normal, recoverable-error and budget-exhaustion trajectories over supplied transport. Identify authored versus supplied code; malformed/unknown tools do not cause unlimited retries.
- **AG-1b / AT-03:** growing transcript → limit → select older complete interactions → working-memory summary → preserved constraints/recent pairs → next prompt. Keep the unchanged full trajectory; record before/after token/prefix identity, parent-linked compaction event and preservation checks. Start deterministic, then one bounded live comparison; actual latency/cache/quality claims need measurements.
- **AG-1c / AT-04:** outcome/trajectory → explicit checks → plausible wrong outputs → evaluator/agent failure distinction → improved independent check and residual limitation. Preserve correct/wrong-aggregate/unsupported-performance examples, fixture provenance, validator decisions and observed false-positive/negative analysis. Do not tune on held-out tasks or mistake a small fixture for a population benchmark.

The inference-analysis agent remains additional to the original workloads. No GPU provisioning/deployment tools are added to it. Attribution and applicable CMU reuse terms remain required; these integrated exercises do not claim completion of CMU's original applications.

<a id="module-b2"></a>
## Preserved B2 bridge — standalone inference learning credit

Approximately **four original J hours**, Modify/Explain: tiny autograd/training step, optimizer-state memory, DP/FSDP/ZeRO, SFT/RLHF/GRPO, verl/Miles/slime weight-version/rollout traces and distillation. Use 10–18 slides, an annotated code/profile, one modification/calculation and teach-back. Required evidence: optimizer-memory calculation, stale-weight/train-inference mismatch diagnosis, and modification of a supplied tiny loop.

This small bridge can be completed from supplied numerical/source fixtures independently of AGT-11–13, closing the original [REL-01](../inference/tasks/advanced-release.md#rel-01) requirement. The canonical owner has moved here; it is not a dependency on completing full agent training. Broader AT-11–14 teaching and real SFT/RL/verl operation remain additional required agent work. Reading or simulated traces do not close those operated gates. Optional CS336 A5 and drafter-training extensions remain discoverable separately.

## Teaching status ledger

Track each unit as blueprint / HTML authored / exercised / explained, and link separate task implementation/operation evidence. December aims at broad conceptual coverage; published guest-material availability is governed by [the update rule](COVERAGE.md#course-update-rule). Do not silently mark a postponed paid run as completed learning evidence.
