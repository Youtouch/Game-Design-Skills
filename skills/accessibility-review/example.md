# Worked example: accessibility review of the sprout seed

Continues the sprout seed chain ([atomizer](../mechanic-atomizer/example.md), [difficulty matrix](../difficulty-matrix/example.md), [feedback](../feedback-and-readability/example.md)). Synthetic review; nothing here has been tested with players.

**Intended challenge:** planning where and when a temporary platform will exist, and jumping within its lifetime. **Not the point:** distinguishing colours, holding buttons, fine stick precision, hearing cues.

## Demand review

| Interaction | Demand | Ability areas | Intended challenge? | Barrier | Option(s) | What the option changes | Default | Status |
|---|---|---|---|---|---|---|---|---|
| Find moss | perceive green texture on stone | colour vision, low vision | no (W2–3); yes in band 5 rooms | green-on-grey may be indistinct | aim marker shape change (from the feedback example); high-contrast moss outline option | marker: removes the inference (solution-like); outline: same information, more visible (equivalent evidence) | marker on; outline off | spec |
| Aim | hold aim button, move stick, release | motor (endurance, precision) | partly (aim is a skill; holding is not) | hold-to-aim | hold or toggle aim; aim snapping to nearest moss within 1 m (option) | toggle: removes an incidental hold; snap: reduces the precision challenge | hold; both options off | spec |
| Wait for the leaf | read the bud swell (visual) and rising pitch (audio) | hearing, vision | yes (timing) | none: both channels carry it | — | — | — | ok |
| Jump before wilt | track flicker during last 1.0 s; act in time | vision, motor (speed), cognition (processing speed) | yes | short slack in bands 4–5 | "slower wilt" assist: lifetime × 1.5 | raises chain slack (band 4: L 2.0 → 3.0 gives S 1.2 → 2.2 s); keeps the planning challenge | off; offered when a player fails a chain room 5 times | spec |
| Wilt flicker | flashing during last second | photosensitivity | no | flicker could exceed safe flash rates if fast and high-contrast | keep the flicker to no more than three flashes in any one second (the WCAG 2.3.1 general threshold) and low contrast; reduce-flashing setting replaces flicker with a steady browning | removes the hazard; keeps the information | safe by default | spec |
| Seed count | read belt pouch | vision, cognition | partly (budgeting is the choice) | small diegetic icon | optional HUD counter with large numerals | same information, more legible | off | spec |
| Recovery | fall and respawn | cognition, motor (fatigue) | partly | long respawn in band 5 rooms | band 5 rooms are opt-in; checkpoint-in-room assist | lowers failure cost only | assist off | spec |

## Priority

1. **Flicker safety:** a potential health hazard. Fix in the default, not an option.
2. **Moss visibility and hold-to-aim:** incidental barriers on the critical path. Already addressed by defaults (marker) and an option (toggle).
3. **Wilt timing:** core challenge. Offer the slower-wilt assist; do not change the default.

## Equivalent evidence vs. solution

The high-contrast moss outline gives the same information more visibly. The aim marker answers "is this moss?" outright. Both are fine in Worlds 2–3. In band 5 rooms, where reading moss is part of the challenge, the marker should show range only; the outline option stays available, because it does not decide for the player.

## Evaluation plan

Recruit players with colour-vision differences, low vision, and limited hand endurance or one-handed play. Record their setup and assistive technology. Tasks: World 2-2 and one band 4 chain room, with options available but not pointed out at first; then ask what they would change. Ask what challenge they wanted to keep. Do not infer a universal setting from their choices.
