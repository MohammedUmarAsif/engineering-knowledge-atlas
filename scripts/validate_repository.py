#!/usr/bin/env python3
"""Validate repository structure, links, metadata, and writing-style rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
REQUIRED = ("id:", "title:", "level:", "status:", "last_reviewed:")
ID = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
PREREQUISITES = re.compile(r"^prerequisites:\s*\[([^]]*)\]\s*$", re.MULTILINE)
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".cff", ".py", ".cpp"}
EM_DASH = chr(0x2014)
JUSTIFIED_HTML = re.compile(
    r"(?:text-align\s*:\s*justify|align\s*=\s*['\"]?justify)", re.IGNORECASE
)


def validate_links() -> list[str]:
    failures: list[str] = []
    for document in ROOT.rglob("*.md"):
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (document.parent / target).resolve()
            if not resolved.exists():
                failures.append(f"{document.relative_to(ROOT)} -> {raw_target}")
    return failures


def validate_topic_metadata() -> list[str]:
    failures: list[str] = []
    topics = ROOT / "knowledge"
    for document in topics.rglob("*.md"):
        text = document.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            failures.append(f"{document.relative_to(ROOT)}: missing front matter")
            continue
        front_matter = text.split("---", 2)[1]
        missing = [field for field in REQUIRED if field not in front_matter]
        if missing:
            failures.append(
                f"{document.relative_to(ROOT)}: missing {', '.join(missing)}"
            )
    return failures


def validate_topic_graph() -> list[str]:
    failures: list[str] = []
    documents = list((ROOT / "knowledge").rglob("*.md"))
    locations: dict[str, list[Path]] = {}

    for document in documents:
        match = ID.search(document.read_text(encoding="utf-8"))
        if match:
            locations.setdefault(match.group(1), []).append(document)

    for topic_id, paths in locations.items():
        if len(paths) > 1:
            rendered = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            failures.append(f"duplicate topic id {topic_id}: {rendered}")

    known_ids = set(locations)
    graph: dict[str, list[str]] = {topic_id: [] for topic_id in known_ids}
    for document in documents:
        text = document.read_text(encoding="utf-8")
        topic_match = ID.search(text)
        match = PREREQUISITES.search(text)
        if not match or not topic_match:
            continue
        prerequisites = [item.strip() for item in match.group(1).split(",") if item.strip()]
        for prerequisite in prerequisites:
            if prerequisite not in known_ids:
                failures.append(
                    f"{document.relative_to(ROOT)}: unknown prerequisite {prerequisite}"
                )
            else:
                graph[topic_match.group(1)].append(prerequisite)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(topic_id: str, path: list[str]) -> None:
        if topic_id in visiting:
            start = path.index(topic_id)
            failures.append(f"prerequisite cycle: {' -> '.join(path[start:] + [topic_id])}")
            return
        if topic_id in visited:
            return
        visiting.add(topic_id)
        for prerequisite in graph[topic_id]:
            visit(prerequisite, path + [topic_id])
        visiting.remove(topic_id)
        visited.add(topic_id)

    for topic_id in graph:
        visit(topic_id, [])

    return failures


def validate_navigation_and_manifests() -> list[str]:
    failures: list[str] = []
    navigation = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    for document in (ROOT / "knowledge").rglob("*.md"):
        relative = str(document.relative_to(ROOT))
        if relative not in navigation:
            failures.append(f"{relative}: missing from mkdocs navigation")

    manifest = (ROOT / "library" / "manifests" / "resources.yml").read_text(
        encoding="utf-8"
    )
    resource_ids = re.findall(r"^\s+- id:\s*(\S+)\s*$", manifest, re.MULTILINE)
    seen: set[str] = set()
    for resource_id in resource_ids:
        if resource_id in seen:
            failures.append(f"duplicate resource id: {resource_id}")
        seen.add(resource_id)

    for overview in (ROOT / "knowledge" / "ai-engineering").glob("*/README.md"):
        text = overview.read_text(encoding="utf-8")
        for heading in ("## Diagnostic", "## Reading order"):
            if heading not in text:
                failures.append(f"{overview.relative_to(ROOT)}: missing {heading}")
    return failures


def validate_writing_style() -> list[str]:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name != ".gitignore":
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if EM_DASH in line:
                failures.append(
                    f"{path.relative_to(ROOT)}:{line_number}: em dash is disallowed"
                )
            if path.suffix == ".md" and JUSTIFIED_HTML.search(line):
                failures.append(
                    f"{path.relative_to(ROOT)}:{line_number}: justified HTML is disallowed"
                )
    return failures


def main() -> int:
    failures = (
        validate_links()
        + validate_topic_metadata()
        + validate_topic_graph()
        + validate_navigation_and_manifests()
        + validate_writing_style()
    )
    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    markdown_count = sum(1 for _ in ROOT.rglob("*.md"))
    print(
        f"Validated {markdown_count} Markdown files: "
        "structure, links, metadata, and style OK"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
