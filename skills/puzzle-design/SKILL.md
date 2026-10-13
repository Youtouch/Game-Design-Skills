---
name: puzzle-design
description: Design or review puzzles and puzzle chains: define the rules the player must know, prove solvability, check for unintended solutions and soft-locks, map dependencies across a level, and write a hint ladder. Use for logic, environmental, physics or adventure-game puzzles, when a puzzle is "too obscure" or "trial and error", or when planning a puzzle level.
---

# Puzzle Design

A puzzle is a problem with a right answer (one or several) that is satisfying to work out (paraphrasing Scott Kim). The satisfaction usually comes from an inference the player makes, not from searching every option. This skill checks the logic and the information, then plans help. Design only.

## Inputs

- The puzzle rules, initial state, and goal; or a puzzle concept.
- What the player already knows at this point (mechanics, conventions taught earlier).
- Intended experience: deduction, lateral insight, spatial reasoning, experimentation, or calm tinkering.

## Procedure

1. **Write the rules as the player must understand them.** Separate rules the game has taught, rules the player must discover here, and rules the player must never need. A puzzle that depends on an untaught, undiscoverable rule is a guess, not a puzzle.
2. **Prove solvability.** Trace a solution from the initial state. For small state spaces, enumerate every state; for larger ones, look for invariants (parity, conservation, ordering) that make goals impossible. A designer's redesign can silently break solvability; re-prove after every rule or layout change.
3. **List all solutions.** Enumerate or argue which other answers exist. Unintended solutions are not defects by default: decide whether each is welcome (an alternate insight), harmless, or a bypass of the intended inference.
4. **Measure the search space.** If the player can try every option faster than they can reason, the puzzle teaches trial and error. Shrink the space by teaching, or make attempts costly or informative so reasoning pays off. Cost should not be punishing for its own sake.
5. **Locate the key inference.** Name the one or two moments of insight ("the lamps form a ring", "the reflection shows the hidden side"). Check that the evidence for each is perceivable, available before it is needed, and not drowned by noise.
6. **Check soft-locks.** Can the player consume a resource, move an object, or trigger a state that makes the puzzle unsolvable? If so: prevent it, offer a reset that keeps knowledge, or accept it deliberately and say why.
7. **Map dependencies for multi-step puzzles** with a puzzle dependency chart (Ron Gilbert): each node is a step or item, each edge "needs". Work backwards from the goal. Look for bottlenecks (everything waits on one step), dead ends, and how many steps are available at once. Several open threads let a stuck player work on something else.
8. **Write a hint ladder.** Each rung gives less than the next: (1) restate the goal, (2) point to where to look, (3) name the relationship, (4) give the step. Decide how hints are reached (on request, after a delay, from an in-world source) and whether using them changes anything.
9. **Plan observation.** What would distinguish "stuck on the inference" from "did not see the evidence", "misread a rule", or "cannot perform the input"?

## Output

- Rules table: `rule | taught where / discovered here / never needed | evidence the player sees`.
- Solvability argument and solution list, with each unintended solution marked welcome, harmless, or bypass.
- Dependency chart (Mermaid) for chains; bottlenecks and open-thread counts.
- Hint ladder per puzzle.
- Risks and observations.

Worked example: [example.md](example.md).

## Pitfalls

- Mistaking obscurity for difficulty. A hidden rule makes a puzzle hard to guess, not hard to reason about.
- Red herrings without purpose. A decoy should test a specific wrong inference; random clutter just adds search.
- Pixel hunts. If the evidence is too small or low-contrast to notice, the challenge becomes perception, not thought; see `feedback-and-readability` and `accessibility-review`.
- Mixing execution with deduction by accident. A timed input inside a logic puzzle changes who can finish it.
- Assuming a puzzle is "fair" because the designer solved it. The designer knew the answer.

## Sources (paraphrased, not quoted)

- Scott Kim, "The Art of Puzzles" talk, TED, 2009, and his puzzle-design writing: a puzzle as a problem with a right answer that is fun to solve; puzzles distinguished from toys and competitive games.
- Ron Gilbert, "Puzzle Dependency Charts", Grumpy Gamer blog, August 2014 ([post](https://grumpygamer.com/puzzle_dependency_charts)): charts of steps and their requirements, worked backwards, to find dead ends and bottlenecks.
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapter on puzzles.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md). For evidence order in spatial puzzles, see [spatial reasoning](../level-metrics-sheet/spatial-reasoning.md), lesson 3.
