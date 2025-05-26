from typing import Any

import yaml
from utils.logging import initiate_logger

from llm.types import LLMParams


def load_llm_params_from_yaml(path: str = "config.yaml") -> LLMParams:
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return LLMParams.from_dict(config)


class LLMEngine:
    def __init__(self, **kwargs: Any) -> None:
        self.params = LLMParams(**kwargs)
        self.logger = initiate_logger(name="main")
        self.logger.info("LLM has been initialized with parameters: %s", self.params)


OPENAI_COST = {
    "gpt-4.5": {
        "context_length": "128k",
        "input": 75.00,
        "cached_input": 37.50,
        "output": 150.00,
    },
    "gpt-4o": {
        "context_length": "128k",
        "input": 2.50,
        "cached_input": 1.25,
        "output": 10.00,
    },
    "gpt-4o-mini": {
        "context_length": "128k",
        "input": 0.15,
        "cached_input": 0.075,
        "output": 0.60,
    },
    "o1": {
        "context_length": "200k",
        "input": 15.00,
        "cached_input": 7.50,
        "output": 60.00,
    },
    "o3-mini": {
        "context_length": "200k",
        "input": 1.10,
        "cached_input": 0.55,
        "output": 4.40,
    },
    "gpt-4o_fine_tuning": {
        "input": 3.75,
        "cached_input": 1.875,
        "output": 15.00,
        "training": 25.00,
    },
    "gpt-4o-mini_fine_tuning": {
        "input": 0.30,
        "cached_input": 0.15,
        "output": 1.20,
        "training": 3.00,
    },
    "realtime_api": {
        "gpt-4o": {"input": 5.00, "cached_input": 2.50, "output": 20.00},
        "gpt-4o-mini": {"input": 0.60, "cached_input": 0.30, "output": 2.40},
    },
    "built_in_tools": {
        "code_interpreter": 0.03,
        "file_search_storage": 0.10,  # per GB per day
        "file_search_tool_call": 2.50,  # per 1k tool calls
    },
    "web_search_tool_call": {
        "gpt-4o": {"low": 30.00, "medium": 35.00, "high": 50.00},
        "gpt-4o-mini": {"low": 25.00, "medium": 27.50, "high": 30.00},
    },
}
