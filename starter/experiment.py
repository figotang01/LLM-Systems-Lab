#!/usr/bin/env python3
"""Supplied InferLab artifact/budget plumbing. No GPU, network, or dependencies.

This deliberately does not compute serving metrics: that is a learner task.
Only explicitly supplied configuration and artifact files are read/recorded.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import uuid


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def nonnegative(value: object, name: str) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Decimal)):
        raise ValueError(f"{name}: expected a finite nonnegative number")
    try:
        number = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"{name}: invalid number") from exc
    if not number.is_finite() or number < 0:
        raise ValueError(f"{name}: expected a finite nonnegative number")
    return number


def positive_integer(value: object, name: str) -> int:
    number = nonnegative(value, name)
    if number < 1 or number != number.to_integral_value():
        raise ValueError(f"{name}: expected a positive integer")
    return int(number)


def budget(plan: dict) -> dict:
    """Rates are PER NODE-hour. gpu_count affects GPU-hours, not billing twice.

    A phase's wall_hours is time per rented node including setup/idle time.
    Example: 2 nodes x 3 hours x 4 GPUs = 6 node-hours and 24 GPU-hours.
    """
    phases = plan.get("phases")
    if not isinstance(phases, list) or not phases:
        raise ValueError("phases must be a nonempty list")
    rows = []
    compute = Decimal(0)
    total_node_hours = Decimal(0)
    total_gpu_hours = Decimal(0)
    for i, phase in enumerate(phases):
        if not isinstance(phase, dict):
            raise ValueError(f"phase {i}: expected an object")
        name = phase.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"phase {i}: a nonempty name is required")
        nodes = positive_integer(phase.get("nodes", 1), f"{name}.nodes")
        gpus = positive_integer(phase.get("gpus_per_node"), f"{name}.gpus_per_node")
        hours = nonnegative(phase.get("wall_hours"), f"{name}.wall_hours")
        rate = nonnegative(phase.get("usd_per_node_hour"), f"{name}.rate")
        node_hours = nodes * hours
        gpu_hours = node_hours * gpus
        cost = node_hours * rate
        total_node_hours += node_hours
        total_gpu_hours += gpu_hours
        compute += cost
        rows.append({"name": name, "node_hours": float(node_hours),
                     "gpu_hours": float(gpu_hours), "compute_usd": float(cost)})
    other = nonnegative(plan.get("other_usd", 0), "other_usd")
    contingency = nonnegative(plan.get("contingency_fraction", 0), "contingency_fraction")
    subtotal = compute + other
    total = subtotal * (1 + contingency)
    if not all(math.isfinite(float(x)) for x in (total_node_hours, total_gpu_hours, total)):
        raise ValueError("budget values too large to serialize")
    return {"phases": rows, "node_hours": float(total_node_hours),
            "gpu_hours": float(total_gpu_hours), "compute_usd": float(compute),
            "other_usd": float(other), "subtotal_usd": float(subtotal),
            "contingency_usd": float(subtotal * contingency),
            "total_before_tax_usd": float(total),
            "note": "Planning estimate; no instances created and no live pricing queried."}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_state(directory: Path) -> dict:
    """Read commit/dirty state; no file contents, remote URLs or credentials."""
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=directory,
                                capture_output=True, text=True, check=True, timeout=3)
        status = subprocess.run(["git", "status", "--porcelain"], cwd=directory,
                                capture_output=True, text=True, check=True, timeout=3)
        return {"commit": commit.stdout.strip(), "dirty": bool(status.stdout.strip())}
    except (OSError, subprocess.SubprocessError):
        return {"commit": None, "dirty": None}


def validate_run_config(config: dict) -> None:
    for field in ("experiment", "hypothesis", "engine", "model", "hardware", "workload"):
        if not isinstance(config.get(field), str) or not config[field].strip():
            raise ValueError(f"run config needs a nonempty string: {field}")
    # This is a scaffold validator, not certification of reproducibility.
    if config.get("measurement_kind") not in ("fixture", "simulation", "measured"):
        raise ValueError("measurement_kind must be fixture, simulation or measured")


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def create_bundle(config_path: Path, output_root: Path, artifacts: list[Path]) -> Path:
    """Snapshot inputs and create an empty result workspace without overwriting runs."""
    config = read_json(config_path)
    validate_run_config(config)
    entries = []
    for artifact in artifacts:
        if not artifact.is_file():
            raise ValueError(f"artifact is not a file: {artifact}")
        entries.append({"name": artifact.name, "sha256": sha256(artifact),
                        "bytes": artifact.stat().st_size})
    # Validate JSON before creating directories. Credentials should never be in config.
    encoded = json.dumps(config, indent=2, allow_nan=False) + "\n"
    now = datetime.now(timezone.utc)
    run_id = now.strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:12]
    target = output_root / run_id
    target.mkdir(parents=True, exist_ok=False)
    config_copy = target / "config.json"
    config_copy.write_text(encoded, encoding="utf-8")
    manifest = {
        "schema_version": 1, "run_id": run_id, "created_utc": now.isoformat(),
        "measurement_kind": config["measurement_kind"],
        "status": "prepared_no_measurements", "config_sha256": sha256(config_copy),
        "python": platform.python_version(), "os": platform.system(),
        "machine": platform.machine(), "git": git_state(Path.cwd()),
        "artifacts": entries,
        "provenance_note": "Model/driver/image revisions must be supplied in config. "
                           "No environment variables or GPU data were automatically captured.",
    }
    write_json(target / "manifest.json", manifest)
    (target / "observations.jsonl").touch(exist_ok=False)
    (target / "REPORT.md").write_text(
        "# " + config["experiment"] + "\n\n"
        "Status: prepared; no measurements collected by this utility.\n\n"
        "Hypothesis: " + config["hypothesis"] + "\n\n"
        "## Setup\n\nSee config.json and manifest.json. Record all missing revisions, "
        "SLOs, cache state, warmup, timing definitions and topology.\n\n"
        "## Results\n\nPending real observations; do not report example fixtures as benchmarks.\n\n"
        "## Explanation and limitations\n\nPending analysis, uncertainty and failure accounting.\n\n"
        "## Reproduce\n\nAdd the exact tested command and required environment.\n",
        encoding="utf-8",
    )
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    estimate = commands.add_parser("budget", help="calculate explicit node-hour budget")
    estimate.add_argument("plan", type=Path)
    bundle = commands.add_parser("bundle", help="create a unique experiment workspace")
    bundle.add_argument("--config", required=True, type=Path)
    bundle.add_argument("--out", required=True, type=Path)
    bundle.add_argument("--artifact", action="append", default=[], type=Path,
                        help="explicit file to hash; content is not copied")
    args = parser.parse_args()
    try:
        if args.command == "budget":
            print(json.dumps(budget(read_json(args.plan)), indent=2, allow_nan=False))
        else:
            print(create_bundle(args.config, args.out, args.artifact))
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
