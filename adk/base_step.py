# adk/base_step.py
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

class BaseStep(ABC):
    """
    Abstract base class for a step in an agent pipeline.
    Each step processes input data and updates shared context.
    """

    @abstractmethod
    def apply(self, input_data: Any, context: Dict[str, Any]) -> Tuple[Any, Dict[str, Any]]:
        """
        Apply the logic of the step to the input data.

        Args:
            input_data (Any): The input data to be processed.
            context (Dict[str, Any]): A shared dictionary to pass data across steps.

        Returns:
            Tuple[Any, Dict[str, Any]]: The processed output data and the updated context.
        """
        pass

    @abstractmethod
    def explain(self) -> str:
        """
        Generate a human-readable explanation of what this step performed.

        Returns:
            str: Explanation of the step’s processing.
        """
        pass
