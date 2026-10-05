---
name: game-design-doc
description: Write, restructure, or update game design documents at the right level of detail (one-pager, feature spec, system spec), anchored on design pillars and player experience goals. Use when asked to draft a GDD, pitch a concept, spec a feature or system, or keep an existing doc in sync with design changes.
---

# Game Design Doc

Design docs are communication tools, not archives. Write the smallest doc that lets the reader make the next decision.

## 1. Pick the level of detail

| Doc | Reader / purpose | Length | Must contain |
|---|---|---|---|
| One-pager | Pitch, alignment, greenlight | 1 page | Hook, fantasy, pillars (usually 2–3), core loop, audience, references, key risk |
| Feature spec | Team building one feature | 2-6 pages | Goal tied to a pillar, player experience goal, player-facing flow, rules, states, edge cases, tuning knobs, open questions |
| System spec | Designers and implementers of an interacting system | As needed | Purpose, inputs/outputs, rules and formulas, parameters with ranges, interactions with other systems, failure modes, telemetry hooks |

If the request is ambiguous, default to the one-pager for new concepts and the feature spec for anything inside an existing game. State the choice.

## 2. Anchor before writing

1. Confirm or draft **pillars**: usually 2–3 short statements for a one-pager, more only when useful to its scope; make them testable statements of what the game must feel like. A pillar that cannot reject a feature is too vague.
2. Write **player experience goals (PXGs)** per feature: "The player should feel X when Y", followed by a proposed mechanism and observations or neutral questions that could support or weaken it. An emotion is not directly established by a behavior count.
3. Every section of a spec traces back to a pillar or PXG. Flag sections that do not.

## 3. Write

- Lead with intent (why), then player-facing behaviour (what), then rules (how). Implementation belongs to engineering; stay engine-agnostic.
- Use tables for rules, states, and parameters; prose only for intent and feel.
- Name tuning knobs explicitly with starting values, units, model domains, and provisional ranges with validation status.
- Apply Rational Game Design framing where relevant: what the player must **understand** (signs and feedback), what **skills** the feature demands, and how difficulty parameters scale.
- End with **Open questions** and **Risks**, each with an owner if known.

Templates: [templates.md](templates.md).

## 4. Maintain

- When the design changes, update the doc in the same pass; add a dated change-log line at the top.
- Mark speculative content `[TBD]` rather than inventing detail.
- Cut stale sections instead of letting them drift. A shorter true doc beats a longer wrong one.

## Pitfalls

- Writing a bible nobody reads. Split by reader instead.
- Pillars that are genres ("open world") rather than experiences.
- Specifying feel with adjectives only. Add a causal hypothesis, plausible rival explanation, and observation that could distinguish them.
- Mixing decided and undecided content without marking which is which.

## Sources

- Tracy Fullerton, *Game Design Workshop*, chapters on formal elements and on communicating designs (documentation).
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapters on the experience and on the team/documents.
- Rational Game Design framing (skills, signs and feedback, difficulty parameters); see [source boundaries](../design-critique/sources.md) for reviewed practitioner material and access limits.

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
