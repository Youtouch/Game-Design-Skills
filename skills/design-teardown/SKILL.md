---
name: design-teardown
description: Analyse an existing game or feature as a design reference, separating firsthand observation, developer statements and inference, then extract transferable principles with the conditions they depend on. Use for competitive analysis, reference research before a pitch, "how does game X handle Y?", or when a team wants to borrow a mechanic.
---

# Design Teardown

A teardown explains why a design works (or does not) for its audience, so a principle can transfer to a different game. Copying surface features without their supporting conditions is the common failure. Design only; describe mechanics in design terms.

## Inputs

- The reference game or feature, and the version or platform examined.
- The question the teardown serves for your project ("how do they teach without text?", "why do players replay this?").
- Your access: played firsthand (how long, which modes), watched, read about.

## Procedure

1. **State the question and your project's context.** A teardown without a question becomes a review.
2. **Record your evidence base.** Separate what you observed while playing, what developers have said (with source), what others report, and what you infer. Note the version: games change through patches. An agent that has not played the game must say so and work from rules, documentation, and supplied notes; ask the user for their play observations where the question depends on feel or pacing.
3. **Describe the formal elements** relevant to the question: players, objectives, procedures, rules, resources, conflict, boundaries, and outcomes (Tracy Fullerton's formal elements). Rules first, then experience.
4. **Map loops and arcs** (see `core-loop-analysis`) and trace mechanics → dynamics → aesthetics for the features in question.
5. **Identify key decisions.** For each, name the alternative the designers did not choose, and what the chosen option seems to do. Mark designer intent as inference unless a developer has stated it.
6. **Find the supporting conditions.** What else must be true for this to work: audience, session length, platform, art style, monetisation, genre expectations, other systems? A mechanic that works because of a specific economy will not transfer to a game without that economy.
7. **Note costs and known problems.** Every decision has a downside; look for player complaints, patches, and later games in the series that changed it.
8. **Extract transferable principles.** Write each as: principle, the mechanism by which it worked in the reference, conditions it depends on, how it would need to change for your project, and how you would check it. Borrow principles, not expression: do not copy names, art, text, or distinctive content.

## Output

1. Question, version, evidence base.
2. Formal elements and loop summary (only what bears on the question).
3. Key decisions table: `decision | alternative not taken | apparent function | evidence type | supporting conditions | cost`.
4. Transferable principles table: `principle | mechanism | conditions | adaptation for our project | check`.
5. What not to borrow, and why.

Worked example: [example.md](example.md).

## Pitfalls

- Treating a commercial success as proof that each feature caused it. Success has many causes.
- Presenting your inference as the developer's intent.
- Ignoring the version: a teardown of launch-day balance is not a teardown of the current game.
- Borrowing a feature without its supporting conditions, or borrowing so closely it becomes imitation.

## Sources (paraphrased, not quoted)

- Tracy Fullerton, *Game Design Workshop*, chapters on formal and dramatic elements.
- Robin Hunicke, Marc LeBlanc & Robert Zubek, "MDA: A Formal Approach to Game Design and Game Research", 2004 ([pdf](https://users.cs.northwestern.edu/~hunicke/MDA.pdf)).
- For how to weigh developer postmortems as evidence, see [source boundaries](../design-critique/sources.md) (developer accounts are not causal studies).

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
