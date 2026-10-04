---
name: economy-model
description: Model a game economy as sources, sinks, converters and stocks, then check inflation, time-to-earn and resource balance with explicit math. Use when designing or reviewing currencies, crafting, loot, rewards or shops, or when players report "too much gold" or "grind walls".
---

# Economy Model

Design-level economy modelling. No engine code: output is a flow diagram, a rate table and the math behind each verdict.

## When to use

- Designing a new currency, crafting loop, shop or reward schedule.
- Diagnosing inflation, hoarding, grind walls or worthless rewards.
- Checking a monetization or live-ops change against the core loop.

## Inputs to gather (assume and state if missing)

- Resources: currencies, materials, items, energy, time-gated stocks.
- Player archetypes and session profile (minutes/session, sessions/day).
- Target pacing: "a casual player affords X by day N".

## Procedure

1. **Map nodes.** List every resource and tag each node: *source* (creates), *sink* (destroys), *converter* (A -> B), *trader* (player-to-player), *stock* (pool). Draw as a Machinations-style graph (text or Mermaid).
2. **Rate table.** For each flow, write rate per minute of play for each archetype:
   `| flow | type | resource | rate/min (casual) | rate/min (core) | gate/condition |`
3. **Net flow.** Per resource: `net = Σ sources − Σ sinks` (per minute, per archetype). Positive net with no hard cap means stock grows without bound.
4. **Time-to-earn.** For each key purchase: `T = price / net_income`. Convert to sessions and days using the session profile. Compare with the target pacing.
5. **Inflation check.** Track stock over time `S(t) = S0 + net·t`. If prices are fixed while `S(t)` grows, purchasing power of rewards falls; express it as "reward R equals p% of median wallet at day N".
6. **Sink health.** Ratio `sinks/sources` per resource. Below ~0.7 late-game usually means inflation; above 1.0 means stock drains and players stall. Name which sinks scale with wealth (taxes, % fees, repairs) vs fixed sinks.
7. **Converter loops.** Multiply exchange rates around every cycle (A->B->C->A). A product > 1 is an infinite-money exploit.
8. **Stress cases.** Re-run with the top 1% player (max rate), a returning player (large lump), and a payer (purchased currency). Flag where outcomes diverge by more than the design intent.
9. **Verdict and levers.** For each issue, name the lever: change rate, add or scale a sink, add a cap, add decay, or gate by time.

## Output template

See [template.md](template.md) for the report layout and a worked example.

## Pitfalls

- Averaging archetypes hides grind walls; always compute per archetype.
- Fixed sinks lose against compounding sources; prefer sinks that scale with wealth.
- Premium currency must be modelled as a source with its own conversion rate, not ignored.
- Drop tables are expected values; report variance too (time-to-earn at the 90th percentile of bad luck).

## Sources (paraphrased, not quoted)

- Ernest Adams & Joris Dormans, *Game Mechanics: Advanced Game Design* (2012), chapters on internal economy and Machinations diagrams.
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapter on balance (economy lenses).
- Ian Schreiber & Brenda Romero, *Game Balance* (2021), chapters on economic systems and transitive/intransitive balance.
