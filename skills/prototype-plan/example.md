# Worked example: prototyping *Tidewright*'s room effects

Continues the [core-loop example](../core-loop-analysis/example.md), which recommended that restored lighthouse rooms change fishing (the lamp reveals night schools, the workshop crafts lures). Synthetic plan. Team: one designer, one programmer, two weeks before the next milestone.

## 1. Open questions, ranked

| Question | Risk if false | Cost to learn late |
|---|---|---|
| A. Do room effects give players a reason to plan the next session? | high: the long-term loop stays disconnected, the core recommendation fails | high: rooms are the main content budget |
| B. Is reading ripples satisfying for 20–30 minutes? | high | low: a playable catch loop already exists and earlier tests were positive |
| C. Do coin rates still let a casual player restore a room every 2–3 sessions with room effects in place? | medium | low: a spreadsheet answers it in hours |

Prototype A. Answer C on the side, because A's prototype needs its numbers.

## 2. The question, written to fail

"After a room is restored, do players choose to go somewhere or try something different in the next session, without being told, and can they say why?"

## 3–4. Fidelity

| Option | Represents the mechanism? | Verdict |
|---|---|---|
| Spreadsheet | coin flows only, not choices | answers C, not A |
| Paper | session choices and room effects as cards; fishing as a die roll | plausible: the question is about planning across sessions, not about feel |
| Greybox of three sessions | everything, slowly | two weeks of building for a question paper may answer in two days |

**Choice: paper first, then greybox only if paper is ambiguous.** Paper omits the catch loop's feel and real session length. Bias: dice-based fishing makes all spots feel the same, so preferring a spot for its feel can't show up. That could understate how attached players get to spots; note it in the result.

**Side calculation (C):** with the [core-loop example](../core-loop-analysis/example.md)'s rates, a casual 25-minute session at the best spot earns about 25 × 26.7 ≈ 667 coins. A room priced at 1,500 takes about 2.25 sessions. That meets "a room every 2–3 sessions" at the best spot, and misses it at the minnow shore (25 × 15 = 375 per session, 4 sessions). Fine, provided room effects send players to better spots, which is exactly question A.

## 5. Criteria (set before running)

- **Pass:** at least 4 of 6 participants change their plan after a restoration and explain it by the room's effect ("the lamp is on now, I want to see the night schools").
- **Fail:** 2 or fewer do, or the explanations are about coins only.
- **Ambiguous:** 3, or changes happen but explanations are vague. Then build the three-session greybox.
- **Decisions:** pass: spec room effects for all rooms. Fail: revisit the journal-only alternative from the core-loop review. Ambiguous: greybox.

## 6–7. Participants and timebox

Six people outside the team who play relaxed games. Two days to make the cards, one day to run (45 minutes each, simulating six sessions). Total three days of the two weeks.

## Plan table

| Question | Risk if false | Fidelity | Includes | Omits (and bias) | Pass / fail / ambiguous | Participants | Timebox | Decision on each outcome |
|---|---|---|---|---|---|---|---|---|
| A: do room effects drive next-session plans? | high | paper | spots, rooms, effects, coins | catch feel, real session length (may understate spot attachment) | ≥4/6 / ≤2/6 / 3 or vague | 6 outside players | 3 days | spec / revisit journal / greybox |
| C: room cadence | medium | spreadsheet | rates, prices | variance in catches | 2–3 sessions per room at the best spot | — | 2 hours | adjust prices if missed |
