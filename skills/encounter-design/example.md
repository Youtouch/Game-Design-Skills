# Worked example: the pump-house fight

Synthetic shooter encounter; all stats are design estimates.

**Placement:** midpoint of a level, after a quiet traversal section. **Encounter question:** "Will the player spot and prioritise the medic, and use cover against ranged fire while runners flank?" Wave 3 adds a second question: "Can they read the brute's slam?"

## Player toolkit

Rifle: 20 damage, 3 shots/s = 60 DPS; assumed accuracy 0.6 → **36 effective DPS**. 100 HP with 20% damage reduction → **effective HP 125**. Dodge roll available. Full heal from a health station between waves.

## Enemy roles

| Enemy | Role | HP | Damage per hit | Attack interval | Hit chance | Incoming DPS | TTK |
|---|---|---|---|---|---|---|---|
| Grunt | ranged anchor | 80 | 8 | 1.5 s | 0.5 | 2.67 | 2.22 s |
| Runner | flanker (melee) | 50 | 12 | 1.0 s | 0.6 | 7.2 | 1.39 s |
| Medic | support: heals one ally 20 HP/s, no attack | 60 | — | — | — | 0 | 1.67 s |
| Brute | elite (melee slam, 0.8 s tell) | 400 | 30 | 2.5 s | 0.7 | 8.4 | 11.1 s |

While the medic lives, the player's effective DPS against the healed target drops to 36 − 20 = 16.

## Arena

Foothold: a raised doorway overlooking the pump floor, with a clear view of both grunt positions and the medic's alcove. Cover: three pump housings that block grunt fire. Flank routes: two side corridors (runner entrances), both visible from the foothold. Retreat: back up the stairs to the doorway. Health station in the doorway, usable between waves.

## Pressure check

Model assumptions: grunts' shots are blocked while the player uses cover (they still peek to shoot); runners and the brute reach the player anyway; no stagger or crowd control.

**Wave 1: 3 grunts, at most 2 shooting at once.** Clear time 6.7 s. Damage taken in order: 2.22 s × 5.33 + 2.22 s × 5.33 + 2.22 s × 2.67 ≈ **30 of 125**. A warm-up; the question is just "find cover".

**Wave 2: medic, 3 runners, 2 grunts.** All runners attack at once.

| Kill order | Open ground | Using cover | Cover, max 2 runners attacking |
|---|---|---|---|
| Medic → runners → grunts (intended) | 145 (dies) | **96** (survives) | 74 |
| Runner → medic → runners → grunts | 180 | 122 (barely) | 99 |
| Runners → medic → grunts | 212 | 135 (dies) | 113 |

The arithmetic matches the question: with cover, killing the medic first is the difference between surviving and dying. Capping simultaneous runners at two makes every order survivable with cover, which turns the medic from a required priority into a recommended one.

**Wave 3: brute and 2 grunts (grunts first).** Clear time 15.6 s. In open ground 148; in cover 131: still lethal, because cover does not stop the brute. Dodging 70% of slams brings it to **39**; dodging 50%, 65. The wave is survivable only by reading the tell, which is its question.

## Wave table

| Wave | Trigger | Composition | Spawn | Question added | Clear time | Damage taken (intended play) | Readability notes |
|---|---|---|---|---|---|---|---|
| 1 | enter pump floor | 3 grunts | visible, far side | use cover | 6.7 s | 30 / 125 | grunts call out on spotting the player |
| 2 | last grunt dies | medic, 3 runners, 2 grunts | runners from side corridors (audible door slam), medic in lit alcove | prioritise the healer | 10.3 s | 96 / 125 | medic's heal beam must be visible from cover; runner footsteps from their corridor |
| 3 | after heal station use | brute, 2 grunts | brute through the main gate, slow entrance | read the slam | 15.6 s | 39 / 125 at 70% dodge | 0.8 s tell: raised arms, rising sound; never overlap with a grunt volley cue |

## Decisions

1. **Wave 2 runner cap: none, but keep the medic obvious.** The brief wants prioritisation to matter. Without a cap, the medic priority is required; so the medic must be identifiable from the foothold before runners arrive. If players die in wave 2 without having seen the medic, that is a readability failure, not a priority failure, and the fix is presentation, not stats.
2. **Wave 3 brute tell: 0.8 s.** It must exceed the reaction plus dodge-start time for this audience. Untested estimate; flag for playtest.
3. **Checkpoint before wave 2**, not before wave 1: a death in wave 2 should not replay the warm-up.

## Observations for playtest

| Question | Observation | Rival explanation |
|---|---|---|
| Is the medic readable? | time from wave 2 start to first shot at the medic | player saw it but chose runners because they were closer and louder |
| Is wave 2 hard because of priority or because of flanking? | where the player was when they died; which enemy dealt the last hits | missing cover use (a wave 1 lesson not learned) |
| Is the brute tell readable? | dodges started during the tell vs. after the hit | dodge input timing too strict (an execution barrier) |
