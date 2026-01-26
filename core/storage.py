import json
import os
from typing import Dict, Any


class Storage:
    """
    v0.1 Storage:
    Saves provenance records to disk as JSON files.
    """

    @staticmethod
    def save(record: Dict[str, Any], directory: str = "records") -> str:
        os.makedirs(directory, exist_ok=True)

        filename = f"{directory}/{record['intent_id']}.json"

        with open(filename, "w") as f:
            json.dump(record, f, indent=2)

        return filename