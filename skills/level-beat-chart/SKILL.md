---
name: level-beat-chart
description: Build a pacing and beat chart for a level, with an intensity curve, rest beats and a self-check for monotony and difficulty spikes. Use after a level brief exists and before or during blockout, or to critique the pacing of an existing level.
---

# Level Beat Chart

Turns a level brief into an ordered list of beats with a provisional intensity model, so pacing can be reviewed before layout is built. Design only; no engine work.

## Inputs

- A level brief (see `level-brief`), especially mechanics in play and difficulty targets.
- Target playtime. If missing, assume 10–15 minutes and say so.

## Procedure

1. **List beats.** Split the level into 8–20 beats. Each beat has: id, type, mechanic(s), estimated duration, and a one-line player experience.
   Beat types: `intro`, `exposition` (safe teach), `validation` (low-stakes test), `challenge`, `combination`, `rest`, `reward`, `reveal` (story/vista), `climax`, `exit`.
2. **Score intensity (1–10)** per beat from three factors, each 0–3, plus 1: threat (enemies, hazards), execution demand (timing, precision), and cognitive load (new rules, puzzles). Write the factors, not only the total, so the score can be argued.
3. **Check learning opportunities.** Exposition → validation → challenge is one useful structure. Inspect prerequisites and alternate routes; combined discovery can be intentional, and completion does not prove mastery.
4. **Shape pacing against intent.** A rising sawtooth is one option. A dramatic climax can use an easy task to leave attention for narrative; quiet exploration or ritual may sustain a plateau. A numerical curve does not measure flow or emotion.
5. **Draw the curve** as a text chart or a table the reader can paste into a spreadsheet.

## Optional screening heuristics

The numbers below are draft prompts, not validated limits. Use only relevant checks, justify thresholds for the brief, and report intentional exceptions. Keep threat, execution, and cognitive estimates separate even when displaying a total.

| Check | Flag when |
|---|---|
| Monotony | 3+ consecutive beats within ±1 intensity, or the same beat type 3 times in a row |
| Spike | Intensity rises by more than 3 between consecutive beats, or a factor jumps by 2+ with a new mechanic at the same time |
| No rest | More than ~4 minutes, or 3 beats, above intensity 6 without a rest/reward beat |
| Skipped teaching | A mechanic appears in `challenge` before `exposition` |
| Flat ending | Climax is not the highest peak, or there is no release beat after it |
| Front-loading | Highest peak is in the first third of the level |

For a relevant flag, explain the threatened goal and propose a change or a justified preservation decision with a distinguishing observation. A climax below the highest difficulty peak is not inherently a defect.

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

Research-informed application: see [demands and observation](../design-critique/demands-and-observation.md) for contextual diagnosis and [source boundaries](../design-critique/sources.md) for reviewed evidence and limits. Existing bibliography entries beyond that review remain background references, not newly verified claims.
