from dataclasses import dataclass
from typing import Any, Dict, List
import time


def timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


@dataclass
class ProvenanceRecord:
    intent_id: str
    capsule: str
    output: Any
    validations: List[Dict[str, Any]]
    created_at: str = timestamp()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "intent_id": self.intent_id,
            "capsule": self.capsule,
            "output": self.output,
            "validations": self.validations,
            "created_at": self.created_at,
        }