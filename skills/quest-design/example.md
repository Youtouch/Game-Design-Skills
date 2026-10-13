# Worked example: the mill questline

Synthetic three-quest arc in a small village. **Intended experience:** the player's choice about the mill reshapes how the village ends, and the player can see why.

## 1–2. Quests

| Quest | Purpose | Giver | Hook | Objectives | Core mechanics used | Choices | Consequences (where seen) |
|---|---|---|---|---|---|---|---|
| A. Bad Flour | introduce the miller's debt and the guild | baker Ide | people are getting sick from flour | inspect the mill; find the cause | exploration, inspection | expose the miller to the guild, **or** help him hide it, **or** burn the mill to destroy the evidence | guild presence in the square; the mill's state (visible from the road) |
| B. The Ledger | reveal the guild's own corruption | guild clerk | the guild wants the miller's ledger | retrieve the ledger from the mill | stealth | hand the ledger to the guild **or** keep it | clerk's attitude; village notice board |
| C. Harvest Night | resolve the arc | miller Oren | the village festival needs flour | deliver flour; give a speech | conversation | what to say at the festival | ending scene in the square |

## 3. Flags

| Flag | Written by | Read by | Default |
|---|---|---|---|
| `mill_burned` | A (burn) | B, C | false |
| `miller_exposed` | A (expose) | C | false |
| `miller_alive` | A (burn: false, if the player burns the mill while Oren is inside at night) | C | true |
| `has_ledger` | B | C | false |

## 4. Branch trace

A's three choices × B's two choices; B can be done before or after A's resolution.

| Path | Result | Problem |
|---|---|---|
| A expose → B hand over → C | guild runs festival; Oren speaks as a disgraced man | none |
| A hide → B keep → C | Oren grateful; ledger used in the speech | none |
| A burn (day) → B | **B's objective (retrieve the ledger from the mill) is impossible: the ledger burned** | dead end: B can be started but never finished |
| A burn (night, Oren inside) → C | **C's giver is dead** | lost content and a dangling arc: C never starts and nothing replaces it |
| B first (ledger taken) → A burn | fine for B; A's "destroy the evidence" goal is moot because the evidence is already gone | dialogue in A assumes the ledger is in the mill; needs a variant line |

## Fixes

| Problem | Fix | Experience preserved |
|---|---|---|
| B dead end after burning | if `mill_burned`, B updates: the clerk suspects the player and asks them to find Oren's copy at his house (new objective, same quest) | the burn choice stays powerful; B continues instead of breaking |
| C's giver can die | C's giver becomes baker Ide if `miller_alive` is false: the festival goes on in Oren's memory, and the speech choice changes | burning at night remains a real, heavy choice with its own ending |
| A's dialogue after B | add a line conditional on `has_ledger`: "You already took it, didn't you?" | the free quest order survives |

## 5. Consequence visibility

The burned mill stays burned and is visible from the road on every later visit. The guild presence in the square changes with `miller_exposed`. Each ending scene names the cause explicitly in one line of dialogue, so the link between the choice in A and the ending in C is perceivable.

## 6. Objective clarity

The journal states the current objective and the reason ("Find the cause of the bad flour. Ide thinks it comes from the mill."). After a branch changes an objective (B after burning), the journal entry is rewritten and flagged as updated, so returning players do not search the ruined mill for a ledger that no longer exists.
