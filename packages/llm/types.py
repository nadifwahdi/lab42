from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict, Union


class JobInfo(TypedDict):
    id: str
    input_cost: float
    output_cost: float
    total_cost: float
    input_tokens: int
    output_tokens: int
    total_tokens: int


class JobInfoType(TypedDict):
    individual: List[JobInfo]
    aggregated: Dict[str, Union[str, int, float]]


@dataclass
class Prompt:
    prompt: str
    instructions: Optional[str] = None


@dataclass
class LLMParams:
    model: str
    temperature: float = 1.0
    max_tokens: int = 1024
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    stop: Optional[list[str]] = None
    n: int = 1  # number of completions to generate
    stream: bool = False
    logprobs: Optional[int] = None
    echo: bool = False
    user: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LLMParams":
        return cls(
            model=data.get("model", "gpt-4"),
            temperature=float(data.get("temperature", 1.0)),
            max_tokens=int(data.get("max_tokens", 1024)),
            top_p=float(data.get("top_p", 1.0)),
            frequency_penalty=float(data.get("frequency_penalty", 0.0)),
            presence_penalty=float(data.get("presence_penalty", 0.0)),
            stop=data.get("stop"),
            n=int(data.get("n", 1)),
            stream=bool(data.get("stream", False)),
            logprobs=data.get("logprobs"),
            echo=bool(data.get("echo", False)),
            user=data.get("user"),
        )
