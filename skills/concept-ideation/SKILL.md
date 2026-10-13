---
name: concept-ideation
description: Generate a varied set of game or feature concepts from a brief and its constraints, then narrow them by fit, riskiest assumption, and cheapest test, ending with two or three concepts ready for one-pagers. Use for pitches, game jams, new features, brainstorming sessions, or when a team is stuck on a single idea.
---

# Concept Ideation

Generate widely, then judge. Mixing the two produces the first plausible idea, which is usually the most familiar one. This skill separates divergence from convergence and ends each surviving concept with the assumption most likely to kill it and the cheapest way to test that. Design only.

## Inputs

- The brief: theme or problem, audience, platform and input, session length, team size, time budget, and any pillars.
- Hard constraints versus preferences. Ask which is which if unclear.
- What already exists (the team's previous games, the current game's systems, for feature ideation).

## Procedure

### Diverge

1. **Restate the brief as constraints and openings.** Constraints rule ideas out; openings are what the brief leaves free.
2. **Generate with several methods**, a few ideas each, without judging:
   - *Verb first:* pick an unusual core action and ask what game needs it.
   - *Experience first:* start from a feeling or situation (being trusted with something fragile, being slowly outnumbered) and find mechanics that could produce it.
   - *Constraint as feature:* turn a limitation into the hook (one button; no text; a two-minute session).
   - *Subtract a convention:* remove something the genre always has (a platformer without jumping; a shooter where you cannot aim) and see what fills the gap.
   - *Collide two systems:* combine mechanics from distant genres and look for the interaction, not the sum.
   - *Change the point of view:* play the obstacle, the tool, the bystander, the place.
3. **Aim for spread, not count.** After generating, check the set along a few axes (core verb, tone, solo/social, skill/strategy/expression). If most ideas cluster, generate more in the empty regions. Watch for defaults: if an idea is the first thing anyone would think of for this theme, keep it but generate past it.
4. **Write each idea as one line:** name, hook, core verb, intended experience.

### Converge

5. **Filter by hard constraints only.** Remove ideas that cannot fit the platform, input, time, or team. Do not filter by taste yet.
6. **Cluster and merge.** Duplicates and near-duplicates collapse; sometimes two halves make one strong idea.
7. **For each survivor, name the riskiest assumption** (the belief that, if false, sinks the concept: "dragging the tide line is fun for more than a minute") and the **cheapest test** (paper, a toy prototype, a video mock-up, a one-hour code-free simulation).
8. **Compare survivors** on fit to the brief, novelty relative to the nearest references (name them and the difference), scope against the budget, and how cheap the riskiest test is. Do not total a score; explain the trade-off you would choose and why.
9. **Pick two or three** and hand them to `game-design-doc` as one-pagers, or to a prototype plan.

## Output

1. Constraints and openings.
2. Divergent list (one line each), grouped by method, with a note on spread.
3. Convergence table: `concept | hook | core verb | experience | fits constraints? | nearest reference and difference | riskiest assumption | cheapest test | scope risk`.
4. Recommendation: chosen concepts, trade-offs, and the first test to run.

Worked example: [example.md](example.md).

## Pitfalls

- Judging while generating. It narrows the set before it exists.
- Theme as decoration. A theme should change what the player does, not only the art.
- Novelty for its own sake. A familiar loop with one meaningful twist is often stronger than five twists.
- Ending with a favourite instead of a test. The output of ideation is a question to answer next.

## Sources (paraphrased, not quoted)

- Tracy Fullerton, *Game Design Workshop*, chapter on conceptualisation (brainstorming methods, alternating divergent and convergent work).
- Brenda Brathwaite & Ian Schreiber, *Challenges for Game Designers* (2008): constrained design exercises.
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapters on ideas and on iteration (riskiest problems first, cheapest prototype).

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
