from typing import Optional
from FERS_core.settings.enums import AnalysisOrder, Dimensionality


class AnalysisOptions:
    _analysis_options_counter = 1

    def __init__(
        self,
        id: Optional[int] = None,
        solver: Optional[str] = "newton_raphson",
        tolerance: Optional[float] = 0.01,
        max_iterations: Optional[int] = None,
        dimensionality: Optional[Dimensionality] = Dimensionality.THREE_DIMENSIONAL,
        order: Optional[AnalysisOrder] = AnalysisOrder.LINEAR,
    ):
        self.analysis_options_id = id or AnalysisOptions._analysis_options_counter
        if id is None:
            AnalysisOptions._analysis_options_counter += 1

        self.solver = solver
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.dimensionality = dimensionality
        self.order = order

    def to_dict(self):
        return {
            "id": self.analysis_options_id,
            "solver": self.solver,
            "tolerance": self.tolerance,
            "max_iterations": self.max_iterations,
            "dimensionality": self.dimensionality.value,
            "order": self.order.value,
        }
