import pytest
from pydantic import ValidationError

from config import PipelineConfig


def test_valid_config():
    config = PipelineConfig(
        file_path="data/sample_data.csv",
        batch_size=10,
        mode="clean",
    )

    assert config.batch_size == 10
    assert config.mode.value == "clean"


def test_invalid_batch_size():
    with pytest.raises(ValidationError):
        PipelineConfig(
            file_path="data/sample_data.csv",
            batch_size=-5,
            mode="clean",
        )


def test_invalid_mode():
    with pytest.raises(ValidationError):
        PipelineConfig(
            file_path="data/sample_data.csv",
            batch_size=10,
            mode="invalid_mode",
        )


def test_nonexistent_file():
    with pytest.raises(ValidationError):
        PipelineConfig(
            file_path="data/not_found.csv",
            batch_size=10,
            mode="clean",
        )


def test_missing_required_field():
    with pytest.raises(ValidationError):
        PipelineConfig(
            file_path="data/sample_data.csv",
            batch_size=10,
        )