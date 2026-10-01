# Ownership, assistance, status, and evidence

[Index](../../README.md) · [Tasks](../../tracks/inference/tasks/README.md)

## Learning modes

Use four learning modes:

| Mode | Your responsibility | What can be provided |
|---|---|---|
| **Build** | Design and implement the mechanism; defend invariants and measure it | Interfaces, fixtures, hints, independent correctness checks |
| **Modify** | Explain supplied code, make a substantive change, test it | Complete baseline and integration glue |
| **Operate** | Deploy, configure, measure, break and diagnose a real implementation | Versioned launch scripts and manifests |
| **Explain** | Derive the mechanism and solve a concrete exercise | Annotated reference, small executable example or recorded profile |

“Provided” means lower value to reimplement **for this project**, not unimportant engineering. Reading supplied code alone does not earn an implementation claim. For every supplied component, trace one request, change one behavior, and explain one failure. Keep authorship in the README: learner-authored, adapted, or supplied.

## Status is distinct from authorship

| Dimension | Values and meaning |
|---|---|
| Implementation status | planned; in progress; blocked with reason; implemented with validation evidence |
| Authorship | learner-authored; learner-modified; supplied/scaffolded; mixed with per-component attribution |
| Scope | required; optional extension; deferred to a named later milestone |
| Validation | not run; passed on specified environment; failed with reproduction; unavailable with reason |

A comment-only file is **planned**, not implemented or usable scaffolding. A supplied working component can be implemented without earning learner-authored credit. A documentation blueprint is delivered documentation, not a delivered lesson or runtime. Optional and deferred describe scope/timing, not successful execution.

Current artifact status lives in [validation](../VALIDATION.md); individual implementation status lives in each task brief. Do not infer completion from directory existence, a dependency being installed, a proposed résumé bullet, or a test file containing only comments.

## Assistance and learning workflow

Write a small design/state trace before agent-assisted core implementation. After assistance, inspect the diff, predict a failure, run an independent oracle, explain every relevant line, and reconstruct a small mechanism without assistance. Supply loaders, transport, SDK wrappers, build machinery, charts, collectors, launch recipes, and plotting rather than repeating previously learned infrastructure work.

After 60–90 minutes blocked on boilerplate, use an attributed reference and complete a substantive modification/debugging exercise. Reading supplied code alone is insufficient. Preserve provenance and license/course-use constraints; do not publish prohibited course solutions. CMU 11-768 is now the explicit exception: all published syllabus topics and integrated assignment/research objectives are required. Other reference courses remain at their selected depths; adapting CMU exercises does not claim completion of its original assignments.

Keep core mechanisms in the production package; teaching examples are small and focused. Production modules must never import teaching reference solutions. A reference-assisted radix implementation remains permitted under the approved recovery rules, with honest attribution and the original learning gates intact.

## Completion record

For every completed task record implementation paths/commit or patch checksum, ownership, exact commands/environment, independent checks, observed outcomes, limitations, and a learner explanation. CPU simulation, source reading, and real GPU operation earn different evidence labels. No positive speedup, broad production-scale claim, or upstream merge is required.

The teaching rubric is canonical in [the teaching contract](../../teaching/CONTRACT.md). Technical defense and source-level development tasks supplement general coding/systems interview preparation; they do not guarantee employment or mastery of a whole production codebase.

Knowledge coverage, implementation and real operation are distinct: a December agent lesson may be explained while its spring SFT/RL task remains planned. Required-but-deferred work stays required; a supplied result cannot close an operated gate. Track-specific task owners retain the sole completion records.
