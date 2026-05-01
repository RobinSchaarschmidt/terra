# AXIOMA Compute — Quorum Logic

## Scope

This document defines how distributed validators reach reliable outcomes inside Terra.

Quorum logic is used to determine whether a result is:
- accepted
- delayed
- rejected
- escalated

---

## Core Principle

A result is not valid because one entity produced it.

A result becomes valid when independent validators produce sufficiently consistent outputs under verifiable conditions.

---

## Validator Role

Validators are independent nodes that:

- receive tasks
- process inputs
- generate outputs
- sign results
- submit evidence

Validators do not decide truth alone.

They contribute weighted signals.

---

## Minimum Quorum


A task requires a minimum number of validator responses before evaluation.



Default threshold:


```text
minimum_validators = 3

For high-risk decisions:threshold = 0.60
Medium-risk task:threshold = 0.75
High-risk task:threshold = 0.90
Planetary-risk task:threshold = 0.95+

Higher risk requires stronger convergence.

⸻

Finality States

Every task can end in one of five states.

PENDING
VALIDATED
UNCERTAIN
REJECTED
ESCALATED

PENDING

Not enough validator responses.

VALIDATED

Quorum reached and thresholds satisfied.

UNCERTAIN

Evidence is insufficient or outputs diverge.

REJECTED

Result fails validation.

ESCALATED

Risk is too high for normal quorum.

⸻

Outlier Handling

Outliers are not automatically deleted.

They are:

* flagged
* compared
* stored
* reviewed

Outliers may indicate:

* error
* attack
* minority truth
* missing model dimension

Minority Signal Preservation

A minority result is preserved if it contains:

* valid evidence
* unexplained contradiction
* risk not addressed by majority

Majority agreement does not erase valid minority warnings.

⸻

Collusion Resistance

The system reduces coordinated manipulation through:

* validator diversity
* trust decay
* anomaly detection
* random task assignment
* delayed finality for high-risk tasks

⸻

Trust Decay

Trust is not permanent.

Trust decays when validators:

* become inactive
* repeatedly align with false outcomes
* produce unexplained anomalies
* fail to validate under stress

⸻

Escalation Trigger

Escalation occurs when:

* validator disagreement remains high
* decision affects commons
* irreversible harm is possible
* minority warning remains unresolved

Escalated tasks require Guardian Layer review.

⸻

Objective

Quorum logic ensures that:

* no single validator defines truth
* manipulation becomes expensive
* uncertainty remains visible
* system reliability improves over time

End of Quorum Logic

