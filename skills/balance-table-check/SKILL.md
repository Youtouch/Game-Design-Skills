---
name: balance-table-check
description: Audit balance tables of units, items, weapons, cards or abilities for dominated options, cost-curve outliers, intransitive gaps and degenerate combinations. Use when reviewing a stat sheet, card or item set, or roster before playtest, or when one option is picked far more than intended.
---

# Balance Table Check

Design audit of a stat table. Output: a findings list with numeric evidence, a severity, and a suggested lever per finding. No engine code.

## Inputs

- The table (CSV or markdown): one row per option, a `name` column, a `cost` column, numeric stat columns, and optional label columns such as `role`.
- For each stat, whether higher or lower is better. Ask rather than guess when it is ambiguous (a long cooldown is bad; a long stun duration may be good or bad depending on who suffers it).
- The intended role of each option, pick or win data if any, and what the table omits (synergies, map, access, unlock order).

## Procedure

1. **Normalise.** Convert to comparable units where a model supports it, and state the model. DPS = damage / cooldown assumes positive cooldown and sustained fire. Effective HP = HP / (1 − reduction) assumes proportional reduction in [0, 1); immunity is a separate case. List effects the normalisation drops.
2. **Screen with the helper.** [balance_check.py](balance_check.py) (standard library only) validates the table, skips label columns, and reports dominance and a cost curve:
   `python balance_check.py table.csv --lower cooldown --group role`
   Add `--weights damage=6,range=1,cooldown=-20` to price stats from design intent instead of a least-squares fit. Exit code 2 means the input is unusable; fix it rather than working around it.
3. **Dominance.** An option dominates another when it is no worse on every modeled column (cost included) and strictly better on at least one. This is a proof within the represented columns only: an omitted range, access rule, or synergy can justify the dominated row.
4. **Cost curve.** Value = Σ wᵢ · statᵢ, then compare each option's fair cost with its actual cost. A least-squares fit assumes most current costs are roughly right and can produce weights with the wrong sign when roles are mixed or stats correlate; the helper notes this. Report the weights so designers can dispute them. ±15% is a screening default, not a balance boundary.
5. **Role coverage.** Re-run within roles (`--group`). A row that looks overpriced globally may be fairly priced for its specialist job. A deliberate weak or collectible option need not be repaired.
6. **Intransitive check.** For rock-paper-scissors relations, build the matchup matrix. A row with no losses under the represented match conditions is a candidate concern; availability, cost, draws, and skill can change that.
7. **Degenerate combinations.** List multiplicative interactions (damage × attack speed, cost reduction + refund, cooldown reduction near 100%, stacking percentages). Compute the multiplier at max stacks; check caps, repeatability, and resource or time limits. A one-time free option differs from repeatable uncapped gain.
8. **Edge values.** Check minimum and maximum levels, zero and cap values, and rounding at small numbers.
9. **Report** with the template below. Severity reflects consequence for the intended play, not the size of the number.

## Report template

| # | finding | options | evidence (numbers) | severity | lever |
|---|---|---|---|---|---|
| 1 | Dominated | Short Bow | Long Bow ≥ on all modeled stats at the same cost | high | give Short Bow a niche (draw speed, ammo) |

Worked example with the helper's output: [example.md](example.md) (table: [example.csv](example.csv)).

## Pitfalls

- Do not auto-fix a dominated row. Map, synergy, availability, and player skill can justify an apparent outlier; ask what it is for.
- A linear value model misses synergy; pair step 4 with step 7.
- A fitted curve inherits the biases of current costs. Use design weights when the whole table is suspect.
- Pick rates confound power with popularity, ease of use, and visibility.

## Sources (paraphrased, not quoted)

- Ian Schreiber & Brenda Romero, *Game Balance* (2021), chapters on cost curves and on transitive and intransitive balance.
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapter on balance.
- David Sirlin, *Balancing Multiplayer Games* (sirlin.net article series), on viable options and dominant strategies.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
