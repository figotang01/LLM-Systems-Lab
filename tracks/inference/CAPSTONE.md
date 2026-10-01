# Capstone experiment — package I, 36 h

**Primary question:** On two replicas, when does a load-guarded prefix-affinity router improve multi-turn session completion time, and when does cache locality create queue imbalance?

- [ ] Pre-register one primary metric (p95 session completion), secondary metrics (per-turn TTFT, successful-session goodput, fairness, cost), workload mix and SLOs.
- [ ] Primary experiment: one production engine × three routing policies × two load levels × two locality levels × three repetitions = **36 runs**. Choose load relative to measured saturation and use the same offered load across policies.
- [ ] At five measured minutes/run that is three measured node-hours before warmups, cache preparation, failures and profiling; use pilots to set the actual duration/sample count.
- [ ] Add one selected offload interaction and one second-engine cross-check only if the primary study is sound and time remains. Hash/radix attribution belongs to the controlled own-engine experiment, not a vLLM-vs-SGLang product comparison.
- [ ] Use held-out sessions and a popularity-skew or stale-metric stress case; report a negative result if affinity loses.
- [ ] For completion-time claims use dependency-aware replay. The original small live-agent quality/tool check remains required under [agent AGT-04](../agents/ROADMAP.md#agt-04); link its independent report when available without blocking this routing study.
- [ ] Write one coherent report, four useful plots and an artifact bundle. Novel algorithmic superiority is not a graduation requirement.

## Design-to-evidence chain

Goal G5 → platform requirements ROUTE-1/ROUTE-2 → [platform implementation](tasks/platform.md) → [release task REL-02](tasks/advanced-release.md#rel-02) → CP4.

The [measurement/replay contract](engineering/measurement.md) owns all timing, denominators, replay modes, and uncertainty rules. The [agent learning design](../agents/LEARNING.md) owns live task-quality evaluation. Supplied self-contained SessionTrace fixtures satisfy this experiment's input contract; a live agent application is not a prerequisite. Keep those definitions linked rather than redefining them in an experiment script.

## Run protocol

1. Validate the selected same-model pool and backend contract; finish a saturation pilot before fixing the two offered-load levels.
2. Freeze the hypothesis, SLO eligibility rules, held-out session set, cache reset/reuse policy, hardware/cost accounting, configuration and order-randomization plan.
3. Run the declared 36-cell/repetition matrix, retaining errors and incomplete sessions. Add duration/repetitions only when sample support warrants it; never quietly omit a losing configuration.
4. Diagnose one apparent benefit or regression with traces/profiles outside headline timing. Test popularity skew or stale metrics as specified above.
5. Separate replay results from any linked agent quality report; absence of that report prevents agent-quality claims, not completion of the routing experiment. Report uncertainty at session/run granularity and limits of simulated versus physical deployment.

Expected report figures: offered load versus successful-session goodput; session-completion latency by policy/locality; cache reuse versus queue imbalance; cost with failure accounting. These are figure specifications, not invented data. Final plots link to raw bundles, provenance, and analysis commands. A reproducible negative result is acceptable.
