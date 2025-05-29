import os
from typing import Optional

from llm import gemini_client, openai_client
from llm.llm_utils import LLMEngine, load_llm_params_from_yaml
from llm.prompt import ExamplePrompt
from llm.types import Prompt

load_llm_params_from_yaml()


def load_llm_client(
    api_key: str,
    prompt: Prompt = ExamplePrompt.grammar_checker_prompt,
    provider: Optional[str] = None,
) -> object:

    provider = provider or os.getenv("PROVIDER", "openai").lower()
    if provider == "openai":
        return openai_client.OpenAIClient(
            engine=LLMEngine(), prompt=prompt, openai_api_key=api_key
        )
    elif provider == "gemini":
        return gemini_client.GeminiClient(
            engine=LLMEngine(), prompt=prompt, gemini_api_key=api_key
        )
    else:
        raise ValueError(
            f"Client for {provider if provider else 'NONE'} is not available!"
        )
