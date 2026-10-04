---
name: playtest-plan-and-report
description: Plan a playtest (goals, hypotheses, tasks, what to observe, questions to ask) and turn raw playtest notes, recordings summaries, or survey answers into a prioritized findings report. Use when preparing a playtest session or synthesizing results from one.
---

# Playtest Plan and Report

A playtest answers specific questions. No hypothesis, no playtest.

## Mode A: Plan

1. **Goal**: one sentence linking the test to a pillar or player experience goal (PXG).
2. **Hypotheses**: 2-5 falsifiable statements, e.g. "Players find the grapple without a tutorial prompt within 2 minutes."
3. **Build and scope**: which build, which section, what is known-broken (tell testers to ignore it).
4. **Testers**: profile and count; note whether they are new, returning, or genre-experienced. Five or so per profile usually surfaces the major issues.
5. **Tasks**: what the tester is asked to do, phrased as goals, never as instructions that reveal the solution.
6. **Observation sheet**: for each hypothesis, the observable behaviour that confirms or refutes it (hesitation, wrong path, repeated failure, verbal reaction, time to complete).
7. **Questions**: a short post-session interview. Open questions first ("What were you trying to do there?"), ratings last. Avoid leading questions.
8. **Protocol**: think-aloud or silent, moderator does not help unless the tester is stuck for a set time.

Template: [templates.md](templates.md).

## Mode B: Report

1. **Normalize notes**: one line per observation: tester, timestamp or location, what happened (observed) versus what they said (reported).
2. **Cluster** observations into findings. Count how many testers hit each.
3. **Diagnose** each finding with a cause hypothesis, using Rational Game Design framing where useful: a sign not perceived, a sign misunderstood, missing feedback, a skill not yet taught, or a difficulty spike.
4. **Prioritize**: severity (blocks progress / hurts a PXG / friction) x frequency (testers affected).
5. **Check hypotheses**: confirmed, refuted, or inconclusive, with evidence.

Report structure:

1. Summary: top three findings and hypothesis results.
2. Findings table:

| # | Priority | Finding | Testers (n/N) | Evidence | Likely cause | Suggested direction |
|---|---|---|---|---|---|---|

3. What worked (protect it).
4. Open questions and what the next test should check.

## Rules

- Weight behaviour over opinion; players are reliable about problems and unreliable about solutions.
- Never invent counts or quotes. Mark inferences as inferences.
- One tester's issue is a signal to watch, not a fix order, unless it is a blocker.

## Sources

- Tracy Fullerton, *Game Design Workshop*, chapter on playtesting.
- Steve Krug, *Rocket Surgery Made Easy* (small-sample usability testing, think-aloud protocol).
- Celia Hodent, *The Gamer's Brain*, chapters on usability and playtesting.
