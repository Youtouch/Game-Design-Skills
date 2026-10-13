---
name: quest-design
description: Design or review quests and quest chains as goals, obstacles, choices and state changes; trace flags across branches to find contradictions, dead ends and lost content; and check objective clarity and consequence. Use when writing quests or missions, planning a branching questline, or when players get lost, stuck, or report that their choices did not matter.
---

# Quest Design

A quest gives the player a goal, puts something in the way, and changes the world when it resolves. Branching quests add state, and state is where quests break. This skill structures the design and traces that state. Design only: describe flags and conditions in design terms, not scripting.

## Inputs

- The questline: quests, their givers, objectives, choices, and rewards.
- The world state they read and write (characters alive or dead, factions, items, locations unlocked).
- The intended experience: what the quest is for (teaching a mechanic, revealing a character, offering a moral choice, showing a place).

## Procedure

1. **State each quest's purpose** in one line. A quest without a purpose beyond its reward becomes a chore; a short one can still be fine (an errand that shows a place).
2. **Write the structure:** giver → hook (why the player should care) → objectives → obstacles → choices → resolution → consequences. Note which obstacles use the game's core mechanics; a quest that only asks the player to walk between markers uses none.
3. **Model the state.** List every flag the questline reads or writes (`miller_alive`, `mill_burned`, `has_ledger`). For each quest, write preconditions (what must be true to start, to complete each objective) and effects.
4. **Trace branches.** Enumerate the combinations of choices that can occur, including quest order where it is free. For each path, check: can every started quest be finished or explicitly failed? Does any precondition depend on something a previous choice destroyed? Does dialogue reference events that did not happen on this path? A small questline can be enumerated by hand; a large one needs a dependency chart (see `puzzle-design`) and a check per flag.
5. **Check consequences.** For each choice, what changes, and where does the player see it? A consequence the player never perceives does not make the choice meaningful to them. Not every choice needs a large consequence; but a choice presented as weighty should change something visible.
6. **Check objective clarity.** At each step the player should be able to find what to do next, why, and where (journal, markers, dialogue recall). Revisitable objectives matter for players who take breaks. Mystery about *what the answer is* differs from confusion about *what the task is*.
7. **Pace with the level.** Place quest beats on the level beat chart: where do they ask for travel, combat, conversation, or puzzles? Repeated travel between the same two points is a pacing cost unless the route changes.
8. **List failure states:** can the quest fail? Is failure signalled and does it lead somewhere (a different outcome) or nowhere (a dead entry in the journal)?

## Output

1. Quest table: `quest | purpose | giver | hook | objectives | core mechanics used | choices | consequences (where seen)`.
2. Flags table: `flag | written by | read by | default`.
3. Branch trace: each path with its outcome and any contradiction, dead end, or lost content.
4. Fixes, with which experience each preserves.

Worked example: [example.md](example.md).

## Pitfalls

- A choice that silently removes a later quest's precondition. The most common branching bug; trace it.
- Dialogue that assumes one path. Every line that references an event needs the flag that proves it happened.
- Rewards as the only motivation. If the hook is only the reward, the quest is a transaction.
- Treating hidden consequences as depth. Delayed consequences can be powerful, but the player must eventually see the link.

## Sources (paraphrased, not quoted)

- Jeff Howard, *Quests: Design, Theory, and History in Games and Narratives* (2008): quests as structures joining space, challenge, and meaning.
- Ron Gilbert, "Puzzle Dependency Charts", Grumpy Gamer, 2014 ([post](https://grumpygamer.com/puzzle_dependency_charts)): dependency charting, applicable to quest steps.
- Microsoft, [Xbox Accessibility Guideline 109](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109): revisitable objectives and navigation support. Check the current version.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md). For state traces, see [state and experience](../design-critique/state-and-experience.md).
