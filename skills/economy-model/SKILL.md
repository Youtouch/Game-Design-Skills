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
3. **Net flow.** Per resource: `net = Σ sources − Σ sinks` (per minute, per archetype). Sustained positive net with no cap grows stock in this model; changing rates, finite rewards, and optional spending can invalidate that extrapolation.
4. **Time-to-earn.** For constant deterministic positive net income, `T = max(0, price − starting_stock) / net_income`. Zero or negative net cannot reach a higher target under that model. Account for caps, gates, and session rounding. For random discrete rewards, target/mean is not an exact expected stopping time: use state recurrence, enumeration, or a documented simulation; see [chance lesson](../design-critique/chance.md).
5. **Inflation check.** Track stock over time `S(t) = S0 + net·t`. With fixed prices, a fixed reward still buys the same goods; wallet growth can reduce its relative salience, not its purchasing power. Distinguish stock accumulation from market-price inflation; express it as "reward R equals p% of median wallet at day N".
6. **Sink health.** Ratio `sinks/sources` per resource. No universal ratio establishes inflation or stall. Inspect reserves, finite goals, optional spending, changing rates, and the desired accumulation path; a ratio above one drains stock only while those flows persist. Name which sinks scale with wealth (taxes, % fees, repairs) vs fixed sinks.
7. **Converter loops.** Multiply exchange rates around every cycle (A->B->C->A). A product > 1 indicates gross gain per cycle. Check fees, rounding, limits, time, availability, and repeatability before claiming unbounded gain or an exploit; a bounded profitable trade can be intentional.
8. **Stress cases.** Re-run with the top 1% player (max rate), a returning player (large lump), and a payer (purchased currency). Flag where outcomes diverge by more than the design intent.
9. **Verdict and levers.** For each issue, name the lever: change rate, add or scale a sink, add a cap, add decay, or gate by time.

## Output template

See [template.md](template.md) for the report layout and a worked example.

## Pitfalls

- Averaging archetypes hides grind walls; always compute per archetype.
- Compare sink behavior with intended accumulation and distribution; scaling sinks can have costs and are not universally preferable.
- Premium currency must be modelled as a source with its own conversion rate, not ignored.
- Report the reward distribution and, when relevant, progression-time quantiles. A reward variance is not a waiting-time percentile; state how each was computed.

## Sources (paraphrased, not quoted)

- Ernest Adams & Joris Dormans, *Game Mechanics: Advanced Game Design* (2012), chapters on internal economy and Machinations diagrams.
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapter on balance (economy lenses).
- Ian Schreiber & Brenda Romero, *Game Balance* (2021), chapters on economic systems and transitive/intransitive balance.

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
