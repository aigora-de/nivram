"""Mutation regression tests; no repository files are changed."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TestContext(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name)
        for dirname in ("context", "personas", "docs", "scripts"):
            shutil.copytree(ROOT / dirname, self.base / dirname)
        for name in ("AGENTS.md", "CLAUDE.md"):
            shutil.copy2(ROOT / name, self.base / name)

    def run_checker(self):
        return subprocess.run([sys.executable, str(self.base / "scripts/check-context.py"),
                               "--strict"], capture_output=True, text=True)

    def change(self, path, a, b):
        file = self.base / path
        content = file.read_text(encoding="utf-8")
        self.assertIn(a, content)
        file.write_text(content.replace(a, b), encoding="utf-8")

    def fail_after(self, path, a, b):
        self.change(path, a, b)
        result = self.run_checker()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_clean(self):
        r = self.run_checker()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_empty_provenance_and_invalid_date(self):
        self.fail_after("context/memory/principles/empirical-first.md",
                        "source:\n  - docs/02-experimental-programme.md\n  - docs/03-research-questions-and-hypotheses.md", "source:")

    def test_bad_date(self):
        self.fail_after("context/memory/principles/empirical-first.md",
                        "created: 2026-11-17", "created: banana")

    def test_commented_route(self):
        self.fail_after("context/index.md",
                        "[Empirical first](memory/principles/empirical-first.md)",
                        "<!-- [Empirical first](memory/principles/empirical-first.md) -->")

    def test_inactive_still_routed(self):
        self.fail_after("context/memory/principles/empirical-first.md", "status: active", "status: dormant")

    def test_bad_successor(self):
        self.fail_after("context/memory/principles/empirical-first.md", "status: active",
                        "status: superseded\nsuperseded_by: missing-id\ntransition_reason: replaced")

    def test_archive_mismatch(self):
        shutil.move(str(self.base / "context/memory/principles/empirical-first.md"),
                    str(self.base / "context/archive/empirical-first.md"))
        self.assertNotEqual(self.run_checker().returncode, 0)

    def test_missing_persona(self):
        (self.base / "personas/systems-engineer.md").unlink()
        self.assertNotEqual(self.run_checker().returncode, 0)

    def test_missing_authoritative_doc(self):
        (self.base / "docs/02-experimental-programme.md").unlink()
        self.assertNotEqual(self.run_checker().returncode, 0)

    def test_commented_import(self):
        self.fail_after("CLAUDE.md", "@AGENTS.md", "<!-- @AGENTS.md -->")

    def test_missing_claude_no_traceback(self):
        (self.base / "CLAUDE.md").unlink()
        r = self.run_checker()
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("Traceback", r.stderr)

    def test_disclosure(self):
        p = self.base / "context/memory/principles/empirical-first.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n/Users/secretuser/keys\n", encoding="utf-8")
        self.assertNotEqual(self.run_checker().returncode, 0)

    def test_quoted_status(self):
        self.change("context/memory/principles/empirical-first.md", "status: active", "status: 'active'")
        r = self.run_checker()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
