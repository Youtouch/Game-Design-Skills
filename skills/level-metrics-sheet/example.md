# Worked example: metrics audit of the 2-2 critical gap

Continues the sprout seed chain ([atomizer](../mechanic-atomizer/example.md), [level brief](../level-brief/example.md), [beat chart](../level-beat-chart/example.md)). Synthetic layout; all values are design estimates.

## Model

Moving entity: the *Bramblewick* hero, side view, controller. Ability stage: World 2 (run, jump, wall-slide, seeds). Units: metres and seconds.

| Metric / state | Units and model conditions | Derived limit or trace | Challenge / comfort hypothesis | Evidence and omissions |
|---|---|---|---|---|
| Run speed | m/s, flat ground | 6 | — | design value |
| Run-up to full speed | m | 3 | — | design value; acceleration curve omitted |
| Running jump | m horizontal, flat, needs 3 m run-up | 4.5 | — | design value |
| Standing jump | m, no run-up | 2.0 | — | design value |
| Jump from a leaf | m, 1.5 m of run-up | 3.0 | — | design value |
| Jump height | m | 2.0 | — | design value |
| Throw range | m, arc to a surface | 6 | aiming at 5–6 m may be imprecise | estimate |
| Leaf width / lifetime | m / s | 1.5 / 2.5 (band 3) | — | difficulty matrix |
| Single-leaf maximum gap | m, full run-up, zero margin | 4.5 + 1.5 + 3.0 = **9.0** | ≥ 0.5 m margin per jump may feel fair for this audience | hypothesis; untested |
| Single-leaf maximum gap without run-up | m | 2.0 + 1.5 + 3.0 = **6.5** | — | derived |

## Audit: valve room B, the 8 m gap

| Place / state | Claim type | Model / conditions | Trace or calculation | Cue and expected inference | Uncertainty / audience | Preserve or change | Smallest check |
|---|---|---|---|---|---|---|---|
| Launch ledge | capability | ledge is **2 m** long in the blockout | 2 m < 3 m run-up, so the player cannot reach the 4.5 m running jump. Without full run-up the gap limit is 6.5 m < 8 m: **infeasible as built** | — | none: the trace settles it | **change:** extend the ledge to 3 m, or approach from a corridor that keeps momentum | re-trace after the change |
| Moss patch (after fix) | reachability, capability | patch centre 4.75 m out, leaf spans 4.0–5.5 m | jump 1: 4.0 m ≤ 4.5 (0.5 m margin); jump 2: 8 − 5.5 = 2.5 m ≤ 3.0 (0.5 m margin) | — | margins match the planning hypothesis | preserve | prototype timing with the 2.5 s lifetime |
| Moss patch | visibility | camera framing from the ledge; patch 1 m below ledge height | patch is inside the frame at the ledge; it is **outside** the frame from the corridor entrance | player should see the patch before committing to the run-up | do players stop at the ledge or run straight in? | change: frame the patch from the corridor (raise the camera or move the patch up 0.5 m) | first-run observation: where players stop |
| Far ledge | inference | landing ledge is in shadow | reachable (trace above) | "is there somewhere to land?" | low light may hide the landing | change: a light grate above the far ledge, which also echoes the brief's grate lighting | ask after the session what players expected beyond the gap |
| Return | reachability | after valve B, can the player go back? | the far side connects to the upper walkway (brief's order trace); no return across the gap needed | — | none | preserve | — |

## What the audit shows

- **The decisive finding is a capability trace, not a feel question.** The blockout's 2 m ledge made the gap impossible, though the gap width alone looked fine against the 9.0 m maximum. A metrics sheet that lists only "running jump 4.5 m" without its run-up condition would miss it.
- **Feasible is not visible.** After the fix the gap is reachable with 0.5 m margins, but the patch can't be seen from the corridor, so players may commit to a run before they know where to throw. That is a cue problem; the jump distances are not at fault.
- **Margins are hypotheses.** 0.5 m per jump is a planning choice for this audience, to be checked in the prototype, not a universal safety margin.
