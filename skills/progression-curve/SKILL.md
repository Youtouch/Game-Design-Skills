---
name: progression-curve
description: Design XP, level and power curves and compute time-to-level, time-to-cap and pacing checkpoints with explicit formulas. Use when tuning leveling speed, power growth, difficulty scaling, unlock pacing or when a game feels grindy or too fast.
---

# Progression Curve

Design-level curve work. Output: chosen formulas, a level table, time-to-X numbers and pacing checkpoints. No engine code.

## Inputs (assume and state if missing)

- Level cap, target time-to-cap (hours of play) and target first-session milestones.
- XP income model: XP/min by activity, and how it scales with level.
- Power axes: player stats, enemy stats, gear tiers.

## Curve shapes

| shape | XP to next level `x(L)` | modeling use |
|---|---|---|
| Linear | `a + b·L` | constant increase in required XP; duration depends on income |
| Polynomial | `a·L^k` | adjustable growth; k = 1.5–2.5 is an illustrative range, not a default target |
| Exponential | `a·r^L` | multiplicative growth; r = 1.05–1.2 is illustrative; compare against income growth |
| Piecewise | different formula per band | can fit distinct milestones; check transition continuity and actual times |

Cumulative XP `X(L) = Σ x(i)` for i < L. A leading integral approximation for a growing power curve is `a·L^(k+1)/(k+1)`; it omits discrete boundary effects. Validate milestones with the full discrete sum and declared level indexing. Felt pacing remains a hypothesis conditional on activity and audience.

## Procedure

1. **Fix the targets first**, not the formula: e.g. level 5 in session 1 (30 min), level 20 by hour 10, cap 50 by hour 60.
2. **Model income.** `xp_rate(L)` per minute. With constant positive deterministic income within each level, `t(L) = x(L) / xp_rate(L)` estimates that level's duration. Random awards, carryover, caps, and changing activity require a state model. Duration is not a direct measure of felt pacing.
3. **Solve parameters** so cumulative time hits each target. Use piecewise bands when one formula cannot hit all checkpoints.
4. **Level table.** Columns: `L | x(L) | X(L) | xp_rate | minutes for this level | cumulative hours | unlock`.
5. **Pacing checkpoints.** Choose intervals from session context and intended experience; there is no universal unlock cadence. Long stretches may support mastery, ritual, or exploration. Explain the suspected cost and what observation could distinguish it from a valuable quiet interval.
6. **Power vs challenge.** Plot player power `P(L)` against enemy/content difficulty `D(L)`. A ratio `P/D` is meaningful only if the model makes those quantities comparable; it cannot establish flow, boredom, or frustration. Examine ability, information, strategy, and access alongside numeric power. Name deliberate spikes (boss gates) vs accidental ones.
7. **Catch-up and outliers.** Check a player who skips side content (lower income) and a power gamer (high income). Report time-to-cap spread.

A worked example lives in [example.md](example.md).

## Pitfalls

- Tuning raw XP while income also scales: the felt curve can end up flat or inverted.
- Exponential power growth with linear content makes all old content trivial; decide if that is intended.
- Check early-session milestones when relevant to the brief; do not claim a retention effect without suitable evidence.
- Rounding XP thresholds to "nice" numbers shifts cumulative time; recompute after rounding.

## Sources (paraphrased, not quoted)

- Ian Schreiber & Brenda Romero, *Game Balance* (2021), chapters on progression and curves.
- Ernest Adams, *Fundamentals of Game Design*, chapter on progression and balance.
- Raph Koster, *A Theory of Fun for Game Design*, on mastery pacing and boredom.

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
