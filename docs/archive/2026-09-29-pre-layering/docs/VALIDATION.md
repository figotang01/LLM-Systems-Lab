# Delivery validation — 2026-09-28

This is validation of the planning/teaching delivery, not of a completed inference stack.

- Original `PROJECT_PLAN.md` copied verbatim before revision to `docs/archive/PROJECT_PLAN_v2.md`; 1,233 lines retained.
- Current plan’s package budgets sum to 496 learner hours; fall calendar sums to 286 and spring to 210.
- Local Markdown/HTML delivery links checked; HTML element IDs unique.
- `python3 -m unittest discover -s tests -v`: **8 tests passed** (budget units/substitution/invalid inputs, artifact snapshots and empty-results status).
- Both starter CLI examples executed successfully in temporary output directories. Budget result: 120 node-hours, 150 GPU-hours, $280.15 before tax.
- HTML JavaScript passed `node --check`.
- Local headless Chrome checked all 25 slides at 1440×1100 and 390×844: no horizontal page overflow. Navigation boundaries, slide selection, reading view, note reveal, default/modified KV calculation, invalid KV input and default cost calculation passed.
- Cover and desktop/mobile calculator screenshots visually inspected. Long content/notes intentionally scroll; this is a study deck with a separate reading view.

The in-app browser execution tool was unavailable; browser QA used an isolated temporary headless Chrome profile. No user browser profile was used. No GPU was rented, model executed, production stack deployed, cloud account modified or benchmark result fabricated. Later lesson modules and their runtime/platform scaffolds remain planned; lesson 00 and starter tooling are delivered.

## Append-only planning delivery — 2026-09-29

Delivered the [complete earlier December skeleton](DECEMBER_SKELETON.md) as a baseline planning document and the [production-framework/CMU agent supplements](PLAN_ADDITIONS.md) as additive handoff specifications. Appended cross-references and combined-hour accounting to the project plan and curriculum. This section is also appended; the original validation record above remains intact.

### Preservation evidence

Before editing, captured all 12 existing non-cache/non-`.DS_Store` files in a checksum manifest and saved the three documents receiving appends. Compared existing content after editing with those snapshots. The original project plan and curriculum are exact byte prefixes of their updated files:

| File | Preserved original bytes | SHA-256 of preserved original prefix |
|---|---:|---|
| `PROJECT_PLAN.md` | 49,784 | `bb99089ab6f730cfffd7745e3e3a183be808dc61ee383bbe9b4804dc9e618df0` |
| `teaching/CURRICULUM.md` | 27,858 | `5679c18b065e1aaf7abacefbc31e31edb6562064bb786198125b6ce6a462592a` |

These prefix lengths and hashes let a later reviewer recheck preservation without relying on the temporary snapshots. No existing file was deleted. The nine original files outside the three appended documents remain byte-for-byte unchanged, including the archived v2 plan, original HTML lesson, starter code/configuration, tests, and existing resume artifact. The only new repository files are the two Markdown documents linked above.

### Checks and limits

- Baseline curriculum still contains modules **00–24** and bridge entries **B1–B6**.
- The preserved detailed skeleton's module 01–17 allocations sum to **286 h**.
- PF-1–PF-4 sum to **8 + 4 + 8 + 4 = 24 h**; AG-1a–AG-1c sum to **2 + 3 + 3 = 8 h**.
- Combined accounting: **286 + 32 = 318 h** through December; **210 h** January–April unchanged; **496 + 32 = 528 h** overall. Original allocations were not reassigned.
- Local Markdown file links in the modified/new planning documents resolve. External sources retain the references inspected during the preceding planning discussion; no new compatibility or benchmark claim was validated here.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`: **8 tests passed**. No new tests were added for this documentation change.
- Runtime implementations, interface stub files, individual lesson/storyboard files, new HTML slides, GPU experiments, Kubernetes deployments, paid services, and upstream modifications remain deferred. No inference performance or interview-readiness result is claimed.
