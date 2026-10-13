# Worked example: the rare mount and the banner set

Synthetic action-RPG numbers. No real money is involved in this example.

## Brief

- The **Ember Stag** mount drops from a boss with unlimited attempts. One kill takes about 15 minutes including travel. Target: "a committed player gets it within about ten hours of farming" (40 kills).
- Six **guild banners** drop one per dungeon clear, weighted 30, 30, 20, 10, 5, 5. Target: "most players complete the set over the season" (about 60 clears).

## 1–3. The mount at 2%

`python reward_math.py drop --p 0.02`

| Measure | Kills | Hours (15 min/kill) |
|---|---|---|
| Mean | 50 | 12.5 |
| Median | 35 | 8.75 |
| 90th percentile | 114 | 28.5 |
| 99th percentile | 228 | 57 |

Chance of meeting the brief: 1 − 0.98⁴⁰ = **55%**. The median player is fine; 45% miss the target, and one in ten farms nearly three times as long.

## 5. Options

| Option | Mean kills | 90th | 99th | Effect beyond the numbers |
|---|---|---|---|---|
| Keep 2% | 50 | 114 | 228 | rarity preserved; the tail misses the brief |
| Raise to 5.6% (90% within 40) | 17.9 | 40 | 80 | mounts become common; 1% of players still wait 80+ kills |
| 2% with hard pity at 40 | 27.7 | 40 | 40 | brief met for everyone; rarity reduced but bounded |
| 2% plus visible tokens (40 buy it) | 27.7 | 40 | 40 | same numbers as pity; progress is visible, so the grind reads as a plan, not bad luck |

**Choice: visible tokens.** Same distribution as hard pity, but the player can see how far they have to go, which suits "committed player" as the target. Lucky early drops still happen, so the moment of surprise survives. Cost: about 1.8× as many mounts in circulation as before (mean 27.7 vs 50 kills per mount). Acceptable for a cosmetic; it would need an economy check if the mount were tradeable.

## 4. The banner set

`python reward_math.py collect --weights 30,30,20,10,5,5 --percentiles 50,90`

Mean ≈ 32.0 clears; median 27; 90th percentile 59 (simulated, seed 1). The two 5% banners alone average 20 clears each to find. Against "most players complete within about 60 clears", the median player finishes with room to spare and about 90% finish in the season.

Duplicates: in an average run of 32 clears, 26 are duplicates. **Choice:** each duplicate gives 1 banner thread; 8 threads buy any missing banner. This caps the tail without changing early excitement. Recompute with the conversion before shipping (the helper does not model conversion; a short recurrence or a seeded simulation would).

## 7. Disclosure

Show drop chances on the boss and dungeon info panels, and the token and thread rules in the same place. Not required for this design, but cheap, and it removes the "is it bugged?" question.

## 8. Observations

| Question | Observation |
|---|---|
| Does the live drop rate match 2%? | drop logs: kills before each mount, compared with the model's distribution |
| Do tokens change how farming feels? | after-session question: "how close are you to the Stag, and how do you feel about that?" |
| Do players report "never" for banners? | check logs for the reporter before changing weights |
