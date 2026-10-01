"""Checks for the supplied offline documentation auditor, not project runtime tests."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "check_docs", Path(__file__).resolve().parents[1] / "tools/check_docs.py"
)
docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(docs)


class DocumentationChecks(unittest.TestCase):
    def test_heading_duplicates_explicit_anchor_and_fenced_example(self):
        text = '# A **title**\n## A title\n<a id="stable"></a>\n```md\n# Not a heading\n```\n'
        self.assertEqual(docs.anchors(text), {"a-title", "a-title-1", "stable"})

    def test_links_resolve_from_document_not_working_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / 'nested').mkdir()
            (root / 'target.md').write_text('# Good anchor\n')
            page = root / 'nested/source.md'
            page.write_text('[ok](../target.md#good-anchor)\n[bad](../target.md#missing)\n'
                            '[absent](gone.md)\n[remote](https://example.invalid/)\n'
                            '```md\n[example](not-a-real-file.md)\n```\n')
            errors, count = docs.link_errors(root, [page])
            self.assertEqual(count, 3)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any('missing anchor' in e for e in errors))
            self.assertTrue(any('missing target' in e for e in errors))

    def test_duplicate_explicit_anchor_is_an_error(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            page = root / 'README.md'
            page.write_text('<a id="same"></a>\n<a id="same"></a>\n')
            errors, _ = docs.link_errors(root, [page])
            self.assertEqual(len(errors), 1)
            self.assertIn('duplicate explicit anchor', errors[0])

    def test_independent_dags_pass(self):
        self.assertEqual(docs.dependency_errors({
            'FND-01': [], 'SCH-01': ['FND-01'], 'AGT-01': [], 'AGT-02': ['AGT-01']
        }), [])

    def test_cycle_missing_and_cross_track_dependencies_fail(self):
        errors = docs.dependency_errors({
            'FND-01': ['SCH-01'], 'SCH-01': ['FND-01'],
            'AGT-01': ['FND-01', 'ABSENT-01']
        })
        self.assertTrue(any('cycle' in e for e in errors))
        self.assertTrue(any('missing dependency' in e for e in errors))
        self.assertTrue(any('cross-track' in e for e in errors))

    def test_optional_prose_links_do_not_become_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'tracks/inference/tasks').mkdir(parents=True)
            (root / 'tracks/agents').mkdir()
            (root / 'tracks/inference/tasks/example.md').write_text(
                '## BEN-04 — Replay\n**Status:** planned.\n'
                '**Dependencies:** [BEN-02](example.md#ben-02). Optional [AGT-04](other.md).\n'
                '### BEN-04 startup sequence\nA substep is not a new task.\n'
                '## BEN-02 — Load\n**Status:** planned.\n**Dependencies:** none.\n'
            )
            (root / 'tracks/agents/ROADMAP.md').write_text(
                '### AGT-01 — Contracts\n**Status:** planned.\n'
                '**Dependencies:** None. **Design:** [owner](RUNTIME.md).\n'
            )
            tasks, errors = docs.read_tasks(root)
            self.assertEqual(errors, [])
            self.assertEqual(tasks, {'BEN-04': ['BEN-02'], 'BEN-02': [], 'AGT-01': []})


if __name__ == '__main__':
    unittest.main()
