# Calculate the outcome that matters

Use this lesson for reward or progression claims. Specify outcomes, probabilities, dependence, costs, caps, and stopping conditions before calculating. A correct average does not establish balanced or enjoyable play.

For a joint event, P(A and B) = P(A) P(B given A). Multiplying marginal probabilities requires independence, not merely overlapping events. Verify the probability model rather than inheriting an authority's arithmetic.

## Synthetic example: ink packets

A packet independently supplies one ink unit with probability 1/2 or five with probability 1/2. Its mean is three, variance four, and standard deviation two. A fixed three-unit packet has the same mean with zero variance.

With only two spaces left in the bottle, usable expected gain is (1 + 2)/2 = 1.5 for the random packet and two for the fixed packet. A lower usable mean might still be chosen for suspense or expression; that preference is a separate claim.

From empty, how many packets are expected to reach four units? Do not divide four by the mean three. The process stops on the first five-unit packet or after four one-unit packets. The terminal attempt counts have probabilities 1/2, 1/4, 1/8, and 1/8, yielding 15/8 = 1.875 attempts.

Alternatively, let T(r) be expected attempts with r units remaining. Then T(r) = 1 + T(r−1)/2 + T(r−5)/2, with T(r≤0) = 0. The recurrence agrees with terminal-path enumeration. A pity counter or drawing without replacement would require additional state. A cap below the target with no way to spend or expand it makes the target unreachable, so this recurrence would not describe that system.

**Counterexample:** highest mean damage need not be the best attack against a nearly defeated target when misses, overkill, and turn cost matter.

**Exception:** an informed player can prefer variance despite a lower usable reward. Preserve the option when stakes and recovery fit the intended experience; do not adjust the arithmetic to justify the preference.

## Exercise and explained answer

If the first packet yields one, are future odds worse? Under the declared independent process, no. The remaining target changes; the next packet distribution does not. Evidence or an explicit rule is needed before adding depletion or pity. Exact waiting-time arithmetic still says nothing by itself about whether players enjoy the wait.
