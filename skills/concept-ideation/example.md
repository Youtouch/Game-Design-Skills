# Worked example: a 48-hour jam on the theme "tide"

Synthetic brief. Two people (one artist, one designer-programmer), 48 hours, browser game, mouse only, a play session of about five minutes.

## 1. Constraints and openings

- **Constraints:** mouse only; finishable in 48 hours by two people; readable in five minutes without a tutorial screen.
- **Openings:** genre, tone, and what "tide" means are free.

## 2. Divergent list

**Verb first**
1. *Low Water*: drag the tide line itself to strand or float ships.
2. *Comb*: rake the sand between tides; patterns become paths for crabs at night.

**Experience first**
3. *Last Ferry*: be trusted to ferry islanders across before the tide closes the causeway; choose who goes first.
4. *Rockpool*: a tiny ecosystem in one pool; nurture it between tides without touching it directly.

**Constraint as feature**
5. *One Wave*: a single click releases one wave per round; everything depends on where and when.

**Subtract a convention**
6. *Lighthouse Without a Light*: guide ships with sound only (mouse to place bells).
7. *Tidal Tower Defence with no towers*: you defend by shaping the shoreline; the sea is the only weapon.

**Collide two systems**
8. *Moon Garden*: a farming game where the moon's position (dragged by the player) sets tides that water crops.
9. *Tide Chess*: chess-like pieces on a beach; squares flood and dry on a cycle.

**Change the point of view**
10. *The Sandcastle*: you are the castle; arrange your walls before each wave.
11. *Driftwood*: you are a piece of wood carried by tides across years, collecting stories.
12. *The Moon*: you are the moon, pulling oceans and trying not to wake the town.

**Spread check:** verbs span drag, rake, choose, nurture, click-timing, placing, shaping. Tone spans calm (2, 4, 11) to tense (3, 7, 10). Solo only, as the brief implies. The obvious idea for "tide" is a surfing or swimming game; none here, intentionally.

## 5–6. Filter and merge

- Removed by constraints: *Tide Chess* (rules too heavy to read in five minutes without a tutorial); *Driftwood* (needs a lot of writing for 48 hours).
- Merged: *Low Water* and *The Moon* share a verb (pull the water). Merged as *The Moon*: you drag the moon to pull the tide; the town reacts.
- Merged: *Tidal Tower Defence* and *The Sandcastle*: shape defences, then a wave tests them.
- Set aside, not rejected: *Comb*, *Lighthouse Without a Light*, and *Moon Garden* fit the constraints but overlap the survivors' strengths with more scope risk (night cycle, audio design, farming balance). Kept on the list for later jams.

## 7–8. Convergence

| Concept | Hook | Core verb | Experience | Fits? | Nearest reference and difference | Riskiest assumption | Cheapest test | Scope risk |
|---|---|---|---|---|---|---|---|---|
| The Moon | you are the moon; pull tides without waking the town | drag | mischievous care | yes | physics toys: here the goal is restraint, not destruction | dragging water stays interesting after a minute | 2-hour toy: one drag, water level, three boats | water rendering |
| The Sandcastle | shape walls, then one wave hits | place, then watch | anticipation | yes | tower defence: one decisive wave instead of a stream | watching a wave you can't influence is tense, not passive | paper: draw walls, roll dice for the wave | wave simulation |
| Last Ferry | choose who crosses before the causeway floods | choose, route | weight of choice | yes | triage games: a visible tide clock replaces a timer | five minutes is enough to care about the islanders | text prototype with five characters | writing |
| One Wave | one click per round decides everything | time a click | precision | yes | one-button games: the wave's shape is the puzzle | one input carries five minutes | 1-hour toy | low |
| Rockpool | nurture without touching | indirect influence | calm attention | yes | ecosystem toys: tides set the rhythm | indirect influence reads with mouse only | paper simulation | balancing in 48 h |

## 9. Recommendation

Build **The Moon** if the 2-hour toy passes; fall back to **The Sandcastle**.

- *The Moon* has the strongest link between theme and verb (you literally are what makes the tide) and a twist on a familiar toy (restraint instead of destruction). Its risk is testable in two hours.
- *The Sandcastle* is the safest scope and has a clear five-minute arc (build, wave, result), but its risk, passive watching, is serious. The paper test can check it cheaply in parallel.
- *Last Ferry* is the most emotionally ambitious but leans on writing, the scarcest skill on this team.

**First test:** the Moon toy. Pass condition: both teammates keep dragging past one minute without a goal, then try to achieve something specific unprompted. If not, switch. A self-test by the makers is weak evidence: it can only rule out a toy even its makers find dull. If it passes, hand it to one person outside the team before committing the remaining 44 hours.
