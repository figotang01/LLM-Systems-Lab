# Working in LLM Systems Lab

This is a learning project with two independently usable tracks. Read the root [README](README.md), then the selected task and its linked design/lesson. Do not read every archive or implement the whole roadmap to answer a bounded task request.

## Start and resume

- Follow [the handoff guide](docs/HANDOFF.md) for task selection, teaching, implementation and evidence records.
- Inference task status lives in [its task briefs](tracks/inference/tasks/README.md); agent task status lives in [its roadmap](tracks/agents/ROADMAP.md). Those are the only task-status owners.
- Select an explicitly requested task, or the earliest ready task in the requested subsystem. Inspect prerequisite evidence and actual files. If prerequisites are missing, make progress on the earliest required prerequisite and explain the choice.
- At this documentation handoff, the ready starting tasks are FND-01 and AGT-01. Derive later readiness from task records rather than treating this sentence as a permanent queue.

## Authority and scope

User instructions govern the current work. The [project overview](PROJECT_PLAN.md) owns goals, the [shared roadmap](docs/execution/roadmap.md) owns effort/timing, track designs own behavior, tasks own acceptance, and the [teaching contract](teaching/CONTRACT.md) owns lesson standards. Archives are provenance, not competing requirements.

Preserve the approved inference scope, PF supplement, original APP/AG/B2 requirements, full published CMU syllabus and real spring SFT/agentic RL/RL-systems gates. Do not silently fund expansion by dropping tasks. Use the [open decisions](docs/engineering/open-questions.md) to record ordinary implementation choices; do not ask for permission when the task already authorizes them.

## Teaching and authorship

- Follow the requested mode: prepare a lesson, teach interactively, implement, or review. An explicit implementation request authorizes coding; it does not prove the learner understands the result.
- For teaching, explain the state/mechanism before the exercise. Supply low-value plumbing and independent checks. Preserve Build/Modify/Operate/Explain and attribute generated/adapted code honestly.
- Record learner understanding separately from code/test status. Never fabricate a passed teach-back, learner-authored code, real-device execution, measurements, or upstream acceptance.
- HTML lessons must follow the shared contract and the owning blueprint. Current blueprints are not completed HTML or runnable exercises.

## Implementation boundaries

- Keep one authoritative implementation per mechanism. Inference owns engine/serving/performance replay; agents own application state, retrieval, live quality and training. Exchange only the [shared contracts](docs/system/track-contracts.md).
- Create only files needed for the selected increment. The [code map](docs/system/code-map.md) is a planned inventory, not an instruction to create empty files. Production code must not import teaching reference solutions.
- CPU checks must not download models, initialize CUDA, start Kubernetes, or depend on the other track. Run paid/GPU/platform checks only within the authorized, prepared task environment.
- Treat exact framework versions, hardware fit and future course-material availability as evidence to establish, not assumptions. Record real pins and smoke results at implementation.
- Use independent numerical/state/artifact oracles. Keep evaluator truth outside the agent-accessible workspace. Preserve unknown tool outcomes and in-flight GPU ownership.

## Finish and leave a usable handoff

Update the owning task's status and completion record, link actual code/artifacts, record commands/outcomes and the next unfinished increment. Update affected design decisions and code-map paths in the same change. Do not create a second progress spreadsheet or claim the whole task complete from a passing scaffold.

Run the narrow checks appropriate to the change. For documentation/navigation changes, run:

```sh
python3 tools/check_docs.py
python3 -m unittest discover -s tests -v
```

These CPU checks validate repository structure and supplied utilities, not inference/agent performance. Repository metadata/CI scaffolding does not close FND-01 or AGT-01.

Keep résumés, secrets, downloaded weights, raw private trajectories and local recovery ZIPs out of commits. Do not rewrite frozen archives to repair their obsolete links. The declared GitHub URL is in the README; verify local/remote state before a requested publish operation. Never infer that a local change has been pushed.
