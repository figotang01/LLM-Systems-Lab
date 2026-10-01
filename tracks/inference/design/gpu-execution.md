# GPU execution, kernels, and graphs

[Documentation index](../../../README.md) · [Roadmap](../../../docs/execution/roadmap.md) · [Task index](../tasks/README.md)

Status: planned system design; named source paths are reserved in the code map and will be created during implementation.

## Requirements

| ID | Requirement | Goal / evidence |
|---|---|---|
| <a id="gpu-1"></a>GPU-1 | Direct paged prefill/decode reads with correct metadata and numeric behavior | [G1](../../../PROJECT_PLAN.md#g1); independent tiny reference and page-boundary suite |
| <a id="gpu-2"></a>GPU-2 | One learner Triton normalization kernel plus substantive CUDA C++ modification | [G4](../../../PROJECT_PLAN.md#g4); dtype/tail correctness and microbenchmark |
| <a id="gpu-3"></a>GPU-3 | Safe graph buffers/buckets and a bounded streams/events overlap exercise | [G1](../../../PROJECT_PLAN.md#g1)/[G2](../../../PROJECT_PLAN.md#g2); eager/graph comparison and annotated trace |
| <a id="gpu-4"></a>GPU-4 | Explain end-to-end bottlenecks using profiles and matched runs | [G2](../../../PROJECT_PLAN.md#g2); evidence-backed gap to production baseline |

## Backend boundary

The executor owns model execution and backend scratch buffers, while the coordinator owns request lifecycle and the pool owns page leases. FlashInfer translates logical page tables to its pinned prefill/decode metadata, including layout, indices/indptr, last-page lengths, dtype, GQA and positions. Reject unsupported combinations before a sweep. Keep vendor wrapper types out of the scheduler API.

Build a gathered PyTorch oracle before integrating direct paged reads. Complete a supplied tiled forward exercise using online softmax: maintain running maximum, denominator and rescaled accumulator. Explain split-KV/Flash-Decoding and FlashAttention IO reduction. This does not require writing every optimized attention kernel or completing the whole CS336 systems assignment.

## Kernel task

Choose RMSNorm or fused residual/RMSNorm as the one authored Triton kernel. Explain reduction axes, epsilon, accumulation dtype, masking and bytes moved. Modify the supplied equivalent CUDA C++ kernel/launch parameters and attribute the baseline. The build machinery is supplied. Compare eager PyTorch, torch.compile, Triton and CUDA only after independent correctness and warmup.

Faster kernel time is not proof of faster serving. Include small and irregular shapes, tail masking, dtype range and accumulation behavior. Large advanced matmul, SwiGLU, split-KV kernels and Blackwell competitions remain bounded references/optional depth under the advanced bridge, not newly required December kernels.

## Graph lifecycle

Allocate stable input/output/workspace buffers per supported bucket. Populate inputs and masks without changing captured addresses; ensure padded/dummy slots cannot write live KV. Capture only supported execution paths, record when a shape/backend/configuration change requires invalidation, and fall back to eager execution for unsupported cases.

Retain graph/workspace memory in capacity accounting. Do not assume captured kernels support all variable sequence layouts. Exact bucket sets and backend graph combinations require OQ-02/OQ-03 preflight. Input refresh and buffer policy are learner modifications to the supplied graph lifecycle.

Start with one execution step in flight. Teach host launch versus completed device timing, streams/events, dependency ordering and a bounded overlap demonstration. A fully asynchronous multi-stream serving pipeline is not part of the core completion contract.

## Failure cases, tests and profiling

Test tail lengths at page boundaries, mismatched head layout, illegal page size/dtype, eager versus graph, bucket padding, stale inputs on replay, dummy writes, and cancellation while a step holds leases. If an error may leave outstanding device work, do not recycle its memory merely because the host raised.

Use Nsight Systems to identify host launch gaps and device idle intervals; use Nsight Compute on one kernel to explain bandwidth/occupancy/arithmetic-intensity limits. Include profiler overhead only in diagnostic runs. Freeze model/config/workload and compare the custom runtime with a same-model vLLM baseline; SGLang remains a required operational comparison elsewhere.

[GPU/serving tasks](../tasks/gpu-serving.md) own implementation order. Follow [correctness](../engineering/correctness.md) and [measurement](../engineering/measurement.md). Accept CP2 only with real GPU checks, authored/modified kernel evidence, graph/profile interpretation, streaming lifecycle validation, and a measured comparison; simulator results cannot close this gate.
