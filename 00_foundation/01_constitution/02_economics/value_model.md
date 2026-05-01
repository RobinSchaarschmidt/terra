# Terra Economics — Value Model

## Scope

This document defines how Terra evaluates value.

Value is not treated as price alone.  
Value is treated as the measurable relationship between contribution, scarcity, utility, risk, distribution, and time.

---

## Core Principle

A system action has value only if it improves or preserves system stability without creating hidden long-term harm.

Market price may signal demand.  
It does not prove value.

---

## Value Function

Terra uses a dynamic task-based value model:

```text
V_task = F(S, D, Q, U, R, T)
Where:S = Scarcity
D = Distribution
Q = Quality
U = Utility
R = Risk / Harm
T = Time impact

The function is context-dependent.

Different tasks use different weights, but the same core dimensions.

⸻

Dimension: Scarcity (S)

Scarcity measures how limited or difficult to replace a resource, skill, action, or output is.

High scarcity increases value only if the output is useful and does not create unacceptable risk.

Scarcity alone does not justify high value.

⸻

Dimension: Distribution (D)

Distribution measures how value, access, and burden are spread across affected actors.

A system action loses value if it concentrates benefit while distributing harm.

Fair distribution increases long-term stability.

⸻

Dimension: Quality (Q)

Quality measures reliability, durability, accuracy, and fitness for purpose.

Low-quality output reduces value even if demand is high.

Quality must be validated, not merely claimed.

⸻

Dimension: Utility (U)

Utility measures actual usefulness to humans, communities, ecosystems, or system stability.

Utility must be connected to real outcomes.

Symbolic or speculative utility receives lower weighting unless validated by measurable effect.

⸻

Dimension: Risk / Harm (R)

Risk measures potential damage, uncertainty, reversibility, and externalized cost.

Higher risk reduces value.

Irreversible risk has nonlinear penalty weight.

⸻

Dimension: Time Impact (T)

Time impact measures how effects unfold across time.

Short-term benefit is discounted if it creates long-term instability.

Long-term preservation receives higher weighting than temporary extraction.

Basic Evaluation Logic

A simplified model can be expressed as:
V_task = (S + D + Q + U + T) - R

For high-risk domains:
V_task = (S * Q * U * T * D) / (1 + R)

This prevents high-risk
actions from appearing valuable merely because they are profitable.

⸻

Risk Penalty

Risk is weighted more strongly when:

* damage is irreversible
* affected systems are planetary commons
* future generations carry the cost
* uncertainty is high
R_effective = R * irreversibility_factor * uncertainty_factor
Time Weighting

Time modifies value.
T_effective = short_term_gain - delayed_harm + long_term_stability

An action with high immediate benefit but severe delayed harm receives reduced total value.

⸻

Commons Constraint

If an action violates planetary commons constraints, its value cannot be positive.
if commons_violation == true:
    V_task <= 0

No economic benefit can override constitutional limits.

⸻

Token Interaction

The value model influences:

* WORK validation
* CREDIT issuance
* TERRA weighting
* GOVT trust adjustment

Valid contribution can increase token influence.

Harmful or unverifiable activity reduces it.

⸻

Governance Interaction

Governance decisions must include value modeling.

A proposal is incomplete if it does not define:

* expected value
* risk profile
* affected actors
* time horizon
* validation method

⸻

Guardian Interaction

The Guardian Layer triggers when:

* R_effective exceeds threshold
* commons constraints are affected
* T_effective shows delayed harm
* uncertainty remains unresolved

⸻

Simulation Interaction

All simulations use the value model to compare:

* predicted value
* actual outcome
* delayed consequences
* error rate

This updates future weighting.

⸻

Invalid Value

A value claim is invalid if it is based only on:

* market price
* popularity
* authority
* speculation
* incomplete data

⸻

Objective

Ensure that Terra evaluates value as:

* real contribution
* system benefit
* long-term stability
* accountable impact
