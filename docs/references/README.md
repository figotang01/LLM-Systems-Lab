# References and reading map

[Documentation index](../../README.md) · [Full preserved URL inventory](README.md#preserved-reference-inventory)

The inference track uses a course spine plus selected primary references. The agent track requires the **full published CMU 11-768 syllabus**, with integrated exercises preserving assignment objectives. The first table preserves the inference review's assigned depth and September 28 checks; the agent research snapshot below is September 30. Neither snapshot guarantees future availability or install compatibility. Before relying on concrete APIs, source symbols, hardware formats or provider prices, pin and smoke-test the selected set.

| Order / source (checked 2026-09-28) | Use in InferStack | Assigned depth |
|---|---|---|
| [Stanford CS336](https://cs336.stanford.edu/) | PyTorch/resource accounting; GPU/Triton; inference | Diagnostic portions of lecture 2, GPU/kernel lectures and inference lecture; no full A1 prerequisite given your experience |
| [CMU ML Systems schedule](https://mlsyscourse.org/schedule) | CUDA, attention, serving, parallelism | Primary lecture spine immediately before each lab; schedule supports teaching CUDA/attention before deep serving internals |
| [CS336 systems assignment](https://github.com/stanford-cs336/assignment2-systems) | Profiling and tiled-attention exercise format | Selected subproblems; inspect current assignment and course policy before adapting |
| [MIT accelerated computing](https://accelerated-computing.academy/fall25/) | GPU memory and execution intuition | Selected introductory/tiling exercises for a CUDA newcomer |
| [MIT efficient AI, 2024 archive](https://hanlab.mit.edu/courses/2024-fall-65940) | Quantization/deployment | Quantization and deployment material, bounded lab excerpt; do not assume every future offering's files exist |
| [CMU advanced ML systems](https://www.cs.cmu.edu/~zhihaoj2/15-779/schedule.html) | Broader research paper map | Reference when a specific mechanism becomes relevant |
| [Orca](https://www.usenix.org/conference/osdi22/presentation/yu) | Iteration scheduling | Draw a scheduling example and implement it |
| [PagedAttention](https://arxiv.org/abs/2309.06180) | Memory management and sharing | Study design/invariants; original throughput numbers are historical, not your acceptance threshold |
| [SGLang paper](https://arxiv.org/abs/2312.07104) | Radix reuse and structured generation | Cache design and control-flow connection |
| [Sarathi-Serve](https://arxiv.org/abs/2403.02310) | Chunked prefill trade-offs | Work an iteration-packing example and test interference |
| [Mini-SGLang](https://github.com/sgl-project/mini-sglang) | Compact executable reference | Read the module matching the mechanism; pin a revision before relying on filenames |
| [vLLM prefix design](https://docs.vllm.ai/en/latest/design/prefix_caching/) | Prefix key, ownership, eviction | Compare with your design after writing the invariants |
| [FlashInfer attention API](https://docs.flashinfer.ai/api/attention.html) | Paged-backend integration | Pick one supported API, record shapes/layouts, test the pinned version |
| [Triton normalization tutorial](https://triton-lang.org/main/getting-started/tutorials/05-layer-norm.html) | Reduction/fusion | Adapt ideas for RMSNorm; layer norm and RMSNorm are not identical operations |
| [vLLM reproducibility](https://docs.vllm.ai/en/latest/usage/reproducibility/) | Numerical and sampling tests | Understand conditions and limits before requiring cross-run equality |
| [AIPerf metric reference](https://docs.nvidia.com/aiperf/reference/ai-perf-metrics-reference) | New resource for measurement semantics | Map each reported metric to its timestamp/count source |
| [AIPerf replay guide](https://docs.nvidia.com/aiperf/tutorials/datasets-inputs/inputs-json-replay) | New resource for replay semantics | Compare fixed content with live-agent execution |
| [Gateway Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/) | Routing contracts and control-plane responsibilities | Understand gateway, pool and endpoint picker before deploying |
| [Model-server protocol proposal](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/main/docs/proposals/003-model-server-protocol/README.md) | Contract starting point | Verify against actual released implementation; proposal alone is not conformance |
| [llm-d](https://github.com/llm-d/llm-d) | Supported deployment guides | Choose one supported routing setup; do not install all guides simultaneously |
| [LMCache](https://docs.lmcache.ai/) | Host-memory KV tier | Integration/usage for the pinned engine, plus restore/recompute experiment |
| [vLLM disaggregated prefill](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | P/D scope and connector integration | One compatible connector, two-GPU comparison |
| [vLLM quantization support](https://docs.vllm.ai/en/latest/features/quantization/) | Actual format/backend hardware constraints | Read before choosing a rental or checkpoint |
| [Speculative decoding](https://arxiv.org/abs/2211.17192) | Verifier correctness | Work exact categorical examples, then a supported serving run |
| [Continuum](https://arxiv.org/abs/2511.02230) | Session retention and tool gaps | Read methods before trying a TTL policy |
| [XPerf](https://arxiv.org/abs/2608.20370) | Agent workload replay | Methods comparison; not a second benchmark framework implementation |
| [AgentSysBench](https://arxiv.org/abs/2608.15127) | Non-LLM stages and state | Use to question whether LLM optimization improves the whole task |
| [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) | SDK/protocol boundary | The previously checked spec describes stateless self-contained requests; app/tool state still needs handling |
| [Lambda instance pricing](https://lambda.ai/instances) | GPU cost scenarios | Per-GPU vs per-node rate, topology, availability and tax |
| [Runpod pricing](https://www.runpod.io/pricing) | Alternative quote source | Check current SKU, cloud tier, storage, privileges and topology before booking; no assumed cheapest-rate guarantee |
| [NVIDIA RTX A6000](https://www.nvidia.com/en-us/design-visualization/rtx-a6000/) | Correct GPU architecture identity | Avoid confusing Ampere A6000 with RTX 6000 Ada |

## Added production and agent sources

- [SGLang contribution guide](https://docs.sglang.io/docs/developer_guide/contribution_guide): PF source/patch/testing workflow.
- [vLLM V1 architecture](https://docs.vllm.ai/en/latest/design/arch_overview/): equivalent request/component mapping.
- [CMU 11-768](https://www.cmu-agents.com/), [Assignment 1](https://github.com/cmu-agents/assignment-1/blob/main/ASSIGNMENT.md), [Assignment 2](https://github.com/cmu-agents/assignment-2/blob/main/ASSIGNMENT.md): full syllabus and substantive assignment objectives, adapted to one engineering workspace. The original eight-hour supplement is preserved inside the expanded track; original course hosting/team/grading rules are not project requirements.

<a id="agent-track-research"></a>
## Agent-track research and assigned depth

The September 30 research snapshot informs the approved scope. [Coverage](../../tracks/agents/COVERAGE.md) maps every published course slot to an owning lesson/task; its update rule governs material availability and review. Popularity and job titles do not determine completion depth: the evidence below does.

| Primary source | Assigned project use |
|---|---|
| [CMU syllabus](https://www.cmu-agents.com/) | Full coverage, including all four training blocks, both guest slots and research milestones |
| [mini-SWE-agent](https://github.com/SWE-agent/mini-swe-agent) | Read a minimal control loop; author and test the project's own bounded harness |
| [LangGraph](https://github.com/langchain-ai/langgraph), [persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | Integrate durable state/checkpoints, interruptions and recovery; reuse authored components |
| [OpenHands](https://github.com/OpenHands/OpenHands), [tool architecture](https://docs.openhands.dev/sdk/arch/tool-system) | Source walkthrough, operation and substantive tool/skill modification |
| [DeepAgents](https://github.com/langchain-ai/deepagents) | Compare context offloading, planning and subagents; no second full application |
| [Google ADK](https://github.com/google/adk-python), [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Bounded architecture/API comparison exercises |
| [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture), [A2A](https://a2a-protocol.org/latest/topics/what-is-a2a/) | Implement MCP tools and one bounded agent handoff; pin protocol versions |
| [Qdrant hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/) | Dense/BM25/RRF/reranking experiments; preserve the pgvector comparison |
| [DSPy](https://github.com/stanfordnlp/dspy) | One measured optimization experiment with protected evaluation data |
| [Phoenix](https://github.com/Arize-ai/phoenix) | OpenTelemetry-based application traces, quality/cost analysis and redaction |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Study and adapt adversarial tool/document inputs; test actual permissions |
| [TRL SFT](https://huggingface.co/docs/trl/en/sft_trainer), [GRPO](https://huggingface.co/docs/trl/en/grpo_trainer) | Real small-model training with learner-owned masks, rewards and independent evaluation |
| [Qwen3](https://github.com/QwenLM/Qwen3) | Candidate 0.6B plumbing and 1.7B training targets; verify tool ability and hardware fit |
| [verl](https://github.com/verl-project/verl), [multi-turn SGLang rollouts](https://verl.readthedocs.io/en/latest/sglang_multiturn/multiturn.html) | Operate and inspect rollout/learner coordination, versions, synchronization and recovery |
| [Miles](https://github.com/radixark/miles) | Preserve B2's rollout-system comparison, alongside verl/slime concepts |
| [ReAct](https://arxiv.org/abs/2210.03629), [CodeAct](https://arxiv.org/abs/2402.01030) | Trace reasoning/action boundaries and programmatic tool composition |
| [PPO](https://arxiv.org/abs/1707.06347), [GAE](https://arxiv.org/abs/1506.02438), [GRPO/DeepSeekMath](https://arxiv.org/abs/2402.03300) | Independently checked numerical objectives before trainer integration |

Released lecture decks at that snapshot: [01 foundations](https://www.cmu-agents.com/slides/lecture-01-agents.pdf), [02 tools](https://www.cmu-agents.com/slides/lecture-02-tool-use.pdf), [03 context](https://www.cmu-agents.com/slides/lecture-03-long-context.pdf), [04 memory/skills](https://www.cmu-agents.com/slides/lecture-04-memory-and-skills.pdf), [05 planning](https://www.cmu-agents.com/slides/lecture-05-planning.pdf), [06 coding](https://www.cmu-agents.com/slides/lecture-06-coding-agents.pdf), [07 computer use](https://www.cmu-agents.com/slides/lecture-07-computer-use-agents.pdf), [08 SFT](https://www.cmu-agents.com/slides/lecture-08-sft.pdf), [09 RL foundations](https://www.cmu-agents.com/slides/lecture-09-rl-basics.pdf), [10 research](https://www.cmu-agents.com/slides/lecture-10-deep-research-agents.pdf), [11 advanced RL](https://www.cmu-agents.com/slides/lecture-11-rl-advanced.pdf). Follow each lecture's cited primary work for algorithm variants, with exact equation/source attribution in the later lesson. Later decks, training-assignment details and guest topics were not captured in that review; verify their present availability before treating them as unreleased. Their learning slots remain required.

| Sampled employer source | Skill signal used in the design |
|---|---|
| [Amazon agentic diagnostics SDE](https://amazon.jobs/en/jobs/10461352/software-development-engineer-catalog-diagnostics-agentic-analytics) | Maintainable services, data pipelines, orchestration, testing and operational traceability |
| [Amazon agent evaluation scientist](https://www.amazon.jobs/en/jobs/10481484/applied-scientist-support-agent-intelligence-and-evaluation) | Retrieval and conversation quality, calibration, latency and experiment-to-feature work |
| [Apple evaluation MLE](https://jobs.apple.com/en-us/details/200657984-0670/ml-engineer-evaluation-analysis-metric-and-data-strategy?team=SFTWR) | Representative datasets, statistical comparison, multistep evaluation and failure analysis |
| [Google agentic data/evaluations](https://www.google.com/about/careers/applications/jobs/results/90844022636978886-staff-software-engineer-agentic-data-and-evals?sort_by=date) | Verified data generation, post-training and model-improvement infrastructure |

These are a sample of skill signals, including senior roles. They are not current-opening guarantees or claims that this student project reproduces production scale. The [coverage ledger](../../tracks/agents/COVERAGE.md#industry-skill-and-evidence-map) translates them into assessable artifacts.

## Historical material and source discipline

The inventory preserves specialized papers, other courses (including CS149, CMU deep-learning systems and the Berkeley agent course), compact reference engines, ecosystem alternatives and historical recruiting links from v2. They remain discoverable even when not mandatory assignments. Older targets, warm-up requirements, deployment counts and performance claims do not override approved scope; see [migration/coverage](../archive/scope-map.md).

Use exact source sections/symbols in later lesson reading files. No assertion of research novelty, objectively best course, universal fastest engine, or current job availability follows from a preserved link. Course solution redistribution must follow the applicable source terms. A source's existence does not demonstrate compatible software/hardware or a reproduced result.

## Preserved reference inventory

Every distinct external URL extracted from the prior plan, review, skeleton, supplements, curriculum and v2 catalog is retained below. This is provenance/discovery, not a new validation of availability, compatibility or factual claims. Older job postings, mirrors and secondary sources are historical context; primary sources govern technical implementation. Dates/versions inside URLs are not current support promises.

| Reference | Origin |
|---|---|
| [accelerated-computing.academy/fall25/](https://accelerated-computing.academy/fall25/) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [agenticai-learning.org/f25](https://agenticai-learning.org/f25) | `docs/archive/PROJECT_PLAN_v2.md` |
| [arxiv.org/abs/2211.17192](https://arxiv.org/abs/2211.17192) | `docs/PLAN_REVIEW.md` |
| [arxiv.org/abs/2309.06180](https://arxiv.org/abs/2309.06180) | `docs/PLAN_REVIEW.md` |
| [arxiv.org/abs/2312.07104](https://arxiv.org/abs/2312.07104) | `docs/PLAN_REVIEW.md` |
| [arxiv.org/abs/2403.02310](https://arxiv.org/abs/2403.02310) | `docs/PLAN_REVIEW.md` |
| [arxiv.org/abs/2511.02230](https://arxiv.org/abs/2511.02230) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [arxiv.org/abs/2608.15127](https://arxiv.org/abs/2608.15127) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [arxiv.org/abs/2608.20370](https://arxiv.org/abs/2608.20370) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [cs149.stanford.edu/](https://cs149.stanford.edu/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [cs336.stanford.edu/](https://cs336.stanford.edu/) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [dlsyscourse.org/](https://dlsyscourse.org/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [docs.flashinfer.ai/api/attention.html](https://docs.flashinfer.ai/api/attention.html) | `docs/DECEMBER_SKELETON.md`, `docs/PLAN_REVIEW.md` |
| [docs.lmcache.ai/](https://docs.lmcache.ai/) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [docs.nvidia.com/aiperf/reference/ai-perf-metrics-reference](https://docs.nvidia.com/aiperf/reference/ai-perf-metrics-reference) | `PROJECT_PLAN.md`, `docs/PLAN_REVIEW.md` |
| [docs.nvidia.com/aiperf/tutorials/datasets-inputs/inputs-json-replay](https://docs.nvidia.com/aiperf/tutorials/datasets-inputs/inputs-json-replay) | `PROJECT_PLAN.md`, `docs/PLAN_REVIEW.md` |
| [docs.sglang.io/docs/developer_guide/contribution_guide](https://docs.sglang.io/docs/developer_guide/contribution_guide) | `docs/PLAN_ADDITIONS.md` |
| [docs.vllm.ai/en/latest/design/arch_overview/](https://docs.vllm.ai/en/latest/design/arch_overview/) | `docs/PLAN_ADDITIONS.md` |
| [docs.vllm.ai/en/latest/design/prefix_caching.html](https://docs.vllm.ai/en/latest/design/prefix_caching.html) | `docs/archive/PROJECT_PLAN_v2.md` |
| [docs.vllm.ai/en/latest/design/prefix_caching/](https://docs.vllm.ai/en/latest/design/prefix_caching/) | `docs/PLAN_ADDITIONS.md`, `docs/PLAN_REVIEW.md` |
| [docs.vllm.ai/en/latest/features/disagg_prefill/](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | `docs/PLAN_REVIEW.md` |
| [docs.vllm.ai/en/latest/features/quantization/](https://docs.vllm.ai/en/latest/features/quantization/) | `PROJECT_PLAN.md`, `docs/PLAN_REVIEW.md` |
| [docs.vllm.ai/en/latest/usage/reproducibility/](https://docs.vllm.ai/en/latest/usage/reproducibility/) | `PROJECT_PLAN.md`, `docs/PLAN_REVIEW.md` |
| [freehire.me/jobs/software-engineer-model-runtime-openai-nrxqkret](https://freehire.me/jobs/software-engineer-model-runtime-openai-nrxqkret) | `docs/archive/PROJECT_PLAN_v2.md` |
| [gateway-api-inference-extension.sigs.k8s.io/](https://gateway-api-inference-extension.sigs.k8s.io/) | `PROJECT_PLAN.md`, `docs/DECEMBER_SKELETON.md`, `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/accelerated-computing-class](https://github.com/accelerated-computing-class) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/ai-dynamo/aiperf](https://github.com/ai-dynamo/aiperf) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/ai-dynamo/dynamo](https://github.com/ai-dynamo/dynamo) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/cmu-agents/assignment-1/blob/main/ASSIGNMENT.md](https://github.com/cmu-agents/assignment-1/blob/main/ASSIGNMENT.md) | `docs/PLAN_ADDITIONS.md`, `teaching/CURRICULUM.md` |
| [github.com/cmu-agents/assignment-2/blob/main/ASSIGNMENT.md](https://github.com/cmu-agents/assignment-2/blob/main/ASSIGNMENT.md) | `docs/PLAN_ADDITIONS.md`, `teaching/CURRICULUM.md` |
| [github.com/kubernetes-sigs/gateway-api-inference-extension/blob/main/docs/proposals/003-model-server-protocol/README.md](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/main/docs/proposals/003-model-server-protocol/README.md) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/llm-d/llm-d](https://github.com/llm-d/llm-d) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/llm-d/llm-d-inference-sim](https://github.com/llm-d/llm-d-inference-sim) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/llm-d/llm-d-inference-sim/blob/main/docs/kv-cache.md](https://github.com/llm-d/llm-d-inference-sim/blob/main/docs/kv-cache.md) | `docs/DECEMBER_SKELETON.md` |
| [github.com/mit-han-lab/TinyChatEngine](https://github.com/mit-han-lab/TinyChatEngine) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/mlsyscourse](https://github.com/mlsyscourse) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-07-28-spec-ga/index.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-07-28-spec-ga/index.md) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/radixark/miles](https://github.com/radixark/miles) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/sgl-project/mini-sglang](https://github.com/sgl-project/mini-sglang) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/sgl-project/sglang](https://github.com/sgl-project/sglang) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/sgl-project/sglang/tree/main/sgl-model-gateway](https://github.com/sgl-project/sglang/tree/main/sgl-model-gateway) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/stanford-cs149](https://github.com/stanford-cs149) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/stanford-cs336](https://github.com/stanford-cs336) | `docs/archive/PROJECT_PLAN_v2.md` |
| [github.com/stanford-cs336/assignment2-systems](https://github.com/stanford-cs336/assignment2-systems) | `docs/PLAN_REVIEW.md` |
| [github.com/vllm-project/vllm/releases](https://github.com/vllm-project/vllm/releases) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [hanlab.mit.edu/courses/2024-fall-65940](https://hanlab.mit.edu/courses/2024-fall-65940) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [hanlab.mit.edu/courses/2026-fall-65940](https://hanlab.mit.edu/courses/2026-fall-65940) | `docs/archive/PROJECT_PLAN_v2.md` |
| [huggingface.co/Qwen/Qwen3-0.6B-Base/blob/main/config.json](https://huggingface.co/Qwen/Qwen3-0.6B-Base/blob/main/config.json) | `docs/PLAN_REVIEW.md` |
| [job-boards.greenhouse.io/anthropic/jobs/5385998008](https://job-boards.greenhouse.io/anthropic/jobs/5385998008) | `docs/archive/PROJECT_PLAN_v2.md` |
| [jobs.dukecapitalpartners.duke.edu/companies/fluidstack/jobs/70694933-software-engineer-inference-platform](https://jobs.dukecapitalpartners.duke.edu/companies/fluidstack/jobs/70694933-software-engineer-inference-platform) | `docs/archive/PROJECT_PLAN_v2.md` |
| [jobs.nvidia.com/careers/job/893393884394](https://jobs.nvidia.com/careers/job/893393884394) | `docs/archive/PROJECT_PLAN_v2.md` |
| [kaden-projects.com/blog/kubernetes-llm-inference-stack-2026/](https://kaden-projects.com/blog/kubernetes-llm-inference-stack-2026/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-overview](https://kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-overview) | `docs/archive/PROJECT_PLAN_v2.md` |
| [lambda.ai/instances](https://lambda.ai/instances) | `PROJECT_PLAN.md`, `docs/PLAN_REVIEW.md` |
| [mlsyscourse.org/](https://mlsyscourse.org/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [mlsyscourse.org/schedule](https://mlsyscourse.org/schedule) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [modelcontextprotocol.io/specification/2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [siliconangle.com/2026/01/22/inferact-launches-150m-funding-commercialize-vllm/](https://siliconangle.com/2026/01/22/inferact-launches-150m-funding-commercialize-vllm/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [triton-lang.org/main/getting-started/tutorials/05-layer-norm.html](https://triton-lang.org/main/getting-started/tutorials/05-layer-norm.html) | `docs/PLAN_REVIEW.md` |
| [vllm.ai/blog/2026-09-22-vllm-metal-v0-28-0](https://vllm.ai/blog/2026-09-22-vllm-metal-v0-28-0) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.builtinchicago.org/job/forward-deployed-engineer-ai-inference-vllm-and-kubernetes/8291315](https://www.builtinchicago.org/job/forward-deployed-engineer-ai-inference-vllm-and-kubernetes/8291315) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.businesswire.com/news/home/20260505077157/en/RadixArk-Launches-with-$100-Million-in-Seed-Funding-Led-by-Accel-to-Grow-SGLang-and-Democratize-Frontier-AI-Infrastructure](https://www.businesswire.com/news/home/20260505077157/en/RadixArk-Launches-with-$100-Million-in-Seed-Funding-Led-by-Accel-to-Grow-SGLang-and-Democratize-Frontier-AI-Infrastructure) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.cmu-agents.com/](https://www.cmu-agents.com/) | `docs/PLAN_ADDITIONS.md`, `teaching/CURRICULUM.md` |
| [www.cs.cmu.edu/~zhihaoj2/15-779/](https://www.cs.cmu.edu/~zhihaoj2/15-779/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.cs.cmu.edu/~zhihaoj2/15-779/schedule.html](https://www.cs.cmu.edu/~zhihaoj2/15-779/schedule.html) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
| [www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/](https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.lmsys.org/blog/2026-07-30-sglang-google-tpu/](https://www.lmsys.org/blog/2026-07-30-sglang-google-tpu/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.lmsys.org/blog/2026-08-04-specforge-v0-3](https://www.lmsys.org/blog/2026-08-04-specforge-v0-3) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.nvidia.com/en-us/design-visualization/rtx-a6000/](https://www.nvidia.com/en-us/design-visualization/rtx-a6000/) | `PROJECT_PLAN.md`, `docs/PLAN_REVIEW.md` |
| [www.runpod.io/pricing](https://www.runpod.io/pricing) | `docs/PLAN_REVIEW.md` |
| [www.spheron.network/blog/deploy-qwen-3-5-gpu-cloud/](https://www.spheron.network/blog/deploy-qwen-3-5-gpu-cloud/) | `docs/archive/PROJECT_PLAN_v2.md` |
| [www.usenix.org/conference/osdi22/presentation/yu](https://www.usenix.org/conference/osdi22/presentation/yu) | `docs/PLAN_REVIEW.md`, `docs/archive/PROJECT_PLAN_v2.md` |
