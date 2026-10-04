"""Balance table audit: Pareto dominance and value/cost outliers.

Usage: python balance_check.py table.csv [--lower cost,cooldown] [--tol 0.15]
CSV needs a 'name' column, a 'cost' column and numeric stat columns.
Columns in --lower are better when smaller (cost is always lower-is-better).
Value per row = sum of stats normalised by column mean (equal weights).
"""
import argparse
import csv
import statistics


def load(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    stats = [c for c in rows[0] if c not in ("name", "cost")]
    for r in rows:
        r["cost"] = float(r["cost"])
        for c in stats:
            r[c] = float(r[c])
    return rows, stats


def dominates(a, b, stats, lower):
    better = False
    for c in stats + ["cost"]:
        sa, sb = (-a[c], -b[c]) if (c in lower or c == "cost") else (a[c], b[c])
        if sa < sb:
            return False
        if sa > sb:
            better = True
    return better


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv")
    p.add_argument("--lower", default="")
    p.add_argument("--tol", type=float, default=0.15)
    args = p.parse_args()
    rows, stats = load(args.csv)
    lower = set(filter(None, args.lower.split(",")))

    print("## Dominance")
    found = False
    for a in rows:
        for b in rows:
            if a is not b and dominates(a, b, stats, lower):
                print(f"- {a['name']} dominates {b['name']}")
                found = True
    if not found:
        print("- none")

    print("\n## Value / cost")
    means = {c: statistics.mean(r[c] for r in rows) or 1.0 for c in stats}
    ratios = {}
    for r in rows:
        v = sum((-1 if c in lower else 1) * r[c] / means[c] for c in stats)
        ratios[r["name"]] = v / r["cost"] if r["cost"] else float("inf")
    med = statistics.median(ratios.values())
    for name, q in sorted(ratios.items(), key=lambda kv: -kv[1]):
        dev = (q - med) / med if med else 0.0
        flag = " OUTLIER" if abs(dev) > args.tol else ""
        print(f"- {name}: {q:.3f} ({dev:+.0%}){flag}")


if __name__ == "__main__":
    main()
