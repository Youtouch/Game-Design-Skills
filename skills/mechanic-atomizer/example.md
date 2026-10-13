# Worked example: the sprout seed

Synthetic mechanic used across the Rational Game Design examples in this repo ([difficulty matrix](../difficulty-matrix/example.md), [introduction plan](../mechanic-introduction-plan/example.md), [level brief](../level-brief/example.md), [beat chart](../level-beat-chart/example.md)). All values are design estimates, not playtested.

**Game.** *Bramblewick*, a 2D side-view platformer. The hero runs at 6 m/s, jumps 2.0 m high, and clears 4.5 m with a running jump (3.0 m from a short run-up such as a leaf).

**Mechanic.** The hero throws a seed. If it lands on moss, a bud swells and then opens into a 1.5 m leaf platform that lasts a few seconds, flickers, and wilts. The hero carries two seeds and refills on touching solid ground.

## 1. Player goal

Cross gaps and reach heights that running and jumping alone cannot, by planning where and when a temporary platform will exist.

## 2–5. Atoms, skill loops, parameters

| Atom | Type | Skill learned | Parameter | Unit | Range (*estimate*) | Demand changed | Depends on |
|---|---|---|---|---|---|---|---|
| Throw | player action | aim an arc to a target | throw range | m | 4–6 | execution (aim) | — |
| | | | windup | s | 0.2 | execution (timing) | |
| Seed flight | world rule | predict arc and landing time | flight time at max range | s | 0.3–0.5 | inference | Throw |
| Moss rule | world rule | recognise which surfaces accept seeds | moss patch size | m | 0.5–3 | perception, execution | — |
| | | | moss contrast vs. background | qualitative band | high → subtle | perception | |
| Sprout delay | world rule | wait for the leaf before committing | delay from landing to platform | s | 0.6–1.2 | inference, execution (timing) | Moss rule |
| Leaf platform | world rule | judge reach from a short platform | leaf width | m | 1.0–2.0 | execution | Sprout delay |
| | | | lifetime | s | 1.6–3.0 | execution (time pressure) | |
| Wilt warning | feedback | read remaining time | warning duration before vanishing | s | 0.5–1.0 | perception | Leaf platform |
| Seed supply | world rule | budget seeds across a chain | seeds carried | count | 1–2 | choice, recovery | — |
| | | | refill condition | rule | touch ground | choice | |
| Bud swell | feedback | confirm a successful plant | — | — | — | perception | Moss rule |
| Miss feedback | feedback | learn why a throw failed | — | — | — | perception, inference | Moss rule |

Skill-atom loop for **Throw**: aim and release → seed flies, sticks or bounces → bud swells (hit) or seed drops with a dull sound (miss) → player updates beliefs about range and which surfaces count as moss.

## 6. Dependencies

- **Real prerequisites:** the moss rule before any sprout use; seed supply before chains of two.
- **Preferred teaching order, not a prerequisite:** delay and lifetime can be learned together on a forgiving single-leaf crossing; separating them would add a beat without removing a real dependency.
- **Coupled concept:** "throw while standing on a leaf" combines throw, lifetime, and supply. It is learnable only once both are familiar, and it is where the timing interaction lives (see the [difficulty matrix](../difficulty-matrix/example.md)).

## 7. Issues

1. **Miss feedback is undefined.** Without a distinct miss response, a player who misses cannot tell "out of range" from "not moss". Highest-priority gap: it blocks the skill loop.
2. **Nonlinear interaction:** delay, lifetime, and flight time combine into one timing window for chained leaves. Tuning any one alone gives misleading difficulty.
3. **Redundancy check:** wilt warning and lifetime are separate parameters on purpose; the warning can lengthen without changing actual time pressure.
4. **Not an issue:** the refill rule has almost no tuning range. That is fine; its job is to bound chains, and it is easy to explain.

## Why this decomposition

Splitting "plant a seed" into throw, flight, moss rule, and delay lets a playtest failure be located: a player who throws at stone has a perception or inference problem, one who throws at moss and falls has a timing problem. A coarser atom ("use seed") would hide which repair to try.
