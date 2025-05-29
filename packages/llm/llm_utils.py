from typing import Any

import yaml
from utils import initiate_logger

from llm.types import LLMParams


def load_llm_params_from_yaml(
    path: str = "config.yaml", config_name: str = "default"
) -> LLMParams:
    """
    Load LLM parameters from YAML configuration file

    Args:
        path: Path to the YAML config file
        config_name: Name of the configuration to load (e.g., 'default', 'creative_writing', etc.)

    Returns:
        LLMParams instance with loaded configuration
    """
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    # Get the specific configuration by name
    if config_name not in config:
        raise ValueError(f"Configuration '{config_name}' not found in {path}")

    return LLMParams.from_dict(config[config_name])


# Example usage functions
def load_config_examples() -> None:
    """Example of how to load different configurations"""

    # Load default configuration
    default_params = load_llm_params_from_yaml("config.yaml", "default")
    print(f"Default config: {default_params}")

    # Load creative writing configuration
    creative_params = load_llm_params_from_yaml("config.yaml", "creative_writing")
    print(f"Creative config: {creative_params}")

    # Load code generation configuration
    code_params = load_llm_params_from_yaml("config.yaml", "code_generation")
    print(f"Code config: {code_params}")


class LLMEngine:
    def __init__(
        self,
        config_name: str = "default",
        config_path: str = "config.yaml",
        **kwargs: Any,
    ) -> None:
        # Load from YAML first, then override with any kwargs
        if config_path and config_name:
            yaml_params = load_llm_params_from_yaml(config_path, config_name)
            # Convert to dict and update with kwargs
            params_dict = yaml_params.__dict__.copy()
            params_dict.update(kwargs)
            self.params = LLMParams(**params_dict)
        else:
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

GEMINI_COST = {
    "gemini-2.5-flash-preview-05-20": {"input": 1.25, "output": 1.50},
    "gemini-1.5-pro": {
        "input": 1.25,  # $1.25 per 1M tokens
        "cached_input": 0.3125,  # $0.3125 per 1M tokens (75% discount)
        "output": 5.00,  # $5.00 per 1M tokens
        "context_window": 2000000,  # 2M tokens
        "rate_limit_rpm": 360,  # requests per minute
        "rate_limit_tpm": 4000000,  # tokens per minute
    },
    "gemini-1.5-pro-002": {
        "input": 1.25,  # $1.25 per 1M tokens
        "cached_input": 0.3125,  # $0.3125 per 1M tokens (75% discount)
        "output": 5.00,  # $5.00 per 1M tokens
        "context_window": 2000000,  # 2M tokens
        "rate_limit_rpm": 360,
        "rate_limit_tpm": 4000000,
    },
    "gemini-1.5-flash": {
        "input": 0.075,  # $0.075 per 1M tokens
        "cached_input": 0.01875,  # $0.01875 per 1M tokens (75% discount)
        "output": 0.30,  # $0.30 per 1M tokens
        "context_window": 1000000,  # 1M tokens
        "rate_limit_rpm": 1000,
        "rate_limit_tpm": 4000000,
    },
    "gemini-1.5-flash-002": {
        "input": 0.075,  # $0.075 per 1M tokens
        "cached_input": 0.01875,  # $0.01875 per 1M tokens (75% discount)
        "output": 0.30,  # $0.30 per 1M tokens
        "context_window": 1000000,  # 1M tokens
        "rate_limit_rpm": 1000,
        "rate_limit_tpm": 4000000,
    },
    "gemini-1.5-flash-8b": {
        "input": 0.0375,  # $0.0375 per 1M tokens
        "cached_input": 0.009375,  # $0.009375 per 1M tokens (75% discount)
        "output": 0.00015,  # $0.15 per 1M tokens
        "context_window": 1000000,  # 1M tokens
        "rate_limit_rpm": 1000,
        "rate_limit_tpm": 4000000,
    },
    "gemini-1.0-pro": {
        "input": 0.50,  # $0.50 per 1M tokens
        "cached_input": None,  # No caching available
        "output": 1.50,  # $1.50 per 1M tokens
        "context_window": 30720,  # ~30K tokens
        "rate_limit_rpm": 360,
        "rate_limit_tpm": 120000,
    },
    "text-embedding-004": {
        "input": 0.001,  # $0.01 per 1M tokens
        "cached_input": None,  # No caching for embeddings
        "output": None,  # No output tokens for embeddings
        "context_window": 2048,  # 2K tokens
        "rate_limit_rpm": 1500,
        "rate_limit_tpm": 1500000,
    },
}
