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
1. **Identify demands.** Separate perception, inference, choice, execution, and recovery. If the matrix models execution only, say so and keep the other demands visible; a wider timing window does not repair an unreadable cue.
2. **Set the range** for each: easiest playable value, hardest fair value, unit. Mark values *estimate* until playtested.
3. **Define provisional levels** useful to this audience and decision. Five named bands are an optional convention, not a validated scale. Give each parameter a value per band.
4. **Model combinations.** Prefer the parameter vector. If a weighted score helps compare drafts, disclose the chosen weights, units, and untested additive assumption; it is not measured perceived difficulty.
5. **Inspect interactions.** Identify combinations that may amplify demands. Proposed caps are hypotheses until checked; do not assume a score proves safety or that two parameters can never peak together.
6. **Define the sweet spot** per game phase: target score band for tutorial, mid-game, and late-game content.
7. **Plan validation:** which observations distinguish misunderstanding, execution difficulty, intended challenge, and participation barriers. Record audience, exposure, assists, and build; failure counts alone do not confirm perceived difficulty.

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

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
