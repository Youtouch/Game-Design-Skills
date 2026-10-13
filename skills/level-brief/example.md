# Worked example: level brief for 2-2 "Cistern Steps"

Continues the sprout seed chain ([atomizer](../mechanic-atomizer/example.md) → [difficulty matrix](../difficulty-matrix/example.md) → [introduction plan](../mechanic-introduction-plan/example.md)). Synthetic; values are design estimates.

```markdown
# Level Brief: Cistern Steps
- Position: World 2, level 2 of 4. Prev: 2-1 "Mossgate" (seed exposition, safe floor). Next: 2-3 "Root Lift" (seed supply, first chain).
- Playtime target: 6–9 min first visit (production estimate for a mid-world level; not a player target).

## Player goals
- Objective: drain the cistern by reaching the sluice wheel at the far end.
- Moment-to-moment: pick a moss patch, plant, cross before the leaf wilts.
- Designer intent: players become confident with single leaves over real drops, without a safety floor, and start reading moss in natural lighting.

## Mechanics in play
| Mechanic | Status | Demands / parameters / validation status | Entry | Peak | Exit |
|---|---|---|---|---|---|
| Run, jump, wall-slide | reinforced | from World 1; metrics sheet values | — | — | — |
| Seed: single leaf | reinforced (challenge) | gap 7→8 m, patch 2→1.5 m, lifetime 3.0→2.5 s; *estimates* | band 2 | band 3 | band 2 |
| Moss contrast | reinforced | bright → natural lighting | band 2 | band 3 | band 2 |
| Rising water | new (world rule, low stakes) | water level rises one step after each sluice valve; changes which moss is reachable | — | — | — |

No new player action. The rising water is a new world rule, but it changes routes, not execution, and is revealed by a view rather than a fail state.

## Setting constraints
- Flooded stone cistern; the sluice wheel is visible from the entrance across the main hall (landmark).
- Light from grates above: natural moss contrast in lit areas, shadow elsewhere.
- Reuses the World 2 tile set; one new prop (valve).

## Spatial relationships
| Decision / state | Destinations and return | Evidence / channels | Expected inference | Intentional uncertainty | Missing model / check |
|---|---|---|---|---|---|
| Entrance overlook | main hall; return to 2-1 hub | sluice wheel visible; water sound | "the wheel is the goal" | route to the wheel | none |
| After valve 1 (water +1) | floating walkway rises: higher moss comes within throw range, lowest moss goes under | water line marks on walls before and after | "the water changes what I can reach" | which valve next | trace: can the player strand themselves by turning valves in the wrong order? |
| Shadowed alcove | optional secret | faint moss in shadow; single drip sound | "something might be there" | whether it is reachable | off critical path by design |

Order trace: each valve raises the water one step and cannot be undone. Both valves are reachable at water level 0 and at +1; the route to the wheel needs +2 and uses only moss above the +2 line. So either order works, and no order strands the player (checked on paper against the layout sketch). Returning to the entrance is always possible via the upper walkway.

## Metric references
- Running jump 4.5 m; leaf jump 3.0 m; leaf width 1.5 m (metrics sheet).
- Single-leaf maximum gap 9.0 m at zero margin; this level's widest critical gap is 8 m.
- Gap: no metric yet for jump height from a leaf. Flagged for the metrics sheet.

## Success criteria
| Criterion | How observed |
|---|---|
| Players cross the 8 m gap without a floor | rule trace: feasible with 1.0 m total margin; observation: falls before vs. after the leaf opened |
| Players read natural-light moss | first throw target in the lit hall (new players, no prior exposure, no hints) |
| Players understand the water rule | ask after the session: "what happened when you turned the valve?" |
| The level is not a difficulty spike from 2-1 | compare retries per room with 2-1; ask what was hard and why |

## Risks and open questions
- Risk: rising water could feel like a fail state; preview the water line before the first valve.
- Risk: the 8 m gap at 2.5 s lifetime may be band 4 in practice. Prototype it first.
- Open: should the secret alcove use a decoy surface? (Deferred to World 3.)
```

## Notes on the choices

- **Why a world rule but no new action.** The introduction plan reserves 2-2 for single-leaf challenge. A new action would compete for attention; a route-changing world rule adds a thinking layer without adding execution load.
- **Why the order trace.** Two valves in either order is a nonlinear state change. Without the trace, "can the player soft-lock?" is unanswered, and no playtest count can prove it either way.
- **Why the success criteria differ in kind.** Gap feasibility is a rule trace; moss readability needs first-encounter observation; understanding the water rule needs the player's own account.
