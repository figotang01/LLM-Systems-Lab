# SGLang and vLLM source development

[Curriculum](../../../teaching/CURRICULUM.md) · [Teaching contract](../../../teaching/CONTRACT.md) · [Roadmap](../../../docs/execution/roadmap.md)

This guide groups existing module blueprints. Read only the module assigned by your current task. Module IDs, hours, objectives, exercises and exit gates are unchanged; HTML and runnable labs remain planned except the existing orientation.

Use the teaching contract for independent oracles, numerical/state examples, the explain/trace/predict/implement/measure rubric and one-week/one-month retrieval checks. Task briefs own implementation acceptance and authorship.

- [PF-1 — SGLang source walkthrough and runtime-state investigation (8 h)](#module-pf-1)
- [PF-2 — vLLM V1 architectural comparison (4 h)](#module-pf-2)
- [PF-3 — Bounded SGLang modification with regression coverage (8 h)](#module-pf-3)
- [PF-4 — Technical walkthrough and interview practice (4 h)](#module-pf-4)

<a id="module-pf-1"></a>
## PF-1 — SGLang source walkthrough and runtime-state investigation (8 h)

**Status:** blueprint delivered; source study, patch, execution and evidence remain planned.

**Prerequisites:** module 03 baseline setup; modules 04–10 supply the model, scheduling, memory, and prefix-cache concepts. Begin the request-path reading after 03, and finish cache/lifecycle investigation after the corresponding mechanism lessons.

**Storyboard:** one input request → process/component boundaries → tokenization and admission → scheduling iteration → prefix lookup and page ownership → model execution → streaming completion → cancellation and cleanup. Contrast the actual pinned source with InferStack's simpler coordinator.

**Future learner work:**

- Trace one cold request and a repeated-prefix request; identify which component owns each relevant state transition.
- Inspect one cancellation path, including when ownership can actually be released.
- Map inspected symbols to `GenerationRequest`, `RequestState`, `Scheduler`, `PrefixIndex`, `BlockPool`, and `Executor` without forcing the frameworks to share an implementation.
- Annotate an observed trace or debugger/log sequence. If a device run is unavailable, label the walkthrough source-only and leave the execution gate pending.

**Supplied assistance:** source-navigation pointers for the pinned revision, launch/debug instructions, tiny prompts, and an artifact template. The learner supplies the state explanation, not just a copied call graph.

**Acceptance/evidence:** revision-linked diagram; request/cache/cancellation trace; one mismatch between an initial prediction and actual behavior explained; exact commands and environment record. Instrumentation must not be left enabled in headline performance measurements.

Canonical implementation task: [PF-1](../tasks/framework.md#pf-1). Required source map: [references](../../../docs/references/README.md). These hours are additional to all baseline modules.

<a id="module-pf-2"></a>
## PF-2 — vLLM V1 architectural comparison (4 h)

**Status:** blueprint delivered; source study, patch, execution and evidence remain planned.

**Prerequisites:** module 03's vLLM baseline and PF-1's request-path map; finish after the cache/scheduling lessons.

**Storyboard:** same request and workload → V1 API/engine/worker boundaries → scheduler and KV ownership → prefix lookup and preemption → output and abort handling → comparison with SGLang and InferStack.

**Future learner work:** identify the corresponding pinned V1 components and explain at least three concrete differences in responsibilities or state management. Separate source observations from behavior confirmed in a run. Keep model, tokenization, generation limits, and metric definitions matched in any empirical comparison.

**Acceptance/evidence:** a source-linked comparison table plus one request-path walkthrough. Explain that paging, prefix indexing, eviction, and scheduling are separate design dimensions; do not reduce the comparison to “vLLM has paging, SGLang has radix caching.” All earlier vLLM tests, baselines, and later labs remain required.

Canonical implementation task: [PF-2](../tasks/framework.md#pf-2). Required source map: [references](../../../docs/references/README.md). These hours are additional to all baseline modules.

<a id="module-pf-3"></a>
## PF-3 — Bounded SGLang modification with regression coverage (8 h)

**Status:** blueprint delivered; source study, patch, execution and evidence remain planned.

**Prerequisites:** PF-1 and the baseline correctness lesson corresponding to the changed component.

**Storyboard:** concrete behavior/invariant → minimal reproduction → source inspection → bounded change → independent regression check → measured or state-based validation → limitations and review.

**Assignment boundary:** use a prepared task in the pinned source, such as request/cache-state instrumentation or a narrowly scoped bookkeeping/validation change. Select and document one concrete task at handoff time after verifying the relevant source exists. Discovering a novel upstream bug is not a prerequisite. Do not rewrite a scheduler or add a new serving subsystem in this time box.

**Future learner work:** make a local patch, explain each changed behavior, and add focused coverage. A bug fix requires a reproducer that fails before and passes after; new instrumentation requires known-state assertions and a check that enabling it preserves relevant output/lifecycle semantics. If claiming performance impact, preserve raw before/after runs and compare under matched settings; a positive speedup is not required.

**Acceptance/evidence:** patch against a recorded commit; reproduction command; regression results; short rationale and limits; explicit attribution for supplied assistance. The patch must concern runtime behavior, validation, or diagnostic capability; an unrelated cosmetic edit does not meet this task. Upstream submission or merge is not the December exit gate, and no public communication is performed by this documentation task.

Canonical implementation task: [PF-3](../tasks/framework.md#pf-3). Required source map: [references](../../../docs/references/README.md). These hours are additional to all baseline modules.

<a id="module-pf-4"></a>
## PF-4 — Technical walkthrough and interview practice (4 h)

**Status:** blueprint delivered; source study, patch, execution and evidence remain planned.

**Prerequisites:** PF-1–PF-3 and the relevant December engine/GPU evidence.

**Storyboard:** defend the architecture → calculate capacity → inspect a performance trace → locate unfamiliar production code → explain a patch/test → critique a benchmark claim.

**Future learner work:** two practice sessions including preparation and correction. First cover a full request lifecycle and the SGLang patch; second cover a KV-capacity calculation, a latency/debugging scenario, and a comparison with vLLM V1. Attempt explanations without AI or notes, then consult source and record corrections.

**Acceptance/evidence:** questions, initial answers, corrected explanations, and unresolved gaps. Demonstrate code navigation, causal reasoning, and a defensible limitation rather than memorizing framework names. Reuse the curriculum's understanding rubric. This is a preparation rubric, not a claim about any employer's private interview process or guaranteed readiness.

Canonical implementation task: [PF-4](../tasks/framework.md#pf-4). Required source map: [references](../../../docs/references/README.md). These hours are additional to all baseline modules.
