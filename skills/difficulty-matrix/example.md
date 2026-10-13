# Worked example: sprout seed difficulty matrix

Builds on the [atomizer example](../mechanic-atomizer/example.md). Synthetic values, not playtested. Audience: players who have finished World 1 (run and jump only) and are new to seeds.

## 1. Demands

| Demand | What the player must do | Parameters that change it |
|---|---|---|
| Perception | find moss; read the wilt warning | moss contrast, patch size, warning duration |
| Inference | predict where and when the leaf appears | delay, flight time, decoy surfaces |
| Choice | pick a landing point; budget two seeds | number of valid moss patches, chain length |
| Execution | aim; jump after the leaf opens and before it wilts | patch size, gap width, chain slack |
| Recovery | survive a mistake | what lies below: floor, short respawn, long respawn |

## 2. Derived timing parameter

For a chain (throwing the next seed while standing on a leaf), the timing demand comes from four values together, not lifetime alone. Let L be lifetime, d delay, f flight time, w windup (0.2 s), and j transfer airtime (0.6 s). The latest moment after a leaf opens that the player can still stand on it, throw, and transfer safely is

**chain slack S = L + j − (w + f + d)**

With L = 3.0, d = 0.8, f = 0.4: S = 3.0 + 0.6 − 1.4 = **2.2 s**. Shortening lifetime to 2.0 gives 1.2 s; also raising delay to 1.2 gives 0.8 s. The model omits reaction time and assumes the player throws immediately on landing; treat S as an upper bound, not a comfort target.

## 3. Bands (provisional)

| Parameter | Unit | 1 Intro | 2 Practice | 3 Standard | 4 Hard | 5 Mastery |
|---|---|---|---|---|---|---|
| Gap width | m | 6 (one leaf) | 7 | 8 | 11 (two leaves) | 12.5 (two leaves) |
| Moss patch size | m | 3 | 2 | 1.5 | 1 | 0.75 |
| Moss contrast | band | glowing | bright | natural | natural + shadow | natural, near decoys |
| Lifetime L | s | 3.0 | 3.0 | 2.5 | 2.0 | 2.0 |
| Delay d | s | 0.8 | 0.8 | 0.8 | 0.8 | 1.2 |
| Chain length | leaves | 1 | 1 | 1 | 2 | 2 |
| Chain slack S | s | n/a | n/a | n/a | 1.2 | 0.8 |
| Recovery | — | floor below | floor below | short respawn | short respawn | long respawn |

Margins: one leaf spans at most 4.5 + 1.5 + 3.0 = 9.0 m at zero margin, so an 8 m gap leaves 1.0 m spread across two jumps. Two leaves span at most 4.5 + 1.5 + 3.0 + 1.5 + 3.0 = 13.5 m; 11 m leaves 2.5 m across three jumps and 12.5 m leaves 1.0 m. Margins are planning estimates, not measured comfort.

## 4–5. Interactions and constraints

- **Rule-impossible:** chain length 3 (the hero carries two seeds and refills only on ground). No band can ask for it.
- **Near-infeasible if combined:** L = 1.4 with d = 1.2 gives S = 2.0 − 1.8 = 0.2 s, leaving almost no time to react after landing. Treat any S under about 0.5 s as a prototype question before it reaches a level.
- **Amplifying pair:** small patches (aim) with short slack (timing) stack execution demands at the same moment. Band 5 does this on purpose; nowhere else should.
- **Perception is not execution:** if players do not notice subtle moss, longer lifetimes or narrower gaps will not help. Keep contrast as its own column.

## 6. Targets by phase

| Phase | Bands | Notes |
|---|---|---|
| World 2, levels 1–2 | 1–2 | single leaf, safe recovery |
| World 2, levels 3–4 | 3, one beat of 4 | first chain appears once, with a floor |
| World 3 | 3–4 | combine with moving hazards (new demand, keep seeds at band 3) |
| Optional challenge rooms | 5 | opt-in; never on the critical path |

## 7. Validation plan

| Question | Observation that distinguishes | Rival explanation |
|---|---|---|
| Is moss readable at band 3? | first throw target per room; throws at non-moss | aim error (throw lands near moss) |
| Is chain slack the barrier at band 4? | falls after a leaf opened vs. before | player jumped before the leaf opened: an inference problem, not slack |
| Is band 5 a fair challenge? | retries, quit points, post-session "what were you trying?" | frustration with long respawn rather than with timing |

Record audience, prior exposure, assists, and build. A failure count alone does not establish perceived difficulty.
