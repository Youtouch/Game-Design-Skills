# Worked example: chain-room playtest, plan and report

Synthetic plan and **synthetic notes**: the observations below are invented to show the reporting method, not results. Tests the riskiest assumption from the [Bramblewick one-pager](../game-design-doc/example.md): do chained leaves feel like planning or like execution timing?

## Plan

```
Test name / date / build: Chain rooms v1 / 2026-10-20 / greybox build 14
Goal (pillar or PXG): "Plan, then move": players should feel clever when a planned chain works
Questions / hypotheses:
  H1: Failures in the band 4 chain room come mostly from timing, not planning.
      Support if: most falls happen after the second leaf opened (late jump).
      Weaken if: most failures follow throws at non-moss or at the wrong patch.
      Rival explanation: players never noticed the second moss patch (perception).
  H2: Players plan before acting.
      Support if: players stop and look before the first throw in a new room.
      Weaken if: first throws happen within 2 s of entering.
      Rival: stopping reflects confusion about the goal, not planning; check in interview.
Section in scope: World 2-3 rooms 4-6 (first chain with floor), band 4 chain room
Known limitations and impact: greybox art makes moss less readable than final art;
  this biases toward perception failures, so H1 results on perception are conservative.
Testers (profile x count): 6 players who play platformers monthly; none have seen the game
Prior exposure / access needs / accommodations: record per tester; controller remapping available
Protocol and rationale: silent play + replay interview (think-aloud would disrupt timing)
Assistance rule and actual interventions: no help unless stuck 5 minutes in one room; log every intervention
Tasks: "Reach the exit of each room."
Observation sheet columns: tester | time/room | behaviour | quote | hypothesis
Post-session questions:
  1. In the last room, what were you trying to do? (play back the clip)
  2. What made it hard, when it was hard?
  3. How did you decide where to throw?
  4. (last) Rate the room from too easy to too hard, 1-5.
```

## Synthetic notes (normalized)

```
P1 | 03:10 | band 4 | threw at stone twice, then moss; crossed on 4th try | H1 (planning)
P1 | 03:40 | band 4 | said "I didn't see the second moss at first" | H1 rival (perception)
P2 | 02:55 | band 4 | 5 falls, all after the second leaf opened; said "too fast" | H1 (timing)
P3 | 01:20 | room 4 | paused ~6 s at entrance, looked at both walls | H2
P3 | 02:30 | band 4 | 2 falls before the second leaf opened; jumped early | H1 (inference)
P4 | 04:05 | band 4 | 3 falls after leaf opened; succeeded once wilt flicker noticed | H1 (timing)
P5 | 01:05 | room 4 | threw within 1 s of entering, at stone | H2 weaken
P6 | 03:30 | band 4 | did not find second moss patch for 2 min; intervention at 5 min not needed | H1 rival
ALL | rooms 4-6 | completion log: all 6 testers crossed rooms 4-6 | —
INT | interview Q3 | P1, P3, P4, P6 described a plan ("worked out where the leaves go"); P2, P5 described retrying | H2
```

## Report

**Summary.** H1 is *not supported in these conditions*: of the six testers, two failed mainly from timing (P2, P4), two from not finding the second moss patch (P1, P6), one from jumping before the leaf opened (P3), and one has no band 4 failure data logged (P5). Failures split across perception, inference, and timing. H2 is *unresolved*: room-entry behaviour was logged for only two testers (P3 paused, P5 threw immediately); in interview, four of six described a plan.

| # | Priority | Finding | Testers (n/N) | Evidence | Likely cause | Suggested direction |
|---|---|---|---|---|---|---|
| 1 | high | Second moss patch not found | 2/6 | P1 quote; P6 searched 2 min | perception: patch in shadow, greybox contrast | raise contrast in greybox; recheck with final art before changing layout |
| 2 | medium | Falls after leaf opened | 2/6 | P2 5 falls, P4 3 falls | timing (chain slack 1.2 s) or not noticing the wilt flicker (P4 succeeded once noticed) | test slack 1.6 s vs. a stronger wilt cue in separate rooms, not both at once |
| 3 | medium | Jumping before the leaf opened | 1/6 | P3 | inference: delay not internalised | check whether the bud swell is visible from the leaf |
| 4 | — | Planning behaviour at room entry | 1 paused, 1 did not, 4 not observed | sheet gaps | observation gap | add an entry-time column; review recordings |

**What worked:** all six crossed the floored chain rooms 4–6 (completion log); four of six described a plan in interview (P1, P3, P4, P6), which is reported evidence for H2 but not behaviour. Protect the floor under the first chain.

**Open questions and next test:** separate perception from timing: same band 4 room with high-contrast moss for half the testers. Record room-entry behaviour for every tester. Six testers cannot rank these causes by frequency with confidence; the next test should check whether finding 1 persists with clearer moss.

## Notes on the method

- **Counts carry denominators** and gaps are reported as gaps (P5's missing band 4 data), not filled in.
- **"Not supported in these conditions"**, not "false": six greybox testers can weaken a hypothesis without settling it.
- **Finding 2 has two causes and the test separates them** rather than changing slack and the cue together.
