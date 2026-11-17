#!/usr/bin/env python3
"""Check Nivram's tracked memory contract; Python standard library only."""
from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / "context"
TYPES = set("principle constraint practice feedback decision research".split())
STATES = set("candidate active dormant archived superseded".split())
LIMITS = {"AGENTS.md": 5120, "CLAUDE.md": 2048, "context/index.md": 8192, "context/state.md": 4096}
COMMENT = re.compile(r"<!--.*?-->", re.S)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HEADER = re.compile(r"\A---\n(.*?)\n---(?:\n|$)", re.S)
KEY = re.compile(r"^([a-z][a-z0-9_]*):\s*(.*?)\s*$")
SENSITIVE = {
 "absolute home path": r"/Users/[^/\s)]+/",
 "credential-like string": r"(?i)\b(?:sk-[\w-]{16,}|gh[pousr]_[\w-]{16,}|github_pat_[\w-]{16,})\b",
 "personal email": r"(?i)\b[\w.+-]+@[\w.-]+\.[a-z]{2,}\b",
 "private Marvin repository URL": r"https?://github\.com/aigora-de/marvin(?:/|\b)",
}

def clean_value(v):
    if len(v) > 1 and v[0] == v[-1] and v[0] in ("'", '"'):
        return v[1:-1]
    return v

def parse(text, label, errors):
    m = HEADER.match(text)
    if not m:
        errors.append(f"{label}: missing frontmatter")
        return {}
    result = {}
    last = None
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith("  - "):
            if not last or not isinstance(result.get(last), list):
                errors.append(f"{label}: unexpected YAML item")
            else:
                val = clean_value(line[4:].strip())
                if not val: errors.append(f"{label}: empty {last} list item")
                result[last].append(val)
            continue
        match = KEY.fullmatch(line)
        if not match:
            errors.append(f"{label}: unsupported YAML syntax: {line}")
            continue
        k, v = match.groups()
        if k in result: errors.append(f"{label}: duplicate key {k}")
        result[k] = clean_value(v) if v else []
        last = k if not v else None
    required = "id title type status source triggers created reviewed".split()
    for k in required:
        if not result.get(k): errors.append(f"{label}: missing/empty {k}")
    for k in ("source", "triggers"):
        if k in result and not isinstance(result[k], list):
            errors.append(f"{label}: {k} requires a nonempty list")
    for k in ("id", "title", "type", "status", "created", "reviewed"):
        if k in result and not isinstance(result[k], str):
            errors.append(f"{label}: {k} requires a scalar")
    if result.get("type") not in TYPES: errors.append(f"{label}: invalid type")
    if result.get("status") not in STATES: errors.append(f"{label}: invalid status")
    for k in ("created", "reviewed"):
        v = result.get(k)
        if isinstance(v, str):
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v): raise ValueError()
                date.fromisoformat(v)
            except ValueError: errors.append(f"{label}: invalid {k} date {v}")
    for source in result.get("source", []) if isinstance(result.get("source"), list) else []:
        if source.startswith("attested:"):
            if not source[9:].strip(): errors.append(f"{label}: empty attestation")
        elif "://" in source:
            errors.append(f"{label}: unqualified external source (use attested:): {source}")
        elif not (ROOT / source.split("#")[0]).is_file():
            errors.append(f"{label}: missing source file {source}")
    return result

def links(p):
    if not p.is_file(): return set()
    content = COMMENT.sub("", p.read_text(encoding="utf-8"))
    return {(p.parent / ref.split("#")[0]).resolve()
            for ref in LINK.findall(content) if "://" not in ref and not ref.startswith("#")}

def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("--strict", action="store_true")
    strict = arg.parse_args().strict
    errors, warnings = [], []
    for name, cap in LIMITS.items():
        p = ROOT / name
        if not p.is_file(): errors.append(f"missing {name}")
        elif p.stat().st_size > cap: warnings.append(f"{name}: exceeds {cap} bytes")
    claude = ROOT / "CLAUDE.md"
    if claude.is_file() and not re.search(r"(?m)^@AGENTS\.md\s*$", COMMENT.sub("", claude.read_text(encoding="utf-8"))):
        errors.append("CLAUDE.md: missing active @AGENTS.md import")
    records, active, inactive = {}, set(), set()
    for base in (C / "memory", C / "archive"):
        for p in sorted(base.rglob("*.md")) if base.is_dir() else []:
            if p.name == "index.md": continue
            label = str(p.relative_to(ROOT))
            meta = parse(p.read_text(encoding="utf-8"), label, errors)
            ident = meta.get("id")
            if isinstance(ident, str):
                if ident in records: errors.append(f"duplicate id {ident}")
                records[ident] = (p, meta)
            status = meta.get("status")
            if base.name == "archive" and status != "archived":
                errors.append(f"{label}: non-archived record in archive")
            if base.name == "memory" and status == "archived":
                errors.append(f"{label}: archived status outside archive")
            (active if status == "active" else inactive).add(p.resolve())
            if status in ("dormant", "archived", "superseded") and not meta.get("transition_reason"):
                errors.append(f"{label}: missing transition_reason")
            if meta.get("superseded_by") and status != "superseded":
                errors.append(f"{label}: successor on non-superseded record")
            if p.stat().st_size > (102400 if base.name == "archive" else 16384):
                warnings.append(f"{label}: over topic budget")
    for ident, (p, meta) in records.items():
        successor = meta.get("superseded_by")
        if successor and (not isinstance(successor, str) or successor not in records):
            errors.append(f"{p.relative_to(ROOT)}: nonexistent successor {successor}")
        seen = set()
        at = ident
        while at in records and at not in seen:
            seen.add(at)
            at = records[at][1].get("superseded_by")
            if not isinstance(at, str): break
        if isinstance(at, str) and at in seen:
            errors.append(f"supersession cycle: {ident}")
    ai, hi = C / "index.md", C / "archive" / "index.md"
    if not ai.is_file() or not hi.is_file():
        errors.append("active and historical indices required")
    ar, hr = links(ai), links(hi)
    for p in active - ar: errors.append(f"{p.relative_to(ROOT)}: missing active route")
    for p in inactive - hr: errors.append(f"{p.relative_to(ROOT)}: missing historical route")
    for p in inactive & ar: errors.append(f"{p.relative_to(ROOT)}: inactive record in active index")
    for p in active & hr: errors.append(f"{p.relative_to(ROOT)}: active record in historical index")
    all_records = active | inactive
    for index, routes in ((ai, ar), (hi, hr)):
        for target in routes:
            if target.is_relative_to(C / "memory") or target.is_relative_to(C / "archive"):
                if target not in all_records and target.name != "index.md":
                    errors.append(f"{index.relative_to(ROOT)}: unknown memory route {target}")
    paths = [ROOT / "AGENTS.md", claude, C / "README.md", ai, hi, C / "state.md"]
    paths += list((C / "memory").rglob("*.md")) + list((C / "archive").rglob("*.md"))
    paths += list((ROOT / "personas").rglob("*.md"))
    for p in dict.fromkeys(paths):
        if not p.is_file(): continue
        text = p.read_text(encoding="utf-8")
        for target in links(p):
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{p.relative_to(ROOT)}: broken link to {target}")
        for reason, pattern in SENSITIVE.items():
            if re.search(pattern, text):
                warnings.append(f"{p.relative_to(ROOT)}: possible disclosure: {reason}")
    agent = ROOT / "AGENTS.md"
    if agent.is_file():
        for name in re.findall(r"\x60((?:docs|context|personas)/[\w./-]+\.md)\x60", agent.read_text(encoding="utf-8")):
            if not (ROOT / name).is_file():
                errors.append(f"AGENTS.md: broken referenced path {name}")
    print(f"Checked {len(records)} memory IDs; {len(active)} active routes.")
    for w in warnings: print("WARN:", w)
    for e in errors: print("FAIL:", e)
    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
    return int(bool(errors or (strict and warnings)))

if __name__ == "__main__":
    sys.exit(main())
