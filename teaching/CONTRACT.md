# Teaching delivery contract

[Curriculum](CURRICULUM.md) · [Authorship/status rules](../docs/engineering/ownership.md)

## Teaching contract

Audience: experienced Python/PyTorch/transformer user with C/C++ OS and distributed-systems projects, new to CUDA and Kubernetes. Teach GPU execution and Kubernetes explicitly; use PennOS scheduling/ownership and PennCloud failure/routing experience as bridges. Skip rebuilding HTTP, durable KV or an autodiff framework as prerequisites.

**Delivered now:** lesson 00 and the dependency-free [starter utility](../starter/README.md). **Planned:** inference modules 01–24/PF and bridge capsules, plus agent AT-00–15, their exercise scaffolds and reference solutions. Application modules 14/15, AG and B2 have canonical owners in the agent curriculum; replay remains inference-owned. This document specifies those deliverables; links to code under future module paths are path specifications, not existing files. Do not mistake a syllabus for completed courseware.

Inference delivery order follows its existing sequence; agent AT units run in parallel with broad December knowledge and spring practical training. Historical inference sequence: 00–13 for fall engine learning; 14–17 for December applications/first gateway; deeper 18–19 in January; 20–23 in February; 24 and bridges in March/April. Teach the conceptual overview of advanced topics early without turning it into a prerequisite for the engine.

A full technical module normally consists of 25–40 slides plus expandable notes, a 45–75-minute teaching session, 1–2 hours of small exercises and the project lab assigned in the master plan. Larger topics split into sessions A/B. This is **inside** the package budgets, not extra homework. Lesson 00 is an orientation/reference deck, not a substitute for the deep modules.

Each module must contain:

1. Three to five observable learning objectives and a short prerequisite check.
2. A concrete request or failure that motivates the mechanism.
3. A visual state trace before abstract equations or production code.
4. Equations with units, tensor shapes, assumptions and a worked numerical example.
5. A minimal readable implementation and mapping to a pinned production reference.
6. At least two misconception/debugging examples and a deliberately broken fixture.
7. “Predict before running” questions with revealable answers; notes explain why wrong answers fail.
8. A scaffolded learner task, independent correctness oracle, one bounded experiment and an exit explanation.
9. Exact source links, tested software/hardware, and an explicit limit on what the lesson demonstrates.

**Notes:** include reasoning, intermediate steps, edge cases and what to inspect in code. Do not hide essential explanation exclusively in a spoken lecture. A learner must be able to study offline with no instructor.

**HTML:** plain HTML/CSS/JS, no required CDN, keyboard next/previous and direct slide selection, URL anchors, reading view, print styles, expandable notes/answers, accessible labels, responsive code blocks and high contrast. Use inline SVG/CSS state diagrams and small interactive simulators. Synthetic animations/calculators must say “illustrative”; performance plots must link to real raw data. Do not invent benchmark graphs.

**Code tree for later delivery:**

```text
teaching/modules/<id>/
  README.md          objectives, environment, run commands, ownership, time box
  scaffold/          working transport/build/plumbing; learner TODOs clearly marked
  exercises/         only the mechanism under study
  fixtures/          deterministic inputs and independent expected results
  tests/             correctness/state invariants; no perf assertion on a laptop
  reference/         complete annotated solution, opened when useful
  experiments/       fixed small sweep + collection recipe + expected qualitative questions
  reading.md         paper sections and pinned source symbols
teaching/slides/<id>.html
```

The AI tutor first supplies explanation, then code assistance. After understanding, ask it to implement your stated design, review its diff, and run independent checks. Request a walkthrough of any line you cannot explain. Rebuild a small part without the agent at each exit gate. Supplied reference code is clearly credited and never silently described as your independent implementation.

## Code assistance priorities

| Provide complete code | Keep learner ownership |
|---|---|
| Experiment directories, manifest/report formatting, plot styling | Measurement definitions and causal interpretation |
| HTTP/SSE transport, API schema adapters, tokenizer/weight loading | Request lifetime/cancellation and model math |
| RAG service/MCP wrappers/vector-store setup | Retrieval ablation, prompt identity, eval and agent policy |
| CUDA extension build, GPU provisioning/collection, distributed launch | One kernel, collective algebra and profile explanation |
| Graph capture shell and FlashInfer binding scaffolds | Buffer/state invariants, shape metadata and safe padding |
| Helm, dashboards, EPP registration, offload/P/D launch recipes | Routing score, failure/scaling policy and controlled experiments |

Give complete assistance code with explanations, not opaque generated files. For version-sensitive components, use the exact dependency set tested for the lesson, include a local smoke test and disclose whether validation used real GPUs. Use a clean environment and a tiny model before larger runs. Keep CPU agent application, training, GPU inference and platform environments independent.

## Lesson acceptance rubric

Score each dimension 0 (cannot), 1 (with notes), 2 (independent): explain; trace state/shapes; predict failure; implement/modify; design/interpret measurement. Advance at 8/10 with no zero in correctness. If a module stalls, use a reference and repeat a smaller variation; do not silently skip the concept.

Check understanding again one week and one month later with a five-minute reconstruction or oral explanation. At each milestone, identify one limitation you can defend. This is the guard against AI-generated code creating the appearance of mastery without the ability to reason about it.

## Assignment handoff requirements

The [handoff guide](../docs/HANDOFF.md) owns session modes and the step-by-step teaching-to-code procedure. Track blueprints own lesson content; task briefs own implementation/evidence. Do not interpret an explicit implementation request as proof of learner understanding or insert a redundant approval gate.

Before a coding/lesson agent implements a module, its brief must identify prerequisite artifacts, exact permitted production modules, contracts to preserve, a bounded checklist, supplied fixtures and independent oracles, hardware class, concrete commands, expected artifact types, exclusions, January continuation and ownership/evidence. Record exact commands after selecting the actual environment; do not invent working commands for the planned code paths.

Default checks stay lightweight and CPU-only. GPU, weight-download and Kubernetes checks are explicitly selected. A completed lesson must be authorable from its storyboard without inventing the mechanism, numeric/state examples or lab requirements. Keep reference solutions separate from the normal implementation path.

## Layered documentation handoff

Each module section in a topic guide now owns its pedagogical blueprint; system requirements and tasks are linked from it. Follow the blueprint's original concept sequence and add worked examples, diagrams, misconception fixtures, predict-before-run questions and exit checks when writing the actual lesson. Future storyboard/example/source-code files must link back to the module and the implementation task rather than duplicate a second runtime.

Current modules are Markdown blueprints, not completed HTML lessons, runnable exercises, or reference solutions. Only lesson 00's HTML and starter utilities are delivered. The original lesson 00 still reflects the baseline planning snapshot; consult the [roadmap](../docs/execution/roadmap.md) for the approved baseline plus agent expansion.

For a later authored storyboard, specify diagram states, numeric inputs and expected reasoning, assumptions/units/shapes, exact code/source targets, independent test oracle and bounded experiment. The standard sequence is prerequisite → motivating failure → state trace → mechanism → code walkthrough → debugging → learner task → experiment/teach-back. The skeleton's 01–17 hours are a partition of the baseline, not new assignments; PF/AG are separate additional records.

Keep source-specific citation and provenance in each lesson and use the central [reference map](../docs/references/README.md) for discovery. Pin code revisions at handoff, name whether a command was CPU/GPU validated, and preserve course licensing/publication constraints. Code provided by an agent does not earn learner-authored credit merely because it passes a generated test.

## Full agent-course delivery

Every published CMU 11-768 topic is required, including SFT, RL foundations, advanced algorithms and RL systems; integrated exercises preserve assignment/research objectives. Agent [curriculum](../tracks/agents/CURRICULUM.md) and [coverage](../tracks/agents/COVERAGE.md) are canonical. This supersedes the former policy of using only selected CMU harness/evaluation methods; it does not change assigned depth for unrelated external courses.

Teach complete action/observation traces, independent outcome checking, failure attribution and a case where extra complexity fails to help. Preserve exact mask/reward numerical exercises and actual SFT/multi-turn RL operation gates. Supplied training/distributed infrastructure does not remove learner responsibility for objectives/data/rewards. Guest/unpublished content stays pending external material, never invented. Code/HTML creation remains a later task, with authored, supplied, studied and operated status recorded separately.
