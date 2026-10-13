---
name: core-loop-analysis
description: Map a game's loops at each timescale (moment, session, long-term) and its one-time arcs, trace how actions feed goals and rewards, and diagnose broken, dominated or disconnected loops. Use when pitching or reviewing a concept, when a game "has no hook" or players stop after a few sessions, or before speccing systems that must feed each other.
---

# Core Loop Analysis

A loop is a repeated cycle: the player forms a goal, acts, the game responds, and the result changes what the player wants next. An arc is a path the player traverses once, such as a story or a scripted reveal (Daniel Cook's loops-and-arcs distinction). This skill maps both and checks how they connect. Design only.

## Inputs

- Concept, pitch, or design doc; the intended experience and audience.
- Session context: typical session length and frequency, if known.
- Any observed behaviour (where players stop, what they repeat), kept separate from the designer's predictions.

## Procedure

1. **List loops by timescale.** Moment-to-moment (seconds), session (minutes), long-term (days or the whole game). Do not force three tiers: a puzzle game may have no long-term loop, and that can be right.
2. **Write each loop as a cycle:** goal → action → system response → feedback → reward or progress → new goal. Name the resource, information, or state that carries each step into the next. A step with nothing carried is a break.
3. **Connect the tiers.** For each loop, what does it consume from and produce for the loop above or below? A moment loop that never changes session goals is a disconnected toy; that can be valid (pure play), but say so.
4. **List arcs** (story beats, one-off reveals, unlocks that happen once). Mark where arcs refresh a loop by changing its context, and where an arc stands alone. Arcs are consumed; loops are repeated. Content plans that rely on arcs need a content budget.
5. **Trace mechanics → dynamics → aesthetics** for the main loop (Hunicke, LeBlanc & Zubek's MDA). Rules are designed; dynamics are predicted from rules; the experience is a hypothesis until players report it. Write the chain explicitly so each link can be questioned.
6. **Name the motivation hypothesis**: what need or interest is the loop meant to serve (for example competence, autonomy, relatedness, curiosity, expression, collection)? Treat it as a hypothesis about this audience, not a property of the mechanic.
7. **Diagnose.** Use the checks below. For each issue, state the evidence type (rule trace, calculation, observation, or prediction) and a plausible rival explanation.
8. **Recommend levers** that act on the broken link, and what each might cost.

## Checks

| Symptom | Likely break | First question |
|---|---|---|
| Players repeat one action and ignore others | a dominant strategy inside the loop | is the alternative ever better? trace payoffs (see `balance-table-check`) |
| Players stop after a few sessions | long-term goal invisible, or session loop produces nothing it needs | what does a session leave the player wanting? |
| Rewards feel meaningless | reward not consumed by any loop | where is this reward spent or used? |
| The game feels like a list of chores | loops connected by obligation, not by goals the player holds | which steps does the player choose, and which are toll gates? |
| Content runs out fast | arcs carry the experience; loops are thin | which loop survives once arcs end? |
| Mastery plateaus | the moment loop stops presenting new decisions | what changes in the decision space after hour one? |

Not every symptom is a defect. A short, complete arc game is legitimate; so is a toy with no goals.

## Output

1. A loop diagram (text or Mermaid) per timescale, with the carried resource or state on each edge.
2. A table: `loop | timescale | goal | action | feedback | reward / carried state | feeds | motivation hypothesis | evidence`.
3. Arcs list with what each refreshes.
4. Findings: break, evidence type, rival explanation, lever, cost, and the smallest check.

Worked example: [example.md](example.md).

## Pitfalls

- Drawing a loop with no decision in it. If the player cannot act differently, it is a sequence, not a loop.
- Calling a loop "engaging" because it has rewards. Rewards that feed nothing are noise.
- Treating a motivation model as a measurement. Motivation labels organize hypotheses; they do not confirm them.
- Fixing retention by adding more rewards rather than repairing the link that is broken.

## Sources (paraphrased, not quoted)

- Daniel Cook, "Loops and Arcs", Lostgarden, April 2012 ([post](https://lostgarden.com/2012/04/30/loops-and-arcs)): loops as repeated, nested feedback cycles; arcs as one-time paths that are efficient but consumed.
- Robin Hunicke, Marc LeBlanc & Robert Zubek, "MDA: A Formal Approach to Game Design and Game Research", AAAI workshop paper, 2004 ([pdf](https://users.cs.northwestern.edu/~hunicke/MDA.pdf)): designers author mechanics; players experience aesthetics through dynamics.
- Richard M. Ryan, C. Scott Rigby & Andrew Przybylski, "The Motivational Pull of Video Games: A Self-Determination Theory Approach", *Motivation and Emotion* 30(4), 2006 ([doi](https://doi.org/10.1007/s11031-006-9051-8)): reported associations between perceived autonomy, competence and relatedness and enjoyment in their samples. Correlational survey and lab findings; they do not prove any particular loop will satisfy those needs.
- Daniel Cook, "The Chemistry of Game Design", Lostgarden, 2007: skill atoms as the smallest loops.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
