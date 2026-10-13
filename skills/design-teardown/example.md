# Worked example: Minesweeper teardown

**Question for our project:** we are designing a short deduction game for commuters. What makes classic Minesweeper's deduction satisfying, and where does it break?

**Version and evidence base:** the classic grid rules common to desktop versions (beginner 9×9 with 10 mines, intermediate 16×16 with 40, expert 30×16 with 99). This example is written from those published rules and widely documented behaviour; no developer statements are used. A real teardown should add dated firsthand play notes. Statements about "players" below are inferences, marked as such.

## Formal elements (relevant part)

- **Objective:** reveal every safe cell.
- **Procedures:** reveal a cell; flag a cell (optional bookkeeping).
- **Rules:** a revealed safe cell shows how many of its eight neighbours are mines; zero cascades to reveal neighbours; revealing a mine ends the game.
- **Information:** each number is a local constraint; the whole board is a constraint-satisfaction problem.
- **Conflict:** the player against hidden information, and often a clock.

## Loop

Moment loop (seconds): read numbers → deduce a safe cell or mine → reveal → new numbers. Each reveal adds constraints, so the loop feeds itself. Session loop (minutes): board → win or loss → new board (optionally chasing a faster time). No long-term loop, which suits short sessions.

## Key decisions

| Decision | Alternative not taken | Apparent function | Evidence type | Supporting conditions | Cost |
|---|---|---|---|---|---|
| Numbers count all eight neighbours | four orthogonal neighbours | richer overlapping constraints, so pairs of numbers interact | rule analysis | square grid; small, readable digits | harder for newcomers to read diagonals |
| Zero cascades | reveal one cell at a time | skips trivial work; opens space quickly | rule analysis | random mine placement with typical density | none obvious |
| Random boards, no solvability check (classic) | generate only boards solvable without guessing | simple generation; endless variety | rule analysis: random placement can leave positions no deduction resolves | — | **forced 50/50 guesses**: the player can deduce perfectly and still lose, which contradicts the deduction fantasy |
| First reveal is safe (in many versions) | first click can be a mine | avoids a loss before any information exists | documented behaviour of common desktop versions | — | none; it fixes the worst case of the previous row |
| Flags are optional | required marking | experts skip bookkeeping for speed; newcomers use it as memory | inference | — | none |
| Instant loss on a mine | lives or a penalty | stakes on every reveal; a clean end to each attempt | rule analysis | very short sessions; low cost of restarting | a forced guess ends a long expert board abruptly |

## What works, and why

- **Every action adds information.** The moment loop never stalls in a solvable position: each reveal produces new constraints. Mechanism: local numbers combine into global inferences.
- **Patterns become vocabulary.** Recurring local configurations become recognisable chunks, which is a plausible mechanism for the feeling of growing skill (inference).
- **Short, restartable attempts.** Instant loss is tolerable because a board takes minutes and restarting is free.

## Known problem

Forced guesses. They are a generation choice, not inherent to the rules: a generator can check each board with a solver that never guesses and regenerate (or move mines) wherever the solver gets stuck. Variants that advertise "no-guess" boards take this approach.

## Transferable principles

| Principle | Mechanism | Conditions | Adaptation for our commuter game | Check |
|---|---|---|---|---|
| Each action should yield new information | reveals add constraints that feed the next decision | player can always find a move that informs | design reveal rules so a logical move always exists; generate boards with a solver check | paper prototype plus a solver: what share of positions have a deducible move? |
| Never punish before information exists | safe first move | — | guarantee the opening | rule trace |
| Instant loss only if attempts are short | low restart cost keeps stakes from feeling unfair | sessions under a few minutes | commute sessions may be interrupted: keep instant loss, but save mid-board on interruption | observe whether interrupted players resume or abandon |
| Remove guesses where deduction is the fantasy | forced guesses break the promise | deduction is the intended experience | no-guess generation | solver check on every generated board |

## What not to borrow

The 30×16 expert grid: too fine for a phone held in one hand on a train. The concept of hidden mines is generic; the specific presentation (mine and flag icons, smiley button) is not ours to copy and does not serve the question.
