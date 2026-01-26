from dataclasses import dataclass
from typing import Any, Dict, List, Callable
from validator import Validator, ValidatorResult
from provenance import ProvenanceRecord


@dataclass
class Capsule:
    name: str
    transform: Callable[[Dict[str, Any]], Any]
    validators: List[Validator]

    def run(self, intent_id: str, inputs: Dict[str, Any]) -> ProvenanceRecord:
        """
        v0.1 Capsule execution with provenance:
        1. Run the transform
        2. Run validators
        3. Return a ProvenanceRecord
        """
        output = self.transform(inputs)

        validation_results: List[Dict[str, Any]] = []
        for v in self.validators:
            result: ValidatorResult = v.run(inputs)
            validation_results.append(
                {
                    "name": result.name,
                    "passed": result.passed,
                    "details": result.details,
                }
            )

        return ProvenanceRecord(
            intent_id=intent_id,
            capsule=self.name,
            output=output,
            validations=validation_results,
        )