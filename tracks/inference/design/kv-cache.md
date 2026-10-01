# KV memory, ownership, and prefix caching

[Documentation index](../../../README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Task index](../tasks/README.md)

Status: planned system design; named source paths are reserved in the code map and will be created during implementation.

## Requirements

| ID | Requirement | Goal / evidence |
|---|---|---|
| <a id="kv-1"></a>KV-1 | Conserved page pool with explicit request/cache/in-flight ownership | [G1](../../../PROJECT_PLAN.md#g1); randomized state transitions |
| <a id="kv-2"></a>KV-2 | Correct page tables, append/slot mappings, tails and shared-tail copy-on-write | [G1](../../../PROJECT_PLAN.md#g1); gathered numerical oracle and boundary tests |
| <a id="cache-1"></a>CACHE-1 | Full identity and ancestry prevent incompatible prefix reuse | [G1](../../../PROJECT_PLAN.md#g1); isolation and parent-prefix fixtures |
| <a id="cache-2"></a>CACHE-2 | Hash and radix indexes share pool/page size/eligibility and comparison policy | [G2](../../../PROJECT_PLAN.md#g2); isolated ablations |

## Responsibilities and interface

BlockPool owns physical identifiers, free capacity and refcounts. BlockTable maps a request's logical token pages to physical pages and offsets. BlockLease represents retained ownership; cache nodes or scheduler queues cannot bypass the pool to free pages.

PrefixIndex provides match/acquire, publish, release and evict. It returns reusable token count plus explicit leases, not just a boolean hit. Request-local mutable tails remain outside reusable immutable full-page entries. Hash/radix implementations sit behind this one interface and use the same physical pool; only one indexing strategy is selected per controlled run.

## Page lifecycle and invariants

Free → reserved → successfully written → active/shared and optionally cached → evictable/released → free. These are conceptual states; exact enum/type names are still a contract task. Cache and active membership can overlap: conservation counts distinct physical pages, not a naive sum of active-page and cache-page counts.

- Every non-free page has a reservation, request, cache, or in-flight owner; refcounts never become negative.
- No writer mutates an immutable shared page. Appending into a shared partial page allocates/copies its valid region before mutation.
- Reservation failure rolls back all new ownership before execution; never leave half-updated tables visible.
- Successful device completion precedes publication of reusable writes. Cancellation does not let the allocator recycle a page the device may still read/write.
- Eviction removes cache ownership only when safe; it cannot reclaim a page with remaining request/in-flight references.
- Repeated release/cancel paths must not double-free; invalid handles/stale IDs must be diagnosed by tests.

## Identity and reuse

Cache identity includes model/revision, adapter and trusted namespace, tokenizer/template-relevant input identity, positions and representation constraints. Block hashes chain parent-prefix identity with the current block; identical blocks under different parents are not interchangeable. A caller-chosen salt alone is not authentication.

Cache only completed full pages for the baseline. A full-prompt hit still needs a final-position computation to obtain next-token logits unless a separately designed logits cache exists; no logits cache is required. Do not count unusable matched tokens as executed reuse.

Resolve the exact reusable-token boundary and final-position execution in KV-03 against the chosen backend. Recomputing the last position must not overwrite a shared immutable cache page: the plan must retain read-only ownership and prepare any required writable tail through the same copy-on-write rules. A full-hit fixture must check both logits and unchanged shared-page contents. The precise execution strategy is an implementation decision, not an assumed logits-cache feature.

The radix index must handle compressed-edge match, split/insert, page-aligned reuse, locks and eviction. Node/index bookkeeping does not replace physical-page ownership. The task must specify how node locks translate to leases and how victims obey the common eviction contract before coding. A reference implementation is permitted if necessary, with modification/debugging and honest ownership.

## Comparisons and trade-offs

First hold page size, memory, prompt identity, scheduler and eviction policy constant to compare lookup/index cost and reusable tokens. Then separately compare LPM/cache-aware ordering with aging against FCFS. Branching alone does not imply a radix win; physical paging and prefix indexing solve different problems.

Initial page size is selected from the real backend contract (OQ-03), not inferred from an archived example. Broader block-size sweeps are bounded experiments after correctness. Hash collision assumptions and identity verification must be documented; do not market the educational cache as a hardened multi-tenant security boundary.

## Failure fixtures and implementation

Test allocate/append/fork/release, shared partial tails, pool exhaustion mid-reservation, identical content under different parents/namespaces/adapters, full-prompt hits, radix partial-edge splitting, locked eviction, cancellation around device completion, and reuse after preemption.

[KV-01–KV-04](../tasks/memory-cache.md) turn these requirements into tasks. [Correctness](../engineering/correctness.md) owns oracle/tolerance rules. Acceptance requires random transition conservation and numeric equivalence, plus one matched hash/radix comparison with lookup overhead, reused tokens, recomputation, TTFT, and waiting-time fairness. Reference gather results must not be labeled GPU paged-attention performance.
