---
name: level-metrics-sheet
description: Derive spatial level metrics (traversal distances, gap and jump ranges, cover spacing, sightlines, corridor widths) from a character's capabilities, then check a written blockout description against them. Use when defining metrics for a new character or game, or when reviewing a blockout for metric violations.
---

# Level Metrics Sheet

Metrics are the measured rules of space: they make levels readable and let difficulty be tuned on purpose. This skill derives them from character capabilities and audits blockouts against them. Design only; units are game units (state the scale, e.g. 1 unit = 1 m).

## Part A: derive the sheet

Inputs: character height and width, walk/run/sprint speed, jump height and distance (standing and running), any traversal abilities (double jump, mantle, wall-run, dash), weapon effective ranges, camera type. If missing, keep values symbolic or mark a worked example as hypothetical; do not substitute a human character for an unspecified design.

Derive and tabulate, each with a *comfortable*, *challenging* and *impossible* value:

1. **Traversal.** Time-to-cross for key distances at run speed; maximum distance between points of interest before travel feels empty (state as seconds of travel).
2. **Gaps and jumps.** Safe gap ≈ well under max running jump; challenge gap close to max; impossible gap clearly beyond max so it reads as "not a jump". Same for heights: step, mantle, out-of-reach. Avoid values in the ambiguous band just above the max, which read as possible but fail.
3. **Cover.** Low and high cover heights relative to character crouch/stand height; spacing between cover pieces as seconds of exposed movement (McMillan, *The Metrics of Space: Tactical Level Design*).
4. **Sightlines and combat ranges.** Close / mid / long engagement bands from weapon ranges; longest uninterrupted sightline per space type.
5. **Corridors and doors.** Minimum width for one character, for two side by side, and for camera clearance in third person; door width and height.

Output table:

```markdown
| Metric | Comfortable | Challenging | Impossible / limit | Derived from |
```

## Part B: check a blockout description

Input: a written blockout (rooms, distances, gaps, cover, sightlines). For each measurable statement:

1. Map it to a metric row.
2. Classify: `ok`, `challenging` (check it is intended by the brief/beat chart), `ambiguous band`, or `violation`.
3. Flag unstated measurements the check needs, rather than guessing them.
4. Propose a concrete fix with the target value.

```markdown
| Location | Statement | Metric | Value | Verdict | Fix |
```

## Pitfalls

- Third-person cameras need more width and height than the character does.
- Metrics change when abilities unlock; keep one column per ability stage if needed.
- Investigate disagreement between observed and derived values: model omissions, measurement error, build, ability stage, and participant context may differ. Update the relevant model or scoped target; an observation of confusion does not overturn a physical reachability proof.

## Sources (paraphrased, not quoted)

- Nassib Azar, *The Metrics of Space: Molecule Design*, Game Developer.
- Luke McMillan, *The Metrics of Space: Tactical Level Design*, Game Developer.
- Luke McMillan, *The Rational Design Handbook: Four Primary Metrics*, Game Developer.
- *Gameplay metrics: game design's best kept secret?*, intelligent-artifice.com, 2015.

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
