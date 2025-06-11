from abc import ABC, abstractmethod

class BaseStep(ABC):
    """
    Abstract base for a step in an agent pipeline.
    """
    @abstractmethod
    def apply(self, input_data, context: dict):
        """Process input_data, possibly reading/updating context. Return (output_data, context)."""
        pass

    @abstractmethod
    def explain(self) -> str:
        """Return a human-readable explanation of what this step did."""
        pass