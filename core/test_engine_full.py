from intent_frame import IntentFrame
from capsule import Capsule
from validator import Validator
from constraint_engine import Constraint, ConstraintEngine
from execution_engine import ExecutionEngine


def dummy_transform(inputs):
    return {"length": len(inputs.get("resume_text", ""))}


# -----------------------------
# Constraints
# -----------------------------
constraints = ConstraintEngine([
    Constraint("resume_text_required", lambda i: "resume_text" in i),
    Constraint("resume_text_not_empty", lambda i: len(i.get("resume_text", "")) > 0),
])


# -----------------------------
# Intent
# -----------------------------
intent = IntentFrame(
    goal="Full engine test",
    inputs={"resume_text": "This is a test resume."},
    validators=["resume-style-check", "keyword-density"],
)


# -----------------------------
# Capsules
# -----------------------------
capsules = [
    Capsule(
        name="resume-analysis",
        transform=dummy_transform,
        validators=[
            Validator("resume-style-check"),
            Validator("keyword-density"),
        ],
    )
]


# -----------------------------
# Execution Engine
# -----------------------------
engine = ExecutionEngine(capsules, constraints)


# -----------------------------
# Run the full pipeline
# -----------------------------
records = engine.run(intent)

for r in records:
    print(r.to_dict())