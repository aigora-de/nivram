#!/usr/bin/env python3
"""Validate Nivram's tracked, model-neutral context and routing surfaces.

No external dependencies, no model-provider tooling. Safe read-only check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT / "context"
SOFT_LIMITS = {
    "AGENTS.md": 5 * 1024,
    "CLAUDE.md": 2 * 1024,
    "context/index.md": 8 * 1024,
    "context/state.md": 4 * 1024,
}
VALID_TYPES = {"principle", "constraint", "feedback", "decision", "research"}
VALID_STATUSES = {"candidate", "active", "dormant", "archived", "superseded"}
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")
ID = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
FIELD = lambda name: re.compile(rf"^{name}:\s*(.*?)\s*$", re.MULTILINE)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[str] = []
    for relative, limit in SOFT_LIMITS.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
        elif path.stat().st_size > limit:
            warnings.append(f"{relative} exceeds {limit} bytes")
        else:
            checks.append(f"{relative}: budget OK")

    index = CONTEXT / "index.md"
    indexed = index.read_text() if index.exists() else ""
    discovered: dict[str, Path] = {}
    active_paths = []
    for path in sorted((CONTEXT / "memory").rglob("*.md")):
        rel = path.relative_to(ROOT)
        data = path.read_text()
        if not data.startswith("---\n") or "\n---\n" not in data[4:]:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        fm = data.split("\n---\n", 1)[0]
        ident = ID.search(fm)
        if not ident:
            errors.append(f"{rel}: missing id")
        elif ident.group(1) in discovered:
            errors.append(f"{rel}: duplicate id {ident.group(1)}")
        else:
            discovered[ident.group(1)] = path
        typ = FIELD("type").search(fm)
        status = FIELD("status").search(fm)
        if not typ or typ.group(1) not in VALID_TYPES:
            errors.append(f"{rel}: invalid or missing type")
        if not status or status.group(1) not in VALID_STATUSES:
            errors.append(f"{rel}: invalid or missing status")
        if not FIELD("source").search(fm):
            errors.append(f"{rel}: missing provenance source")
        if not FIELD("triggers").search(fm):
            errors.append(f"{rel}: missing routing triggers")
        if not FIELD("created").search(fm) or not FIELD("reviewed").search(fm):
            errors.append(f"{rel}: missing creation/review date")
        if path.stat().st_size > 16 * 1024:
            warnings.append(f"{rel}: topic exceeds 16 KiB soft cap")
        if status and status.group(1) == "active":
            target = path.relative_to(CONTEXT).as_posix()
            active_paths.append(target)
            if f"({target})" not in indexed:
                errors.append(f"{rel}: active memory not routed by context/index.md")
        elif status and status.group(1) != "active":
            target = path.relative_to(CONTEXT).as_posix()
            if f"({target})" in indexed:
                errors.append(f"{rel}: inactive memory still in active index")

    for path in [ROOT / "AGENTS.md", ROOT / "CLAUDE.md", *CONTEXT.rglob("*.md")]:
        if not path.is_file():
            continue
        data = path.read_text()
        for target in LINK.findall(data):
            if "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken/out-of-repo link {target}")
        if path.is_relative_to(CONTEXT / "archive") and path.suffix == ".md":
            if path.stat().st_size > 100 * 1024:
                warnings.append(f"{path.relative_to(ROOT)}: archive exceeds 100 KiB soft cap")

    if not (ROOT / "CLAUDE.md").read_text().count("@AGENTS.md"):
        errors.append("CLAUDE.md: missing @AGENTS.md import")
    if not active_paths:
        warnings.append("no active memory topics")
    print(f"Checked {len(discovered)} memory IDs, {len(active_paths)} active routes.")
    for msg in checks:
        print("OK:   " + msg)
    for msg in warnings:
        print("WARN: " + msg)
    for msg in errors:
        print("FAIL: " + msg)
    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
