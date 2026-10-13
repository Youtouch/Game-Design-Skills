---
name: prototype-plan
description: Plan a design prototype around the riskiest open question, choosing the cheapest fidelity that can actually answer it (paper, spreadsheet, toy, greybox, video mock-up, facilitated play), stating what it cannot tell you, and fixing pass/fail criteria and a timebox before building. Use when deciding what to prototype next, when a team wants to build "a vertical slice" too early, or when a prototype ran but nobody knows what it proved.
---

# Prototype Plan

A prototype is a question with a build attached. The question decides the fidelity: a paper map can test whether a route makes sense, never whether a jump feels good. This skill picks the question, the cheapest build that can answer it, and the result that would change a decision, before anything is built. Design only: describe what to build, not how to implement it.

## Inputs

- The concept or feature and its intended experience.
- Open questions and assumptions (from `concept-ideation`, `core-loop-analysis`, a critique, or a playtest).
- Budget: people, days, and tools available.

## Procedure

1. **List the open questions** and rank by risk: if this is false, how much of the design dies, and how expensive is it to find out late? Pick one (at most two) for this prototype.
2. **Write the question so a result can answer it.** "Is the fishing fun?" cannot fail. "Do players choose a different spot after a room is restored, without being told?" can.
3. **Choose the cheapest fidelity that represents the mechanism in question:**

   | Fidelity | Can answer | Cannot answer |
   |---|---|---|
   | Spreadsheet or calculation | flows, rates, feasibility, balance | whether anyone wants to do it |
   | Paper or tabletop | rules, choices, information, turn structure | timing, motion, feel, real-time pressure |
   | Toy (one mechanic, no goals) | whether the core action is satisfying to repeat | whether it sustains a session |
   | Greybox level or room | spatial reading, routes, pacing, encounter flow | final readability (art changes cues), long-term motivation |
   | Video or animatic mock-up | tone, pitch, whether an idea reads to an audience | anything interactive |
   | Facilitated play (a person runs the rules) | systems too costly to build yet, AI or narrative responses | unaided discovery; the facilitator is part of the test |

   If the mechanism depends on timing, motion, sound, or real-time pressure, paper cannot represent it: go up a level.
4. **State what the prototype omits** and how that could bias the result (greybox art makes cues harder to read; a facilitator explains rules a game would have to teach).
5. **Set pass, fail, and ambiguous criteria before building.** Name the observation and the threshold you'll act on, and what you will do in each case: continue, change, or drop. A threshold chosen after the result is not a criterion.
6. **Choose participants:** the team (can only rule out ideas even its makers find weak), people outside the team, or the target audience. Match to the question.
7. **Timebox it.** If the build will take longer than the decision is worth, cut scope or lower fidelity.
8. **After running it:** report the result against the pre-set criteria, including ambiguous outcomes, and what the omissions mean for the conclusion. Feed it to `playtest-plan-and-report` if participants were involved.

## Output

| Question | Risk if false | Fidelity | Includes | Omits (and bias) | Pass / fail / ambiguous | Participants | Timebox | Decision on each outcome |
|---|---|---|---|---|---|---|---|---|

Worked example: [example.md](example.md).

## Pitfalls

- Building a vertical slice to answer a question a toy could answer. Polish hides whether the core works.
- Testing what is easy to build instead of what is risky.
- Picking a fidelity that cannot represent the mechanism (paper for a timing question), then trusting the result.
- Moving the goalposts after seeing the result.
- Treating a prototype as the first version of the product. Its job is the answer; throwing it away is normal.

## Sources (paraphrased, not quoted)

- Jesse Schell, *The Art of Game Design: A Book of Lenses*, first edition, chapter 7 (pp. 82–95): prototypes answer questions; fidelity must represent the disputed mechanism. See [source boundaries](../design-critique/sources.md).
- Tracy Fullerton, *Game Design Workshop*, chapters on prototyping (physical and digital).
- Alex Beachum, ["Demaking Outer Wilds"](https://www.mobiusdigitalgames.com/news/demaking-outer-wilds), 2015: a simplified prototype helped with narrative relationships but distributed information differently from traversal. See [spatial source notes](../level-metrics-sheet/spatial-sources.md).

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md) (section on choosing a prototype), [source boundaries](../design-critique/sources.md).
