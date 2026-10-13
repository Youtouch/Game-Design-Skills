# Worked example: critique of a two-player heist room

Synthetic design and brief. Shows the full output of this skill: a decisive rule trace, a perspective tension, a convention-breaking choice kept, and the smallest next check.

## The design under review

**Brief (supplied):** a co-op stealth room for two players on voice chat. "Each player depends on the other; the hacker trusts the lookout's eyes." Audience: friends playing together, moderate stealth experience. Decision pending: approve the room for greybox.

**Rules (supplied):**
- The hacker must stay at a terminal for **40 s uninterrupted**; leaving resets progress.
- The hacker's camera faces the terminal and cannot see the corridor.
- A guard patrols on a **30 s loop** and is in view of the terminal for **6 s** of each loop; if the hacker is at the terminal then, an alert starts.
- The lookout sees the whole corridor and can **distract the guard for 12 s**, with a **45 s cooldown**.
- Designer's note: "the distraction is what makes the hack possible."

## 1. Decision and claims

The decision is whether the room works as specified. Three claims to keep apart: the hack is possible under the rules; players can discover and execute the plan; the room delivers "trust your partner's eyes" for this audience.

## 2. Trace

**Rule trace (decisive).** Without distraction, the hacker has 30 − 6 = 24 s of safe time per loop, less than 40 s. With one distraction, the window grows to at most 24 + 12 = 36 s, still less than 40. A second distraction in the same window is impossible: the 45 s cooldown is longer than the 30 s loop, so the next distraction falls in a later loop. **As specified, the hack cannot be completed without an alert.** This needs no playtest; the arithmetic settles it. (Assumes the distraction pauses the guard rather than adding a second patrol loop; if the designer meant something else, the rule needs restating.)

**Repairs, by what they preserve:**

| Repair | Effect | Cost to the brief |
|---|---|---|
| Hack time 34 s (fits 36 s with 2 s slack) | the one-distraction plan works, tightly | none; tension stays high, slack is thin |
| Distraction 18 s | window 42 s; works with 2 s slack | lookout's action becomes more powerful; same tension |
| Progress persists when the hacker steps away | several short hacks between passes | removes the need for a distraction; weakens "depend on each other" |

Recommend the first or second; reject the third for this brief, because it lets the hacker succeed without the lookout.

**Perspective: roles (staged pass, not an independent review).** The lookout's only action is one distraction per 45 s, plus calling out the guard. Information pass: calling out is constant, meaningful work, because the hacker sees nothing. Agency pass: the lookout makes one decision per loop (when to distract). These disagree about whether the lookout is under-engaged. They are predictions, not observations. Different players may want different things: some friends enjoy the quieter "eyes" role. Keep both readings.

**Convention-breaking choice: the hacker cannot see the corridor.** A rule of thumb says players should see threats that can hurt them. Here, blindness is the mechanism of the brief: it is what makes the hacker trust the lookout. Preserve it. The cost: if voice chat fails or one partner is quiet, the hacker is helpless. Watch for that.

## 3. Findings

**Strongest finding:** the room is impossible as specified (rule trace). Fix the numbers before greybox.

**What works:** the information asymmetry directly produces the brief's dependence. It should survive any repair.

| # | Finding | Goal affected | Evidence / trace | Uncertainty | Direction |
|---|---|---|---|---|---|
| 1 | Hack cannot finish without an alert | the room's basic function | 24 + 12 = 36 < 40; cooldown 45 > loop 30 | none, given the rules as written | hack 34 s or distraction 18 s |
| 2 | Lookout may be under-engaged | "each depends on the other" | one decision per loop; constant callouts | prediction; players differ | observe; consider a second lookout tool only if observation supports it |
| 3 | Hacker helpless without communication | the experience degrades for quiet pairs or without voice | rule: hacker has no view | likely, frequency unknown | an optional ping the lookout can place (shows direction, not timing) |

**Preserve:** the hacker's blindness; one-distraction pacing. **Change:** hack or distraction time. **Leave conditional:** extra lookout tools, pending observation.

## 4. Smallest useful check

After the timing fix, a paper or greybox run with three pairs. Observe: callouts per loop, when the distraction is used, whether the lookout looks for something else to do between distractions. Ask each player separately afterwards what they were doing in the quiet moments. **What would reverse finding 2:** lookouts describe the role as busy or tense; then add nothing.
