import os
from pathlib import Path

from dotenv import load_dotenv

from utils import initiate_logger

# Find project root - go up until we find the directory containing .env
current_path = Path(__file__).resolve()
project_root = current_path
while project_root.parent != project_root:  # Stop at filesystem root
    if (project_root / ".env").exists():
        break
    project_root = project_root.parent

dotenv_path = project_root / ".env"
load_dotenv(dotenv_path)


class Safebox:
    def __init__(self) -> None:
        self.logger = initiate_logger(self.__class__.__name__)
        for key, value in os.environ.items():
            if key.startswith("SECRET_"):
                self.logger.info(f"Using {key.replace('SECRET_', '')} from safebox...")
                attr_name = key.replace("SECRET_", "").lower()
                setattr(self, attr_name, value)
