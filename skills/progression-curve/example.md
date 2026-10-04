# Worked Example: polynomial curve with scaling income

Targets: cap 30, level 5 within 30 min, level 30 at ~20 h.

Assume `x(L) = 100·L^1.8` and `xp_rate(L) = 40 + 6·L` XP/min.

| L | x(L) | xp/min | min for level | cumulative |
|---|---|---|---|---|
| 1 | 100 | 46 | 2.2 | 2 min |
| 2 | 348 | 52 | 6.7 | 9 min |
| 3 | 723 | 58 | 12.5 | 21 min |
| 4 | 1,213 | 64 | 19.0 | 40 min |
| 10 | 6,310 | 100 | 63 | ~5.5 h |
| 29 | 42,900 | 214 | 199 | ~20 h |

Verdict: level 5 lands at ~40 min, missing the 30-min target. Fix with a piecewise tutorial band: `x(L) = 100·L` for L ≤ 4 (1,000 XP, cumulative ~18 min), keep the polynomial after. Re-check that hour 20 still holds (shift ~-0.8 h, acceptable).
