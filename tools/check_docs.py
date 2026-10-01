"""Supplied repository maintenance: check active docs and task structure, offline.

Scope: Markdown inline local links, explicit/heading anchors, canonical task
dependencies, track independence and preserved scope IDs. This is deliberately
not a general Markdown renderer, remote-link checker or implementation validator.
See docs/HANDOFF.md. Planned source paths in backticks need not exist.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[([^\]]*)\]\(([^\s)]+)\)")
TASK = re.compile(r"^#{2,3} ((?:[A-Z]+)-\d+) —[^\n]*$", re.MULTILINE)
EXPLICIT_ID = re.compile(r"\bid=[\"']([^\"']+)[\"']")


def visible_markdown(text: str) -> str:
    """Ignore fenced examples, preserving line positions for diagnostics."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            lines.append("\n")
        else:
            lines.append("\n" if fence else line)
    return "".join(lines)


def anchors(text: str) -> set[str]:
    text = visible_markdown(text)
    result = set(EXPLICIT_ID.findall(text))
    seen: Counter[str] = Counter()
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        title = LINK.sub(r"\1", title)
        title = re.sub(r"<[^>]+>", "", title).replace("`", "").replace("*", "")
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        index = seen[slug]
        seen[slug] += 1
        result.add(slug + (f"-{index}" if index else ""))
    return result


def active_docs(root: Path) -> list[Path]:
    roots = [root / name for name in ("docs", "tracks", "teaching", "starter")]
    candidates = list(root.glob("*.md"))
    for directory in roots:
        candidates.extend(directory.rglob("*.md"))
    return sorted(p for p in candidates if not (
        p.relative_to(root).as_posix().startswith("docs/archive/")
        and p.relative_to(root).as_posix() not in (
            "docs/archive/README.md", "docs/archive/scope-map.md"
        )
    ))


def link_errors(root: Path, paths: list[Path]) -> tuple[list[str], int]:
    errors = []
    count = 0
    cache = {}
    for path in paths:
        text = visible_markdown(path.read_text())
        duplicate_ids = [key for key, n in Counter(EXPLICIT_ID.findall(text)).items() if n > 1]
        for anchor in duplicate_ids:
            errors.append(f"{path.relative_to(root)}: duplicate explicit anchor {anchor}")
        for match in LINK.finditer(text):
            url = urlsplit(match.group(2))
            if url.scheme or url.netloc:
                continue
            count += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            location = f"{path.relative_to(root)}:{text[:match.start()].count(chr(10)) + 1}"
            if not target.is_relative_to(root):
                errors.append(f"{location}: local link escapes repository: {match.group(2)}")
                continue
            if not target.exists():
                errors.append(f"{location}: missing target {match.group(2)}")
                continue
            if url.fragment and target.suffix == ".md":
                if target not in cache:
                    cache[target] = anchors(target.read_text())
                if unquote(url.fragment) not in cache[target]:
                    errors.append(f"{location}: missing anchor {match.group(2)}")
    return errors, count


def read_tasks(root: Path) -> tuple[dict[str, list[str]], list[str]]:
    paths = sorted((root / "tracks/inference/tasks").glob("*.md"))
    paths.append(root / "tracks/agents/ROADMAP.md")
    tasks = {}
    errors = []
    for path in paths:
        if not path.exists():
            errors.append(f"Missing task source: {path.relative_to(root)}")
            continue
        text = path.read_text()
        matches = list(TASK.finditer(text))
        for i, match in enumerate(matches):
            task = match.group(1)
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            body = text[match.end():end]
            dep = re.search(r"\*\*Dependencies:\*\* ([^\n]+)", body)
            if dep is None:
                errors.append(f"{task}: missing Dependencies field")
                continue
            # Only the declared dependency sentence; following prose may link
            # optional reports or explicitly nonblocking study prerequisites.
            prefix = dep.group(1).split(". ", 1)[0]
            if task in tasks:
                errors.append(f"Duplicate task owner: {task}")
            tasks[task] = re.findall(r"\[([A-Z]+-\d+)\]", prefix)
            if not re.search(r"\*\*Status:\*\*", body):
                errors.append(f"{task}: missing Status field")
    return tasks, errors


def dependency_errors(tasks: dict[str, list[str]]) -> list[str]:
    errors = []
    done = set()
    active = []

    def visit(task: str) -> None:
        if task in active:
            errors.append("Dependency cycle: " + " -> ".join(active + [task]))
            return
        if task in done:
            return
        active.append(task)
        for dependency in tasks[task]:
            if dependency not in tasks:
                errors.append(f"{task}: missing dependency {dependency}")
                continue
            if task.startswith("AGT-") != dependency.startswith("AGT-"):
                errors.append(f"Mandatory cross-track edge: {task} -> {dependency}")
            visit(dependency)
        active.pop()
        done.add(task)

    for task in tasks:
        visit(task)
    return errors


def scope_errors(root: Path, paths: list[Path], tasks: dict[str, list[str]]) -> list[str]:
    """Retained IDs are floors, not ceilings on future documented work."""
    errors = []
    counts = {"FND": 4, "MOD": 4, "KV": 4, "SCH": 5, "GPU": 4,
              "SRV": 2, "BEN": 4, "PLT": 5, "ADV": 4, "REL": 3, "AGT": 14}
    required_tasks = {f"{key}-{i:02}" for key, n in counts.items() for i in range(1, n + 1)}
    required_tasks |= {f"PF-{i}" for i in range(1, 5)}
    for task in sorted(required_tasks - tasks.keys()):
        errors.append("Missing required task owner: " + task)
    all_ids = set().union(*(anchors(p.read_text()) for p in paths))
    required_ids = {f"module-{i:02}" for i in range(25)}
    required_ids |= {f"module-b{i}" for i in range(1, 7)}
    required_ids |= {f"module-pf-{i}" for i in range(1, 5)} | {"module-ag-1"}
    required_ids |= {f"at-{i:02}" for i in range(16)}
    for anchor in sorted(required_ids - all_ids):
        errors.append("Missing required teaching anchor: " + anchor)
    agent_ids = anchors((root / "tracks/agents/ROADMAP.md").read_text())
    for alias in ["app-01", "app-02", "app-03", "app-04", "ag-1a", "ag-1b", "ag-1c"]:
        if alias not in agent_ids:
            errors.append("Missing legacy task alias: " + alias)
    scope = (root / "docs/archive/scope-map.md").read_text()
    actual = set(re.findall(r"^\| ([A-J]\.\d+) \|", scope, re.MULTILINE))
    counts = dict(A=6, B=7, C=7, D=6, E=6, F=6, G=8, H=5, I=7, J=6)
    expected = {f"{key}.{i}" for key, n in counts.items() for i in range(1, n + 1)}
    for item in sorted(expected - actual):
        errors.append("Missing original scope item: " + item)
    return errors


def audit(root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    paths = active_docs(root)
    errors, links = link_errors(root, paths)
    tasks, task_errors = read_tasks(root)
    errors += task_errors + dependency_errors(tasks)
    errors += scope_errors(root, paths, tasks)
    return errors, {"documents": len(paths), "local_links": links, "tasks": len(tasks)}


def main() -> int:
    errors, counts = audit()
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {counts['documents']} active Markdown documents, "
          f"{counts['local_links']} local links and {counts['tasks']} task owners.")
    print(f"FAIL: {len(errors)} issues" if errors else "PASS: links, task graph and required scope IDs")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
