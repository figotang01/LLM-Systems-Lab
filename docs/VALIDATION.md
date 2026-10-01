# Current delivery and handoff review — 2026-09-30

[Start here](../README.md) · [Handoff procedure](HANDOFF.md) · [Original scope audit](archive/scope-map.md) · [Agent coverage](../tracks/agents/COVERAGE.md)

**Implemented:** supplied experiment/budget tooling, the offline documentation checker and their tests. **Delivered:** one historical orientation HTML, system/task documentation and teaching blueprints. Inference runtime, agent application, training runs, deployments, executable project lessons and new HTML remain planned. The CPU GitHub workflow is supplied configuration; a hosted run has not been verified.

## Review verdict

The workspace is ready for another agent to start a bounded teaching or implementation task. It is not a frozen specification for automatically implementing the whole project. Exact APIs, environment pins, hardware-dependent behavior and later lesson details are resolved at the owning task, with explicit decisions and independent evidence.

The review found four material handoff gaps and addressed them:

| Gap | Improvement |
|---|---|
| Inference material mixed into shared directories | Moved 27 existing documents into the inference track; both tracks now own their detailed material |
| New agents lacked a concise entry procedure | Added root AGENTS.md and one shared handoff guide covering read order, task selection, teaching/implementation modes and resumption |
| First tasks and important examples left too much implicit | Added bounded FND-01/AGT-01 startup sequences, a contract trace, a private-verifier workspace seed, a six-iteration scheduler oracle and a numerical metric fixture |
| Local checks/history were not portable to GitHub | Added a repeatable offline checker with meaningful tests, supplied CPU CI, and removed active links requiring the ignored local ZIP |

Shared endpoint/trace responsibilities now live in one [track contract](system/track-contracts.md). Existing source/package boundaries remain unchanged. No new inference/agent placeholder forest was created, and no project scope or learner-hour allocation was added by supplying repository-maintenance tools or refining existing tasks.

## Preservation

Checks compared the pre-handoff workspace with the reorganized content:

| Check | Result |
|---|---|
| Original scope | All 64 A–J item IDs/locators and 26 named technical topics retained |
| Tasks | 43 inference and 14 agent task owners; all existing work/acceptance checklist bullets unchanged after normalizing link destinations |
| Task graph | Acyclic; no mandatory implementation edge crosses tracks; legacy APP/AG aliases remain in agent owners |
| Teaching | All 36 original module/bridge/supplement IDs and 16 AT units retained; worked examples refine existing allocations |
| Course map | All 30 recorded schedule slots remain, with assignment objectives and material-review uncertainty explicit |
| Planned code | All 128 pre-handoff inventory entries retained, including the original 88 responsibilities and their twelve application relocations |
| References | All 112 pre-handoff catalog URLs retained, including the earlier 73-source inventory |
| Protected artifacts | Existing starter code/tests, orientation HTML, frozen archive texts/checksums and local recovery ZIP remain unchanged in this handoff |
| Navigation | Active Markdown local links/anchors pass; frozen historical layouts are excluded |

The earlier extraction deliberately replaced obsolete application dependencies in BEN-04, ADV-02 and REL-02 with standalone fixtures and separate live-quality ownership. Those decisions remain. Required B2 study remains independently completable; full SFT/RL is additional required agent work. Development feedback stays separate from the sealed capstone test set, and unknown tool outcomes remain distinct from failure.

Historical accounting remains **528 hours** (318 through December, 210 January–April); the separately approved 280–400-hour expansion gives **808–928 total**. The shared working allocation remains **$600 within $500–700**. Supplied repository checks are not new learner work packages.

## Executed checks and limits

- `python3 tools/check_docs.py` — passed local navigation, 57 task owners, dependency graphs and required scope IDs.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` — **14 tests passed**: eight existing starter tests and six tests for the documentation checker.
- A clean-copy rehearsal excluded local recovery ZIPs, résumés, caches, secrets and run/checkpoint directories; documentation checks and all 14 tests passed there too. This was a local export simulation, not an actual GitHub clone or hosted Actions result.
- Direct preservation comparisons confirmed unchanged original task checklists, source inventories, reference URLs and protected artifact hashes. Hand calculations checked the supplied scheduler counters, metric example and synthetic agent-fixture arithmetic.

Checks ran locally on Python 3.14.2. The supplied CI selects Python 3.12 for these standard-library utilities; its hosted environment remains unverified. That CI choice does not pin the future PyTorch/CUDA/agent-training environments. The checker covers this repository's inline Markdown links and task-field conventions, not every Markdown extension or the truth of technical claims. It does not prove learner understanding, model quality, GPU compatibility or performance.

## GitHub and history

Declared repository: [figotang01/LLM-Systems-Lab](https://github.com/figotang01/LLM-Systems-Lab). The local workspace is not a Git checkout. Remote inspection failed through the browser and local Git network lookup, so no claim is made about remote visibility, branches, contents or synchronization. No commit, push or cloud operation was performed.

The optional local `docs/archive/pre-simplification-2026-09-29.zip` retains 179 project files from the older layout after the previous user-requested résumé removal. It is ignored by Git and unnecessary for a clean checkout. Frozen Markdown preserves historical wording; the current scope map and track documents govern work. No résumé file is stored in the current workspace or recovery ZIP.

## Remaining task-level detail

Software/model/template pins, exact Python interfaces, persistence/reconciliation adapters, fixture manifests, mask/reward implementations and real hardware fit remain implementation deliverables. January platform work and advanced distributed labs need topology-specific detail before their runs. Later CMU materials not inspected in the earlier review require an availability/content check under the [course update rule](../tracks/agents/COVERAGE.md#course-update-rule); absence from the review is not proof of non-publication.

The current orientation HTML still describes the older baseline; read the project overview/roadmap first. No new HTML lessons were authored here. Full agent and inference implementation remains ahead, with initial CPU-first entry through [FND-01](../tracks/inference/tasks/model.md#fnd-01-startup-sequence) or [AGT-01](../tracks/agents/ROADMAP.md#agt-01-startup-sequence).
