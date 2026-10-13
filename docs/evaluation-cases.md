# Evaluation cases

Prompts for checking whether the skills improve an agent's design reasoning, as required by [multi-lens design analysis](multi-lens-design-analysis.md#evaluation-requirements). Each case has a trap: a plausible but wrong answer. All scenarios are synthetic and original.

## How to use

Run each prompt with and without the relevant skill loaded, under the same model and settings, and record cost (tokens, time). Grade each answer against **Pass** and **Fail** below; do not reward length, number of lenses, or confident tone. A pass on the trap matters more than overall polish. Keep the answers; these cases have not yet been run, so no improvement is claimed.

## Numbers

**N1. Mean is not the wait** (`loot-table-design`)
Prompt: "A legendary drops at 1% per run. Runs take 6 minutes. Our target is 'most players get it within 10 hours'. Are we on target?"
Trap: mean 100 runs = 10 hours, so "yes".
Pass: computes P(within 100 runs) = 1 − 0.99¹⁰⁰ ≈ 63%, reports median (69 runs) and an unlucky percentile (90%: 230 runs = 23 h), and asks what "most" means.
Fail: answers from the mean alone.

**N2. Dividing by the mean reward** (`economy-model`, `design-critique` chance lesson)
Prompt: "Chests give 1 key (50%) or 5 keys (50%). How many chests on average to reach 4 keys from zero?"
Trap: 4 / 3 ≈ 1.33.
Pass: 15/8 = 1.875 by enumeration or recurrence.
Fail: 1.33, or any answer from dividing by the mean.

**N3. Mixed-role cost fit** (`balance-table-check`)
Prompt: give the [example table](../skills/balance-table-check/example.csv) and ask, "Is range overvalued? The fit gives it a negative weight."
Trap: "range is a liability; lower its price."
Pass: explains that melee and ranged roles confound the fit, re-runs within roles or with design weights, and withholds a verdict on range.
Fail: recommends a change to range from the global fit.

**N4. Additive stacking** (`balance-table-check`)
Prompt: "Two −40% cooldown charms on a 2.5 s, 30-damage crossbow. DPS?"
Trap: picks one stacking rule silently.
Pass: asks or states the stacking rule; gives 60 DPS additive and ≈33 DPS multiplicative; flags the additive case.

**N5. Time-to-level with scaling income** (`progression-curve`)
Prompt: "x(L) = 100·L^1.8 XP, income 40 + 6L XP/min. When is level 5 reached?"
Pass: ≈ 40.3 minutes by summing levels 1–4 discretely.
Fail: uses only the integral approximation without saying so, or ignores income scaling.

**N6. Attack concurrency** (`encounter-design`)
Prompt: "A wave has 10 grunts. Each dies in 1.5 s of focused fire and deals 4 DPS while attacking. The player has 120 effective HP. Is the wave survivable?"
Trap: answers without asking how many grunts attack at once.
Pass: shows the answer depends on concurrency: if all attack, damage taken over the clear is 1.5 × 4 × (10 + 9 + … + 1) = 330 (lethal); with at most 2 attacking, 1.5 × 4 × (2 × 9 + 1) = 114 (barely survivable). Names cover, healing, or crowd control the design may rely on.
Fail: one number with the concurrency assumption hidden.

## Rules and state

**S1. Parity trap** (`puzzle-design`)
Prompt: "Five lamps in a ring, five levers; each lever flips the two lamps beside it. Lamps 1 and 3 start lit. Write a hint ladder for lighting all five."
Trap: writes hints for an unsolvable puzzle.
Pass: proves impossibility (lit count parity is invariant) before writing hints; proposes a solvable start.

**S2. Branch destroys a precondition** (`quest-design`)
Prompt: describe a quest where burning a building is an option, and a later quest's objective is "retrieve the ledger from that building".
Pass: finds the dead end, proposes a branch-aware objective, and checks dialogue that references the ledger.
Fail: reviews tone and rewards without tracing state.

**S3. Resource soft-lock** (`design-critique` state lesson)
Prompt: the tide archive scenario with costs changed (start 5 charge, display 3, lift 3).
Pass: display-first leaves 2 < 3: trap; direct path works; repairs chosen according to the brief.
Fail: "make the lift cost more visible" as the repair.

**S4. Systemic forbidden outcome** (`systems-interaction-map`)
Prompt: "Fire spreads to flammable objects; our critical-path bridge is rope. Players love burning things. What do we do?"
Trap: "make the bridge unburnable" (invisible exception).
Pass: changes a visible property (chains, stone) or adds recovery; re-checks new interactions the change introduces.

**S5. Feasible is not inviting** (`level-metrics-sheet`)
Prompt: "Our 4.4 m gap is under the 4.5 m running jump. Players keep walking past it. Is the gap broken?"
Trap: "it's feasible, so players are wrong", or "widen the jump".
Pass: separates capability (feasible, with 0.1 m margin) from affordance and visibility (do players read it as jumpable from where they stand?); checks the approach view and run-up space; proposes an observation that distinguishes "didn't notice" from "judged it too far".

## Perception and learning

**P1. Wrong fix for a perception problem** (`difficulty-matrix`, `feedback-and-readability`)
Prompt: "Players fall in the chain rooms. Should we lengthen leaf lifetime?"
Pass: asks whether falls happen before or after the leaf opens and whether moss was noticed; separates perception, inference, and execution before recommending.
Fail: lengthens lifetime immediately.

**P2. Completion is not learning** (`mechanic-introduction-plan`)
Prompt: "After we added a bypass, more players finish the tutorial room. Did the tutorial get better at teaching timing?"
Pass: no evidence of timing learning; checks route used and a fresh application; notes the bypass may serve exploration.

**P3. Readability vs. intentional mystery** (`design-critique`, `feedback-and-readability`)
Prompt: "Reviewers say our impossible-architecture level is confusing. Should we add signposts?"
Trap: "yes, maximise clarity".
Pass: asks whether disorientation is the intended experience; separates confusion about the rule from inaccessible evidence or a trap; proposes a way to check.

## People

**H1. Misleading consensus** (`design-critique` perspectives)
Prompt: three generated reviews all say "the stealth section is too hard"; one notes that the guard's vision cone is not shown.
Pass: treats the three as one hypothesis; keeps the vision-cone finding as distinct and testable.
Fail: "all reviewers agree, so lower difficulty".

**H2. Asymmetric roles** (`design-critique` demands lesson)
Prompt: "In our co-op, one player navigates and the other drives. Navigators press fewer buttons. Is it unbalanced?"
Pass: defines the intended relationship; compares information, decisions, and downtime rather than button counts; keeps both possible player preferences.

**H3. Accessibility vs. core challenge** (`accessibility-review`)
Prompt: "Our rhythm game's timing windows are tight. A player with limited hand mobility can't play. Should we widen them for everyone?"
Pass: separates core challenge (timing) from incidental demands; proposes an option for the window and input alternatives, keeps the default, recommends checking with affected players.
Fail: widens for everyone, or refuses because timing is the point.

**H4. Missing evidence** (`playtest-plan-and-report`)
Prompt: "Summarise our playtest: P1 got lost, P2 loved the boss." (only two notes)
Pass: reports only what is there with denominators, marks inferences, and says what the next test should check.
Fail: invents counts, quotes, or trends.

**H5. Downtime falls on the newcomer** (`social-play-design`)
Prompt: "Our co-op has a 30 s respawn. Groups are often one veteran and three newcomers. Any concerns?"
Pass: computes downtime by skill (newcomers die more, so they spectate more), ties it to the intended relationship, and weighs revives, respawn-with-something-to-do, or shorter timers with their costs.
Fail: judges the timer by its length alone, or proposes hidden difficulty scaling without discussing what it does to the shared experience.

## Convention-breaking

**C1. Easy climax** (`level-beat-chart`)
Prompt: "Our final level is the easiest in the game. Is that a pacing failure?"
Pass: asks what the ending is for; an easy climax can serve narrative or release; names an observation that would show it fails.

**C2. A loop with no long-term goal** (`core-loop-analysis`)
Prompt: "Our toy has no progression. Is it broken?"
Pass: a toy can be complete; asks about intended experience and session context before recommending progression.

## Process

**R1. Teardown honesty** (`design-teardown`)
Prompt: "Tear down how game X's movement feels."
Pass: states whether the agent has played it, works from documentation and the user's notes, and asks for play observations when feel is the question.
Fail: describes "how it felt to play" without a firsthand basis.

**R2. Ideation spread** (`concept-ideation`)
Prompt: "Ten concepts for the theme 'tide'."
Pass: concepts vary by verb, tone, and point of view; the obvious idea is acknowledged; ends with riskiest assumptions and cheap tests.
Fail: ten variations of the same genre, or a ranked list with no test.

**R3. A pillar that rejects nothing** (`game-design-doc`)
Prompt: "Our pillars are 'Fun combat', 'Beautiful world', 'Deep story'. Draft the one-pager."
Pass: points out that these pillars cannot reject a feature, proposes testable rewrites with an example feature each would reject, and marks the rewrites as proposals for the team to decide.
Fail: writes the one-pager around the pillars unchanged.

**R4. Over-routing** (`game-design-companion`)
Prompt: "Is a 5% drop rate with no pity fair for a cosmetic hat?"
Pass: routes to `loot-table-design` alone, gives the median and 90th-percentile wait (14 and 45 attempts), and separates the arithmetic from the fairness question.
Fail: runs a multi-skill critique, or answers "fair" from the mean (20 attempts) alone.
