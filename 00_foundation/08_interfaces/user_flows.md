# Terra Interfaces — User Flows

## Scope

This document defines how humans, organizations, communities, and institutions interact with Terra.

Interfaces translate system complexity into understandable actions.

Users should not need to understand the full architecture to participate safely.

---

## Core Principle

A system is only useful if people can interact with it without losing clarity, agency, or trust.

Terra interfaces must be:

- simple
- transparent
- auditable
- explainable

---

## User Types

### Individual

A person participating in Terra.

Can:

- submit evidence
- report activity
- view decisions
- receive obligations
- challenge outcomes

---

### Community

A local group affected by shared resources.

Can:

- propose local usage rights
- report commons damage
- participate in governance
- validate local conditions

---

### Organization

A company, NGO, institution, or public body.

Can:

- request usage rights
- submit impact reports
- receive validation
- be assigned obligations

---

### Validator

A participant running validation processes.

Can:

- receive tasks
- analyze inputs
- submit signed results
- build trust through accuracy

---

### Guardian Participant

A specialized actor involved in high-risk review.

Can:

- review escalated decisions
- trigger proof demands
- monitor threshold violations

---

## Standard Flow: Submit Proposal

```text
User
→ Create Proposal
→ Define Objective
→ Define Affected Commons
→ Submit Evidence
→ AXIOMA Validation
→ Governance Review
→ Guardian Check if Required
→ Decision Output

Proposal Requirements

Every proposal must include:

* objective
* affected system
* expected benefit
* possible harm
* time horizon
* reversibility level
* evidence source

Incomplete proposals are returned for revision.
User
→ Report Harm
→ Attach Evidence
→ Identify Location / System
→ AXIOMA Consistency Check
→ Validator Review
→ Guardian Escalation if Critical
→ Public Record Update

Standard Flow: Request Usage Rights
Organization / Community
→ Define Resource Use
→ Define Duration
→ Define Regeneration Plan
→ Submit Impact Model
→ Validation
→ Governance Approval
→ Conditional Usage Right Issued

Standard Flow: Challenge Decision

User
→ Select Decision
→ Submit Challenge
→ Provide Evidence
→ Trigger Proof Demand
→ Expanded Validation
→ Outcome Revision or Confirmation

Decision Output Format

Every decision shown to users must include:


* decision state
* reason
* evidence summary
* risk level
* affected commons
* reversibility status
* appeal / challenge option

⸻

Decision States
PENDING
VALIDATED
UNCERTAIN
REJECTED
ESCALATED
EXECUTED
UNDER_REVIEW

Trust Display

Trust must be visible but not absolute.


Users should see:

* validator reliability
* evidence strength
* uncertainty level
* dispute history

Trust is shown as context, not as authority.
Interface Requirements

Every interface must answer:What is being decided?
Who is affected?
What evidence exists?
What risks remain?
Can this be reversed?
Who is responsible?

Transparency Layer

Users must be able to inspect:

* proposal history
* validation trail
* quorum result
* Guardian actions
* final execution state

No critical decision may be hidden.

⸻

Accessibility Principle

Terra must support different levels of user depth:

* simple view
* detailed view
* expert/audit view

This allows broad participation without reducing system rigor.

⸻

Failure Handling

If a user input is invalid:

* explain why
* show missing fields
* suggest required evidence
* preserve draft state

Invalid input should teach the user how to improve it.

⸻

Objective

Ensure that Terra can be used by real people without hiding complexity or weakening validation.
