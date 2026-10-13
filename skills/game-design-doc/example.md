# Worked example: one-pager and feature spec for *Bramblewick*

Synthetic. The one-pager pitches the game; the feature spec covers the sprout seed, drawing on the [atomizer](../mechanic-atomizer/example.md), [difficulty matrix](../difficulty-matrix/example.md), and [feedback](../feedback-and-readability/example.md) examples.

## One-pager

```
# Bramblewick
Hook: A platformer where you plant your own footholds, but they wilt.
Player fantasy: a small gardener who turns dead stone into a path.
Pillars:
  1. Plan, then move. Every hard jump is solved before it is attempted.
  2. Growth is temporary. Nothing the player plants lasts; timing is the craft.
  3. Kind failure. Mistakes cost seconds, not progress.
Core loop: read the room -> plant -> cross before the leaf wilts -> read the next room
Audience and platform: players who like precision platformers but dislike punishing ones; PC and console, controller first.
Comparables: precision platformers with short retries; ours differs because the player
  builds the platforms, so the challenge is planning as much as execution.
Biggest risk and how we test it first: chained leaves may feel like execution
  timing rather than planning. Test: a greybox room with a two-leaf chain;
  observe whether failures come from planning (wrong moss) or timing (late jump).
```

**Pillar check:** "Kind failure" rejects a lives system and long checkpoints, so it can reject features: it passes. "Growth is temporary" rejects permanent platforms, even as an upgrade; the team should decide now whether that is intended.

## Feature spec (abridged)

```
# Feature: Sprout seed        Status: review
Change log: 2026-10-13  added miss feedback and aim marker (from readability review)
Pillar(s) served: Plan, then move; Growth is temporary
Player experience goal: The player should feel clever when a chain they planned works,
  because they chose where and when the leaves appeared.
  Mechanism: planning is required (gaps exceed running reach); timing is
  forgiving at first (single leaves last 3.0 s; the first chain has a floor
  under it and 1.2 s of chain slack). Observation: players pause to look
  before throwing; after success, they describe the plan, not the reflexes.
  Rival: they succeed by trial and error. Distinguish by throws per success.
Summary: Throw a seed at moss; after a delay a leaf platform grows; it wilts after
  a few seconds. Carry two seeds; refill on touching ground.
Player flow:
  1. Hold aim; an arc and landing marker appear (marker shows a sprout over moss).
  2. Release: the seed flies and lands.
  3. On moss: a bud swells (0.8 s), then a leaf opens.
  4. The leaf lasts its lifetime, flickers in its last second, and wilts.
Rules:
  | condition                         | result                          |
  | seed lands on moss                | bud, then leaf after delay      |
  | seed lands elsewhere              | bounces, miss feedback          |
  | seed reaches max range in air     | drops, out-of-range feedback    |
  | seeds = 0                         | throw does nothing; empty gesture |
  | hero touches solid ground         | seeds refill to 2               |
States and transitions: seed (held -> flying -> bud -> leaf -> wilting -> gone)
Signs and feedback: see readability table (aim marker, miss reasons, wilt flicker)
Skills required / taught: aim an arc; predict delay; jump within lifetime; budget seeds
Tuning knobs:
  | name       | start | provisional range / status | effect                |
  | delay d    | 0.8 s | 0.6-1.2 s, estimate        | inference and timing  |
  | lifetime L | 3.0 s | 1.6-3.0 s, estimate        | time pressure         |
  | leaf width | 1.5 m | 1.0-2.0 m, estimate        | landing precision     |
  | throw range| 6 m   | 4-6 m, estimate            | reach, aim            |
Edge cases: seed lands on moss under water [TBD]; leaf grows into an enemy [TBD];
  two leaves overlapping on one patch (allowed; second replaces first?) [TBD]
Dependencies: moss placement in levels; wilt flicker must meet the flashing limit
Open questions (question | owner):
  | Does aim snapping undermine "plan, then move"? | design lead |
  | Should the aim marker be off in optional band 5 rooms? | level design |
Risks: chains may read as execution tests (see one-pager test); flicker safety
```

## Why it is written this way

- **The PXG names a mechanism and a rival.** "Feel clever" alone cannot be checked; "throws per success" can distinguish planning from trial and error.
- **Tuning knobs carry status.** Every range is marked as an estimate until a prototype checks it.
- **Undecided edge cases are marked `[TBD]`,** not invented. The spec is honest about what is not designed yet.
- **The change log points to the review that caused the change,** so later readers know why the aim marker exists.
