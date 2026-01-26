from typing import List
from intent_frame import IntentFrame
from capsule import Capsule
from provenance import ProvenanceRecord
from constraint_engine import ConstraintEngine
from chaining import CapsuleChain
from signature import Signature
from storage import Storage


class ExecutionEngine:
    """
    v0.2 Execution Engine:
    - Runs constraints
    - Executes capsule chain
    - Generates provenance
    - Signs provenance
    - Stores provenance
    """

    def __init__(self, capsules: List[Capsule], constraints: ConstraintEngine):
        self.capsules = capsules
        self.constraints = constraints

    def run(self, intent: IntentFrame) -> List[ProvenanceRecord]:
        # 1. Validate constraints
        self.constraints.validate(intent.inputs)

        records: List[ProvenanceRecord] = []
        current_inputs = intent.inputs

        # 2. Capsule chaining
        for capsule in self.capsules:
            record = capsule.run(intent.intent_id, current_inputs)

            # 3. Sign provenance
            record_dict = record.to_dict()
            record_dict["signature"] = Signature.sign(record_dict)

            # 4. Store provenance
            Storage.save(record_dict)

            # 5. Add to results
            records.append(record)

            # 6. Chain output into next capsule
            current_inputs = CapsuleChain.merge_inputs(current_inputs, record.output)

        return records