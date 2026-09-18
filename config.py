from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field, field_validator


class PipelineMode(str, Enum):
    CLEAN = "clean"
    UPPERCASE = "uppercase"


class PipelineConfig(BaseModel):
    file_path: Path
    batch_size: int = Field(gt=0, le=10000)
    mode: PipelineMode
    output_enabled: bool = True

    @field_validator("file_path")
    @classmethod
    def validate_file_path(cls, value):
        if not value.exists():
            raise ValueError(f"File does not exist: {value}")

        if not value.is_file():
            raise ValueError(f"Path is not a file: {value}")

        return value