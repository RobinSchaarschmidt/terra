#!/usr/bin/env python3
"""
Terra × AXIOMA — Minimal Proof of Reality

Purpose:
- Submit a proposal
- Validate structure
- Simulate validators
- Calculate quorum
- Produce decision state

No external dependencies.
Python standard library only.
"""

from dataclasses import dataclass
from statistics import median
from typing import List, Dict, Any
import hashlib
import json
import time


# ------------------------------------------------------------
# Data Models
# ------------------------------------------------------------

@dataclass
class Proposal:
    title: str
    actor: str
    affected_common: str
    objective: str
    expected_benefit: str
    possible_harm: str
    time_horizon_years: int
    reversibility: str
    evidence: List[str]


@dataclass
class ValidatorResult:
    validator_id: str
    score: float
    trust: float
    notes: str


# ------------------------------------------------------------
# AXIOMA Structural Validation
# ------------------------------------------------------------

def validate_proposal_structure(proposal: Proposal) -> Dict[str, Any]:
    missing = []

    for field, value in proposal.__dict__.items():
        if value is None or value == "" or value == []:
            missing.append(field)

    if missing:
        return {
            "state": "INVALID",
            "reason": "Missing required fields",
            "missing": missing
        }

    if proposal.affected_common.lower() not in [
        "water",
        "atmosphere",
        "biodiversity",
        "climate",
        "human_foundation"
    ]:
        return {
            "state": "UNCERTAIN",
            "reason": "Affected common is not recognized clearly",
            "missing": []
        }

    return {
        "state": "STRUCTURALLY_VALID",
        "reason": "Proposal contains required fields",
        "missing": []
    }


# ------------------------------------------------------------
# Risk Classification
# ------------------------------------------------------------

def classify_risk(proposal: Proposal) -> str:
    risk_score = 0

    if proposal.affected_common.lower() in ["water", "climate", "biodiversity"]:
        risk_score += 2

    if proposal.time_horizon_years >= 10:
        risk_score += 2

    if proposal.reversibility.lower() in ["low", "irreversible"]:
        risk_score += 3

    harm_words = ["depletion", "collapse", "pollution", "irreversible", "extinction"]
    if any(word in proposal.possible_harm.lower() for word in harm_words):
        risk_score += 2

    if risk_score >= 6:
        return "HIGH"
    if risk_score >= 3:
        return "MEDIUM"
    return "LOW"


# ------------------------------------------------------------
# Validator Simulation
# ------------------------------------------------------------

def simulate_validators(proposal: Proposal) -> List[ValidatorResult]:
    """
    In a real system, validators would be separate devices/nodes.
    Here we simulate independent validator outputs.
    """

    risk = classify_risk(proposal)

    if risk == "HIGH":
        scores = [0.41, 0.44, 0.46, 0.39, 0.48]
    elif risk == "MEDIUM":
        scores = [0.68, 0.72, 0.75, 0.70, 0.66]
    else:
        scores = [0.84, 0.88, 0.86, 0.91, 0.83]

    validators = []

    for index, score in enumerate(scores, start=1):
        validators.append(
            ValidatorResult(
                validator_id=f"validator_{index}",
                score=score,
                trust=0.80 + (index * 0.02),
                notes=f"Simulated validation result for {risk} risk proposal"
            )
        )

    return validators


# ------------------------------------------------------------
# Quorum Logic
# ------------------------------------------------------------

def calculate_quorum(results: List[ValidatorResult], risk: str) -> Dict[str, Any]:
    if not results:
        return {
            "state": "PENDING",
            "reason": "No validator results"
        }

    scores = [r.score for r in results]
    trusts = [r.trust for r in results]

    median_score = median(scores)
    near_median = [
        score for score in scores
        if abs(score - median_score) <= 0.10
    ]

    agreement_score = len(near_median) / len(scores)
    average_trust = sum(trusts) / len(trusts)
    weighted_consensus = agreement_score * average_trust * median_score

    thresholds = {
        "LOW": 0.55,
        "MEDIUM": 0.65,
        "HIGH": 0.78
    }

    threshold = thresholds.get(risk, 0.75)

    if weighted_consensus >= threshold:
        state = "VALIDATED"
    elif agreement_score < 0.60:
        state = "ESCALATED"
    else:
        state = "UNCERTAIN"

    return {
        "state": state,
        "risk": risk,
        "median_score": round(median_score, 3),
        "agreement_score": round(agreement_score, 3),
        "average_trust": round(average_trust, 3),
        "weighted_consensus": round(weighted_consensus, 3),
        "threshold": threshold
    }


# ------------------------------------------------------------
# Guardian Layer
# ------------------------------------------------------------

def guardian_check(proposal: Proposal, quorum: Dict[str, Any]) -> Dict[str, Any]:
    risk = quorum.get("risk", classify_risk(proposal))

    if risk == "HIGH":
        return {
            "guardian_state": "TRIGGERED",
            "action": "PROOF_DEMAND",
            "reason": "High-risk proposal affecting planetary commons"
        }

    if quorum["state"] in ["UNCERTAIN", "ESCALATED"]:
        return {
            "guardian_state": "TRIGGERED",
            "action": "DELAY_AND_EXPAND_VALIDATION",
            "reason": "Validation uncertainty remains unresolved"
        }

    return {
        "guardian_state": "NOT_TRIGGERED",
        "action": "ALLOW_CONDITIONAL_PROGRESS",
        "reason": "Risk and validation within acceptable range"
    }


# ------------------------------------------------------------
# System Hash
# ------------------------------------------------------------

def create_record_hash(data: Dict[str, Any]) -> str:
    encoded = json.dumps(data, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


# ------------------------------------------------------------
# Full Pipeline
# ------------------------------------------------------------

def run_pipeline(proposal: Proposal) -> Dict[str, Any]:
    structural = validate_proposal_structure(proposal)

    if structural["state"] == "INVALID":
        return {
            "proposal": proposal.title,
            "state": "REJECTED",
            "structural_validation": structural
        }

    risk = classify_risk(proposal)
    validator_results = simulate_validators(proposal)
    quorum = calculate_quorum(validator_results, risk)
    guardian = guardian_check(proposal, quorum)

    final_state = quorum["state"]

    if guardian["guardian_state"] == "TRIGGERED":
        final_state = "ESCALATED"

    record = {
        "timestamp": int(time.time()),
        "proposal": proposal.__dict__,
        "structural_validation": structural,
        "risk": risk,
        "validators": [v.__dict__ for v in validator_results],
        "quorum": quorum,
        "guardian": guardian,
        "final_state": final_state
    }

    record["record_hash"] = create_record_hash(record)

    return record


# ------------------------------------------------------------
# Example Scenario
# ------------------------------------------------------------

if __name__ == "__main__":
    proposal = Proposal(
        title="Industrial Groundwater Extraction",
        actor="Example Industrial Organization",
        affected_common="water",
        objective="Extract groundwater for manufacturing",
        expected_benefit="Job creation and industrial output",
        possible_harm="Groundwater depletion and ecosystem stress",
        time_horizon_years=10,
        reversibility="low",
        evidence=[
            "regional groundwater report",
            "industrial demand forecast",
            "partial recharge model"
        ]
    )

    result = run_pipeline(proposal)

    print(json.dumps(result, indent=2))
