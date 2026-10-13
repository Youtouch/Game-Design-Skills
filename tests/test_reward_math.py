"""Tests for skills/loot-table-design/reward_math.py. Run: python -m unittest discover tests"""
import contextlib
import io
import math
import os
import sys
import unittest
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "skills", "loot-table-design"))

import reward_math as rm  # noqa: E402


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = rm.main(list(args))
    return code, out.getvalue(), err.getvalue()


class Drop(unittest.TestCase):
    def test_geometric_mean_and_percentiles_match_closed_form(self):
        p = 0.02
        mean, out = rm.summarize(rm.drop_distribution(p), [50, 90])
        self.assertAlmostEqual(mean, 1 / p, places=6)
        for q in (50, 90):
            expected = math.ceil(math.log(1 - q / 100) / math.log(1 - p))
            self.assertEqual(out[q], expected)

    def test_hard_pity_mean(self):
        p, n = 0.02, 60
        mean, out = rm.summarize(rm.drop_distribution(p, pity=n), [99])
        self.assertAlmostEqual(mean, (1 - (1 - p) ** n) / p, places=9)
        self.assertEqual(out[99], n)

    def test_pmf_sums_to_one_with_soft_pity(self):
        total = sum(pr for _, pr in rm.drop_distribution(0.006, 90, 74, 0.06))
        self.assertAlmostEqual(total, 1.0, places=12)

    def test_certain_drop(self):
        mean, _ = rm.summarize(rm.drop_distribution(1.0), [50])
        self.assertEqual(mean, 1.0)

    def test_zero_chance_without_pity_rejected(self):
        code, _, err = run("drop", "--p", "0")
        self.assertEqual(code, 2)
        self.assertIn("--p", err)

    def test_zero_chance_with_pity_is_fixed_wait(self):
        code, out, _ = run("drop", "--p", "0", "--pity", "10")
        self.assertEqual(code, 0)
        self.assertIn("mean attempts: 10.00", out)


class Collect(unittest.TestCase):
    def test_equal_items_mean_is_n_harmonic(self):
        n = 8
        mean, _ = rm.summarize(rm.collect_equal_distribution(n), [50])
        self.assertAlmostEqual(mean, n * sum(1 / i for i in range(1, n + 1)), places=6)

    def test_weighted_mean_matches_inclusion_exclusion(self):
        w = [30, 30, 20, 10, 5, 5]
        p = [x / sum(w) for x in w]
        exact = sum((-1) ** (r + 1) / sum(c)
                    for r in range(1, len(p) + 1) for c in combinations(p, r))
        self.assertAlmostEqual(rm.collect_mean_weighted(p), exact, places=3)

    def test_simulation_is_reproducible(self):
        a = rm.collect_simulated([0.5, 0.5], 500, 7, [50, 90])
        b = rm.collect_simulated([0.5, 0.5], 500, 7, [50, 90])
        self.assertEqual(a, b)

    def test_bad_weights_rejected(self):
        code, _, _ = run("collect", "--weights", "1,0,2")
        self.assertEqual(code, 2)

    def test_bad_percentile_rejected(self):
        code, _, _ = run("drop", "--p", "0.1", "--percentiles", "100")
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
