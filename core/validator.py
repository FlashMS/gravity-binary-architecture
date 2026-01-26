from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ValidatorResult:
    name: str
    passed: bool
    details: Dict[str, Any]


@dataclass
class Validator:
    name: str

    def run(self, inputs: Dict[str, Any]) -> ValidatorResult:
        """
        v0.1 placeholder logic.
        Real validators will override this method.
        """
        return ValidatorResult(
            name=self.name,
            passed=True,
            details={"message": "Validator v0.1 default pass"}
        )