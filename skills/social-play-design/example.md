# Worked example: *Lantern Divers*, four-player co-op

Synthetic design and numbers. **Mode:** four players dive through a flooded ruin for treasure in 20-minute runs. **Who plays:** groups of friends with mixed skill, often one experienced player bringing newcomers. **Communication:** voice optional; pings available.

## 1. Relationship

"Friends of different skill who feel they got through it together, and where the newcomer matters."

## 2. Interdependence (current design)

| Role | Alone | Needs others for | Can do to others | Information it has | Information it lacks |
|---|---|---|---|---|---|
| Lamp-bearer | light a small radius | — | leave others in the dark | sees hazards in the light | anything outside it |
| Diver (×3) | fight, loot | light | take loot first; block narrow tunnels | what is in their hands | where the lamp is going |

**Shared loot is first come, first served.** The experienced player, faster and better at reading the ruin, picks up most of it.

## 3. Role comparison

| Role | Decisions per minute | Downtime | Recovery | Visible contribution | Who might prefer it |
|---|---|---|---|---|---|
| Lamp-bearer | route choice, often | low | cannot die (design rule) | high: everyone follows the light | a calm player who likes leading |
| Diver | combat, looting | death respawn 30 s | respawn | loot count on the end screen | action-focused players |

**Downtime by skill (calculation).** In a 20-minute run, a newcomer who dies 6 times waits 6 × 30 s = 180 s, 15% of the run, watching a black screen. An experienced player who dies once waits 30 s (2.5%). The design punishes the player it most wants to include.

## 4. Negative interactions

| Interaction | Decision | Why |
|---|---|---|
| Taking all the loot | **limit:** each pickup is split four ways automatically; the end screen shows "treasure found by" separately from the shared total | keeps the thrill of finding without making the newcomer's share depend on speed |
| Lamp-bearer racing ahead | **play, with a soft limit:** the light dims slightly when divers fall behind | leading is the lamp role's identity; dimming signals the cost without forbidding it |
| Blocking tunnels | **prevent:** divers pass through each other in tunnels | blocking adds nothing to the relationship |
| Quitting mid-run | **limit:** the quitter's share goes to the group; a bot lamp takes over if the lamp-bearer leaves | the group should not lose a 20-minute run to one departure |

## 5. Skill gap

Respawn becomes a **revive**: a teammate reaches the fallen diver's lantern within 10 s, or the diver respawns at the lamp. With revives, the newcomer's downtime drops to about 6 × 10 s = 60 s (5%), and each revive is a moment where the experienced player helps visibly. Cost: the strong player may spend the run babysitting. Watch for that, and keep the fallback respawn so nobody waits on a teammate who won't come.

Rejected: scaling enemy damage down for weaker players only. It splits the group's experience of the same fight and is invisible, so the newcomer can't feel they earned anything.

## 6. Observations

| Question | Observation |
|---|---|
| Does the newcomer feel they mattered? | separate interviews: "what did you contribute?", compared across partners |
| Is revive babysitting a burden? | revives per player; ask the experienced player what the run felt like |
| Do pings carry the lamp's route without voice? | groups without voice: how often divers lose the light |

Record pairings, familiarity, and whether voice was used. One group's experience will not generalise to strangers.
