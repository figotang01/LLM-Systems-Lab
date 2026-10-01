# Historical plans and migration map

[Current overview](../../PROJECT_PLAN.md) · [Documentation index](../../README.md) · [Scope coverage](scope-map.md)

The current layered documentation preserves the approved v3 plan, first detailed skeleton and PF/AG additions, then integrates the approved two-track expansion. The restructuring request superseded the previous append-only *editing restriction*; it did not authorize scope deletion. The later full-CMU agent expansion explicitly adds scope. Historical planning texts remain intact here; the ZIP has the explicit résumé-removal exception documented below.

## Snapshots

- [Original v2](PROJECT_PLAN_v2.md): concept catalog and historical ambitions. Its deadlines, cut-order, exactness claims and mandatory expansions were superseded by v3; retain its readings and optional extensions as mapped in current scope.
- [Pre-layering project plan](2026-09-29-pre-layering/PROJECT_PLAN.md): v3 plus approved append-only additions.
- [Pre-layering detailed skeleton](2026-09-29-pre-layering/docs/DECEMBER_SKELETON.md): first complete code/teaching blueprint.
- [Pre-layering additions](2026-09-29-pre-layering/docs/PLAN_ADDITIONS.md): detailed PF/AG handoffs.
- [Pre-layering curriculum](2026-09-29-pre-layering/teaching/CURRICULUM.md): all 25 modules, six bridges and added blueprints.
- [Prior design review](2026-09-29-pre-layering/docs/PLAN_REVIEW.md): research and correction rationale.
- [Prior validation record](2026-09-29-pre-layering/docs/VALIDATION.md): earlier checks, dates and limits.
- [Snapshot checksum manifest](2026-09-29-pre-layering/manifest.json): exact archived bytes and hashes.
- [Unchanged artifact checksums](2026-09-29-pre-layering/unchanged-artifacts.sha256): original starter, tests, lesson, résumé and v2 hashes recorded before simplification; paths are relative to the repository root. The lesson now has one repaired review link, so its current hash differs. The résumé was subsequently removed from the workspace at the user’s request; its historical hash is provenance only.

Frozen documents retain their original relative links, branding and assertions for historical fidelity. Some links assumed the old repository layout or refer to planned files; use this index and the root README for current reading. Do not repair archives by silently rewriting them.

## Where current content lives

| Old source | Current canonical home |
|---|---|
| Plan §§1–3, 12 | Overview for goals; ownership, roadmap and task evidence for detailed execution |
| Plan §4 coverage | Scope map, subsystem designs, advanced scope and individual teaching blueprints |
| Plan §5 A–J calendar/checklists | Roadmap and linked subsystem task briefs |
| Plan §6 and December skeleton architecture | System architecture, design documents and source-header inventory |
| Plan §§7–8 | Correctness and measurement/replay methodology |
| Plan §9 | Resources and historical cost scenarios |
| Plan §§10–11, curriculum | Teaching contract, module blueprints, roadmap recovery rules |
| Supplements / plan §13 | Framework tasks and AG workload tasks; roadmap combined accounting |
| Design review | Current design constraints and reference map; historical review preserved above |
| Validation | Current status/checks, with prior reports linked rather than repeated |

The original accounting remains 286 + 32 = 318 hours through December and 210 in January–April, totaling 528. It is now the historical baseline within the approved 808–928-hour expanded project. The additional 280–400 agent hours are recorded separately in the [sole effort ledger](../execution/roadmap.md#agent-expansion); moving old requirements between tracks does not add hours.

## Workspace simplification

`docs/archive/pre-simplification-2026-09-29.zip` (optional local recovery copy, excluded from Git) retains 179 project files from the preceding 180-file layout. At the user’s request, its résumé copy was removed along with the active `resume/` directory. Every retained ZIP entry was verified byte-for-byte unchanged; the ZIP container itself consequently has a new hash. It includes the removed comment-only source files and separate lesson READMEs. Extract into a separate directory if needed; do not overwrite the current workspace just to read history.

The current [scope audit](scope-map.md) is retained here for reference, outside the daily reading path. Teaching now uses seven inference topic guides and one canonical [agent curriculum](../../tracks/agents/CURRICULUM.md), under the shared contract. Proposed paths live in the [code map](../system/code-map.md). The three superseded active workload documents were consolidated into the six [agent documents](../../tracks/agents/README.md); their preceding contents also remain in the ZIP. Old pointer documents and the second documentation index remain removed.

## Reading history from a fresh clone

The optional ZIP is local recovery material and is deliberately ignored by Git. Its absence does not block learning, validation or implementation. Versioned historical Markdown and the scope map retain planning provenance; frozen links may reflect the old layout. The current track documents and shared handoff are authoritative.
