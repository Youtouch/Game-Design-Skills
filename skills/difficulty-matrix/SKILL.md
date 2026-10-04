---
name: difficulty-matrix
description: Builds a Rational Game Design difficulty matrix per mechanic (difficulty parameters, ranges, intensity levels, safe combinations) as an engine-agnostic hand-off table. Use when tuning challenge, planning difficulty curves, or handing difficulty targets to level designers or implementers.
---

# Difficulty Matrix

Turn atomic parameters into graded intensity levels so challenge can be dialled deliberately instead of guessed. Output is a design table, not engine data.

## Inputs
- Atoms and parameters for the mechanic (ideally from `mechanic-atomizer`).
- Target audience and intended difficulty curve, if known.

## Process
1. **Pick difficulty parameters.** Keep only parameters that change execution demand (timing window, speed, distance, count, reaction time, precision). Move pure complexity parameters to a separate note.
2. **Set the range** for each: easiest playable value, hardest fair value, unit. Mark values *estimate* until playtested.
3. **Define intensity levels** (default 5: Trivial, Easy, Medium, Hard, Expert). Give each parameter a value per level.
4. **Weight parameters** by how much each contributes to perceived difficulty (e.g. 1–3). Score a configuration as the weighted sum of its parameter levels.
5. **Define safe combinations.** List which parameters may be raised together and caps on combined score; flag pairs that multiply difficulty (e.g. speed × small target) and must not both peak.
6. **Define the sweet spot** per game phase: target score band for tutorial, mid-game, and late-game content.
7. **Plan validation:** what playtest signal (fail rate, retries, time to clear) confirms each level, and how to adjust if it misses.

## Output

| Parameter | Unit | Weight | Trivial | Easy | Medium | Hard | Expert | Notes |
|---|---|---|---|---|---|---|---|---|

Then: combination rules (allowed / capped / forbidden), score bands per phase, and playtest targets.

## Checks
- Each level differs from the next in a perceptible way.
- No forbidden combination appears in any sweet-spot band.
- Complexity is tracked separately so new rules are not mistaken for harder execution.

## Sources (paraphrased, not quoted)
- Sunder Iyer, "Rational Game Design in a Hurry", dev.to, 2021 (difficulty matrix, sweet spot).
- Luke McMillan, "The Rational Design Handbook: An Intro to RLD", Game Developer, 2013 (complexity vs difficulty, modifiers, playtest regression).
- Chris McEntee, "Rational Design: The Core of Rayman Origins", Game Developer, 2012.
