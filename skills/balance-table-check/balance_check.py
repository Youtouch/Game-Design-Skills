"""Balance table screen: Pareto dominance, duplicates and cost-curve outliers.

Usage:
    python balance_check.py table.csv --lower cooldown [--group role]
        [--ignore notes] [--weights damage=2,hp=0.5] [--tol 0.15]

CSV: one row per option, a 'name' column, a 'cost' column and stat columns.
Columns that are not fully numeric are treated as labels and skipped (listed
in the report). Cost is always lower-is-better; name other lower-is-better
stats with --lower. --group compares options only within the same label
value (for example, within a role).

Cost curve: with --weights, value = sum(w * stat) and the fair cost is that
value scaled so the table's total value equals its total cost. Without
weights, the script fits cost = b0 + sum(w * stat) by least squares, which
assumes most current costs are about right. Either way the output is a
screening aid for a designer to dispute, not a validated utility model.

Standard library only. Exit code 2 means the input could not be screened.
"""
import argparse
import csv
import math
import sys


class InputError(Exception):
    pass


def parse_number(text):
    try:
        value = float(text)
    except (TypeError, ValueError):
        return None
    return value if math.isfinite(value) else None


def load(path, ignore):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise InputError("file has no header row")
        fields = [c.strip() for c in reader.fieldnames]
        rows = [{k.strip(): (v or "").strip() for k, v in r.items() if k}
                for r in reader]
    for required in ("name", "cost"):
        if required not in fields:
            raise InputError(f"missing required column '{required}'")
    rows = [r for r in rows if any(r.values())]
    if len(rows) < 2:
        raise InputError("need at least two options to compare")

    names = [r["name"] for r in rows]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if "" in names:
        raise InputError("every row needs a name")
    if dupes:
        raise InputError("duplicate names: " + ", ".join(dupes))

    for r in rows:
        cost = parse_number(r["cost"])
        if cost is None:
            raise InputError(f"{r['name']}: cost '{r['cost']}' is not a finite number")
        if cost < 0:
            raise InputError(f"{r['name']}: negative cost {cost:g}")
        r["cost"] = cost

    stats, labels = [], []
    for c in fields:
        if c in ("name", "cost") or c in ignore:
            continue
        values = [parse_number(r[c]) for r in rows]
        if all(v is not None for v in values):
            stats.append(c)
            for r, v in zip(rows, values):
                r[c] = v
        else:
            labels.append(c)
    if not stats:
        raise InputError("no numeric stat columns found")
    return rows, stats, labels


def parse_list(text):
    return [s.strip() for s in text.split(",") if s.strip()]


def parse_weights(text, stats):
    weights = {}
    for item in parse_list(text):
        key, sep, raw = item.partition("=")
        key = key.strip()
        value = parse_number(raw)
        if not sep or value is None:
            raise InputError(f"bad weight '{item}', expected stat=number")
        if key not in stats:
            raise InputError(f"weight for unknown stat '{key}'")
        weights[key] = value
    return weights


def oriented(row, col, lower):
    """Value where larger is always better."""
    return -row[col] if (col == "cost" or col in lower) else row[col]


def compare(a, b, cols, lower):
    """Return 'dominates', 'identical' or None for a versus b."""
    better = False
    for c in cols:
        sa, sb = oriented(a, c, lower), oriented(b, c, lower)
        if sa < sb:
            return None
        if sa > sb:
            better = True
    return "dominates" if better else "identical"


def solve(matrix, vector):
    """Gaussian elimination with partial pivoting; None if singular."""
    n = len(vector)
    m = [row[:] + [v] for row, v in zip(matrix, vector)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(m[i][col]))
        if abs(m[pivot][col]) < 1e-9:
            return None
        m[col], m[pivot] = m[pivot], m[col]
        for i in range(col + 1, n):
            f = m[i][col] / m[col][col]
            for j in range(col, n + 1):
                m[i][j] -= f * m[col][j]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def fit_costs(rows, stats):
    """Least-squares cost = b0 + sum(w*stat). Returns (weights, intercept) or None."""
    if len(rows) <= len(stats) + 1:
        return None
    design = [[1.0] + [r[c] for c in stats] for r in rows]
    k = len(stats) + 1
    xtx = [[sum(d[i] * d[j] for d in design) for j in range(k)] for i in range(k)]
    xty = [sum(d[i] * r["cost"] for d, r in zip(design, rows)) for i in range(k)]
    coef = solve(xtx, xty)
    if coef is None:
        return None
    return dict(zip(stats, coef[1:])), coef[0]


def fair_costs(rows, stats, weights, lower, notes):
    if weights:
        value = {r["name"]: sum(weights.get(c, 0.0) * r[c] for c in stats) for r in rows}
        total_value = sum(value.values())
        total_cost = sum(r["cost"] for r in rows)
        if total_value <= 0 or total_cost <= 0:
            notes.append("weighted values or costs do not sum to a positive total; "
                         "cost curve skipped")
            return None, weights, 0.0
        scale = total_cost / total_value
        return ({n: v * scale for n, v in value.items()},
                {c: w * scale for c, w in weights.items()}, 0.0)
    fitted = fit_costs(rows, stats)
    if fitted is None:
        notes.append(f"least-squares fit needs more than {len(stats) + 1} rows and "
                     "non-collinear stats; supply --weights from design intent")
        return None, None, 0.0
    w, b0 = fitted
    scale = max(abs(r["cost"]) for r in rows) or 1.0
    for c in stats:
        span = max(r[c] for r in rows) - min(r[c] for r in rows)
        if abs(w[c]) * span < 1e-9 * scale:
            w[c] = 0.0
            continue
        wrong = (w[c] > 0) if c in lower else (w[c] < 0)
        if wrong:
            notes.append(f"fitted weight for '{c}' has the opposite sign to its declared "
                         "direction; the current costs may not reflect it, or it "
                         "correlates with another stat")
    if abs(b0) < 1e-9 * scale:
        b0 = 0.0
    return {r["name"]: b0 + sum(w[c] * r[c] for c in stats) for r in rows}, w, b0


def report_group(title, rows, stats, lower, weights, tol, out):
    if title:
        out.append(f"\n# Group: {title}")
    if len(rows) < 2:
        out.append("- only one option; nothing to compare")
        return
    cols = stats + ["cost"]
    out.append("\n## Dominance (within modeled columns only)")
    found = False
    for i, a in enumerate(rows):
        for j, b in enumerate(rows):
            if i == j:
                continue
            verdict = compare(a, b, cols, lower)
            if verdict == "dominates":
                out.append(f"- {a['name']} dominates {b['name']}")
                found = True
            elif verdict == "identical" and i < j:
                out.append(f"- {a['name']} and {b['name']} are identical on every column")
                found = True
    if not found:
        out.append("- none")

    out.append("\n## Cost curve")
    notes = []
    fair, used, b0 = fair_costs(rows, stats, weights, lower, notes)
    if fair is not None:
        source = "design weights, scaled to total cost" if weights else "least-squares fit"
        terms = "".join(f" {'-' if used[c] < 0 else '+'} {abs(used[c]):.4g}*{c}"
                        for c in stats if c in used)
        out.append(f"- model ({source}): fair cost = {b0:.4g}{terms}")
        out.append("")
        out.append("| option | cost | fair cost | gap | flag |")
        out.append("|---|---|---|---|---|")
        ranked = sorted(rows, key=lambda r: -(fair[r["name"]] - r["cost"])
                        / (r["cost"] or 1e-9))
        for r in ranked:
            f_cost, cost = fair[r["name"]], r["cost"]
            if cost > 0:
                gap = (f_cost - cost) / cost
                gap_text = f"{gap:+.0%}"
                flag = ("underpriced" if gap > tol else
                        "overpriced" if gap < -tol else "")
            else:
                gap_text = f"{f_cost:+.3g} (zero cost)"
                flag = "free: review" if f_cost > 0 else ""
            out.append(f"| {r['name']} | {cost:g} | {f_cost:.3g} | {gap_text} | {flag} |")
        out.append(f"\nGap = (fair - cost) / cost; tolerance ±{tol:.0%} is a screening "
                   "choice, not a balance boundary.")
    for n in notes:
        out.append(f"- note: {n}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("csv")
    p.add_argument("--lower", default="", help="comma-separated lower-is-better stats")
    p.add_argument("--ignore", default="", help="comma-separated columns to skip")
    p.add_argument("--group", default="", help="label column to compare within")
    p.add_argument("--weights", default="", help="stat=weight pairs for the cost curve")
    p.add_argument("--tol", type=float, default=0.15, help="screening tolerance (0.15 = 15%%)")
    args = p.parse_args(argv)
    try:
        if not math.isfinite(args.tol) or args.tol < 0:
            raise InputError("--tol must be a finite nonnegative number")
        ignore = set(parse_list(args.ignore))
        rows, stats, labels = load(args.csv, ignore)
        lower = set(parse_list(args.lower))
        unknown = sorted(lower - set(stats) - {"cost"})
        if unknown:
            raise InputError("--lower names unknown or non-numeric columns: "
                             + ", ".join(unknown))
        weights = parse_weights(args.weights, stats)
        if args.group and args.group not in labels:
            raise InputError(f"--group '{args.group}' is not a label column")
    except (InputError, OSError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    out = [f"Stats: {', '.join(stats)} | lower-is-better: "
           f"{', '.join(sorted(lower | {'cost'}))}"]
    skipped = [c for c in labels if c != args.group]
    if skipped:
        out.append(f"Skipped non-numeric columns: {', '.join(skipped)}")
    if args.group:
        groups = {}
        for r in rows:
            groups.setdefault(r[args.group], []).append(r)
        for key in sorted(groups):
            report_group(f"{args.group} = {key}", groups[key], stats, lower,
                         weights, args.tol, out)
    else:
        report_group("", rows, stats, lower, weights, args.tol, out)
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
