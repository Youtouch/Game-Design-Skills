---
name: balance-table-check
description: Audit balance tables of units, items, weapons or abilities for dominant options, cost/benefit outliers and degenerate combinations. Use when reviewing a stat sheet, a card or item set, or a roster before playtest, or when one option is picked far more than intended.
---

# Balance Table Check

Design audit of a stat table. Output: a findings list with evidence and a suggested lever per finding. No engine code.

## Inputs

- The table (CSV or markdown): one row per option, a `cost` column and numeric stat columns.
- Context: which stats are "good when higher" vs "good when lower", the intended role of each option, and pick-rate data if any.

## Procedure

1. **Normalise.** Convert stats to a common unit where possible (e.g. DPS = damage / cooldown, effective HP = HP / (1 − armor%)).
2. **Dominance (Pareto) check.** Option A dominates B if A is ≥ on every stat, > on one, and costs ≤ B. A dominated option is a trap; a dominating option is a must-pick. Run [balance_check.py](balance_check.py) for this.
3. **Cost curve.** Fit `value = Σ w_i · stat_i` (weights from design intent or least squares against cost). Ratio `value / cost` per row; flag rows outside ±15% of the median as outliers. Report the weights so designers can dispute them.
4. **Role coverage.** Group by role; each role should have at least one non-dominated option. Empty roles or roles with a single viable pick are findings.
5. **Intransitive check.** For rock-paper-scissors systems, build the matchup matrix; each option should beat something and lose to something. A row with no losses is dominant regardless of cost.
6. **Degenerate combinations.** List multiplicative interactions (damage × attack speed buffs, cost reduction + refund, cooldown reduction near 100%, stacking %). Compute the combined multiplier at max stacks; flag anything that breaks a cap or reaches zero cost or infinite loops.
7. **Edge values.** Check min/max levels, zero and cap values, and rounding at low numbers.
8. **Report** using the template below.

## Report template

| # | finding | options | evidence (numbers) | severity | lever |
|---|---|---|---|---|---|
| 1 | Dominated | Short Bow | Long Bow ≥ on all stats at same cost | high | give Short Bow a niche (speed) |

## Pitfalls

- A table audit is a hypothesis; context (map, synergies, skill ceiling) can justify an outlier. State it, do not auto-fix.
- Linear value models miss synergy; pair step 3 with step 6.
- Pick rates confound power with popularity and ease of use.

## Sources (paraphrased, not quoted)

- Ian Schreiber & Brenda Romero, *Game Balance* (2021), chapters on cost curves, transitive and intransitive balance.
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapter on balance.
- David Sirlin, *Balancing Multiplayer Games* (sirlin.net article series), on viable options and dominant strategies.
