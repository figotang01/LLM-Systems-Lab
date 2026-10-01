# Open decisions and design maturity

[Index](../../README.md) · [Resources](../execution/resources.md)

Approved scope and invariants do not require a new decision. The choices below were not settled by earlier plans. Proposed defaults are suggestions, not secretly implemented commitments. Resolve a choice in its owning design and task record before dependent integration; continue independent work meanwhile.

| ID | Question / known constraint | Proposed direction or decision procedure | Gate / owner |
|---|---|---|---|
| OQ-01 | Rental/provider and real compatibility; planning budget is resolved | Confirmed $500–700 combined range, $600 working allocation; quote current hardware/node billing and check host privileges before prepared paid runs | FND-01 / AGT-11–13 procurement preflight |
| OQ-02 | Tested model/image/backend/SDK/gateway versions and GPU topology | Start with one dense Qwen3 0.6B or 1.7B revision and a fitting NVIDIA GPU; pin an actual successful compatibility set | BEN-03, GPU-01, PLT-01 |
| OQ-03 | Page size, dtype tolerances, full-hit final-position strategy, graph bucket shapes | Derive from model/backend constraints and tiny reference experiments; do not invent universal tolerances | MOD-02, KV-02/03, GPU-01/03 |
| OQ-04 | Exact scheduler priority, aging bound, chunk sizes, victim selection | Proposed baseline: FCFS admission with decode-sensitive iteration packing and bounded aging; document/tune without changing cancellation invariants | SCH-02/03/04 |
| OQ-05 | Concrete gateway implementation, packaging, observability backend | kind local is approved; choose one supported Gateway/EPP pair and one Helm/Kustomize path; choose Tempo or Jaeger; supplied integration | PLT-01 |
| OQ-06 | Go score normalization, queue guard, freshness/TTL and endpoint epoch signal | Pure policy plus fixtures first; fit units and restart identity to the pinned EPP; December locality is bounded history, explicitly approximate | PLT-02 |
| OQ-07 | Exact public HTTP option subset, finish/error schema and disconnect detection | Use supplied compatibility transport; document supported fields, reject unsupported ones; greedy is the integration baseline | SRV-01/02 |
| OQ-08 | Concrete workspace/cases, model capability, compaction thresholds and independent verifier | Engineering workspace is approved; Qdrant and three original tools retained. AGT-01 fixes fixture manifests/permissions, AGT-02/04 label outcomes, AGT-05 pilots compaction. Keep scoring private | AGT-01–05 |
| OQ-09 | Concrete SGLang patch | Select a bounded state/validation/instrumentation task after source inspection; novel bug discovery is not required | PF-3 |
| OQ-10 | Actual SLO thresholds, two load levels, run duration and uncertainty support | Predeclare after pilot; no arbitrary performance promise; preserve 36-run base design | BEN-03, REL-02 |
| OQ-11 | Actual pace for 808–928 estimated total hours | Both tracks start now, inference prioritized; December RAG/broad knowledge, remaining agents in spring. Review at RAG/harness milestones; record date changes without dropping requirements | Shared roadmap / agent milestones |
| OQ-12 | Tensor container signatures, async completion and fatal GPU failure semantics | Logical contracts are approved; lock concrete types in FND-01 and backend integration. Proposed fatal-device policy is to fail affected work and restart, never recycle unsafe pages | FND-01, GPU-01, SRV-01 |
| OQ-13 | Detailed later CMU decks, Assignment 3 and both guest topics were not captured in the earlier review; current availability needs verification | Required slots and update procedure are in [coverage](../../tracks/agents/COVERAGE.md#course-update-rule); do not invent content or mark it complete | AT-07–15 lesson handoff / AGT-14 |
| OQ-14 | Agent/training SDK, model/template and GPU compatibility pins | Logical boundaries and stack selected; validate each application/training/backend combination with a tiny smoke before a paid experiment | AGT-01/03/06/11–13 |
| OQ-15 | Concrete durable checkpointer backend and tool-outcome reconciliation API | Start with a supported local backend such as SQLite; test crash/concurrency behavior. Use PostgreSQL only if needed. Specify each side-effecting adapter's idempotency/status support | AGT-06 |

## Areas requiring later engineering detail

December designs below specify responsibilities, invariants, task boundaries, and acceptance. They are ready for bounded first tasks; exact vendor adapters and numerical/configuration choices require their listed preflights. January multi-GPU deployment/recovery/offload and February TP/EP/P/D transport need topology-specific designs before implementation. Advanced feature selection and hardware support remain bounded compatibility work, not a promise that every named stack can run.

Full CMU scope, integrated assignments, independent tracks, spring agentic RL and the combined budget are resolved decisions. No new user decision blocks documentation restructuring or CPU-first task preparation. Real paid resource use, incompatible hardware, or a requested deadline beyond the available effort may require input later.
