import hashlib
import json
from typing import Any, Dict


class Signature:
    """
    v0.1 Signature:
    Creates a hash of the provenance record for integrity.
    """

    @staticmethod
    def sign(record: Dict[str, Any]) -> str:
        serialized = json.dumps(record, sort_keys=True).encode("utf-8")
        return hashlib.sha256(serialized).hexdigest()