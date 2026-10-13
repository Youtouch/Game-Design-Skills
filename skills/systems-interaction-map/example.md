# Worked example: fire, water, wind, and the rope bridge

Synthetic adventure game. **Brief:** players should experiment with elements to solve encounters in their own way. **Forbidden outcomes:** the critical path becomes impassable; a quest-giver dies before giving their quest.

## 1. Properties

| Property | Objects |
|---|---|
| flammable | grass, wooden crates, rope, wooden bridge, cloth awnings |
| wet | anything in rain or water; removes flammable while wet |
| conductive | metal gates, water puddles, armoured enemies |
| light | crates, leaves, small enemies (wind moves them) |
| burning (state) | any flammable object that ignites; lasts until fuel runs out |

## 2. Interaction matrix

| Cause ↓ / property → | flammable | wet | conductive | light |
|---|---|---|---|---|
| Fire arrow | ignites (burning 8 s, spreads to adjacent flammable each 2 s) | extinguished; steam puff | none | none |
| Burning (state) | spreads (as above) | extinguished | none | none |
| Water bolt | none | sets wet (30 s) | electrified if lightning present | pushes 1 m |
| Rain (weather) | sets wet (while raining + 30 s) | — | none | none |
| Lightning bolt | ignites | stuns everything in the wet area | stuns, chains 3 m | none |
| Wind gust | spreads burning 2× faster downwind | dries after 10 s | none | pushes 4 m |

Every cell is filled; "none" is a decision. Note "lightning ignites flammable": it matches player expectations from fire, so it was added to keep rules consistent.

## 4. Chains

| Start | Chain | Outcome | Class | Action |
|---|---|---|---|---|
| Fire arrow at grass near a camp | grass burns → spreads to cloth awnings → enemies flee | camp cleared without combat | keep | the intended kind of invention |
| Water bolt then lightning | puddle wet → lightning stuns all enemies standing in it | group stun | keep | make puddles visible near camps |
| Fire arrow at rope | rope burns → **critical-path bridge falls** | path impassable | **fix** | see section 6 |
| Wind gust at a burning crate | crate pushed 4 m into dry grass → field fire → reaches village | **quest-giver in village could die** | **fix** | see section 6 |
| Rain during a fire encounter | everything wet → fire arrows do nothing | the player's chosen tool fails | decide | keep: signalled by visible rain; other tools work. Add a sheltered area where fire still works |

## 5. Loops and limiters

**Fire spread** re-triggers itself through grass. Limiters: each object burns once (fuel), wet blocks spread, and spread stops at bare ground. At the largest grass field (120 m across, 2 m grass tiles), spreading one tile every 2 s crosses it in 120 s from one edge, or 60 s from a fire started in the middle. Downwind, a gust halves those times. Fuel still bounds it: each tile burns once. Check in a prototype that a full-field fire reads as spectacle and leaves the encounter playable.

## 6. Forbidden outcomes and protections

| Outcome | Chains reaching it | Protection | Why this one |
|---|---|---|---|
| Critical-path bridge falls | fire arrow / lightning / spreading fire → rope | Bridge ropes are **iron chains** (not flammable, visibly metal). Optional side bridges keep rope and can burn. | follows the visible rule; no invisible exception |
| Quest-giver dies | field fire → village | village sits on a stone plaza with a stream around it (bare ground and water stop spread); quest-givers flee fire rather than standing in it | uses existing limiters rather than making NPCs fireproof |

Re-check after the fix: iron chains are conductive, so lightning at the bridge now stuns anyone standing on it. That is a new chain. It does not break the path, and it gives players an ambush option, so keep it, and make sure enemies can be lured onto the bridge as well as the player.

The rejected protection, "the bridge simply does not burn", would contradict the flammable rule and teach players that experiments fail unpredictably.

## 7. Readability

Flammable objects share a dry, straw-coloured palette and crackle when hit; wet objects darken and drip; conductive objects have a metallic sheen and hum near lightning. Iron chains on the critical bridge must read as metal from a distance, or players will try to burn them and conclude the rule is inconsistent.
