from typing import Any, Dict, List


class ConstraintFailure(Exception):
    pass


class Constraint:
    """
    v0.1 Constraint:
    A simple rule that checks the intent inputs before execution.
    """

    def __init__(self, name: str, rule):
        self.name = name
        self.rule = rule  # rule: Callable[[Dict[str, Any]], bool]

    def check(self, inputs: Dict[str, Any]) -> None:
        if not self.rule(inputs):
            raise ConstraintFailure(f"Constraint failed: {self.name}")


class ConstraintEngine:
    """
    v0.1 Constraint Engine:
    Runs a list of constraints before capsule execution.
    """

    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints

    def validate(self, inputs: Dict[str, Any]) -> None:
        for constraint in self.constraints:
            constraint.check(inputs)