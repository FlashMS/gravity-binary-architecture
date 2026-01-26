from typing import Any, Dict


class CapsuleChain:
    """
    v0.1 Capsule Chaining:
    Passes output of one capsule into the next capsule's inputs.
    """

    @staticmethod
    def merge_inputs(original: Dict[str, Any], new_output: Dict[str, Any]) -> Dict[str, Any]:
        merged = original.copy()
        merged.update(new_output)
        return merged