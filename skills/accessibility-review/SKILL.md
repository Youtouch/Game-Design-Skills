---
name: accessibility-review
description: Review a mechanic, level, or feature for barriers across vision, hearing, motor, cognitive and situational limits by separating the intended challenge from incidental demands, then propose options that keep player choice. Use when speccing a feature, before a milestone review, when adding difficulty or assist options, or when a player reports they cannot play a section.
---

# Accessibility Review

Start from demands, not a checklist. Every interaction asks the player to perceive, understand, decide, act, and recover. Some of those demands are the challenge the game offers; others are incidental. Incidental barriers usually deserve removal or an alternative by default. Core challenges deserve options that let players choose their own experience. Design only.

## Inputs

- The mechanic, level, or feature, with its metrics and signs (see `feedback-and-readability`).
- The intended experience: which demands are the point.
- Platforms and input devices.
- Any reports from players, especially disabled players, kept with their context.

## Procedure

1. **Name the intended challenge** in one line. Everything else is a candidate incidental demand. Be honest: "precise timing" may be the point of a rhythm game and incidental in a story game.
2. **Inventory demands** per interaction: perception (what must be seen, heard, felt; size, contrast, duration), cognition (reading, memory, simultaneous tracking, time pressure), choice, execution (precision, timing windows, simultaneous or repeated inputs, holds, speed), and recovery (cost of failure).
3. **Check each demand across ability areas:** vision (low vision, colour-vision differences, blindness), hearing, motor (reach, strength, precision, endurance, one hand), cognition (attention, memory, reading, processing speed), speech if voice is used, and photosensitivity. Add situational limits: muted audio, small screens, glare, interruptions.
4. **Classify each barrier.** *Incidental:* not part of the intended challenge; fix in the default or provide an alternative. *Core:* part of the challenge; offer options (assists, settings, alternate routes) and decide defaults. *Unknown:* needs evidence from affected players.
5. **Propose options by type**, noting what each changes:
   - *Presentation:* redundant channels, text size and contrast, subtitles with speaker and sound captions, colour-independent shapes, reduced flashing and motion.
   - *Input:* full remapping, hold-to-toggle, adjustable timing windows, alternatives to simultaneous presses, support for alternative devices.
   - *Challenge:* assists that adjust a specific parameter (slower timer, wider window, extra recovery), skips, and their effect on rewards or progression.
   - *Cognition:* objective reminders, journals, pause anywhere, replayable instructions, consistent symbols.
   Prefer options that adjust the specific demand over a single "easy mode" that changes everything at once.
6. **Separate equivalent evidence from solutions.** Describing a visual cue in audio gives the same information; announcing the answer removes the inference. Both can be valid options; label which is which.
7. **Cross-check against guidelines** after the demand analysis (Game Accessibility Guidelines; Xbox Accessibility Guidelines; WCAG flash thresholds for flashing content). A guideline met does not prove the game is playable for a given player; a guideline missed is a lead, not a verdict.
8. **Plan evaluation with affected players.** Recruit disabled players, record their setup and assistive technology, and ask what they want from the experience. Do not assume disability equals preferring less challenge.

## Output

| Interaction | Demand | Ability areas affected | Intended challenge? | Barrier | Option(s) | What the option changes | Default | Evidence / status |
|---|---|---|---|---|---|---|---|---|

Then: priority (participation blockers first, regardless of how many players they affect), options summary for the settings menu, and the evaluation plan.

Worked example: [example.md](example.md).

## Pitfalls

- Treating accessibility as a late checklist. Many barriers are cheapest to remove during design (a shape instead of a colour costs nothing at spec time).
- One global difficulty slider for everything. It forces players to trade away challenge they wanted to keep.
- Counting affected players to deprioritise a blocker. A blocker stops play entirely for those it affects.
- Assuming a guideline-compliant design works. Evaluate with people.

## Sources (paraphrased, not quoted)

- Game Accessibility Guidelines ([gameaccessibilityguidelines.com](https://gameaccessibilityguidelines.com/)): recommendations grouped by motor, cognitive, vision, hearing, speech, and general, in basic, intermediate, and advanced tiers weighing reach, impact, and cost.
- Microsoft, Xbox Accessibility Guidelines, including [XAG 103](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103) (additional sensory channels) and [XAG 109](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109) (objectives and navigation support). Check current versions.
- W3C, WCAG 2.x success criterion 2.3.1, "Three Flashes or Below Threshold": a widely used reference for limiting flashing content. Written for web content; apply as a reference, not a game certification.
- Martinez, Froehlich & Fogarty, "Playing on Hard Mode", CHI 2024 ([doi](https://doi.org/10.1145/3613904.3642804)): qualitative accounts from thirteen disabled players about difficulty, adaptation, and joy. Informs questions about agency, not prevalence.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
