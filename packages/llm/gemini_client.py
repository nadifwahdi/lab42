from dataclasses import asdict
from typing import Any, Dict, Literal, Optional, Union

from google import genai
from google.genai import types
from google.genai.types import GenerateContentResponse
from utils import initiate_logger

from llm.base import LLMClientBase
from llm.llm_utils import GeminiCost, LLMEngine
from llm.types import (
    JobInfo,
    JobInfoType,
    JobType,
    Prompt,
)


class GeminiClient(LLMClientBase):
    def __init__(
        self, engine: LLMEngine, prompt: Prompt, gemini_api_key: Optional[str]
    ):
        self.logger = initiate_logger(self.__class__.__name__)
        self.client = genai.Client(api_key=gemini_api_key)
        self.engine = engine
        self.prompt = prompt
        self.job_info = JobInfoType(individual=[], aggregated={})

    def call_request(
        self,
        job_name: JobType,
    ) -> GenerateContentResponse:
        if job_name == JobType.CHAT_COMPLETION:
            self.logger.info(f"Calling Gemini API and request with {job_name} job...")
            response = self.__chat_completion()
        else:
            self.logger.error(f"The {JobType.value} job is not currently available!")

        # add each call information to job info dictionary
        self.job_info["individual"].append(self.__get_job_info(response))

        return response

    def get_cost_info(
        self,
        type: Literal["aggregated", "individual"] = "aggregated",
        call_no: Optional[Union[int, Literal["all"]]] = None,
    ) -> Any:
        if type == "aggregated":
            self.logger.info("Calculating overall total cost...")
            aggregate_keys = [
                ("input_tokens", 0),
                ("output_tokens", 0),
                ("total_tokens", 0),
                ("input_cost", 0.0),
                ("output_cost", 0.0),
                ("total_cost", 0.0),
            ]

            for key, default in aggregate_keys:
                self.job_info["aggregated"][f"overall_{key}"] = sum(
                    getattr(call, key, default)
                    for call in self.job_info["individual"]
                    if isinstance(call.get(key, default), (int, float))
                )

            aggregated = self.job_info["aggregated"]
            self.logger.info(
                f"Total cost for all calls: USD {aggregated.get('total_cost', 0.0):.5f}"
            )
        else:
            if call_no == "all":
                return self.job_info["individual"]
            elif call_no is None:
                raise ValueError("call_no must be provided for individual type")
            elif self.job_info["individual"] == []:
                raise ValueError("No individual job data available.")
            else:
                return self.job_info["individual"][call_no]

    def get_call_metadata(self) -> Dict[str, Any]:
        return {
            "job_parameters": asdict(self.engine.params),
            "job_cost": {
                "individual": self.job_info["individual"],
                "aggregated": self.job_info["aggregated"],
            },
        }

    def __chat_completion(self) -> GenerateContentResponse:
        response = self.client.models.generate_content(
            model=self.engine.params.model,
            config=types.GenerateContentConfig(
                system_instruction=self.prompt.instructions,
                temperature=self.engine.params.temperature,
                top_p=self.engine.params.top_p,
                top_k=self.engine.params.top_k,
                presence_penalty=self.engine.params.presence_penalty,
                frequency_penalty=self.engine.params.frequency_penalty,
            ),
            contents=self.prompt.prompt,
        )

        return response

    def __get_job_info(self, response: GenerateContentResponse) -> JobInfo:
        input_cost = getattr(GeminiCost, self.engine.params.model).input
        output_cost = getattr(GeminiCost, self.engine.params.model).output
        input_tokens = response.usage_metadata.prompt_token_count
        output_tokens = response.usage_metadata.candidates_token_count
        total_tokens = response.usage_metadata.total_token_count
        return {
            "id": response.response_id,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "input_cost": (input_tokens / 1_000_000) * input_cost,
            "output_cost": (output_tokens / 1_000_000) * output_cost,
            "total_cost": ((input_tokens / 1_000_000) * input_cost)
            + ((output_tokens / 1_000_000) * output_cost),
        }


if __name__ == "__main__":
    import os

    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("SECRET_GEMINI_API_KEY")
    prompt = Prompt(
        instructions="You are a kindergarten teacher, Mrs.Smith, in your day one at work",
        prompt="Mrs. Smith..... Who is Einstein?",
    )
    params = {"model": "gemini-2.5-flash-preview-05-20"}
    engine = LLMEngine(**params)
    client = GeminiClient(engine=engine, prompt=prompt, gemini_api_key=api_key)
    response = client.call_request(job_name=JobType.CHAT_COMPLETION)
    print(response.text)
