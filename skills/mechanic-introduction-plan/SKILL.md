---
name: mechanic-introduction-plan
description: Sequences mechanics through exposition, validation, challenge and combination across a level or campaign, checking that each step adds only one new demand. Use when planning tutorials, onboarding, level order, or a campaign's learning curve.
---

# Mechanic Introduction Plan

Plan how and when each mechanic is taught so players learn one thing at a time and later combine what they know.

## Inputs
- Mechanic list with dependencies (from `mechanic-atomizer`).
- Intensity levels (from `difficulty-matrix`), if available.
- Scope: one level, a world, or the full campaign.

## Process
1. **Order mechanics** by dependency, then by importance to the core loop.
2. **Plan four beats per mechanic:**
   - *Exposition*: shown in a safe space, low or no failure cost.
   - *Validation*: player must use it once to progress; failure is cheap.
   - *Challenge*: intensity raised through the difficulty matrix.
   - *Combination*: paired with an already-mastered mechanic.
3. **Apply the one-new-demand rule.** Each beat may add exactly one of: a new mechanic, a higher intensity, or a new pairing. Never two at once.
4. **Pace intensity.** Alternate peaks with rest beats; after a new exposition, drop intensity of known mechanics.
5. **Add reminders** for mechanics unused for a long stretch before challenging them again.
6. **Mark mastery gates**: beats the player cannot pass without the skill, so later content can assume it.

## Output

| Beat # | Location / level | Mechanic(s) | Beat type | Intensity | New demand | Failure cost | Notes |
|---|---|---|---|---|---|---|---|

Followed by a list of rule violations found (beats with zero or multiple new demands) and suggested fixes.

## Checks
- Every mechanic reaches validation before any challenge.
- No beat introduces more than one new demand.
- Combinations only use mechanics that have passed a challenge beat.

## Sources (paraphrased, not quoted)
- Chris McEntee, "Rational Design: The Core of Rayman Origins", Game Developer, 2012 (exposition, validation, challenge learning structure).
- Luke McMillan, "The Rational Design Handbook: An Intro to RLD", Game Developer, 2013 (flow channel, pacing).
