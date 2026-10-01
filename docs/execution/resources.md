# Shared resources and compute/API budget

[Shared effort ledger](roadmap.md) · [Agent training design](../../tracks/agents/LEARNING.md) · [Open decisions](../engineering/open-questions.md)

## Current approved planning allocation

Confirmed range: **$500–700 total across both tracks**. Use the **$600 working allocation** below. These are planning envelopes, not purchases or provider-enforced limits. Record each GPU/API/storage charge once even when an experiment serves both tracks.

| Allocation | USD |
|---|---:|
| Inference-track GPU experiments | 300 |
| Agent training and rollout experiments | 120 |
| Hosted text/vision models and supplementary judging | 60 |
| Storage and related costs | 20 |
| Shared contingency | 100 |
| **Working total** | **600** |

Agentic RL is the main added compute driver: multiple trajectories per task, repeated model calls as context grows, tool/verifier execution and learner updates. Tree search, multi-agent execution, GUI/vision and repeated judging also multiply inference costs. Small curated SFT runs are more controllable; larger model/context/batch sizes change both memory fit and throughput.

Prepare fixtures and dry correctness checks locally. Start training with 0.6B plumbing checks and 1.7B as the initial substantive target; measure fit and capability before scale-up. Use short prepared single-GPU sessions and one bounded supported multi-GPU systems exercise, reusing rented capacity where practical. On the 16 GB Mac, run local models, vector stores and heavy containers sequentially as needed. Application tests must not require the training or CUDA environment.

Bound paid runs by time, tokens/steps, samples and explicit cleanup. Inspect actual provider bills/usage against the local ledger; SDK timeouts do not establish zero cost. If an operated requirement exceeds funds or lacks compatible hardware, retain it as pending practical work while continuing conceptual/local work. Do not cut course topics or claim operation from a supplied trace. Re-estimate within the confirmed range before consuming the shared reserve; no cloud provisioning is performed by this documentation handoff.

The approved plan's September 30 pricing check listed Lambda A6000 at $1.09/GPU-hour before applicable tax. Treat it as a dated reference, recheck rates/availability and bill all GPUs in a rented node. [Official pricing](https://lambda.ai/instances)

## Local hardware and compatibility

The Mac is useful for logic, tiny numerical tests, local MLX and HTML. Run the local model and heavy Docker stack at different times on 16 GB. Use one or two simulator replicas and light observability; a full monitoring cluster plus multiple models may exceed memory. Label Mac benchmarks as Mac benchmarks; they are valid local results but do not predict CUDA serving performance.

Start on one 24–48 GB NVIDIA GPU with a tiny dense model, then choose a larger fitting model. Model fit includes weights, KV, activations/workspace, graph pools and runtime overhead. Dense BF16 weight bytes are approximately 2×parameter count; MoE total parameters, not active parameters, determine unsharded weight storage.

The v2 A6000 entry was misgrouped: **RTX A6000 is Ampere**, while RTX 6000 Ada is a different GPU. Hardware support depends on the specific quantization kernel, format and software build. Do not infer FP8 tensor-core performance from the ability to store FP8 KV. Check the actual backend matrix and run a smoke test. [NVIDIA A6000](https://www.nvidia.com/en-us/design-visualization/rtx-a6000/) · [vLLM quantization support](https://docs.vllm.ai/en/latest/features/quantization/)

**Historical inference-focused scenario:** the original $300–400 estimate assumed small dense models, sequential prepared sessions and no substantial training. It does not price the expanded agent-training scope. The current combined allocation is above; these old scenarios remain useful cost-model examples, not a competing budget.

Price check on 2026-09-28: Lambda lists A6000 at $1.09/GPU-hour, A100 40 GB at $1.99/GPU-hour, H100 PCIe at $3.29/GPU-hour, and H100 SXM at $4.19/GPU-hour for its two-GPU tier. Listed prices exclude applicable tax and availability is not reserved. [Official instance pricing](https://lambda.ai/instances)

| Resource | Planned billed time (includes setup) | Rate used | Cost |
|---|---:|---:|---:|
| 1× A6000 development node | 80 node-hours = 80 GPU-hours | $1.09/node-hour | $87.20 |
| 2× A6000 experiment node | 30 node-hours = 60 GPU-hours | $2.18/node-hour | $65.40 |
| 1× H100 PCIe specialist session | 10 node-hours = 10 GPU-hours | $3.29/node-hour | $32.90 |
| Storage/download/other allowance | — | assumed allowance | $30.00 |
| Subtotal + 30% contingency | — | — | **$280.15 before applicable tax** |

This is **120 node-hours and 150 GPU-hours**. It assumes the advanced backends you select work on those GPUs; validate first. Replacing the two-GPU allocation with 2× A100 40 GB at the listed $1.99/GPU-hour raises the total with contingency to **$350.35**. Using 2× H100 SXM for all those 30 node-hours raises it to **$521.95**. Thus compatibility and premium multi-GPU runtime can move the budget substantially. You need only a short specialist session, not H100s for all development.

| Topics | Compute requirement / main cost driver | Cost control |
|---|---|---|
| Allocator, scheduler, prefix indexes, Go policy, basic RAG/MCP fixtures, HTML | CPU/Mac; algorithmic complexity rather than GPU hours | Exhaustive logic tests locally, virtual clock |
| Dense executor, paged backend, Triton/CUDA/graphs | One 24–48 GB GPU; repeated correctness and profiling runs | 0.6B/1.7B first, fixed shape suite, prepared scripts |
| RAG/agent trace generation and lm-eval | One GPU; total generated tokens, long contexts and large eval suites | Small held-out pilot, reuse traces, cache downloaded models |
| Quantization / calibration | One GPU; checkpoint memory and calibration passes; format-specific hardware | Supplied checkpoint first, bounded calibration, no training |
| Speculation | Target + draft weights/KV simultaneously; bigger memory and load sweeps | N-gram first, one compatible draft/target pair |
| Routing, scale-up, offload | Two replica GPUs; repeated multi-minute load runs and idle cold-start time | Reuse one two-GPU node; CPU tools/embeddings; simulate first |
| TP / EP / MoE / P/D | Highest infrastructure requirement: ≥2 GPUs, topology/transport compatibility, total expert weights | Tiny collective lab then short production run; no wide-EP or 70B fleet |
| Drafter training / Blackwell kernel competition | Optional extensions with potentially large training or premium-GPU spend | Preserve the bounded original core; price extensions separately |
| Required agentic RL and RL systems | Added rollout/learner compute, accounted for in the current combined budget above | Use small models, short verified runs and cost caps; conceptual work alone cannot close the practical gate |

Inference spend checkpoints: target ~$30–50 for initial environment/baselines and review near $150 before the multi-GPU study. The current shared contingency is $100; do not add the historical $75–100 reserve a second time. These are targets, not provider-enforced caps. Do not spend the reserve on larger models before the headline experiment works.

Use the supplied budget command to change counts, billed hours and per-node rates. Provision only for prepared runs; use provider-side expiration/cleanup and verify destruction. No cloud accounts or instances are created by this planning revision.

For two-GPU work record interconnect, peer access and container privileges. A marketplace “GPU rental” may not support k3s, host drivers or desired transport. If Kubernetes cannot run there, use a university VM/bare-metal node for the platform sprint and containers for engine labs. Log the difference.

## Interpretation in the current scope

The prices and dollar examples above are historical 2026-09-28 planning inputs, preserved rather than refreshed in this restructuring. They are not current offers or guaranteed availability. Recheck provider pricing, node-level billing, storage, taxes, host privileges, and compatible hardware before any purchase.

The historical PF/AG additions did not carry a separate cash allowance. The later agent expansion now has the explicit combined allocation above. The $500–700 planning range is confirmed; rental/provider/compatibility choices remain [open decisions](../engineering/open-questions.md). No cloud action is authorized merely by creating this documentation or its planned code map.

Before locking an environment, record image digest, OS/architecture, driver, CUDA, PyTorch, backend, engine commit, gateway/EPP/chart versions, MCP SDK, model/tokenizer/template revision, precision, GPU topology, and exact smoke command/outcome. CPU tools, custom GPU runtime, production images, and Go/platform dependencies stay separate. Compatibility must be demonstrated as a set, not inferred from independent latest releases.

[Roadmap](roadmap.md) · [Ownership](../engineering/ownership.md) · [Task index](../../tracks/inference/tasks/README.md)
