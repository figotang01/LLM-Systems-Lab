# Teaching and implementation handoff

[Start here](../README.md) · [Agent instructions](../AGENTS.md) · [Teaching contract](../teaching/CONTRACT.md) · [Ownership](engineering/ownership.md)

This guide owns the working procedure, not project scope or a second task list. A new coding/tutoring agent should be able to select one bounded increment, teach or implement it, validate it, and leave enough evidence for its successor.

## Read a small task packet

1. Read AGENTS.md and the chosen track entrance.
2. Open the task brief: its status, prerequisites, ownership, change boundary and acceptance.
3. Read the linked design sections and the linked lesson blueprint. Consult shared correctness/resources/decisions only where this task needs them.
4. Inspect prerequisite code and evidence. A dependency link, an unchecked checklist or a planned filename is not implemented functionality.

Do not use a résumé, archived calendar, course-outline checkbox or this guide as proof that code exists. Avoid loading every document into context; expand the packet when a concrete dependency or ambiguity requires it.

| Need | Canonical owner |
|---|---|
| Inference behavior | [Architecture](../tracks/inference/ARCHITECTURE.md), then its linked subsystem design |
| Inference sequence/status | [Task briefs](../tracks/inference/tasks/README.md) |
| Agent behavior | [Runtime](../tracks/agents/RUNTIME.md) and [evaluation/learning](../tracks/agents/LEARNING.md) |
| Agent sequence/status | [Agent roadmap](../tracks/agents/ROADMAP.md) |
| Lesson content | [Curriculum entrance](../teaching/CURRICULUM.md), then the selected track blueprint |
| Supplied versus learner work | [Ownership rules](engineering/ownership.md), specialized by the task |
| Concrete unresolved choice | [Decision register](engineering/open-questions.md); update its owning design when resolved |

## Choose the mode from the request

| Request | Deliverable and stopping point |
|---|---|
| “Prepare the next lesson” | Complete the requested self-contained lesson and relevant runnable fixtures/scaffold. Keep the learner's Build exercise distinct from the attributed reference solution. Do not implement unrelated production tasks. |
| “Teach me the next topic” | Explain one coherent mechanism, work an example and give a prediction/exercise. Continue interactively from the learner's answer; do not mark their understanding passed on their behalf. |
| “Implement task X” | Complete the authorized bounded code/tests/integration work and evidence. Provide a concise explanation and leave understanding unassessed until demonstrated. No redundant approval is needed for ordinary task choices. |
| “Review/fix task X” | Check actual behavior against its invariants and independent oracles; repair authorized issues, then update evidence. Do not turn the review into a new curriculum or rewrite unrelated systems. |

When both teaching and implementation are requested, use the sequence below. A request to produce a full reference implementation is compatible with learning: label it supplied/assisted and leave independent reconstruction as learner work.

## One teaching-to-code increment

1. **Orient:** name the task, goal, prerequisites, machine class and boundary. State what is actually available and which code will be supplied.
2. **Explain:** use a concrete request/trajectory/state diagram before API details. Show a worked calculation or deterministic state transition, including its assumptions.
3. **Predict:** provide an input and a failure case with independently derived expected behavior. During interactive teaching, obtain the learner's reasoning; during lesson authoring, provide revealable answers.
4. **Specify:** settle the smallest interface/policy needed for this increment. Record the decision, alternatives and unresolved constraints in the owning design. Do not freeze unrelated future APIs.
5. **Build/modify:** implement the selected mechanism or supplied scaffold according to authorship rules. Work in useful substeps, keeping a runnable boundary; no forest of empty future modules.
6. **Verify:** test the independent oracle, deliberate failure, integration boundary and relevant recovery path. Run real GPU/platform/model checks only when the task requires and supports them.
7. **Explain and measure:** distinguish logic correctness, model quality and performance. A successful test, a shorter prompt or a GPU trace is not automatically a speedup. Record the learner's teach-back separately.
8. **Record:** update the owning task, link artifacts, and state one next unfinished increment. Leave the successor a reproducible command and the actual failure/limitation when blocked.

The shared HTML contract remains mandatory: worked examples, annotated code, independent checks, debugging, accessible offline reading/print/navigation and honest illustrative versus measured results. Preparing lesson 01 does not require delivering the entire runtime lab for later modules.

## Task selection examples

- **First inference work:** [FND-01](../tracks/inference/tasks/model.md#fnd-01), using its startup sequence. FND-02 and SCH-01 follow its actual contracts; the production-engine benchmark does not block CPU contracts.
- **“Next scheduler task”:** inspect SCH-01–05. With the current planned state, SCH-01 needs FND-01. Complete that missing prerequisite first if implementing; when teaching, its lifecycle example can already be explained without CUDA.
- **First agent work:** [AGT-01](../tracks/agents/ROADMAP.md#agt-01), then AGT-02 for RAG. RAG does not wait for BEN-03, BEN-04 or the custom engine.
- **SFT/RL study:** AT-11–14 concepts can be studied before the corresponding GPU implementations. A theory exercise cannot close AGT-11–13's real training gates.
- **Capstone preparation:** AGT-14's proposal and split/protocol work starts after AGT-04, before optimization; all completion dependencies need not be finished before planning the experiment.

For an unspecified task within a track, select the earliest ready task in its canonical index, preferring the requested subsystem. For an unspecified track, prioritize inference as approved. This is a selection rule, not an instruction to complete multiple milestones in one turn.

## Evidence in the owning task

Replace or extend the existing completion-evidence paragraph in that task; do not make a parallel status ledger. During a long task, use the same block for resumption. Large raw logs belong in the existing experiment/artifact layout and are linked by path/hash.

```text
Implementation: planned | in progress | blocked (specific reason) | implemented
Current increment / next unfinished increment:
Code and artifact paths; commit or patch/content hashes:
Authorship by component: learner-authored | learner-modified | supplied | mixed
Lesson: blueprint | HTML authored | exercised (link actual artifact)
Learner understanding: not assessed | with assistance | independently demonstrated
Decisions made; remaining decision IDs:
Environment/model/data/template revisions and hardware:
Executed command -> actual outcome; independent oracle used:
Acceptance: map each original criterion to evidence or an explicit pending item
Limitations / failed or unavailable checks:
```

Implementation may be validated while learner understanding remains unassessed. Report both. Do not claim the overall learning milestone complete until its required explanation/reconstruction and operated evidence exist. Dependencies for code integration require the relevant implemented artifacts; teaching prerequisites concern concepts, not all future deployments.

“Supplied” in a plan is a future authorship assignment. Except for the existing starter, orientation and repository-maintenance tools, supplied transports, launchers, dashboards and training adapters still need to be authored and validated. A successor must not import nonexistent supplied code or assume it has passed a hardware smoke test.

## How to make a lesson implementation-ready

The selected blueprint gives scope; its author supplies the detailed storyboard at delivery. For each session, specify:

- A concrete input/state and expected progression, not just a topic list.
- The equation, units/shapes and worked values; for stateful topics, a transition table and conserved quantity.
- One correct and one deliberately broken case with an oracle independent of the implementation.
- Exact production/fixture/reference boundaries and what the learner writes or modifies.
- A bounded experiment, raw output to retain and a teach-back that can reveal a misconception.
- Source sections and tested dependency set; unresolved course-specific details stay explicitly pending review.

Use lesson IDs to distinguish shared output: `teaching/modules/01/` and `teaching/slides/01.html` for original numbered lessons; `teaching/modules/AT-00/` and `teaching/slides/AT-00.html` for agent units. Split long units with session suffixes. Create only delivered session files; no duplicate implementations of shared model/cache theory.

## Repository and publishing boundary

Declared remote: [figotang01/LLM-Systems-Lab](https://github.com/figotang01/LLM-Systems-Lab). At this handoff the local directory is not initialized as a Git checkout, and remote contents could not be inspected because network access failed. Do not infer an empty remote, default branch or successful synchronization.

When publication is requested, inspect the remote first. If it has commits, start from its history and apply the workspace changes; do not force-push an unrelated initial history. If it is empty, initialize a normal local history and configure the provided origin. Review staged files and ignore rules before committing/pushing. These are handoff instructions, not operations performed by this documentation change.

The local recovery ZIP is deliberately ignored and is not required by a fresh clone. Active documentation links only to versioned source documents. Keep private résumés, secrets, checkpoints and raw private run data outside the tracked tree. A license choice remains the repository owner's decision before claiming permissions for third-party reuse; no license is invented here.

## Repeatable repository checks

From the repository root:

```sh
python3 tools/check_docs.py
python3 -m unittest discover -s tests -v
python3 starter/experiment.py budget starter/budget.example.json
```

The documentation checker covers active local links/anchors, task dependencies, track independence and required scope IDs. It does not check remote availability, pedagogy, numerical correctness, compatibility or learner understanding. Run subsystem-specific tests in addition once implementation exists. The CPU GitHub workflow runs only the documentation checker and repository utility tests; it never provisions GPUs or calls model APIs.
