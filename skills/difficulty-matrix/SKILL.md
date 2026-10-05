---
name: difficulty-matrix
description: Builds a Rational Game Design difficulty matrix per mechanic (difficulty parameters, ranges, provisional intensity levels, interactions) as an engine-agnostic hand-off table. Use when tuning challenge, planning difficulty curves, or handing difficulty targets to level designers or implementers.
---

# Difficulty Matrix

Turn atomic parameters into graded intensity levels so challenge can be dialled deliberately instead of guessed. Output is a design table, not engine data.

## Inputs
- Atoms and parameters for the mechanic (ideally from `mechanic-atomizer`).
- Target audience and intended difficulty curve, if known.

## Process
1. **Identify demands.** Separate perception, inference, choice, execution, and recovery. If the matrix models execution only, say so and keep the other demands visible; a wider timing window does not repair an unreadable cue.
2. **Set provisional ranges** with units, model conditions, and audience. Separate hard rule limits from proposed challenge or fairness targets; mark untested values as estimates.
3. **Define provisional levels** useful to this audience and decision. Five named bands are an optional convention, not a validated scale. Give each parameter a value per band.
4. **Model combinations.** Prefer the parameter vector. If a weighted score helps compare drafts, disclose the chosen weights, units, and untested additive assumption; it is not measured perceived difficulty.
5. **Inspect interactions.** Identify combinations that may amplify demands. Proposed caps are hypotheses until checked; do not assume a score proves safety or that two parameters can never peak together.
6. **Set demand targets** by phase, audience, and ability stage. Prefer the parameter vector. If score bands are useful, state assumptions and validation status; a band does not establish perceived difficulty or safety.
7. **Plan validation:** which observations distinguish misunderstanding, execution difficulty, intended challenge, and participation barriers. Record audience, exposure, assists, and build; failure counts alone do not confirm perceived difficulty.

## Output

| Demand / parameter | Unit | Entry condition | Proposed values or bands | Interactions | Evidence / uncertainty |
|---|---|---|---|---|---|

Then list modeled constraints, intended combinations, and distinguishing observations. Weights and named bands are optional. Separate rule-impossible combinations from untested demanding combinations.

## Checks
- Each level differs from the next in a perceptible way.
- Check modeled constraints and justify intended demanding combinations; do not infer safety from a summary score.
- Complexity is tracked separately so new rules are not mistaken for harder execution.

## Sources (paraphrased, not quoted)
- Sunder Iyer, "Rational Game Design in a Hurry", dev.to, 2021 (difficulty matrix, sweet spot).
- Luke McMillan, "The Rational Design Handbook: An Intro to RLD", Game Developer, 2013 (complexity vs difficulty, modifiers, playtest regression).
- Chris McEntee, "Rational Design: The Core of Rayman Origins", Game Developer, 2012.

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
