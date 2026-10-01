# Advanced labs, bridge topics and capstone

[Curriculum](../../../teaching/CURRICULUM.md) · [Teaching contract](../../../teaching/CONTRACT.md) · [Roadmap](../../../docs/execution/roadmap.md)

This guide groups existing module blueprints. Read only the module assigned by your current task. Module IDs, hours, objectives, exercises and exit gates are unchanged; HTML and runnable labs remain planned except the existing orientation.

Use the teaching contract for independent oracles, numerical/state examples, the explain/trace/predict/implement/measure rubric and one-week/one-month retrieval checks. Task briefs own implementation acceptance and authorship.

- [20 — Speculation as an exact probabilistic algorithm (H)](#module-20)
- [21 — Quantization with quality gates (H)](#module-21)
- [22 — Collectives, TP and expert parallelism (H)](#module-22)
- [23 — Disaggregated prefill/decode (H)](#module-23)
- [24 — Capstone, statistical argument and reproduction (I + J)](#module-24)
- [B1 — advanced kernels/compilers](#module-b1)
- [B2 — training and rollout systems](../../agents/CURRICULUM.md#module-b2)
- [B3 — nonstandard attention](#module-b3)
- [B4 — multimodal](#module-b4)
- [B5 — alternative accelerators](#module-b5)
- [B6 — routing languages and control planes](#module-b6)

<a id="module-20"></a>
## 20 — Speculation as an exact probabilistic algorithm (H)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** Within H 54 h (~10 h speculation). Hours are owned by the roadmap.

**Concept prerequisites:** [08](runtime.md#module-08), [13](gpu-serving.md#module-13). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** prove the acceptance rule, understand proposer economics and preserve cache state.
- **Slides 1–12:** sequential decoding, draft/verify, exact categorical example, acceptance and residual distribution. **13–24:** bonus token, rejection rollback, EOS, greedy vs stochastic equivalence. **25–38:** n-gram, draft-target, EAGLE/MTP/DFlash families; load-dependent break-even.
- **Code:** learner small verifier/ngram proposal; supplied draft-worker plumbing and supported serving recipe. Explain SpecForge/drafter training without requiring it.
- **Experiment/exit:** exact small probability checks, statistical output check, then off/on at low/high load. Do not compare same-seed trajectories as the correctness proof.

### Implementation connections

- [ADV-01](../tasks/advanced-release.md#adv-01) — Speculation verifier and supported proposer; Build + Operate + Explain.

**Design context:** [advanced-labs](../design/advanced-labs.md).

<a id="module-21"></a>
## 21 — Quantization with quality gates (H)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** Within H 54 h (~12 h quantization). Hours are owned by the roadmap.

**Concept prerequisites:** [05](runtime.md#module-05), [13](gpu-serving.md#module-13). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** distinguish storage formats, compute kernels and error controls.
- **Slides 1–10:** scales/zero points, symmetric/asymmetric, channel/group granularity, error. **11–24:** GPTQ/AWQ/SmoothQuant, calibration and leakage, W4A16 vs W8A8 and KV quantization. **25–38:** FP8/FP4 variants and hardware support, dequant overhead, quality-memory-latency Pareto.
- **Code:** learner groupwise INT8 reference; supplied LLM Compressor/evaluation scripts and fixed calibration/held-out split.
- **Experiment/exit:** one real compressed checkpoint plus a KV precision ablation; unsupported formats get a numerical exercise and a clearly limited claim.
- **References:** MIT efficient-AI quantization/deployment, vLLM support matrix, papers in v2.

### Implementation connections

- [ADV-02](../tasks/advanced-release.md#adv-02) — Quantization with quality gates; Build + Operate.

**Design context:** [advanced-labs](../design/advanced-labs.md).

<a id="module-22"></a>
## 22 — Collectives, TP and expert parallelism (H)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** Within H 54 h (~12 h collectives/EP). Hours are owned by the roadmap.

**Concept prerequisites:** [02](foundations.md#module-02), [13](gpu-serving.md#module-13). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** derive row/column shards, communication bytes and MoE dispatch/combine; compare with training parallelism.
- **Session A:** DP/PP/TP, FSDP/ZeRO memory bridge, rank groups, NCCL/MPI, ring traffic, two-rank algebra, shard loading and GQA caveats. **Session B:** MoE total/active parameters, expert routing/skew, all-to-all, DP-attention, DeepEP/EPLB and topology.
- **Code:** supplied launchers/sharded loader; learner two-rank linear/transformer block and toy expert dispatcher; production TP/EP configuration only when supported.
- **Experiment/exit:** TP=1 vs 2 at equal model/settings with topology recorded; explain a slowdown. Tiny MoE lab remains possible when production EP is unavailable.

### Implementation connections

- [ADV-03](../tasks/advanced-release.md#adv-03) — Collectives, tensor and expert parallelism; Build + Modify + Operate.

**Design context:** [advanced-labs](../design/advanced-labs.md).

<a id="module-23"></a>
## 23 — Disaggregated prefill/decode (H)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** Within H 54 h (~12 h P/D). Hours are owned by the roadmap.

**Concept prerequisites:** [17](platform.md#module-17), [22](advanced.md#module-22). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** account for transfer and compare capacity fairly.
- **Slides 1–10:** interference and separate SLOs, P:D ratio. **11–22:** KV layout/transport, NIXL/Mooncake, staging/overlap, ownership and failure. **23–34:** transfer/recompute model, break-even conditions, equal-GPU baselines and queueing.
- **Code:** supplied transport/connector/routers and transfer driver; learner analytical model plus validation from measured bandwidth.
- **Experiment/exit:** 1P1D vs two colocated replicas; no claimed advantage that merely comes from giving one system an extra GPU.

### Implementation connections

- [ADV-04](../tasks/advanced-release.md#adv-04) — Prefill/decode transfer and fair comparison; Operate + Build analysis.

**Design context:** [advanced-labs](../design/advanced-labs.md).

<a id="module-24"></a>
## 24 — Capstone, statistical argument and reproduction (I + J)

**Status:** Blueprint delivered; HTML, exercises, implementations and validation are planned.

**Allocation:** Within I/J; no additional hours. Hours are owned by the roadmap.

**Concept prerequisites:** [15](../../agents/CURRICULUM.md#module-15), [19](platform.md#module-19). The linked tasks own implementation dependencies; conceptual lesson order is not an extra code dependency.

### Teaching blueprint

- **Objectives:** make a bounded causal claim with trustworthy uncertainty and honest provenance.
- **Slides 1–10:** hypothesis, primary metric, workload/popularity/dependency design. **11–22:** paired configurations, whole-session resampling, tails, errors and cost. **23–36:** explain profiles, falsify alternative causes, negative results, version/artifact bundle and portfolio claim levels.
- **Code:** supplied plot/report template; learner experiment design, analysis and interpretation. Start with 36 primary runs, not a huge Cartesian product.
- **Exit:** a stranger can reproduce one main figure; oral defense connects routing, queue, KV and session behavior. No required positive result or upstream merge.

### Implementation connections

- [REL-02](../tasks/advanced-release.md#rel-02) — Capstone experiment and report; Build experiments + Explain.
- [REL-03](../tasks/advanced-release.md#rel-03) — Clean reproduction, regression policy and release; Build policies + Explain.

**Design context:** [ownership](../../../docs/engineering/ownership.md), [capstone](../CAPSTONE.md).

<a id="module-b1"></a>
## B1 — advanced kernels/compilers

**Status:** planned lesson/exercise; blueprint delivered. **Allocation:** approximately four learner hours within J, not an extra package. **Mode:** Modify / Explain, with a real run only where explicitly required.

### Teaching scope

Tiled matmul, tensor cores, warp specialization, FlashAttention generations, TVM/TIRx and mega-kernel annotated examples

### Required evidence

Modify tile parameter; compare IO/occupancy predictions to one profile

Use 10–18 slides, an annotated code/profile artifact, one modification/calculation and a teach-back. Supplied traces/numerical examples are acceptable for unavailable hardware, with studied versus operated status stated. No fabricated GPU measurement.

### Connections and bounds

Implementation/release task: [REL-01](../tasks/advanced-release.md#rel-01). Optional deeper extensions stay in the advanced-scope document and are not required to finish this capsule. Corpus/model/artifact versioning, SQL, leakage and IaC recur in the baseline; they do not form an additional unbudgeted project.

## Training bridge ownership

B2's complete four-hour blueprint and original exercises now live in the [canonical agent curriculum](../../agents/CURRICULUM.md#module-b2). Inference REL-01 may complete that capsule independently of full agent SFT/RL. Its original J allocation is preserved once; the expanded course/training is additional work.

<a id="module-b3"></a>
## B3 — nonstandard attention

**Status:** planned lesson/exercise; blueprint delivered. **Allocation:** approximately four learner hours within J, not an extra package. **Mode:** Modify / Explain, with a real run only where explicitly required.

### Teaching scope

MLA latent, sliding window, hybrid recurrent/Gated DeltaNet/Mamba state examples

### Required evidence

Checkpoint/restore a tiny recurrence; explain prefix reuse constraints and state size

Use 10–18 slides, an annotated code/profile artifact, one modification/calculation and a teach-back. Supplied traces/numerical examples are acceptable for unavailable hardware, with studied versus operated status stated. No fabricated GPU measurement.

### Connections and bounds

Implementation/release task: [REL-01](../tasks/advanced-release.md#rel-01). Optional deeper extensions stay in the advanced-scope document and are not required to finish this capsule. Corpus/model/artifact versioning, SQL, leakage and IaC recur in the baseline; they do not form an additional unbudgeted project.

<a id="module-b4"></a>
## B4 — multimodal

**Status:** planned lesson/exercise; blueprint delivered. **Allocation:** approximately four learner hours within J, not an extra package. **Mode:** Modify / Explain, with a real run only where explicitly required.

### Teaching scope

Supplied VLM encoder/prefill/decode example, image identity and encoder-cache trace

### Required evidence

Identify encoder vs language cost and an invalid image-cache hit

Use 10–18 slides, an annotated code/profile artifact, one modification/calculation and a teach-back. Supplied traces/numerical examples are acceptable for unavailable hardware, with studied versus operated status stated. No fabricated GPU measurement.

### Connections and bounds

Implementation/release task: [REL-01](../tasks/advanced-release.md#rel-01). Optional deeper extensions stay in the advanced-scope document and are not required to finish this capsule. Corpus/model/artifact versioning, SQL, leakage and IaC recur in the baseline; they do not form an additional unbudgeted project.

<a id="module-b5"></a>
## B5 — alternative accelerators

**Status:** planned lesson/exercise; blueprint delivered. **Allocation:** approximately four learner hours within J, not an extra package. **Mode:** Modify / Explain, with a real run only where explicitly required.

### Teaching scope

Local MLX example, vllm-metal architecture, supplied JAX/TPU layout sample

### Required evidence

Run local code and compare layouts; separate Mac performance from NVIDIA results

Use 10–18 slides, an annotated code/profile artifact, one modification/calculation and a teach-back. Supplied traces/numerical examples are acceptable for unavailable hardware, with studied versus operated status stated. No fabricated GPU measurement.

### Connections and bounds

Implementation/release task: [REL-01](../tasks/advanced-release.md#rel-01). Optional deeper extensions stay in the advanced-scope document and are not required to finish this capsule. Corpus/model/artifact versioning, SQL, leakage and IaC recur in the baseline; they do not form an additional unbudgeted project.

<a id="module-b6"></a>
## B6 — routing languages and control planes

**Status:** planned lesson/exercise; blueprint delivered. **Allocation:** approximately four learner hours within J, not an extra package. **Mode:** Modify / Explain, with a real run only where explicitly required.

### Teaching scope

Supplied small Rust load selector; SGLang gateway/Dynamo/KServe map; DRA, KAI/Grove examples

### Required evidence

Modify Rust selection/tie handling; explain who allocates GPUs, picks an endpoint and moves KV

Use 10–18 slides, an annotated code/profile artifact, one modification/calculation and a teach-back. Supplied traces/numerical examples are acceptable for unavailable hardware, with studied versus operated status stated. No fabricated GPU measurement.

### Connections and bounds

Implementation/release task: [REL-01](../tasks/advanced-release.md#rel-01). Optional deeper extensions stay in the advanced-scope document and are not required to finish this capsule. Corpus/model/artifact versioning, SQL, leakage and IaC recur in the baseline; they do not form an additional unbudgeted project.

<a id="long-context-foundations"></a>
## Shared long-context foundations — required CMU coverage

Canonical owner: inference/model teaching; required reader: agent AT-03. This extension does not add support for another model architecture to the custom runtime. The original B3 four-hour recurrence/cache exercise remains unchanged; additional explanation/exercises are funded by the new agent-scope estimate, not squeezed into those four hours.

Prerequisite: [numerical diagnostic](foundations.md#module-01), [dense model](runtime.md#module-04) and [memory accounting](runtime.md#module-05) concepts. Study does not require their full code implementation.

**Storyboard:** prefill/decode and effective context → global versus sliding-window/sparse access → linear attention and DeltaNet/Gated DeltaNet/Kimi Delta Attention state → MLA latent compression and hybrid/Mamba state → RoPE versus NoPE → position interpolation/YaRN and short-to-long training/data → context parallelism → paged/prefix caching and routing → application context policy.

**Worked examples:** count a sliding window's visible positions on an eight-token sequence; trace a two-dimensional linear/delta recurrent state update and its checkpoint/restore; map extended positions to a shorter training range and explain why interpolation changes frequencies/context behavior. Compute KV versus latent/recurrent-state bytes under stated shapes. Draw context shards and identify communication rather than claiming free scaling.

**Failures:** advertised context mistaken for useful retrieval; recurrent state treated like append-only KV; invalid state/prefix reuse; position extension applied without matching training/configuration; sparse attention assumed equivalent to dense attention. Independent numerical traces and source diagrams are acceptable evidence for this conceptual extension, not measured throughput.

**Handoff:** explain each mechanism and predict a failure, then connect to [AT-03 compaction/continuation](../../agents/CURRICULUM.md#at-03). The source [CMU context lecture](https://www.cmu-agents.com/slides/lecture-03-long-context.pdf) governs required breadth. Existing kernel/collective labs own physical execution details; do not create another attention implementation in agent_lab.
