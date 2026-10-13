"""Waiting-time math for random rewards: how many attempts until a drop or a full set.

Usage:
    python reward_math.py drop --p 0.02 [--pity 60] [--percentiles 50,90,99]
    python reward_math.py drop --p 0.006 --soft-start 74 --soft-step 0.06 --pity 90
    python reward_math.py collect --n 8 [--percentiles 50,90]
    python reward_math.py collect --weights 30,30,20,10,5,5 [--trials 20000 --seed 1]

drop: independent attempts with success chance p, optionally rising by
--soft-step per attempt from attempt --soft-start, and guaranteed at --pity.
Exact distribution; "attempts" counts the successful one.

collect: draws with replacement from items until every item is owned.
Equal probabilities (--n) are exact; unequal --weights give an exact mean and
simulated percentiles (seeded, so reruns match).

Assumes independence between attempts. A shuffle bag, a counter that resets
on other rewards, or player choice needs its own model. Standard library only.
"""
import argparse
import math
import random
import sys


def drop_distribution(p, pity=None, soft_start=None, soft_step=0.0, eps=1e-12):
    """Yield (attempt, probability that success happens on this attempt)."""
    survive = 1.0
    k = 0
    while survive > eps:
        k += 1
        chance = p
        if soft_start is not None and k >= soft_start:
            chance = p + (k - soft_start + 1) * soft_step
        if pity is not None and k >= pity:
            chance = 1.0
        chance = min(1.0, max(0.0, chance))
        yield k, survive * chance
        survive *= 1.0 - chance
        if k > 10_000_000:
            raise ValueError("distribution does not terminate; check p")


def summarize(pmf, percentiles):
    mean, cum, out = 0.0, 0.0, {}
    targets = sorted(percentiles)
    i = 0
    for k, prob in pmf:
        mean += k * prob
        cum += prob
        while i < len(targets) and cum >= targets[i] / 100 - 1e-12:
            out[targets[i]] = k
            i += 1
    return mean, out


def collect_equal_distribution(n, eps=1e-12):
    """Exact pmf of draws to own all n equally likely items (Markov chain on owned count)."""
    state = [0.0] * (n + 1)
    state[0] = 1.0
    done_prev = 0.0
    t = 0
    while 1.0 - done_prev > eps:
        t += 1
        nxt = [0.0] * (n + 1)
        for owned in range(n):
            if state[owned]:
                new = (n - owned) / n
                nxt[owned + 1] += state[owned] * new
                nxt[owned] += state[owned] * (1 - new)
        nxt[n] += state[n]
        state = nxt
        yield t, state[n] - done_prev
        done_prev = state[n]


def collect_mean_weighted(probs, steps=200_000):
    """Exact mean via E[T] = integral_0^inf (1 - prod(1 - exp(-p_i t))) dt, numerically."""
    upper = 50.0 / min(probs)
    h = upper / steps
    total = 0.0
    for i in range(steps + 1):
        t = i * h
        f = 1.0 - math.prod(1.0 - math.exp(-q * t) for q in probs)
        total += f * (0.5 if i in (0, steps) else 1.0)
    return total * h


def collect_simulated(probs, trials, seed, percentiles):
    rng = random.Random(seed)
    cum, acc = [], 0.0
    for q in probs:
        acc += q
        cum.append(acc)
    results = []
    for _ in range(trials):
        owned, draws = set(), 0
        while len(owned) < len(probs):
            draws += 1
            r = rng.random() * acc
            lo = 0
            while cum[lo] < r:
                lo += 1
            owned.add(lo)
        results.append(draws)
    results.sort()
    return {q: results[min(trials - 1, math.ceil(q / 100 * trials) - 1)] for q in percentiles}


def parse_percentiles(text):
    vals = [float(x) for x in text.split(",") if x.strip()]
    if not vals or any(not 0 < v < 100 for v in vals):
        raise ValueError("percentiles must be between 0 and 100 (exclusive)")
    return vals


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("drop")
    d.add_argument("--p", type=float, required=True)
    d.add_argument("--pity", type=int)
    d.add_argument("--soft-start", type=int)
    d.add_argument("--soft-step", type=float, default=0.0)
    d.add_argument("--percentiles", default="50,90,99")
    c = sub.add_parser("collect")
    g = c.add_mutually_exclusive_group(required=True)
    g.add_argument("--n", type=int)
    g.add_argument("--weights")
    c.add_argument("--percentiles", default="50,90,99")
    c.add_argument("--trials", type=int, default=20000)
    c.add_argument("--seed", type=int, default=1)
    args = p.parse_args(argv)

    try:
        pct = parse_percentiles(args.percentiles)
        if args.cmd == "drop":
            if not 0 <= args.p <= 1 or (args.p == 0 and args.pity is None and not args.soft_step):
                raise ValueError("--p must be in (0, 1], or 0 with a pity or soft pity")
            if args.pity is not None and args.pity < 1:
                raise ValueError("--pity must be at least 1")
            if args.soft_step < 0 or (args.soft_step and args.soft_start is None):
                raise ValueError("--soft-step needs --soft-start and must be nonnegative")
            mean, out = summarize(
                drop_distribution(args.p, args.pity, args.soft_start, args.soft_step), pct)
            print(f"Per-attempt chance {args.p:g}"
                  + (f", soft pity +{args.soft_step:g}/attempt from {args.soft_start}"
                     if args.soft_start else "")
                  + (f", guaranteed by attempt {args.pity}" if args.pity else ""))
            print(f"- mean attempts: {mean:.2f}")
            for q, k in out.items():
                print(f"- {q:g}% of players succeed within {k} attempts")
        else:
            if args.n is not None:
                if args.n < 1:
                    raise ValueError("--n must be at least 1")
                mean, out = summarize(collect_equal_distribution(args.n), pct)
                print(f"Collect all {args.n} equally likely items (exact)")
                print(f"- mean draws: {mean:.2f}")
                for q, k in out.items():
                    print(f"- {q:g}% of players complete within {k} draws")
            else:
                w = [float(x) for x in args.weights.split(",") if x.strip()]
                if len(w) < 1 or any(not math.isfinite(x) or x <= 0 for x in w):
                    raise ValueError("--weights must be positive numbers")
                if args.trials < 1:
                    raise ValueError("--trials must be at least 1")
                total = sum(w)
                probs = [x / total for x in w]
                mean = collect_mean_weighted(probs)
                print(f"Collect all {len(w)} items, weights {args.weights}")
                print(f"- mean draws (exact, numerical): {mean:.2f}")
                print(f"- rarest item alone: mean {1 / min(probs):.2f} draws")
                sim = collect_simulated(probs, args.trials, args.seed, pct)
                for q, k in sim.items():
                    print(f"- {q:g}% complete within {k} draws "
                          f"(simulated, {args.trials} trials, seed {args.seed})")
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
