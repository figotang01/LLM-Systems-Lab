# Evaluation, model improvement and agent research

[Overview](README.md) · [Runtime](RUNTIME.md) · [Tasks](ROADMAP.md) · [Curriculum](CURRICULUM.md)

Status: required planned work. The full agentic RL implementation is a spring milestone. Studied numerical examples do not close a real training/operation gate.

## Requirements

| ID | Requirement | Owning task |
|---|---|---|
| <a id="al-1"></a>AL-1 | Versioned representative tasks, protected splits and independent verifiers | [AGT-02](ROADMAP.md#agt-02), [AGT-04](ROADMAP.md#agt-04) |
| <a id="al-2"></a>AL-2 | Controlled prompt/search/critic comparisons with evaluator calibration | [AGT-10](ROADMAP.md#agt-10) |
| <a id="al-3"></a>AL-3 | Audited trajectory data, retrieval adaptation and real masked SFT/LoRA | [AGT-11](ROADMAP.md#agt-11) |
| <a id="al-4"></a>AL-4 | Numerical objectives plus real multi-turn agentic RL with trusted rewards | [AGT-12](ROADMAP.md#agt-12) |
| <a id="al-5"></a>AL-5 | Operated RL system with policy versions, synchronization and recovery | [AGT-13](ROADMAP.md#agt-13) |
| <a id="al-6"></a>AL-6 | Independent agent capstone, proposal/check-in/poster/report and reproduction | [AGT-14](ROADMAP.md#agt-14) |

## Datasets and splits

Retain the original pilot: **30 hand-checked RAG questions, 15 deterministic agent tasks, at least one third held out**, and roughly 50 varied initial sessions. December closes a working RAG gate with initial human checks and ablations; complete the original live-agent/pilot evaluation at its January target or record an explicit revised date. The pilot is required, not a substitute for subsequent training/evaluation work. Expansion toward 100 RAG questions/30 agent tasks remains contingent on human review capacity, not an automatic quality claim.

Represent documentation, investigation, research, coding, computer-use and collaboration cases. Version the workspace snapshot, source rights/provenance, environment setup, task-family/template grouping, permitted actions and trusted verifier. Split related templates/near duplicates together **before** trajectory collection or synthetic augmentation. Maintain train/development/held-out partitions; optimize on development data, never the held-out labels.

Retrieval may access the declared corpus containing facts relevant to held-out questions; it must not retrieve hidden answers, grading code or evaluation labels. Training demonstrations and evaluator implementation remain outside the agent-accessible workspace. Preserve both passed and failed attempts and record selection/filtering reasons. Label synthetic records and model-generated labels; independently audit them rather than treating fluency as correctness.

Data growth is driven by failure coverage and human audit, not a fabricated statistically sufficient sample count. Before a training study, assess whether the held-out set supports its claim and uncertainty calculation. Additional generated examples are not independent task families.

Keep the original pilot report distinct from the final capstone test set. A pilot case whose outcomes have influenced design is development evidence for later studies, not a fresh test case. Intermediate SFT/RL debugging and checkpoint/prompt selection use development cases. Before the capstone, freeze all compared configurations and then evaluate the sealed test partition; do not use its scores to choose checkpoints. Earlier task gates can close on independently verified development runs, while final held-out comparison remains an explicit AGT-14 requirement.

## Evaluation architecture

Task loader → isolated environment reset → selected agent/model → raw trajectory/artifacts → independent verifier → diagnostics/aggregate report.

Use exact facts/SQL results, repository behavior tests, browser application state and evidence-reference checks where possible. A candidate's own test suite, final answer or self-score is not the truth source. Keep evaluator execution/credentials separate from agent-controlled code. Store task failure, infrastructure failure, timeout, cancellation and incomplete work; do not silently remove hard cases from denominators.

| Dimension | Measurements and controls |
|---|---|
| Retrieval | Recall@k/MRR, evidence labels, dense/hybrid and reranker ablations; stale/missing/unauthorized evidence |
| Answers/research | Correctness, citation support/coverage, unsupported claims, useful abstention, source conflict handling |
| Tools/agents | Schema/semantic/tool failures; task/session success; steps; recovery; permission violations |
| Coding/GUI | Hidden behavior and preserved tests, patch artifacts, independent end-state checks; failed environment setup remains visible |
| Operations | Stage and session latency, usage/cost with source, cancellations and partial outcomes |
| Evaluation quality | False positives/negatives, class confusion/MCC where suitable, human disagreement and calibration |

Hand checks calibrate any supplementary fixed LLM judge. Track judge model/prompt revisions; test order/verbosity sensitivity and compare with independent outcomes. Use confidence calibration and segment-level analysis where meaningful, without reading model self-confidence as calibrated probability. Statistical units are tasks/families or sessions/runs as appropriate, not correlated tokens or repeated prompts. Report effect sizes and uncertainty without demanding significance from a tiny pilot.

Preserve AG-1c: a correct result, wrong aggregate and unsupported latency/performance claim over known records; show a weak verifier accepting a plausible wrong result, improve an independent check, and document a residual limitation. Adapt CMU Assignment 2's validator/data-creation/error-analysis method, including execution and presentation failures, to project reports/artifacts. An optional model judge never replaces this exercise.

## Prompt, critic and search improvement

Run one DSPy optimization experiment with a frozen development budget and sealed test partition. Record prompts/programs, demonstration selection and optimizer calls/cost; gains must survive independent outcome checks. Compare prompt/model changes separately from tool or retrieval changes.

Distinguish retrieved-evidence rerankers, answer/trajectory critics, process reward models and RL value functions. Implement candidate ranking and a bounded search policy, inspect beam/best-first/MCTS alternatives, and compare to best-of-N/reactive baselines under declared token/time/call budgets. Use reversible environment snapshots for branches. Judge agreement, pass@k and first-attempt success answer different questions; specify the selection procedure and cost.

## Training data and SFT

The learner owns data selection, rendering, masking, objectives and evaluation. Supply loaders, model setup, launch/collection and reporting infrastructure. Use Transformers/PEFT/TRL in a separate training environment; Qwen 0.6B is the plumbing diagnostic and 1.7B the initial substantive target, contingent on measured fit and tool capability.

1. Collect/audit demonstrations and recoveries from training tasks; inspect teacher choice, distribution, successful-shortcut behavior, token-length mixtures and filtering bias.
2. Convert typed actions/observations into exact harness-compatible messages. Record model/tokenizer/template revisions and compare training versus serving renderings, including whitespace/end-of-turn semantics.
3. Build independent token/mask fixtures: padding and tool observations are excluded from policy targets; intended assistant spans and end markers are included. Inspect loss weighting, sequence packing and cross-example boundaries instead of relying on a trainer flag alone.
4. Overfit a tiny diagnostic set; distinguish a data/mask bug from lack of generalization. Run real LoRA SFT and save model/adapter identity, dataset hash, configuration, checkpoint and learning curves.
5. Evaluate in the actual target harness, including recovery from off-demonstration states and regressions outside the tuned subset. Use development tasks for iterative diagnosis and reserve the final held-out families for the frozen comparison above. A decreasing training loss is insufficient.

Require a bounded retrieval adaptation experiment: fine-tune a small bi-encoder with evidence-labeled positives and audited hard negatives, then compare against its frozen baseline. Keep the existing pretrained reranker toggle. Explain alternate reranker training without creating a second full training pipeline.

Teach distillation, teacher/student mismatch, expert iteration, DAgger/exposure bias, code-model pre/mid-training and GUI/long-context data construction. Numerical/data exercises cover expensive mechanisms; actual agent training uses the shared bounded environment. [Primary training references](../../docs/references/README.md#agent-track-research)

## RL objectives and practical training

Derive sequential trajectory probability and expected return before implementing losses. Build independently checked REINFORCE, reward-to-go, baselines/advantages, GAE, clipped PPO and GRPO examples. Explain where environment observations contribute context but not policy log-probability. Use small exact enumerations/finite differences, positive/negative advantages and equal-reward groups as oracles.

Advanced required numerical/source comparisons: DrGRPO normalization, DAPO sampling/objectives, GSPO sequence weighting, CISPO clipped weighting and the course's importance-weighting approaches (including CTPO in the September materials); value/critic versus group baselines; process/outcome rewards; KL/reference policy versus behavior policy; entropy, exploration collapse, curriculum and off/on-policy distillation. Cover RLHF/preference learning and contrast DPO with on-policy environment learning. Running every algorithm at research scale is not an implementation requirement.

The required GPU experiment is **multi-turn tool-using model training**, using TRL's maintained agent/environment support first. The model observes tool results and chooses subsequent actions; a one-shot answer-format reward alone does not close AL-4. Use resettable diagnostic tasks with executable outcome rewards, bounded steps/context and isolated agent actions. Save a real trained checkpoint and evaluate it against base and SFT checkpoints with the same harness, following the development-versus-final-test rule above.

| Invariant | Independent check |
|---|---|
| Equivalent group starts, distinct generation randomness | Compare initial snapshots/task identity; inspect seeds and rollout IDs |
| Exact behavior/context identity | Preserve per-turn inputs/token IDs, policy and template versions; test compaction/re-rendering drift |
| Correct target masks/log probabilities | Known mixed assistant/tool transcript; deliberately shifted or observation-inclusive mask must fail |
| Trusted reward | Correct/incorrect/shortcut candidates; agent cannot edit verifier or inspect private answers |
| Sound terminal semantics | Separate task completion, horizon truncation and environment/tool failure |
| Stable update behavior | Equal rewards/zero advantage, clipping boundaries, finite loss/gradients, checkpoint/resume |
| Genuine outcome evaluation | Compare independent held-out success with training reward and failure distribution |

Keep sparse executable task success as the interpretable baseline. Auxiliary/process rewards require a separate ablation and attack against the verifier. Include an explicit reward-hacking case such as a constant-output patch that passes an incomplete training check but fails independent behavior tests. Do not use grading bugs or privileged evidence as a shortcut to claimed improvement.

## RL systems

Operate a bounded verl/SGLang multi-turn run after the single-process training path works. Retain the original B2 optimizer-memory, DP/FSDP/ZeRO, tiny supplied-loop modification, stale-weight/train-inference mismatch and verl/Miles/slime source comparison. Inference retains engine scheduling/cache/GPU ownership; this track owns rollout/learner policy and reward/dataflow semantics.

Trace task distribution → rollout worker → tool environment → scored trajectory → learner batch → update → checkpoint/weight publication → next rollout. Record actor/reference/critic/optimizer memory, rollout and training utilization, stragglers, sample throughput, policy versions and wait/transfer time. Distinguish asynchronous tool execution from asynchronous learning with stale policy data.

Start with synchronous version-pinned rollouts. Study asynchronous placement using version-tagged examples and the selected framework's supported path; bound stale-policy acceptance and do not relabel data as on-policy. Include a short two-GPU run when the pinned setup fits, reusing prepared rental sessions and logging allocation once. If hardware/backend compatibility blocks an operated requirement, record it pending and retain the numerical/source work; never substitute simulated throughput for operation.

The learner investigates weight synchronization, log-probability consistency, partial/aborted rollouts, checkpoint recovery and token accounting. Supply distributed launch plumbing. Source comparison covers verl, Miles and slime without requiring three deployed training stacks.

## Independent agent capstone

Question: **Can trajectory SFT and verifiable-reward RL improve engineering diagnosis at a fixed execution budget while preserving evidence quality and permission boundaries?**

Begin the proposal and evaluation protocol after AGT-04, before optimizing prompts or collecting training trajectories. Preregister primary verified-task success and constraints; secondary unsupported claims, failure categories, latency, tokens/API cost and training cost. Freeze task splits, verifier, environment, model family, harness and run budget. Compare base, prompt-optimized, SFT and SFT-plus-RL checkpoints/configurations. State whether the optimized prompt is retained for training comparisons so each contrast has a clear interpretation. Later protocol revisions must be dated, justified and made before unsealing test results.

Use fixed RAG only on the answer-only subset. Research/code/GUI/collaboration tasks remain required capability labs; the primary training study can use the bounded diagnosis subset without claiming general improvement across all domains. Memory, search and multi-agent changes receive separate controlled experiments, not a confounded full-stack switch.

Retain all attempted sessions and uncertainty at the task/family level; do not repeatedly tune after inspecting held-out results. Record a negative result if warranted. Deliver a proposal, progress review, reproducible study, report, poster/demo and technical defense. The two guest-topic exercises are required external-material slots; see [coverage](COVERAGE.md#course-update-rule).

No joint inference capstone is required. The original small live-agent quality/tool-behavior check is mandatory here; a versioned report may accompany the independent inference routing study. Fixed transcripts cannot validate fresh-output agent branching.

## Completion records

Link each result to the owning task, source/model/data revisions, exact commands, actual hardware/API usage, raw artifacts, independent checks, learner explanation and limitations. Record supplied versus learner-modified components. Required evidence distinguishes CPU mathematics, source investigation, live agent operation, SFT, multi-turn RL and distributed operation. No positive improvement, production scale or current job eligibility is implied by completing a lab.
