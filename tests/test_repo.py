import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import analyze

class ModelTests(unittest.TestCase):
    def test_scenario_ranks_cover_all_products(self):
        for scenario in analyze.scenarios:
            ranking = analyze.evaluate(analyze.RATINGS, scenario)
            self.assertEqual(len(ranking), len(analyze.environments))
            self.assertEqual(len({row[0]["id"] for row in ranking}), len(analyze.environments))

    def test_rust_scenario_has_explicit_rust_and_tauri_majority(self):
        scenario = next(s for s in analyze.scenarios if s["id"] == "rust")
        self.assertGreater(scenario["stack"]["rust"], 50)
        self.assertGreater(scenario["stack"]["tauri"], scenario["stack"]["web"])

    def test_weighted_scores_stay_in_range(self):
        for scenario in analyze.scenarios:
            for candidate in analyze.environments:
                low, high = analyze.score_range(analyze.RATINGS[candidate["id"]], scenario)
                self.assertGreaterEqual(low, 1)
                self.assertLessEqual(high, 10)
                self.assertLessEqual(low, high)

if __name__ == "__main__":
    unittest.main()
