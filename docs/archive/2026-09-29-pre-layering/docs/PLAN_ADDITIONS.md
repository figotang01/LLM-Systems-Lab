# InferStack — append-only December supplements

Approved 2026-09-29. Status: **planning and handoff specification delivered; exercises, source stubs, integrations, experiments, and HTML lessons remain unimplemented**.

## 1. Preservation and accounting contract

This document adds to the [project plan](../PROJECT_PLAN.md), [complete December skeleton](DECEMBER_SKELETON.md), and [teaching curriculum](../teaching/CURRICULUM.md). It does not replace or summarize away their requirements. The earlier detailed skeleton is the baseline; the later condensed restatement is not authoritative.

Retain every original module 00–24, bridge B1–B6, interface, ownership rule, exercise, correctness and measurement contract, December gate, and January–May topic. Keep all existing vLLM and SGLang operation, comparison, advanced-lab, and capstone requirements. SGLang receives deeper attention **within the added production-framework track only**. No baseline hours or tasks fund the additions.

| Period | Existing learner hours | Added learner hours | Combined learner hours |
|---|---:|---:|---:|
| Through December 20, 2026 | 286 | 32 | **318** |
| January–April 2027 | 210 | 0 | **210** |
| Entire project | 496 | 32 | **528** |

The combined fall estimate is approximately 29 hours/week across the existing eleven-week window, not a guarantee that every week fits that amount. The original calendar remains the baseline; schedule the additional tasks after their prerequisites within the same December checkpoint. Preserve the December 21–January 3 break and late-April buffer. Do not silently move original tasks into January to make room. If actual work overruns, record the gap and request an explicit schedule revision.

The original 496/286-hour totals in preserved sections are **baseline figures**. The 528/318-hour totals above include these supplements. The original 440–560-hour uncertainty range was not re-estimated for the added scope. The January package-C completion, advanced labs, capstone, bridge lessons, and release/upstream-contribution work retain their original allocations. A local December patch does not automatically complete the later contribution/release gate.

These are learner hours, including reading, implementation, checks, and explanation. No paid API credit or additional GPU capacity is assumed. Reuse existing small-model sessions where possible and record any extra billed use. Documentation delivery now does not constitute completion of these future learning hours.

## 2. Production-framework development — 24 additional hours

Stable supplement IDs are PF-1 through PF-4; existing curriculum IDs are unchanged. The detailed hours below sum to 24. Pin each inspected upstream revision and record exact source symbols when starting a task; no version or successful run is invented in this planning delivery.

### PF-1 — SGLang source walkthrough and runtime-state investigation (8 h)

**Prerequisites:** module 03 baseline setup; modules 04–10 supply the model, scheduling, memory, and prefix-cache concepts. Begin the request-path reading after 03, and finish cache/lifecycle investigation after the corresponding mechanism lessons.

**Storyboard:** one input request → process/component boundaries → tokenization and admission → scheduling iteration → prefix lookup and page ownership → model execution → streaming completion → cancellation and cleanup. Contrast the actual pinned source with InferStack's simpler coordinator.

**Future learner work:**

- Trace one cold request and a repeated-prefix request; identify which component owns each relevant state transition.
- Inspect one cancellation path, including when ownership can actually be released.
- Map inspected symbols to `GenerationRequest`, `RequestState`, `Scheduler`, `PrefixIndex`, `BlockPool`, and `Executor` without forcing the frameworks to share an implementation.
- Annotate an observed trace or debugger/log sequence. If a device run is unavailable, label the walkthrough source-only and leave the execution gate pending.

**Supplied assistance:** source-navigation pointers for the pinned revision, launch/debug instructions, tiny prompts, and an artifact template. The learner supplies the state explanation, not just a copied call graph.

**Acceptance/evidence:** revision-linked diagram; request/cache/cancellation trace; one mismatch between an initial prediction and actual behavior explained; exact commands and environment record. Instrumentation must not be left enabled in headline performance measurements.

### PF-2 — vLLM V1 architectural comparison (4 h)

**Prerequisites:** module 03's vLLM baseline and PF-1's request-path map; finish after the cache/scheduling lessons.

**Storyboard:** same request and workload → V1 API/engine/worker boundaries → scheduler and KV ownership → prefix lookup and preemption → output and abort handling → comparison with SGLang and InferStack.

**Future learner work:** identify the corresponding pinned V1 components and explain at least three concrete differences in responsibilities or state management. Separate source observations from behavior confirmed in a run. Keep model, tokenization, generation limits, and metric definitions matched in any empirical comparison.

**Acceptance/evidence:** a source-linked comparison table plus one request-path walkthrough. Explain that paging, prefix indexing, eviction, and scheduling are separate design dimensions; do not reduce the comparison to “vLLM has paging, SGLang has radix caching.” All earlier vLLM tests, baselines, and later labs remain required.

### PF-3 — Bounded SGLang modification with regression coverage (8 h)

**Prerequisites:** PF-1 and the baseline correctness lesson corresponding to the changed component.

**Storyboard:** concrete behavior/invariant → minimal reproduction → source inspection → bounded change → independent regression check → measured or state-based validation → limitations and review.

**Assignment boundary:** use a prepared task in the pinned source, such as request/cache-state instrumentation or a narrowly scoped bookkeeping/validation change. Select and document one concrete task at handoff time after verifying the relevant source exists. Discovering a novel upstream bug is not a prerequisite. Do not rewrite a scheduler or add a new serving subsystem in this time box.

**Future learner work:** make a local patch, explain each changed behavior, and add focused coverage. A bug fix requires a reproducer that fails before and passes after; new instrumentation requires known-state assertions and a check that enabling it preserves relevant output/lifecycle semantics. If claiming performance impact, preserve raw before/after runs and compare under matched settings; a positive speedup is not required.

**Acceptance/evidence:** patch against a recorded commit; reproduction command; regression results; short rationale and limits; explicit attribution for supplied assistance. The patch must concern runtime behavior, validation, or diagnostic capability; an unrelated cosmetic edit does not meet this task. Upstream submission or merge is not the December exit gate, and no public communication is performed by this documentation task.

### PF-4 — Technical walkthrough and interview practice (4 h)

**Prerequisites:** PF-1–PF-3 and the relevant December engine/GPU evidence.

**Storyboard:** defend the architecture → calculate capacity → inspect a performance trace → locate unfamiliar production code → explain a patch/test → critique a benchmark claim.

**Future learner work:** two practice sessions including preparation and correction. First cover a full request lifecycle and the SGLang patch; second cover a KV-capacity calculation, a latency/debugging scenario, and a comparison with vLLM V1. Attempt explanations without AI or notes, then consult source and record corrections.

**Acceptance/evidence:** questions, initial answers, corrected explanations, and unresolved gaps. Demonstrate code navigation, causal reasoning, and a defensible limitation rather than memorizing framework names. Reuse the curriculum's understanding rubric. This is a preparation rubric, not a claim about any employer's private interview process or guaranteed readiness.

### Production-framework references

- [SGLang contribution guide](https://docs.sglang.io/docs/developer_guide/contribution_guide): setup, focused coverage, correctness, profiling, and review conventions. Use the instructions matching the pinned source revision when implementing.
- [vLLM architecture overview](https://docs.vllm.ai/en/latest/design/arch_overview/): V1 component/process map; do not substitute an older V0 description.
- [vLLM prefix caching](https://docs.vllm.ai/en/latest/design/prefix_caching/): compare identity, allocation, and reuse against actual source.
- The existing papers, compact-engine references, profiling material, and source-reading assignments in the baseline remain assigned.

## 3. CMU 11-768 agent-development supplement — 8 additional hours

Supplement ID **AG-1** extends module 15; it does not replace its original 12 December hours or the January completion work. The combined December agent allocation is **12 + 8 = 20 h**. Module 14's RAG allocation and package C's original work remain intact.

The [CMU 11-768 course](https://www.cmu-agents.com/) is an additional primary teaching reference. Its released [Assignment 1](https://github.com/cmu-agents/assignment-1/blob/main/ASSIGNMENT.md) supplies useful examples of harness construction and context compaction; [Assignment 2](https://github.com/cmu-agents/assignment-2/blob/main/ASSIGNMENT.md) motivates evidence-based evaluation and testing the evaluator itself. Adapt these methods to InferStack rather than requiring completion of all course applications. Record the source revision, relevant sections, provenance, and applicable reuse conditions before distributing adapted code.

### Added exercises and hours

| Exercise | Added hours | New evidence beyond the baseline |
|---|---:|---|
| AG-1a: harness implementation | 2 | Learner-written decision/action/observation loop over the existing supplied transport and tools |
| AG-1b: context compaction | 3 | Explicit context policy, preservation fixtures, and paired prompt/token analysis |
| AG-1c: evaluator failures | 3 | Deliberately wrong outputs, verifier failures, and a documented correction/limitation |
| **Total** | **8** | |

**Existing requirements preserved:** MCP SDK/tool wrappers; `docs_search`; read-only benchmark SQL; supplied constrained execution; step/token/time limits; JSON/schema versus semantic validation; structured-output/XGrammar concepts; trace capture; all three measurement/replay modes; held-out tasks; January evaluation expansion; the restricted-runner failure fixtures. Teaching ownership becomes deeper for the added exercises without requiring another general-purpose agent framework or sandbox.

### Additional application: an inference-analysis agent

Reuse the existing tools to answer a small question about a supplied benchmark bundle: retrieve the relevant documentation, query known run records, perform constrained analysis when needed, and produce an answer with evidence identifiers. Use fabricated fixture measurements only when visibly labeled synthetic; use actual experiment bundles for empirical claims. The agent does not provision GPUs, change serving deployments, or replace the original RAG/MCP workloads.

Future separation within the existing `workloads/` boundary: harness policy, context policy, tool adapters, evaluation, and trajectory capture. Do not create another model client, tool transport, benchmark runner, or trace schema merely for this example. If the original schema cannot represent a compaction event, add an optional versioned extension while retaining old trace readability.

### AG-1a storyboard and acceptance (2 h)

**Sequence:** task and observations → model action → tool-call parsing → linked tool result → next decision → termination or budget exhaustion.

Implement the loop over supplied interfaces; use deterministic model/tool responses for offline testing. Preserve tool-call IDs and existing budgets. Inspect malformed arguments, unknown tools, and a tool failure without turning them into unbounded retries. Terminal outcomes must be explicit.

**Evidence:** one normal trajectory, one recoverable tool error, and one exhausted-budget trajectory. Explain what the learner wrote versus the supplied client and MCP plumbing. Retain the original module's broader tests and live/replay distinctions.

### AG-1b storyboard and acceptance (3 h)

**Sequence:** growing transcript → context limit → choose older complete interactions → working-memory summary → preserve recent action/observation pairs → render next prompt → inspect changed token/prefix identity.

Retain the task and constraints plus complete recent tool interactions. Keep the original full trajectory for evaluation; compaction changes the model's active context, not the evidence log. Start with deterministic summary fixtures and one bounded live comparison after the baseline tools work.

**Evidence:** before/after active prompts, token counts with tokenizer/template identity, preservation checks, and a compaction event linked to its parent request. Explain why fewer input tokens can still disrupt prefix reuse. Any claim about latency, cache hits, or answer quality needs actual measurements; otherwise record it as a hypothesis. Do not assume compaction improves task success or serving latency.

### AG-1c storyboard and acceptance (3 h)

**Sequence:** task outcome → inspect result and trajectory → write explicit checks → challenge the evaluator with plausible wrong outputs → distinguish agent failure from evaluator failure → correct one weakness and record a residual limit.

Use an answer grounded in supplied run records. Include at least one correct result, one wrong aggregate, and one unsupported latency/performance claim. Demonstrate a plausible incorrect answer that an initial weak verifier accepts, then add an independent check or document why a human review is still needed. Deterministic checks and hand-checked fixtures are the baseline; an LLM judge is optional and never assumed to be ground truth.

**Evidence:** fixture labels and provenance, validator decisions, a false-positive/false-negative analysis where observed, and a changed check. Do not tune on or expose the original held-out tasks. A small teaching fixture is not a statistically reliable agent benchmark; January quality evaluation remains required.

### Teaching handoff

Apply the baseline storyboard and HTML contracts. The implementation agent supplies wrapper/environment setup, fixed fixtures, and source pointers; the learner owns the added loop, compaction policy, evaluator reasoning, and result interpretation. Do not silently turn the additional eight hours into a complete CMU semester, additional hosted-model deployments, or agent training. Existing spring training/rollout bridge topics remain unchanged.

## 4. Integration order, status, and acceptance

| Addition | Attach to existing work | Completion gate |
|---|---|---|
| PF-1 | Module 03, then 06–10 | Source-linked request/cache/cancellation walkthrough |
| PF-2 | Module 03 and PF-1 | Pinned V1 comparison and request map |
| PF-3 | PF-1 plus the corresponding mechanism lesson | Bounded patch and focused regression evidence |
| PF-4 | December engine/GPU checkpoint and PF-1–PF-3 | Two technical practice sessions and corrected explanations |
| AG-1 | Existing modules 14–15 | Harness, compaction, and evaluator-failure artifacts |

All five tasks target the existing December 20 checkpoint. Interleave reading with the mechanism lessons; do not make production code exploration a prerequisite for learning a concept in the small runtime. These additions are separate entries in the future teaching catalog and work log, not edits to baseline module-hour values. PF-1–PF-4 total 24; AG-1 totals 8; 286 + 24 + 8 = 318 and 496 + 24 + 8 = 528.

**This documentation delivery is complete when:** existing files are unchanged or receive only appended content; the detailed baseline skeleton is recorded; cross-references resolve; counts and hour totals agree; and no source, slide, benchmark, cloud, or upstream-contribution completion is implied.

**Later supplement completion requires:** all original gates plus the evidence above. Keep tasks marked planned until their evidence exists. Unsupported hardware or unavailable resources leave the affected execution gate pending rather than relabeling reading as an executed experiment.
