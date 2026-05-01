# Terra Interfaces — Governance UI

## Scope

This document defines how governance decisions are presented to users.

The interface must make complex decisions understandable without removing necessary detail.

---

## Core Principle

Users must not trust the system blindly.

They must be able to:

- see how a decision was made  
- understand why it was made  
- verify the underlying logic  

---

## Decision View

Every decision must be displayed in a structured format.

### Overview

- Decision Title  
- Status (VALIDATED, PENDING, etc.)  
- Risk Level  
- Affected Systems  

---

### Summary

A short explanation of:

- what is being decided  
- why it matters  
- expected outcome  

This must be human-readable.

---

### Evidence Layer

Shows:

- data sources  
- models used  
- assumptions made  

Users must be able to:

- expand details  
- trace origin of information  

---

### Validation Layer

Displays:

- number of validators  
- agreement level  
- trust weighting  
- outliers detected  

---

### Risk Layer

Shows:

- risk classification  
- reversibility  
- long-term impact  

Must clearly indicate:

- uncertainty  
- unresolved factors  

---

### Guardian Activity

If applicable:

- proof demands issued  
- delays triggered  
- escalation reason  

This must be transparent.

---

## Interaction Options

Users must be able to:

- challenge decision  
- request deeper validation  
- submit additional evidence  
- follow decision updates  

---

## Trust Visualization

Trust must be visualized as:

- reliability indicators  
- consistency history  
- uncertainty markers  

Never as a single absolute score.

---

## Timeline View

Users must see:

```text
Proposal → Validation → Governance → Guardian → Execution

Each step should be clickable and inspectable.

⸻

Multi-Level Detail

The UI must support:

Basic Mode

* summary only
* key outcomes
* minimal detail

Advanced Mode

* full validation data
* model explanations
* trust distribution

Audit Mode

* raw inputs
* validator outputs
* system logs

⸻

Alert System

Users must be notified when:

* decisions affect them
* risk level increases
* Guardian Layer activates
* new evidence changes outcome

⸻

Failure Display

If a decision fails or is uncertain:

* clearly show why
* show missing information
* show next possible steps

No silent failure.

⸻

Design Constraints

The interface must:

* avoid overload
* avoid manipulation
* avoid hidden logic

Clarity is more important than visual complexity.

⸻

Objective

Ensure that every user can:

* understand decisions
* verify reasoning
* interact with the system
* trust the process without blind belief
