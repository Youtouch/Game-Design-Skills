---
name: design-critique
description: Give a structured, prioritized critique of a game or level design (doc, pitch, mechanic, level layout, or playtest footage notes) against its pillars, player experience goals, MDA-style lenses, and Rational Game Design readability. Use when asked to review, critique, sanity-check, or find problems in a design.
---

# Design Critique

Critique the design against its own goals, not your taste. Every issue must cite the goal it threatens.

## 1. Establish the yardstick

- Extract the **pillars** and **player experience goals (PXGs)** from the material. If missing, infer them, state them as assumptions, and flag their absence as an issue.
- Note the target audience and platform; they change what counts as a problem.

## 2. Run the lenses

Work through each lens briefly; skip ones that do not apply and say so.

1. **Pillar fit**: does each element serve at least one pillar? Does anything contradict one?
2. **MDA chain** (Mechanics -> Dynamics -> Aesthetics): from the rules, predict the dynamics players will actually produce, then the feelings those dynamics create. Flag gaps between predicted and intended aesthetics, and dominant strategies or degenerate loops.
3. **Readability (RGD)**: can the player perceive the relevant signs, understand what they mean, and get clear feedback on their actions? Check for missing, ambiguous, or conflicting signs and delayed or absent feedback.
4. **Skills and difficulty (RGD)**: which skills does it demand, are they taught before being tested, and do difficulty parameters ramp without spikes?
5. **Motivation and loop**: is there a clear goal, meaningful choice, and reason to repeat?
6. **Scope and risk**: cost versus value, unknowns that need a prototype.

For levels, add: navigation and landmarks, pacing (intensity curve), sightlines, and whether the space teaches its own mechanics.

## 3. Report

Output in this order:

1. **Verdict** (2-3 lines): does it meet its goals, and what is the single biggest problem.
2. **Issues**, sorted by priority:

| # | Severity | Lens | Issue | Goal threatened | Suggested direction |
|---|---|---|---|---|---|

   Severity: **Blocker** (breaks a pillar or core loop), **Major** (undermines a PXG for many players), **Minor** (friction or polish).
3. **Strengths** worth protecting (short list), so fixes do not remove them.
4. **Questions** that only the designer or a playtest can answer.

## Rules

- Offer directions, not full redesigns, unless asked.
- Separate what you observed in the material from what you predict; mark predictions.
- Prefer one sharp issue over five vague ones. Cap the list at about ten; mention that more minor items exist if they do.
- Recommend a playtest when the disagreement is about feel, not logic (see `playtest-plan-and-report`).

## Sources

- Robin Hunicke, Marc LeBlanc, Robert Zubek, "MDA: A Formal Approach to Game Design and Game Research" (2004).
- Jesse Schell, *The Art of Game Design: A Book of Lenses* (lens-based questioning).
- Rational Game Design and Rational Level Design material (readability, skills, difficulty parameters); see the project research file for links.
