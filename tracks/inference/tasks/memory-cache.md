# KV memory and prefix indexes — implementation tasks

[Task selection rules](README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Ownership](../../../docs/engineering/ownership.md)

Each task is a meaningful engineering increment. Hours belong to the roadmap, not the number of checkboxes. Source paths below are planned targets, created when the task starts. Acceptance checks remain unimplemented unless a task status/evidence record says otherwise.

<a id="kv-01"></a>
## KV-01 — Pool ownership and transactional reservation

**Status:** planned. **Package:** D. **Milestone:** CP2 (early reference/ownership work).

**Requirement/design:** [KV-1](../design/kv-cache.md#kv-1) — [canonical design](../design/kv-cache.md). **Learning mode:** Build. **Authorship target:** learner-authored; state fixtures supplied.

**Dependencies:** [FND-01](model.md#fnd-01).

**Teaching:** [06](../curriculum/runtime.md#module-06).

**Planned change boundary:** `src/inferstack/engine/memory/block_pool.py`, `src/inferstack/engine/memory/leases.py`, `tests/memory/test_ownership.py`

**Work:**

- [ ] Define physical IDs, free/reserved/owned accounting and request/cache/in-flight leases.
- [ ] Implement reserve/retain/release with rollback and idempotent terminal cleanup; test random allocate/fork/free/exhaustion transitions.

**Validation / acceptance:**

- [ ] Distinct physical pages are conserved; no negative refs, double free or unowned live page.
- [ ] Failed multi-page reservation leaves tables/accounting unchanged; stale handles are detected by fixtures.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="kv-02"></a>
## KV-02 — Page tables, writes and shared-tail copy-on-write

**Status:** planned. **Package:** D. **Milestone:** CP2 (early reference/ownership work).

**Requirement/design:** [KV-2](../design/kv-cache.md#kv-2) — [canonical design](../design/kv-cache.md). **Learning mode:** Build. **Authorship target:** learner-authored; gathered oracle fixtures supplied.

**Dependencies:** [KV-01](memory-cache.md#kv-01), [MOD-02](model.md#mod-02).

**Teaching:** [06](../curriculum/runtime.md#module-06).

**Planned change boundary:** `src/inferstack/engine/memory/block_table.py`, `src/inferstack/backends/torch_reference/paged_attention.py`, `tests/memory/test_paging.py`

**Work:**

- [ ] Map logical token positions to physical page/slot and implement append/fork including shared partial-tail COW.
- [ ] Select one supported page size through OQ-03; implement gathered attention as a correctness oracle and compare contiguous/paged capacity.

**Validation / acceptance:**

- [ ] Random append/fork/free preserves values and conservation across page boundaries.
- [ ] Teacher-forced results match contiguous reference; gathered timing is not reported as a fast GPU paged backend.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="kv-03"></a>
## KV-03 — Block-hash prefix index

**Status:** planned. **Package:** E. **Milestone:** CP2.

**Requirement/design:** [CACHE-1](../design/kv-cache.md#cache-1) / [CACHE-2](../design/kv-cache.md#cache-2) — [canonical design](../design/kv-cache.md). **Learning mode:** Build. **Authorship target:** learner-authored.

**Dependencies:** [KV-02](memory-cache.md#kv-02).

**Teaching:** [09](../curriculum/prefix-caching.md#module-09).

**Planned change boundary:** `src/inferstack/engine/prefix/interface.py`, `src/inferstack/engine/prefix/hash_index.py`, `tests/memory/test_prefix_identity.py`

**Work:**

- [ ] Implement chained prefix identity, match/acquire, completed full-page publication and safe cache-owned eviction.
- [ ] Preserve trusted namespace/model/adapter/tokenizer context; handle full-prompt hits by obtaining final logits correctly.

**Validation / acceptance:**

- [ ] Same block under another parent/identity misses; shared active pages cannot be reclaimed by eviction.
- [ ] Cold/warm fixture reports usable reused tokens, not only hit requests; cache-on/off and full-hit logits checks pass without modifying shared cached pages.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.

<a id="kv-04"></a>
## KV-04 — Radix index and controlled comparison

**Status:** planned. **Package:** E. **Milestone:** CP2.

**Requirement/design:** [CACHE-2](../design/kv-cache.md#cache-2) — [canonical design](../design/kv-cache.md). **Learning mode:** Build or Modify with attribution. **Authorship target:** learner-authored or meaningfully modified reference.

**Dependencies:** [KV-03](memory-cache.md#kv-03).

**Teaching:** [10](../curriculum/prefix-caching.md#module-10).

**Planned change boundary:** `src/inferstack/engine/prefix/radix_index.py`, `tests/memory/test_radix_transitions.py`

**Work:**

- [ ] Implement compressed-edge match/insert/split/lock/evict using the same page pool and contract; document locks-to-leases mapping.
- [ ] Compare indexes at matched page size, memory, scheduler and eviction eligibility before changing scheduling policy.

**Validation / acceptance:**

- [ ] Adversarial split/evict and randomized sequences preserve pages and reusable token identity.
- [ ] Report lookup overhead, reused tokens, eviction/recompute and limitations; do not assume branching implies radix superiority.

**Completion evidence:** record actual commands, environment/revisions, raw outcome or test results, authorship, limitations and learner explanation. Evidence is pending; keep this task planned until work begins.
