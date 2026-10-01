"""Tests protect budget units and artifact integrity, not serving performance."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from starter.experiment import budget, create_bundle, read_json, sha256

ROOT = Path(__file__).resolve().parents[1]


class BudgetTests(unittest.TestCase):
    def setUp(self):
        self.plan = read_json(ROOT / "starter/budget.example.json")

    def test_published_example_units_and_total(self):
        result = budget(self.plan)
        self.assertEqual(result["node_hours"], 120)
        self.assertEqual(result["gpu_hours"], 150)
        self.assertEqual(result["compute_usd"], 185.5)
        self.assertEqual(result["total_before_tax_usd"], 280.15)

    def test_multi_node_price_is_not_multiplied_by_gpus_twice(self):
        result = budget({"phases": [{"name": "fixture", "nodes": 2,
                         "gpus_per_node": 4, "wall_hours": 3,
                         "usd_per_node_hour": 10}]})
        self.assertEqual(result["node_hours"], 6)
        self.assertEqual(result["gpu_hours"], 24)
        self.assertEqual(result["compute_usd"], 60)

    def test_zero_price_allocation_is_valid(self):
        self.plan["phases"][0]["usd_per_node_hour"] = 0
        self.assertEqual(budget(self.plan)["phases"][0]["compute_usd"], 0)

    def test_reject_bad_values(self):
        for field, bad in [("wall_hours", -1), ("wall_hours", float("nan")),
                           ("usd_per_node_hour", float("inf")),
                           ("gpus_per_node", 1.5), ("nodes", True), ("nodes", 0)]:
            with self.subTest(field=field, value=bad):
                plan = copy.deepcopy(self.plan)
                plan["phases"][0][field] = bad
                with self.assertRaises(ValueError):
                    budget(plan)

    def test_hardware_substitution(self):
        self.plan["phases"][1]["usd_per_node_hour"] = 3.98
        self.assertEqual(budget(self.plan)["total_before_tax_usd"], 350.35)


class BundleTests(unittest.TestCase):
    def test_unique_runs_snapshot_hash_and_no_fake_results(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = ROOT / "starter/run.example.json"
            first = create_bundle(config, root, [config])
            second = create_bundle(config, root, [])
            self.assertNotEqual(first, second)
            manifest = json.loads((first / "manifest.json").read_text())
            self.assertEqual(manifest["config_sha256"], sha256(first / "config.json"))
            self.assertEqual(manifest["artifacts"][0]["sha256"], sha256(config))
            self.assertEqual(manifest["status"], "prepared_no_measurements")
            self.assertEqual(manifest["measurement_kind"], "fixture")
            self.assertEqual((first / "observations.jsonl").stat().st_size, 0)

    def test_invalid_config_does_not_create_run(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = root / "bad.json"
            config.write_text('{"experiment": "incomplete"}')
            with self.assertRaises(ValueError):
                create_bundle(config, root / "runs", [])
            self.assertFalse((root / "runs").exists())

    def test_missing_artifact_does_not_create_run(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaises(ValueError):
                create_bundle(ROOT / "starter/run.example.json", root / "runs", [root / "missing"])
            self.assertFalse((root / "runs").exists())


if __name__ == "__main__":
    unittest.main()
