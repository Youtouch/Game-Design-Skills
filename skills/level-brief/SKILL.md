---
name: level-brief
description: Produce a one-page level brief (player goals, mechanics in play, difficulty targets, setting constraints, metric references, success criteria) before any layout work. Use when starting a new level, scoping a level for a designer, or reviewing whether a level idea is ready for blockout.
---

# Level Brief

A level brief is the contract between game design and level design: it fixes *what the level must teach, test and feel like* before anyone draws a layout. Design only; no engine work.

## Inputs to ask for (assume and state defaults if missing)

- Game pillars and target player fantasy.
- Where the level sits in the campaign (index, what came before, what comes after).
- Mechanics the player has at this point, and any new mechanic introduced here.
- Character metrics sheet (or use `level-metrics-sheet` to create one).
- Setting / narrative beat, and production limits (size, playtime, reuse of assets).

## Procedure

1. **Player goals.** Write the goal at three scales: level objective (what the player is told), moment-to-moment goal (what they do most of the time), and the designer intent (what the player should learn or feel). Keep each to one sentence.
2. **Mechanics in play.** List mechanics as *atomic* actions (jump, wall-run, throw) and the parameters that make them harder (distance, timing window, enemy count). Tag each: `new`, `reinforced`, or `combined`. Rational Game Design rule: at most one `new` mechanic per level, introduced through exposition → validation → challenge (McEntee, *Rational Design: The Core of Rayman Origins*, 2012).
3. **Difficulty targets.** For each mechanic, give a target band on a 1–5 scale at entry, peak and exit. Prefer raising one parameter at a time (McMillan, *The Rational Design Handbook: An Intro to RLD*, 2013). State the intended failure rate at the peak (e.g. "most players fail the peak once").
4. **Setting constraints.** Theme, landmarks, lighting/time of day, narrative beat, and hard limits (playtime, footprint, reused assets, streaming boundaries stated as design limits, not engine settings).
5. **Metric references.** Point to the metrics sheet values the level relies on (jump distance, cover spacing, combat ranges). Never invent new metrics in the brief; flag gaps instead.
6. **Success criteria.** Write 3–6 *testable* statements, each paired with how it is observed in a playtest (e.g. "80% of testers use the wall-run unprompted in the challenge section, observed by recording").
7. **Risks and open questions.** List what could make the level fail (readability, difficulty spike, scope).

## Output template

```markdown
# Level Brief: <name>
- Position: <chapter / index>, prev: <level>, next: <level>
- Playtime target: <min>
## Player goals
- Objective / Moment-to-moment / Designer intent
## Mechanics in play
| Mechanic | Status (new/reinforced/combined) | Difficulty parameters | Entry | Peak | Exit |
## Setting constraints
## Metric references
## Success criteria
| Criterion | How observed |
## Risks and open questions
```

## Self-check before handing off

- Exactly one `new` mechanic, or a stated reason for more.
- Every difficulty target names the parameter that changes.
- Every success criterion is observable in a playtest.
- No engine or implementation details.

Next steps: `level-beat-chart` for pacing, `level-metrics-sheet` for spatial checks.

## Sources (paraphrased, not quoted)

- Chris McEntee, *Rational Design: The Core of Rayman Origins*, Game Developer, 2012.
- Luke McMillan, *The Rational Design Handbook: An Intro to RLD*, Game Developer, 2013.
- Sunder Iyer, *Rational Game Design in a Hurry*, dev.to, 2021.
