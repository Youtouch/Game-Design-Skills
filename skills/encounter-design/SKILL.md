---
name: encounter-design
description: Design or review a combat encounter: enemy roles and composition, arena layout and footholds, wave timing, threat readability, and a pressure check against the player's survivability and damage output. Use when building a fight, tuning a difficulty spike in combat, or reviewing an arena blockout.
---

# Encounter Design

An encounter is a bounded situation where opposing behaviours, space, and timing put pressure on the player. Design it as a question the player answers with the tools they have. Design only; enemy behaviour is described in design terms, not as AI code.

## Inputs

- Intended experience and where the fight sits in the level beat chart.
- Player toolkit at this point: weapons, abilities, movement, healing, and metrics (speed, ranges).
- Enemy roster with behaviour summaries and stats.
- Arena sketch, or constraints for one.

## Procedure

1. **State the encounter question.** One line: what must the player notice, decide, or execute? ("Can they prioritise the healer while being flanked?") If you cannot write it, the fight has no design focus yet.
2. **Assign enemy roles.** Describe each enemy by the pressure it applies, not its look: *anchor* (holds space), *flanker* (forces movement), *ranged* (punishes standing still in the open), *swarm* (tests area control), *support* (changes other enemies), *elite* (a focused test). Combinations create the question; a uniform group tests one thing.
3. **Lay out the arena.** Mark entrances, footholds (where the player first stands and reads the fight), cover, high ground, chokepoints, flank routes, hazards, and retreat or recovery space. Check sightlines from the foothold: can the player see the threats they must prioritise before they act? See `level-metrics-sheet` for distances and visibility.
4. **Script the waves.** For each wave: trigger, composition, spawn location, and what it changes about the question. Prefer spawns the player can see or hear arriving; spawns behind the player change the question to "punish positioning", which should be intentional.
5. **Run the pressure check** (below). It establishes whether the fight is arithmetically survivable under stated assumptions; it does not establish how it feels.
6. **Plan readability.** Each enemy's attack needs a tell (wind-up, sound, telegraph) longer than the reaction it demands. Note simultaneous tells: two tells at once is a perception demand, not only a damage one. Use `feedback-and-readability` for detail.
7. **Plan recovery and pacing.** Where can the player breathe, heal, or reposition? What happens on death: checkpoint distance and what is replayed? Long replays of the easy part before a hard wave raise frustration without raising challenge.
8. **List playtest observations** that would distinguish an intended challenge from a readability problem or an arithmetic spike.

## Pressure check

With stated assumptions (accuracy, uptime, number of enemies attacking at once):

- **Time to kill (TTK)** per enemy = enemy HP / (player DPS × accuracy).
- **Time to clear** a wave ≈ Σ TTK in the player's likely kill order, plus movement time.
- **Incoming DPS** = Σ over enemies currently attacking of (damage per hit × hit chance / attack interval). Use the number expected to attack at once, not the wave size, if the design limits simultaneous attackers.
- **Time to die (TTD)** = player effective HP / incoming DPS.
- **Margin** = TTD / time to clear. Below 1, the player loses the race unless healing, cover, or crowd control changes the terms. Name which of those the design relies on.
- **Damage taken over the clear** (better when kill order matters): step through the likely kill order; for each kill, multiply its TTK by the incoming DPS of everything still alive and attacking, then sum. Compare with effective HP. Run the intended order and a plausible wrong one: the difference shows how much the fight's question actually matters.

These are race estimates; they omit positioning, cover use, stagger, and enemy AI choices. Use them to find impossible or trivial waves, not to tune feel.

## Output

| Wave | Trigger | Composition (roles) | Spawn | Question added | TTK / clear time | Incoming DPS | TTD | Margin | Tells and readability notes |
|---|---|---|---|---|---|---|---|---|---|

Then: arena sketch notes, recovery points, risks, and observations.

Worked example: [example.md](example.md).

## Pitfalls

- Raising difficulty by adding HP. Damage sponges lengthen a fight without changing its question.
- Spawning out of sight to raise pressure. It turns a reading test into a memory test.
- Ignoring the attack-concurrency rule. Ten enemies that attack one at a time are a different fight from ten that attack together.
- Calling a fight unfair because many players die. Deaths can come from an intended spike, a missed tell, or an unclear goal; observe which.

## Sources (paraphrased, not quoted)

- Robert Yang et al., *The Level Design Book*, "Encounter" page ([book.leveldesignbook.com](https://book.leveldesignbook.com/process/combat/encounter)): combat story, footholds, enemy palette, player personas, arena design.
- Luke McMillan, "The Metrics of Space: Tactical Level Design", Game Developer: FPS-oriented sightline and cover advice; do not apply its rankings outside that genre.
- Ian Schreiber & Brenda Romero, *Game Balance* (2021), chapter on progression in PvE games.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
