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
2. **Dominance (Pareto) check.** A table option dominates another when it is no worse on every modeled dimension (including lower cost) and strictly better on at least one, using each stat's preferred direction. This is table-relative: omitted range, access, synergies, or role can change the conclusion. [balance_check.py](balance_check.py) screens numeric CSVs; set `--lower` explicitly for lower-is-better stats.
3. **Cost curve.** Fit `value = Σ w_i · stat_i` (weights from design intent or least squares against cost). Ratio `value / cost` per row; choose and justify a screening tolerance; ±15% is an optional default, not an established balance boundary. Report the weights so designers can dispute them. The helper uses equal mean-normalized weights, not the fitted model described here; its value/cost output is exploratory and can mislead with zero costs, signed stats, or near-zero medians. Calculate a suitable model separately when those occur.
4. **Role coverage.** Group by role; each role should have at least one non-dominated option. Empty roles or roles with a single viable pick are findings.
5. **Intransitive check.** For rock-paper-scissors systems, build the matchup matrix; each option should beat something and lose to something. A row with no losses is a candidate concern under the represented match conditions; availability, cost, draws, player skill, and strategic constraints can change its value.
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

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
