# Worked example: sprout seed signs and feedback

Continues the [atomizer example](../mechanic-atomizer/example.md), whose highest-priority issue was: *miss feedback is undefined, so a player cannot tell "out of range" from "not moss".* Synthetic; timings are estimates.

## Events and what the player must know

| Event | Player must know | Sign (before) | Feedback (after) | Channels | Timing | Priority / conflicts | Status |
|---|---|---|---|---|---|---|---|
| Aiming | where the seed will land; whether that spot is moss | dotted arc to the landing point; the landing marker turns into a sprout icon over moss, stays a plain ring otherwise | — | visual (shape change, not only colour) | live while aiming | above ambient effects | new |
| Hit moss | the plant worked | — | bud appears and swells; soft "pop" | visual + audio + light haptic | immediate | high | existing (bud swell) |
| Miss: not moss | why it failed | landing marker was a plain ring | seed bounces with a dull "tock" and a brief grey puff; marker flashes a ring with a slash | visual + audio | immediate | high | new |
| Miss: out of range | why it failed | arc ends short of the surface | seed drops at max range; arc tip flashes; no bounce sound | visual | immediate | high | new |
| Leaf opens | it is safe to jump now | bud swelling over 0.8 s, rising pitch | leaf unfurls, click | visual + audio | at 0.8 s | high | existing |
| Leaf wilting | how long remains | — | leaf edges brown, then flicker during the last 1.0 s; descending tone | visual + audio | last 1.0 s | highest while standing on it | existing |
| Out of seeds | why throwing does nothing | seed counter on the hero's belt (diegetic) empties | throw input gives an empty-hand gesture and a soft "fff" | visual + audio | immediate | medium | new |
| Refill | seeds are back | — | belt pouch fills, rustle | visual + audio | on touching ground | low | new |

## Decisions and why

1. **Two distinct miss responses.** "Not moss" bounces with a sound; "out of range" drops silently at the arc tip. The difference is in shape, motion and sound, so it survives a muted device and colour-vision differences.
2. **The aim marker answers the question before the throw.** Turning the landing ring into a sprout icon over moss moves the "is this moss?" inference from after a failure to before the action. This removes a perception barrier but also removes some inference. Accepted in Worlds 2–3, where reading moss is not the intended challenge. The decoy moss planned for optional rooms (difficulty band 5) would conflict: there, the marker should show only range, not validity. Record this as an intended difference between modes.
3. **Wilting outranks everything while the player stands on a leaf.** It is the information that prevents a fall. Collectible sparkles near a leaf are suppressed during the wilt flicker.
4. **No screen shake on planting.** The bud swell and pop already confirm; shake would compete with the wilt warning in chains.

## Priority order (when signals overlap)

1. Wilt warning on the current leaf
2. Threat telegraphs (from World 3)
3. Leaf opening
4. Miss reasons
5. Rewards and collectibles
6. Ambient effects

## Observations

| Question | Observation | Rival explanation |
|---|---|---|
| Do players understand why a throw failed? | after a miss, does the next throw change target (not moss) or distance (range)? | random retry without understanding |
| Is the aim marker relied on? | do throws at non-moss drop to near zero once the marker exists? | players learned moss visually anyway; check in a room without the marker |
| Is wilting noticed in chains? | jumps started during the flicker vs. falls after it | jump timing, not perception (see difficulty matrix: chain slack) |
