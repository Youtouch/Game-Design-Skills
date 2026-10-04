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
5. **List tunable parameters** for each atom: name, unit, plausible range, and whether it changes *difficulty* (execution demand) or *complexity* (how much the player must understand).
6. **Map dependencies:** which atoms require another to be learned first (this feeds `mechanic-introduction-plan`).
7. **Flag issues:** atoms with no clear feedback, parameters that interact non-linearly, redundant atoms, atoms with no meaningful tuning space.

## Output
A markdown table per mechanic:

| Atom | Type | Skill learned | Parameter | Unit | Range | Difficulty / Complexity | Depends on |
|---|---|---|---|---|---|---|---|

Followed by a dependency list and a short "issues" list. Keep ranges as design intent, marked *estimate* until playtested.

## Checks
- Every atom has at least one tunable parameter and one feedback channel.
- No atom bundles two separate decisions.
- Parameters are engine-agnostic (no component or variable names).

## Sources (paraphrased, not quoted)
- Chris McEntee, "Rational Design: The Core of Rayman Origins", Game Developer, 2012 (atomic mechanics, readability).
- Sunder Iyer, "Rational Game Design in a Hurry", dev.to, 2021 (goal → mechanics → atomic parameters).
- Daniel Cook, "The Chemistry of Game Design", Lostgarden, 2007 (skill atoms and feedback loops).
