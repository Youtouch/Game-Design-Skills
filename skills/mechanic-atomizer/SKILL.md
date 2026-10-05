---
name: mechanic-atomizer
description: Breaks a game, feature, or single mechanic down into atomic mechanics and skill atoms, and lists the tunable parameters of each. Use when analysing or documenting a mechanic, preparing a difficulty matrix, or checking that a design is decomposed finely enough to tune and teach.
---

# Mechanic Atomizer

Decompose a design into the smallest units that can be taught, tuned, and tested on their own. Design-level only: parameters are described in design terms (distance, timing, count), never as engine code.

## Inputs
- The game, feature, or mechanic to analyse (description, pitch, or design doc excerpt).
- Optional: target player, core loop, known constraints.

## Process
1. **State the player goal** the mechanic serves (what the player is trying to achieve, in one line).
2. **Split into atomic mechanics.** An atom is one player verb or one world rule that cannot be split further without losing meaning (e.g. "jump" splits into "take off", "airborne control", "land"; stop when a part no longer has its own decision or input).
3. **Classify each atom:** player action, world rule, enemy/obstacle behaviour, or feedback/readability element.
4. **Write the skill atom loop** for each player action: player action → system simulation → feedback → player's updated mental model. Note what the player must learn to master it.
5. **List tunable parameters** for each atom: name, unit, plausible range, and which demands it changes: perception, inference, choice, execution, or recovery. Execution difficulty versus complexity is one useful distinction, not a complete model of challenge.
6. **Map dependencies:** separate actual rule/knowledge prerequisites from a convenient teaching order. Record coupled concepts that may be discovered together (this feeds `mechanic-introduction-plan`).
7. **Flag issues:** atoms with no clear feedback, parameters that interact non-linearly, redundant atoms, atoms whose purpose is unclear. Lack of tuning space alone is not a defect: a unique dramatic action or expressive ritual can be valuable.

## Output
A markdown table per mechanic:

| Atom | Type | Skill learned | Parameter | Unit | Range | Difficulty / Complexity | Depends on |
|---|---|---|---|---|---|---|---|

Followed by a dependency list and a short "issues" list. Keep ranges as design intent, marked *estimate* until playtested.

## Checks
- Identify parameters and feedback where relevant; do not invent a parameter merely to fill the table. Check whether consequences are understandable enough for the intended experience.
- Split decisions when useful for diagnosis or tuning; retain coupled decisions whose meaning would be lost, while recording separable demands.
- Parameters are engine-agnostic (no component or variable names).

## Sources (paraphrased, not quoted)
- Chris McEntee, "Rational Design: The Core of Rayman Origins", Game Developer, 2012 (atomic mechanics, readability).
- Sunder Iyer, "Rational Game Design in a Hurry", dev.to, 2021 (goal → mechanics → atomic parameters).
- Daniel Cook, "The Chemistry of Game Design", Lostgarden, 2007 (skill atoms and feedback loops).

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
