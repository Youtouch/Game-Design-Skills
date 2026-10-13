---
name: game-design-companion
description: Entry point for game and level design help. Routes a request to the right design skills in this set, and states the rules they share (start from the brief, keep claim types apart, label synthetic content). Use when a design request is broad or unclear ("help me design…", "what do you think of my game?"), or spans several skills.
---

# Game Design Companion

Pick the smallest set of skills that answers the actual decision. Most requests need one or two. Design only.

## 1. Find the decision

Ask, or infer and state: what is being decided, for whom, at what stage, under which constraints? If intent is missing, give conditional answers rather than inventing a goal.

## 2. Route

| The request is about… | Start with | Often followed by |
|---|---|---|
| a new idea, a jam theme, "give me concepts" | `concept-ideation` | `game-design-doc` (one-pager) |
| what makes a game tick, retention, "no hook" | `core-loop-analysis` | `economy-model`, `progression-curve` |
| learning from an existing game | `design-teardown` | `core-loop-analysis` |
| what to prototype next, a prototype nobody can interpret | `prototype-plan` | `playtest-plan-and-report` |
| writing or updating a doc or spec | `game-design-doc` | — |
| breaking down a mechanic, tuning parameters | `mechanic-atomizer` | `difficulty-matrix` |
| difficulty ramps, bands, spikes | `difficulty-matrix` | `level-beat-chart` |
| tutorials, onboarding, teaching order | `mechanic-introduction-plan` | `feedback-and-readability` |
| players misreading or missing something | `feedback-and-readability` | `accessibility-review` |
| systemic interactions, unintended combos | `systems-interaction-map` | `balance-table-check` |
| stat tables, dominant options | `balance-table-check` | — |
| currencies, sinks, grind | `economy-model` | `loot-table-design` |
| drop rates, gacha, pity, collections | `loot-table-design` | `economy-model` |
| XP and power curves, time-to-level | `progression-curve` | — |
| a new level, blockout readiness | `level-brief` | `level-beat-chart`, `level-metrics-sheet` |
| pacing of a level | `level-beat-chart` | — |
| jumps, routes, sightlines, getting lost | `level-metrics-sheet` | — |
| a combat fight | `encounter-design` | `feedback-and-readability` |
| a puzzle or puzzle chain | `puzzle-design` | — |
| quests, branching, consequences | `quest-design` | — |
| co-op, versus, roles, griefing | `social-play-design` | — |
| barriers for disabled players, assist options | `accessibility-review` | — |
| a playtest plan or notes to summarize | `playtest-plan-and-report` | — |
| "what do you think?", reviewing a design | `design-critique` | whichever skill its main finding points to |

## 3. Shared rules

- **Keep claim types apart.** A rule trace or calculation, an available cue, a player's interpretation, and a reported experience are established in different ways. Arithmetic can settle feasibility; it cannot settle enjoyment.
- **Check the decisive numbers yourself.** Recompute; do not inherit arithmetic from the user, a source, or an earlier answer.
- **Principles guide, they don't rule.** Breaking a convention can serve the brief. Name who benefits, the cost, and what would reveal a problem.
- **Be honest about evidence.** Do not claim play, playtests, or readings that did not happen. Label invented examples as synthetic.
- **End with the next check:** the smallest observation, prototype, or calculation that could change the recommendation.

## Example

See [example.md](example.md) for three requests and how they route.
