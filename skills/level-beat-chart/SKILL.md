---
name: level-beat-chart
description: Build a pacing and beat chart for a level, with an intensity curve, rest beats and a self-check for monotony and difficulty spikes. Use after a level brief exists and before or during blockout, or to critique the pacing of an existing level.
---

# Level Beat Chart

Turns a level brief into an ordered list of beats with a measured intensity curve, so pacing can be reviewed before layout is built. Design only; no engine work.

## Inputs

- A level brief (see `level-brief`), especially mechanics in play and difficulty targets.
- Target playtime. If missing, assume 10–15 minutes and say so.

## Procedure

1. **List beats.** Split the level into 8–20 beats. Each beat has: id, type, mechanic(s), estimated duration, and a one-line player experience.
   Beat types: `intro`, `exposition` (safe teach), `validation` (low-stakes test), `challenge`, `combination`, `rest`, `reward`, `reveal` (story/vista), `climax`, `exit`.
2. **Score intensity (1–10)** per beat from three factors, each 0–3, plus 1: threat (enemies, hazards), execution demand (timing, precision), and cognitive load (new rules, puzzles). Write the factors, not only the total, so the score can be argued.
3. **Order by learning structure.** Each new mechanic follows exposition → validation → challenge, and only then appears in a combination beat (McEntee, *Rational Design: The Core of Rayman Origins*, 2012).
4. **Shape the curve.** Aim for a rising sawtooth: peaks that climb across the level, each followed by a rest or reward beat, with the climax near the end and a short release after it. Keep the player in the flow band between boredom and anxiety (McMillan, *The Rational Design Handbook: An Intro to RLD*, 2013, building on Csikszentmihalyi's flow model).
5. **Draw the curve** as a text chart or a table the reader can paste into a spreadsheet.

## Self-check (run every time, report findings)

| Check | Flag when |
|---|---|
| Monotony | 3+ consecutive beats within ±1 intensity, or the same beat type 3 times in a row |
| Spike | Intensity rises by more than 3 between consecutive beats, or a factor jumps by 2+ with a new mechanic at the same time |
| No rest | More than ~4 minutes, or 3 beats, above intensity 6 without a rest/reward beat |
| Skipped teaching | A mechanic appears in `challenge` before `exposition` |
| Flat ending | Climax is not the highest peak, or there is no release beat after it |
| Front-loading | Highest peak is in the first third of the level |

For each flag, propose one concrete fix (insert a rest beat, split a beat, move a mechanic later, lower one factor).

## Output template

```markdown
# Beat Chart: <level>
| # | Beat | Type | Mechanics | Min | Threat | Exec | Cog | Intensity | Experience |
|---|------|------|-----------|-----|--------|------|-----|-----------|------------|

Intensity curve
10 |
 5 |   ▂▅▂ ▃▆▃ ▅█▂
 0 +--------------->
## Self-check findings
- <flag>: <beat ids> → <fix>
```

## Sources (paraphrased, not quoted)

- Chris McEntee, *Rational Design: The Core of Rayman Origins*, Game Developer, 2012.
- Luke McMillan, *The Rational Design Handbook: An Intro to RLD*, Game Developer, 2013.
- Mihaly Csikszentmihalyi, *Flow: The Psychology of Optimal Experience*, 1990.
