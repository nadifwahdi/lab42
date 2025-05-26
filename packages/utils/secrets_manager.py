import os
from typing import Any

from dotenv import load_dotenv

from utils import initiate_logger

# load environment from .env
load_dotenv()


class Safebox:
    def __init__(self) -> None:
        self.logger = initiate_logger(self.__class__.__name__)
        for key, value in os.environ.items():
            if key.startswith("SECRET_"):
                self.logger.info(f"Using {key.replace('SECRET_', '')} from safebox...")
                attr_name = key.replace("SECRET_", "").lower()
                setattr(self, attr_name, value)

    # set the secret value to string by default
    def __getattribute__(self, name: str) -> Any:
        return self.__dict__.get(name, "")
