---
name: loot-table-design
description: Design or audit random rewards (drop tables, gacha-style pulls, crafting procs, card packs) by computing waiting-time distributions, duplicate and collection costs, and the effect of pity or bad-luck protection, and by checking disclosure and fairness concerns. Use when setting drop rates, when players report "never getting" an item, or when reviewing paid random rewards.
---

# Loot Table Design

Players live in the distribution, not the average. A 2% drop has a mean of 50 attempts, but one player in ten waits more than 113. This skill turns drop rates into the waits players actually experience, then chooses protections against the brief. Design only.

## Inputs

- The reward process: what is rolled, when, with what probabilities, and whether attempts are independent.
- Cost per attempt in play time, currency, or money.
- The brief: who should get what by when ("a committed player gets the mount within about ten evening hours").
- Whether rewards can be bought with real money.

## Procedure

1. **Write the process exactly.** Independent rolls, drawing without replacement (shuffle bag), counters, guarantees, duplicate handling. If any of these is unknown, say so; they change every number below.
2. **Compute the wait distribution,** not just the mean. Report the median and an unlucky percentile (90th, 99th). With [reward_math.py](reward_math.py):
   `python reward_math.py drop --p 0.02 --percentiles 50,90,99`
   For independent attempts, mean = 1/p and the q-th percentile is ⌈ln(1 − q) / ln(1 − p)⌉. Convert attempts to time or cost.
3. **Compare against the brief.** What fraction of players meet the target? `P(within n) = 1 − (1 − p)^n`. A rate that suits the median player can fail the brief for a large unlucky tail.
4. **Model duplicates and sets.** Collecting all of n equally likely items takes n·(1 + 1/2 + … + 1/n) draws on average (8 items: about 21.7). Unequal weights are dominated by the rarest items; the helper gives an exact mean and seeded percentiles: `python reward_math.py collect --weights 30,30,20,10,5,5`.
5. **Choose protection, if any,** and recompute:
   - *Hard pity:* guaranteed by attempt N. Mean becomes (1 − (1 − p)^N) / p; the tail is cut at N.
   - *Soft pity:* chance rises after a threshold (`--soft-start`, `--soft-step`).
   - *Visible tokens:* each attempt grants a token; N tokens buy the item. Same tail as hard pity, but players can see progress and plan.
   - *Shuffle bag:* draw without replacement from a bag of outcomes; bounds streaks. Needs its own model.
   - *Duplicate conversion:* duplicates become currency toward a chosen item. Turns a collection tail into a bounded cost.
   - *Higher base rate:* simple, but raises the average supply too.
   Each changes supply, scarcity, and the meaning of a rare item. Pick for the brief, not by default.
6. **Check the economy link.** Drops are sources: feed them into `economy-model`. Duplicate conversion and tokens are converters.
7. **Check disclosure and fairness.** State the odds and any pity rule where players can find them. When rewards can be bought with real money, check current platform policies, rating-board labelling, and local law for each market before shipping; these differ by region and change over time. Look for designs that obscure real cost (multiple currency layers, odds hidden behind animation) and say what they do.
8. **Plan observation.** Drop logs give real distributions; compare with the model. Player reports of "never" deserve a check of the logs before a rate change: streaks happen in correct systems, and bugs happen too.

## Output

| Reward | Process | p / weights | Protection | Mean | Median | 90th / 99th | In time or cost | Meets brief? |
|---|---|---|---|---|---|---|---|---|

Then: duplicate and collection costs, chosen protections with rationale, disclosure notes, and observations.

Worked example: [example.md](example.md).

## Pitfalls

- Reporting only the mean. The mean hides the players who quit.
- Dividing a target by the mean reward for discrete random rewards. Use the distribution or a recurrence; see the [chance lesson](../design-critique/chance.md).
- Assuming independence when the implementation uses counters, seeds, or bags. Ask.
- Adding pity without recomputing supply: protections increase the average number of rare items in circulation.
- Treating gambler's-fallacy complaints as proof of a bug, or proof of none. Check logs.

## Sources (paraphrased, not quoted)

- Ian Schreiber & Brenda Romero, *Game Balance* (2021), chapters on probability with dice and cards, pseudorandom numbers, and infinite probabilities.
- Jesse Schell, *The Art of Game Design: A Book of Lenses*, chapter on chance; see [source boundaries](../design-critique/sources.md) for the arithmetic issues found in the first edition.
- Waiting-time results (geometric distribution, coupon collector, and its unequal-probability integral form) are standard probability; the helper's tests check them against closed forms and inclusion–exclusion.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
