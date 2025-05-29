from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, TypedDict, Union


class JobType(Enum):
    CHAT_COMPLETION = "chat_completion"
    TEXT_EMBEDDING = "text_embedding"


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
    stop: Optional[list[str]] = None
    n: int = 1  # number of completions to generate
    stream: bool = False
    logprobs: Optional[int] = None
    echo: bool = False
    user: Optional[str] = None
    top_p: Optional[float] = None
    top_k: Optional[float] = None
    frequency_penalty: Optional[float] = 0.0
    presence_penalty: Optional[float] = 0.0

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LLMParams":
        return cls(
            model=data.get("model", "gpt-4"),
            temperature=float(data.get("temperature", 1.0)),
            max_tokens=int(data.get("max_tokens", 1024)),
            # Fixed: Handle None values properly for optional float fields
            top_p=float(data["top_p"]) if data.get("top_p") is not None else None,
            top_k=float(data["top_k"]) if data.get("top_k") is not None else None,
            frequency_penalty=float(data.get("frequency_penalty", 0.0)),
            presence_penalty=float(
                data.get("presence_penalty", 0.0)
            ),  # Fixed: missing closing parenthesis
            stop=data.get("stop"),
            n=int(data.get("n", 1)),
            stream=bool(data.get("stream", False)),
            logprobs=(
                int(data["logprobs"]) if data.get("logprobs") is not None else None
            ),
            echo=bool(data.get("echo", False)),
            user=data.get("user"),
        )
