# Worked example: routing three requests

Synthetic requests.

## 1. "Players say my roguelike gets boring after a few runs. Thoughts?"

**Decision:** what to change so later runs stay interesting. **Route:** `core-loop-analysis` first: map the run loop and the long-term loop, and find what a run leaves the player wanting. If the break is "the same build wins every time", follow with `balance-table-check` on the item or upgrade table. If it is "nothing to unlock", `progression-curve`.

**Not:** `concept-ideation` (the game exists) or a full `design-critique` of everything (the question is specific).

## 2. "Here's my level layout. Is it good?"

**Decision unclear.** Ask what the level is for, or infer it from the brief if one exists and say so. **Route:** `design-critique` scoped to the level's intent, which usually points to one specialist:

- if the concern is jumps or routes: `level-metrics-sheet` (feasibility traces first);
- if pacing: `level-beat-chart`;
- if a fight in it: `encounter-design`.

Lead the answer with the strongest supported finding, not a checklist of every skill.

## 3. "Make a 5% legendary drop feel fair."

**Decision:** drop protection for one item. **Route:** `loot-table-design`: compute the median and 90th-percentile wait (14 and 45 attempts at 5%), compare with the brief, and choose a protection. If the item feeds an economy (tradeable, sellable), check it against `economy-model`.

**Shared rule in action:** "feel fair" is an experience claim. The arithmetic shows how long unlucky players wait; whether that feels fair needs player evidence. Say so, and propose the check.
