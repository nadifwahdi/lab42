from abc import ABC, abstractmethod
from typing import Any, Dict

from llm.types import JobType


class LLMClientBase(ABC):
    @abstractmethod
    def call_request(self, job_name: JobType) -> Any:
        """
        Execute a request to the LLM with specified input and parameters.

        This method should define how to send a prompt or input to the LLM \
        and return its output.

        It typically handles payload construction, sending the request, and \
        parsing the response.
        """
        pass

    @abstractmethod
    def get_cost_info(self) -> Any:
        """Estimate the cost of a given request to the LLM."""
        pass

    @abstractmethod
    def get_call_metadata(self) -> Dict[str, Any]:
        """Return metadata information about the LLM or the request."""
        pass
