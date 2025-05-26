import os
from typing import Optional

from llm.openai_client import OpenAIClient
from llm.prompt import ExamplePrompt
from llm.types import Prompt
from llm.utils import LLMEngine, load_llm_params_from_yaml

load_llm_params_from_yaml()


def load_llm_client(
    prompt: Prompt = ExamplePrompt.grammar_checker_prompt,
    provider: Optional[str] = None,
) -> object:

    provider = provider or os.getenv("PROVIDER", "openai").lower()
    prompt
    if provider == "openai":
        return OpenAIClient(engine=LLMEngine(), prompt=prompt)
    else:
        raise ValueError(f"Client for {provider} is not available!")
