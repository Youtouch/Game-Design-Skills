"""Tests for skills/balance-table-check/balance_check.py. Run: python -m unittest discover tests"""
import contextlib
import io
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, "..", "skills", "balance-table-check")
sys.path.insert(0, SKILL)

import balance_check  # noqa: E402


def run(csv_text, *args):
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        f.write(csv_text)
        path = f.name
    out, err = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = balance_check.main([path, *args])
    finally:
        os.unlink(path)
    return code, out.getvalue(), err.getvalue()


class Dominance(unittest.TestCase):
    def test_strict_dominance(self):
        code, out, _ = run("name,cost,dmg\nA,10,5\nB,10,4\n")
        self.assertEqual(code, 0)
        self.assertIn("A dominates B", out)
        self.assertNotIn("B dominates A", out)

    def test_lower_is_better_direction(self):
        code, out, _ = run("name,cost,cd\nA,10,1\nB,10,2\n", "--lower", "cd")
        self.assertIn("A dominates B", out)

    def test_cheaper_dominates(self):
        _, out, _ = run("name,cost,dmg\nA,5,4\nB,10,4\n")
        self.assertIn("A dominates B", out)

    def test_identical_rows_reported_once(self):
        _, out, _ = run("name,cost,a\nX,10,1\nY,10,1\n")
        self.assertEqual(out.count("identical"), 1)

    def test_tradeoff_is_not_dominance(self):
        _, out, _ = run("name,cost,dmg,hp\nA,10,5,1\nB,10,1,5\n")
        self.assertIn("- none", out)


class Inputs(unittest.TestCase):
    def test_label_columns_are_skipped(self):
        code, out, _ = run("name,role,cost,dmg\nA,x,10,5\nB,y,10,4\n")
        self.assertEqual(code, 0)
        self.assertIn("Skipped non-numeric columns: role", out)

    def test_unknown_lower_column_is_an_error(self):
        code, _, err = run("name,cost,cd\nA,10,1\nB,10,2\n", "--lower", "cdd")
        self.assertEqual(code, 2)
        self.assertIn("cdd", err)

    def test_duplicate_names_rejected(self):
        code, _, err = run("name,cost,a\nX,1,1\nX,2,2\n")
        self.assertEqual(code, 2)
        self.assertIn("duplicate", err)

    def test_negative_cost_rejected(self):
        code, _, _ = run("name,cost,a\nX,-1,1\nY,2,2\n")
        self.assertEqual(code, 2)

    def test_non_finite_stat_is_label_not_crash(self):
        code, out, _ = run("name,cost,a,b\nX,1,1,inf\nY,2,2,3\n")
        self.assertEqual(code, 0)
        self.assertIn("Skipped non-numeric columns: b", out)

    def test_bad_tolerance(self):
        code, _, _ = run("name,cost,a\nX,1,1\nY,2,2\n", "--tol", "-1")
        self.assertEqual(code, 2)

    def test_group_must_be_label(self):
        code, _, _ = run("name,cost,a\nX,1,1\nY,2,2\n", "--group", "a")
        self.assertEqual(code, 2)


class CostCurve(unittest.TestCase):
    TABLE = ("name,cost,dmg,hp\n"
             "A,30,10,5\nB,50,10,15\nC,70,20,5\nD,90,20,15\n"
             "F,60,15,10\nG,80,25,5\nH,40,5,10\nE,25,10,15\n")

    def test_fit_recovers_exact_linear_costs_and_flags_outlier(self):
        # A-H follow cost = 10 + 2*dmg + 2*hp exactly; E (fair 50) costs 25.
        code, out, _ = run(self.TABLE)
        self.assertEqual(code, 0)
        self.assertIn("least-squares fit", out)
        line = next(l for l in out.splitlines() if l.startswith("| E "))
        self.assertIn("underpriced", line)

    def test_too_few_rows_for_fit(self):
        _, out, _ = run("name,cost,a,b\nX,1,1,2\nY,2,2,1\n")
        self.assertIn("supply --weights", out)

    def test_design_weights_scale_to_total_cost(self):
        _, out, _ = run("name,cost,dmg\nA,10,1\nB,30,3\n", "--weights", "dmg=1")
        self.assertIn("fair cost = 0 + 10*dmg", out)
        self.assertNotIn("underpriced", out)

    def test_zero_cost_does_not_divide(self):
        _, out, _ = run("name,cost,dmg\nA,0,5\nB,10,5\n", "--weights", "dmg=1")
        self.assertIn("free: review", out)
        self.assertNotIn("inf", out)

    def test_wrong_sign_weight_note(self):
        table = ("name,cost,dmg,cd\n"
                 "A,15,1,1\nB,25,2,1\nC,25,1,3\nD,40,3,2\nE,40,2,4\n")
        _, out, _ = run(table, "--lower", "cd")
        # cost = 10*dmg + 5*cd: higher cooldown is priced as a benefit.
        self.assertIn("opposite sign", out)

    def test_no_sign_note_from_rounding_noise(self):
        table = ("name,cost,dmg,cd\n"
                 "A,10,1,1\nB,20,2,2\nC,30,3,3\nD,40,4,5\nE,50,5,4\n")
        _, out, _ = run(table, "--lower", "cd")
        self.assertNotIn("opposite sign", out)
        self.assertIn("fair cost = 0 + 10*dmg + 0*cd", out)

    def test_groups_are_separate(self):
        table = "name,role,cost,dmg\nA,x,10,5\nB,x,10,4\nC,y,10,1\n"
        _, out, _ = run(table, "--group", "role")
        self.assertIn("Group: role = x", out)
        self.assertIn("A dominates B", out)
        self.assertNotIn("dominates C", out)


if __name__ == "__main__":
    unittest.main()
