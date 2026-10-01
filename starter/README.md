# Supplied experiment plumbing

This code saves time on artifact directories, configuration snapshots, hashing, report templates and GPU budget arithmetic. These are lower-priority implementation tasks given your previous HTTP/distributed-systems work. The benchmark's arrivals, metric semantics, goodput and replay policies remain your learning tasks.

Delivered and runnable on the Mac with **Python 3.10+**, standard library only. No cloud instances, downloads, installations or network calls. Run from the project root:

```sh
python3 starter/experiment.py budget starter/budget.example.json
python3 starter/experiment.py bundle --config starter/run.example.json --out /tmp/inferlab-runs --artifact starter/budget.example.json
python3 -m unittest discover -s tests -v
```

The budget example produces **120 node-hours, 150 GPU-hours, $185.50 compute, $30 other, $64.65 contingency, $280.15 total before tax**. It uses the listed prices in the plan; the utility does not refresh them. Change `usd_per_node_hour` to the entire node price, not the per-GPU rate. Two GPUs on one node for three hours = three node-hours and six GPU-hours. Two such nodes = six node-hours and twelve GPU-hours.

The bundle command prints a unique directory containing:

- `config.json`: snapshot of the explicitly provided configuration.
- `manifest.json`: timestamp, config checksum, basic OS/Python architecture, Git commit/dirty state if available, explicit artifact checksums.
- `observations.jsonl`: empty output target for the later harness.
- `REPORT.md`: pending-results template populated with the hypothesis.

No fabricated timings, GPU discovery or invented model versions are added. The fixture is deliberately marked `fixture`; it is not benchmark evidence. The current project directory may not be a Git repo, so a null Git commit is valid. A real run requires the missing provenance fields, a tested command and actual raw results. Config validation checks scaffold structure; it does not certify completeness or correctness of a benchmark.

Read `budget()` and `create_bundle()` once, then treat them as provided infrastructure. Exercise: change the two-GPU node to a $3.98/node-hour A100 node and predict the total before running; expected total with the example's contingency is $350.35. Check why multiplying the node price by GPU count again would be a billing error.

Artifact contents are hashed, not copied. Retain raw data separately if you want long-term reproduction. The utility does not scan environment variables or capture tokens, credentials, private prompts or remote URLs. Keep those out of supplied configs yourself.

Transport/SSE scaffolds, GPU recipes, manifests, reference CUDA kernels and application templates are scheduled in [the curriculum](../teaching/CURRICULUM.md). They have not been delivered or GPU-tested yet.
