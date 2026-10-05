# Worked Example: polynomial curve with scaling income

Targets: cap 30, level 5 within 30 min, level 30 at ~20 h.

Assume `x(L) = 100·L^1.8` and `xp_rate(L) = 40 + 6·L` XP/min.

| L | x(L) | xp/min | min for level | cumulative |
|---|---|---|---|---|
| 1 | 100 | 46 | 2.2 | 2 min |
| 2 | 348 | 52 | 6.7 | 9 min |
| 3 | 722 | 58 | 12.5 | 21 min |
| 4 | 1,213 | 64 | 18.9 | 40 min |
| 10 | 6,310 | 100 | 63.1 | 306.4 min / 5.11 h |
| 29 | 42,886 | 214 | 200.4 | 2,902.6 min / 48.38 h |

Displayed thresholds are rounded to nearest integer; timings use unrounded thresholds. If rounded thresholds become game rules, recompute all times.

Cumulative time in row L includes completing that level's transition to L+1; level 1 is the starting state. Sum every intervening level, not only the displayed rows.

Verdict: level 5 lands at 40.27 min, missing the 30-min target, and cap 30 takes 48.38 h, far above the 20-hour target. A piecewise tutorial band `x(L) = 100·L` for L ≤ 4 reaches level 5 in 17.44 min, but leaves cap time at 48.00 h. This repairs only the early milestone. Refit later thresholds or income before claiming the curve meets both targets; recompute discrete sums after rounding. All timings assume constant deterministic income within each level, without reward carryover or caps.
