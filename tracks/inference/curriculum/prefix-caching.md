# Hash and radix prefix caching

[Curriculum](../../../teaching/CURRICULUM.md) · [Teaching contract](../../../teaching/CONTRACT.md) · [Roadmap](../../../docs/execution/roadmap.md)

This guide groups existing module blueprints. Read only the module assigned by your current task. Module IDs, hours, objectives, exercises and exit gates are unchanged; HTML and runnable labs remain planned except the existing orientation.

Use the teaching contract for independent oracles, numerical/state examples, the explain/trace/predict/implement/measure rubric and one-week/one-month retrieval checks. Task briefs own implementation acceptance and authorship.

- [09 — Block-hash prefix reuse (E)](#module-09)
- [10 — Radix cache and fair cache-aware scheduling (E)](#module-10)

<a id="module-09"></a>
## 09 — Block-hash prefix reuse (E)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 10 baseline h (E). Hours are owned by the roadmap.

**Concept prerequisites:** [06](runtime.md#module-06), [08](runtime.md#module-08). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** derive complete cache identity and evict only safe blocks.
- **Slides 1–10:** full-block prefix chain and ancestry; model/adapter/tenant identities. **11–20:** cache ownership vs active references, LRU queue, full-prompt hit/logit issue. **21–30:** hash collision assumptions, isolation boundaries and cold/warm tests.
- **Code:** learner chained key/lookup/eviction; supplied reused-prefix fixtures and cache visualization.
- **Experiment/exit:** same block under a different parent must miss; new adapter/namespace must miss; quantify reused tokens, not just request hits.
- **Reference:** vLLM automatic-prefix-cache design.

### December storyboard sequence

Prefix ancestry → identity → immutable pages → ownership/eviction → full-hit logits. Implement reuse and show isolation misses and cold/warm behavior.

### Implementation connections

- [KV-03](../tasks/memory-cache.md#kv-03) — Block-hash prefix index; Build.

**Design context:** [kv-cache](../design/kv-cache.md).

<a id="module-10"></a>
## 10 — Radix cache and fair cache-aware scheduling (E)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** 14 baseline h (E). Hours are owned by the roadmap.

**Concept prerequisites:** [09](prefix-caching.md#module-09). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** implement compressed edges, splitting, locks and eviction; isolate indexing from policy effects.
- **Slides 1–10:** draw SYS+A+X / SYS+A+Y / SYS+B+Z. **11–24:** partial-edge match, split/insert, lock propagation, leaf eviction, page alignment. **25–36:** fair comparison with block hashes, LPM/aging, lookup cost and fairness.
- **Code:** learner radix operations over the SAME pool; supplied printer and adversarial split/evict sequence. Use a provided reference if the full implementation threatens the December gate, then modify/debug it.
- **Experiment/exit:** cache-policy comparison with matched resources; explain why branching alone does not guarantee radix superiority.
- **References:** SGLang paper and Mini-SGLang.

### December storyboard sequence

Compressed edges → match/split/insert → locks → eviction → fair comparison. Implement the same prefix contract and isolate index effects from policy effects.

### Implementation connections

- [KV-04](../tasks/memory-cache.md#kv-04) — Radix index and controlled comparison; Build or Modify with attribution.
- [SCH-05](../tasks/scheduler.md#sch-05) — Cache-aware scheduling with fairness guard; Build.

**Design context:** [kv-cache](../design/kv-cache.md), [scheduler](../design/scheduler.md).
