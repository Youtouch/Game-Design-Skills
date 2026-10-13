# Worked example: a starter weapon table

Synthetic table for an action RPG shop: [example.csv](example.csv). Brief: four ranged and four melee weapons for the first two hours; each should have a reason to be bought. `cooldown` is seconds between attacks (lower is better); `range` is metres.

| name | role | cost | damage | range | cooldown |
|---|---|---|---|---|---|
| Short Bow | ranged | 100 | 10 | 20 | 1.0 |
| Long Bow | ranged | 100 | 12 | 25 | 1.0 |
| Crossbow | ranged | 160 | 30 | 22 | 2.5 |
| Sling | ranged | 40 | 5 | 12 | 0.8 |
| Dagger | melee | 60 | 8 | 1 | 0.5 |
| Sword | melee | 120 | 14 | 1.5 | 0.8 |
| Halberd | melee | 180 | 24 | 3 | 1.6 |
| Hammer | melee | 180 | 18 | 1.5 | 1.6 |

## 1. Normalise

Sustained DPS = damage / cooldown: Short Bow 10, Long Bow 12, Crossbow 12, Sling 6.25, Dagger 16, Sword 17.5, Halberd 15, Hammer 11.25. DPS hides burst: the Crossbow's 30 per hit kills a 30 HP target in one shot, which the Long Bow needs three shots and two seconds for. Keep both numbers.

## 2. First pass: global fit

`python balance_check.py example.csv --lower cooldown`

The fit gives `range` a negative weight and `cooldown` a positive one, and the helper notes both. That does not mean range is bad. Melee weapons have short range and short cooldowns and are cheap; ranged weapons have long range and long cooldowns. Mixing the roles lets the fit price "being melee" through the wrong columns. **Lesson:** a wrong-sign weight is a signal to split by role or supply design weights, not a finding about the stat.

## 3. Second pass: within roles, design weights

`python balance_check.py example.csv --lower cooldown --group role --weights damage=6,range=1,cooldown=-20`

The weights are the designer's stated intent (one damage point is worth six range metres; each second of cooldown costs twenty value). The helper scales them so each group's fair costs sum to its actual costs.

| group | option | cost | fair cost | gap | flag |
|---|---|---|---|---|---|
| ranged | Crossbow | 160 | 193 | +21% | underpriced |
| ranged | Long Bow | 100 | 97.8 | −2% | |
| ranged | Sling | 40 | 33 | −17% | overpriced |
| ranged | Short Bow | 100 | 76.2 | −24% | overpriced |
| melee | Halberd | 180 | 206 | +15% | |
| melee | Dagger | 60 | 70 | +17% | underpriced |
| melee | Sword | 120 | 125 | +4% | |
| melee | Hammer | 180 | 139 | −23% | overpriced |

Dominance: Long Bow dominates Short Bow; Halberd dominates Hammer.

## 4. Degenerate combination

Suppose a "Quickdraw" charm gives −40% cooldown and stacks twice. Additive stacking gives −80%: the Crossbow fires every 0.5 s for 60 DPS, five times its base rate. Multiplicative stacking gives 0.6² = 0.36 of base cooldown: 0.9 s and 33.3 DPS. The rule for stacking matters more than any single row here. If additive, cap total reduction or make the second stack weaker.

## 5. Report

| # | finding | options | evidence | severity | lever |
|---|---|---|---|---|---|
| 1 | Dominated | Short Bow | Long Bow is equal or better on every modeled column at the same cost | high | lower price to ~75, or give a niche the table lacks (draw speed while moving, cheaper ammo) |
| 2 | Dominated | Hammer | Halberd: more damage, more range, same cooldown and cost | high, unless an omitted effect exists | ask what the Hammer is for; if it breaks armour or staggers, add that column and re-run |
| 3 | Underpriced burst | Crossbow | +21% under design weights; one-shots 30 HP targets | medium | check against enemy HP thresholds before repricing; burst may be the intended identity |
| 4 | Stacking risk | Crossbow + 2× Quickdraw | 60 DPS additive vs 12 base | high if additive | multiplicative stacking or a cap |
| 5 | Cheap starter reads expensive | Sling | −17% | low | probably fine: a starter can be inefficient if it is affordable on arrival; confirm with the economy model |

## What this example does not show

All values are synthetic. The weights are one designer's intent; another set changes findings 3 and 5. Nothing here predicts pick rates or enjoyment. The next step is to check finding 2 with the designer and findings 1 and 3 against the enemy roster.
