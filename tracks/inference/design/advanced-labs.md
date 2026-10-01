# Advanced labs and preserved breadth

[Documentation index](../../../README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Task index](../tasks/README.md)

Status: planned system design; named source paths are reserved in the code map and will be created during implementation.

This document owns the later technical scope; exact hardware-specific implementation designs remain future work. It does not introduce December runtime stubs for unimplemented advanced features. Requirements ADV-1 through ADV-4 support G4; release/capstone requirements support G5.

## Required guided labs — package H, 54 h

| ID | Required artifact | Named coverage and boundary |
|---|---|---|
| <a id="adv-1"></a>ADV-1 | Small rejection verifier, n-gram proposal, rollback tests and one supported production proposer off/on at low/high load | Draft-target; EAGLE-3, MTP, DFlash; SpecForge/distillation explained. Other proposer families remain readings. No required drafter training or full custom-engine integration |
| <a id="adv-2"></a>ADV-2 | Reference groupwise INT8 math; calibration/held-out split; one supported compressed checkpoint and KV precision ablation; quality/memory/latency plot | GPTQ/AWQ/SmoothQuant, FP8, W4A16, FP8 KV, NVFP4/MXFP4, LLM Compressor, lm-eval. Unsupported formats get numerical labs, never invented throughput |
| <a id="adv-3"></a>ADV-3 | Two-rank row/column linear or transformer-block lab, collective profile, token dispatch/combine and skew exercise; production TP=2 and EP when compatible | TP/DP/PP, FSDP/ZeRO, context parallelism, NCCL/MPI, MoE/EP, DP-attention, DeepEP/EPLB. No wide-EP fleet or full TP integration into InferStack |
| <a id="adv-4"></a>ADV-4 | Transfer/cost model, measured transport benchmark and equal-GPU colocated versus 1P1D comparison | NIXL/Mooncake: operate one supported transport and inspect the other. Include staging/overlap/layout/ownership/failure implications |

Approximate H split stays 10 h speculation, 12 h quantization, 12 h collectives/EP, 12 h P/D, 8 h reporting/compatibility. Operate one primary engine per advanced lab and selected second-engine cross-checks; both production baselines remain mandatory. Real execution is required for an operated claim. Unsupported configurations retain conceptual exercises and an explicit pending/limited execution result.

## Mechanism and validation notes

- Speculation: derive acceptance min(1,p/q) and normalized positive residual, bonus token, rejection/EOS rollback and cache ownership. Exact small distributions plus statistical checks validate sampling; equal random seeds do not prove equal distributions. Retain SpecInfer/token-tree, Medusa, suffix/prompt lookup and lookahead methods as explanatory references; tree-attention verification is optional depth from the old catalog.
- Quantization: distinguish weight storage, compute kernels and KV precision; inspect group/scales/zero-points and calibration leakage. GPU ability to store a type does not establish fast arithmetic support. Quality gates use predeclared held-out checks.
- Collectives: derive row/column shard equations and logical versus per-rank/aggregate traffic. Ring all-reduce's common per-rank traffic model is roughly 2(p−1)/p times tensor bytes; name algorithm/topology assumptions. MoE resident weights depend on total experts, not active parameters. Load skew and communication can dominate.
- P/D: compare 1P1D against two colocated replicas at equal total GPUs/cost, not against a single GPU. Use measured bandwidth and record connector/layout/topology/privilege compatibility. Do not require both transports or simultaneously running every engine.

## Bridges B1–B6 — package J

The six bounded lessons remain required at approximately four learner hours each; the former 1–3-week elective expansions remain optional. The complete blueprints are in [the curriculum](../../../teaching/CURRICULUM.md#bridge-capsules).

| Bridge | Required learning artifact | Optional depth retained |
|---|---|---|
| B1 — advanced kernels/compilers | Annotate a matmul/attention profile, roofline and tile-parameter exercise: tensor cores, warp specialization, TVM/TIRx, mega-kernels, attention generations | Own split-KV paged attention, Blackwell/GPU MODE competition, CS149/MIT advanced labs |
| B2 — training/rollouts | Original four-hour capsule now canonical in [agent curriculum](../../agents/CURRICULUM.md#module-b2): tiny autograd/loop modification, optimizer memory, DP/FSDP/ZeRO, SFT/RLHF/GRPO, verl/Miles/slime versions and distillation | Full multi-turn agentic RL is now required added agent scope; CS336 A5/drafter training remain optional. Inspect batch-invariant rollout behavior in the systems comparison |
| B3 — nonstandard attention | MLA/FlashMLA, sliding-window, Qwen3.5 Gated DeltaNet/Mamba state and tiny checkpoint/restore example | Hybrid model integration and state-aware prefix cache |
| B4 — multimodal | VLM encoder/prefill/decode trace, image cache identity, encoder-cache validity and image-token budget | Multimodal serving/disaggregation study |
| B5 — alternative accelerators | Local MLX run and supplied TPU/JAX layout comparison; MLX/vllm-metal, SGLang-JAX | TPU allocation/port or vllm-metal contribution |
| B6 — routing languages/control planes | Modify supplied Rust selection/tie handling; compare SGLang Model Gateway, Dynamo, KServe and GPU allocation via DRA/KAI/Grove | Standalone Rust router with prefix hashing/power-of-two choices or second platform |

Data/model lifecycle, SQL, corpus/model/tokenizer/artifact versions, held-out leakage and cloud/IaC recur across the existing tasks rather than forming an unbudgeted seventh project. Weight loading/streaming, cold start and sleep-mode ideas belong to platform learning; operating every variant is not mandatory.

## Implementation and acceptance

[Advanced/release tasks](../tasks/advanced-release.md) retain H–J evidence gates. [Correctness](../engineering/correctness.md), [measurement](../engineering/measurement.md), and [resources](../../../docs/execution/resources.md) govern experiments. Before a later hardware-specific lab, expand its adapter/transport design and resolve the relevant compatibility questions. No local placeholder or reference trace can be reported as a completed multi-GPU deployment.

## Independence after the agent expansion

The original B2 artifact can be completed from supplied numerical/source fixtures without AGT-11–13 completion. Its ~4 hours stay in J; full agent training uses the separately added ledger. Quantization uses its own frozen quality fixtures and does not wait for live agent evaluation. No inference advanced lab is removed or made contingent on finishing the agent application.
