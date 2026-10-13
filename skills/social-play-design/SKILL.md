---
name: social-play-design
description: Design or review multiplayer and social play (co-op, competitive, asymmetric roles, team play, shared spaces) by defining the intended relationship between players, then checking interdependence, information, downtime, skill gaps, communication and griefing paths. Use when designing co-op or versus modes, when one role feels left out, when strong players dominate weak ones, or when players hurt each other's experience.
---

# Social Play Design

Multiplayer design shapes relationships, not only rules. The same mechanic can create trust, rivalry, teaching, or resentment depending on what each player can see, do, and do to the others. This skill starts from the relationship the design wants and checks whether the rules produce it. Design only.

## Inputs

- Mode and player count; who plays with whom (friends, strangers, family, mixed skill).
- The intended relationship: rivals, teammates, mentor and newcomer, mutual dependence, parallel play.
- Communication available: voice, text, pings, emotes, none.
- Roles, shared resources, and any ways players can affect each other.

## Procedure

1. **Name the relationship** in one line ("two friends who must trust each other's eyes", "eight strangers who compete but rarely meet"). Everything below checks against it.
2. **Map interdependence.** For each role, what can it do alone, what needs the other players, and what can it do *to* them (help, block, steal, revive)? Dependence creates cooperation and frustration at once; decide where you want each.
3. **Compare roles on more than actions:** information, decisions per minute, downtime, recovery after failure, and visible contribution. Equal button counts do not mean equal agency. Some players want the quieter role; offer choice before forcing equality.
4. **Check information flow.** Who knows what? Information asymmetry drives communication; communication fails without the channels to carry it. Check that each critical piece of information has a way to reach the player who needs it, including without voice (pings, markers, shared UI).
5. **Check the skill gap.** What happens when one player is much stronger? Possible responses: individual difficulty, roles with different skill demands, catch-up mechanisms, or separation by matchmaking. Each has costs: catch-up can feel unfair to the leader; separation can split friends.
6. **Trace negative interactions.** List every way one player can make another's experience worse: friendly fire, stealing loot, blocking, kill-stealing, quitting, stalling. For each, decide: part of the play (intended rivalry), limited (cooldowns, consent, opt-in), or prevented. Ask who carries the cost when someone leaves mid-session.
7. **Check pacing for everyone.** A beat chart per role: does any role wait long while another acts? Downtime can be fine (spectating a teammate's clutch moment) or deadly (waiting a minute to respawn with nothing to watch).
8. **Plan observation.** Record pairings, familiarity, communication used, and role choices. Interview players separately: partners often describe the same session differently.

## Output

1. Relationship statement.
2. Interdependence table: `role | alone | needs others for | can do to others | information it has | information it lacks`.
3. Role comparison: `role | decisions per minute | downtime | recovery | visible contribution | who might prefer it`.
4. Negative-interaction list with decisions (play / limit / prevent).
5. Skill-gap handling and its costs.
6. Observations.

Worked example: [example.md](example.md).

## Pitfalls

- Forcing equal activity on every role. Some players choose quiet roles; check preference before "fixing".
- Interdependence without a channel. If players must coordinate, give them a way that works without voice chat.
- Designing for friends and shipping to strangers. Trust, griefing, and quitting behave differently.
- Judging balance from team win rates alone. They hide whether each role had a good time.

## Sources (paraphrased, not quoted)

- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapters on players, cooperation and competition, and communities.
- Tracy Fullerton, *Game Design Workshop*, on player interaction patterns (formal elements chapter).
- Richard M. Ryan, C. Scott Rigby & Andrew Przybylski, 2006 ([doi](https://doi.org/10.1007/s11031-006-9051-8)): relatedness among the needs associated with enjoyment in their samples, including a multiplayer community survey. Correlational; it does not show which multiplayer rules satisfy that need.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md) (section on roles), [source boundaries](../design-critique/sources.md). See also the heist-room [critique example](../design-critique/example.md).
