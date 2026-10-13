---
name: feedback-and-readability
description: Specify and audit the signs and feedback that tell players what they can do, what is happening, and what just happened, across visual, audio, haptic and text channels, including priority when signals compete and the feel of an action's response. Use when players misread a mechanic, miss a threat, cannot tell why they failed, or when a feature spec needs its signs-and-feedback section.
---

# Feedback and Readability

Players act on what they perceive and infer, not on the rules as written. This skill inventories what the player needs to know at each moment and how the game tells them. Design only: describe signals, timing, and priority, not shaders or audio middleware.

## Terms

- **Sign (before):** tells the player what is possible or coming: an affordance, a telegraph, a cue. Rational Game Design calls these signs.
- **Feedback (during and after):** confirms what happened and why: a hit, a miss, a state change, a reason for failure.
- **Response (feel):** how the action itself answers input: timing, motion, weight. Steve Swink's game-feel model treats input, response, context, polish, metaphor, and rules as parts of feel.
- **Channel:** visual, audio, haptic, text or speech, UI.

## Procedure

1. **List the events that matter** for the mechanic or scene: player actions, enemy or world actions, state changes, success, failure.
2. **For each, write what the player must know** and when: before acting, during, after. Ask the counterfactual: if they did not know this, what wrong action would they take?
3. **Specify the sign and the feedback.** Include the reason on failure: "you missed" is less useful than "out of range" or "not a valid surface". A failure the player cannot explain cannot teach.
4. **Assign channels with redundancy for critical information.** Anything required to progress or avoid harm should reach the player through at least two channels, or one channel plus a selectable alternative. Colour alone, sound alone, or vibration alone excludes some players and fails in some contexts (muted phone, colour vision differences, busy screen).
5. **Check timing.** A telegraph must last longer than the reaction it demands for this audience; feedback should arrive close enough to the action to be attributed to it. Do not invent universal millisecond thresholds; state an estimate and how it will be checked in the target build.
6. **Set priority.** List which signals can occur together. When they compete, which wins? Critical threats should not be masked by reward effects. Keep a noise budget: every signal added makes the others harder to notice.
7. **Check consistency.** One visual language per meaning (the same colour or sound should not mean "danger" in one place and "collectible" in another), unless a deliberate subversion is part of the experience and is recoverable.
8. **Tune response for feel** only after the information works. Screen shake, hit pause, and particles can strengthen a correct message; they cannot repair a missing one.
9. **Plan observation.** Distinguish "did not perceive", "perceived but misread", and "understood but could not act".

## Output

| Event | Player must know | Sign (before) | Feedback (after) | Channels | Timing | Priority / conflicts | Status |
|---|---|---|---|---|---|---|---|

Then: priority order for simultaneous signals, consistency notes, and observations.

Worked example: [example.md](example.md) (the sprout seed's missing miss feedback).

## Pitfalls

- Adding juice to fix a comprehension problem. Spectacle can make a wrong message louder.
- Tutorial text as the only sign. Text read once is not a sign the player can consult at the moment of action.
- Feedback that confirms but does not explain. Players will invent explanations, often wrong ones.
- Treating readability as maximum clarity everywhere. Mystery and surprise can be the point; then decide what remains readable (stakes, recovery) while the answer stays hidden.

## Sources (paraphrased, not quoted)

- Steve Swink, *Game Feel: A Game Designer's Guide to Virtual Sensation*, Morgan Kaufmann, 2008/2009: feel as a vocabulary of input, response, context, polish, metaphor, and rules.
- Chris McEntee, "Rational Design: The Core of Rayman Origins", Game Developer, 2012: signs and feedback as part of the design vocabulary for teaching mechanics.
- Celia Hodent, *The Gamer's Brain* (2017), chapters on perception, attention, and usability.
- Microsoft, [Xbox Accessibility Guideline 103](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103): providing information through additional sensory channels. Practice guidance; check the current version.

Evidence standards: [demands and observation](../design-critique/demands-and-observation.md), [source boundaries](../design-critique/sources.md).
