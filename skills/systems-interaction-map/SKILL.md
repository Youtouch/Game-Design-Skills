---
name: systems-interaction-map
description: Map how verbs, object properties and systems interact (an interaction matrix), trace chains of consequences, and find gaps, surprising emergent combinations, runaway loops and soft-locks. Use when designing systemic or sandbox mechanics (elements, physics, AI factions, crafting), when players find unintended combos, or before adding a new system to an existing set.
---

# Systems Interaction Map

Systemic design states general rules ("fire spreads to flammable things") rather than scripting each case. The payoff is combinations nobody scripted; the risk is combinations nobody checked. This skill makes the rules explicit enough to trace. Design only.

## Inputs

- Player verbs and world systems (elements, physics, factions, weather, crafting).
- Object properties those systems read (flammable, conductive, heavy, wet, hostile).
- The intended experience: how much surprise and player invention the game wants, and which outcomes must never happen (critical path broken, permanent loss).

## Procedure

1. **List properties, not objects.** Rules should read and write properties ("wooden → flammable"), so new objects inherit behaviour. Objects are bundles of properties.
2. **Build the interaction matrix:** rows are causes (verbs, systems, states such as burning), columns are properties. Each cell is a rule: the effect, its magnitude or duration, and whether it changes a property. Empty cells are decisions: "nothing happens" should be chosen, not forgotten.
3. **Check consistency.** If arrows pin wooden targets, do they pin wooden doors? Players generalise rules; exceptions read as bugs unless signalled.
4. **Trace chains.** Start from each player verb and follow effects two or three steps (fire → burns rope → bridge falls → enemy falls). Record chains that create interesting options (keep), trivialise intended challenges (decide), or reach a forbidden outcome (fix).
5. **Find loops.** A loop where an effect re-triggers its cause (fire spreads to grass, grass burns, more fire) needs a limiter: fuel, decay, a cap, or a counter-system (rain). Check that the limiter holds at the largest scale the game allows.
6. **Protect forbidden outcomes.** For each must-not-happen outcome, find every chain that reaches it and pick a protection: make the critical object lack the property, provide a recovery path, or accept and signal the risk. Prefer protections that do not contradict visible rules (an unburnable wooden bridge reads as a bug; a stone bridge does not).
7. **Check readability.** Can players predict a rule from what they see? Systemic play depends on players forming correct hypotheses. Use consistent visual and audio language for properties (see `feedback-and-readability`).
8. **Budget the space.** n causes × m properties grows fast. Keep the matrix small enough to reason about; add a property only if it creates new decisions.

## Output

1. Properties list with which objects have them.
2. Interaction matrix (causes × properties), each cell an effect or an explicit "none".
3. Chains table: `start | chain | outcome | classification (keep / decide / fix) | action`.
4. Loops with their limiters.
5. Forbidden outcomes with protections.

Worked example: [example.md](example.md).

## Pitfalls

- Hand-authored exceptions that contradict a visible rule. They teach players that experimentation does not work.
- Adding a system without filling its row and column against existing ones.
- Treating every unintended chain as an exploit. Some are the best moments in a systemic game; judge against the brief.
- Uncapped loops tested only at small scale.

## Sources (paraphrased, not quoted)

- Ernest Adams & Joris Dormans, *Game Mechanics: Advanced Game Design* (2012), on emergence, feedback loops, and internal economies.
- Daniel Cook, "Loops and Arcs", Lostgarden, 2012 ([post](https://lostgarden.com/2012/04/30/loops-and-arcs)): nested loops and unexpected dynamics.
- Robin Hunicke, Marc LeBlanc & Robert Zubek, "MDA", 2004 ([pdf](https://users.cs.northwestern.edu/~hunicke/MDA.pdf)): dynamics as the run-time behaviour of mechanics.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md). For state traces that check soft-locks, see [state and experience](../design-critique/state-and-experience.md).
