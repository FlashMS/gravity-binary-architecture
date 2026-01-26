from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import uuid
import time


def generate_intent_id() -> str:
    return f"intent-{uuid.uuid4()}"


def timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


@dataclass
class IntentFrame:
    intent_id: str = field(default_factory=generate_intent_id)
    goal: str = ""
    inputs: Dict[str, Any] = field(default_factory=dict)
    context_window: Dict[str, Any] = field(default_factory=dict)
    constraints: Dict[str, Any] = field(default_factory=dict)
    validators: List[str] = field(default_factory=list)
    success_criteria: Dict[str, Any] = field(default_factory=dict)
    failure_modes: Dict[str, Any] = field(default_factory=dict)
    plan: Optional[List[Dict[str, Any]]] = None
    created_at: str = field(default_factory=timestamp)

    def describe(self) -> Dict[str, Any]:
        return {
            "intent_id": self.intent_id,
            "goal": self.goal,
            "inputs": self.inputs,
            "context_window": self.context_window,
            "constraints": self.constraints,
            "validators": self.validators,
            "success_criteria": self.success_criteria,
            "failure_modes": self.failure_modes,
            "plan": self.plan,
            "created_at": self.created_at,
        }


if __name__ == "__main__":
    frame = IntentFrame(
        goal="Refactor resume for recruiter visibility",
        inputs={"resume_text": "..."},
        context_window={"job_target": "Cloud Engineer"},
        constraints={"tone": "professional"},
        validators=["resume-style-check", "keyword-density"],
        success_criteria={"improved_readability": True},
        failure_modes={"missing_sections": ["experience", "skills"]},
    )
    print(frame.describe())