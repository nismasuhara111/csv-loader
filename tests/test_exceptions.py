import pytest

from exceptions import (
    FileLoadError,
    DataValidationError,
    ProcessingError,
)

from error_handler import load_file, validate_data, process_data


def test_file_load_error():
    with pytest.raises(FileLoadError):
        load_file("data/not_found.csv")


def test_data_validation_error():
    with pytest.raises(DataValidationError):
        validate_data([])


def test_processing_error():
    with pytest.raises(ProcessingError):
        process_data("ERROR")


def test_exception_hierarchy():
    assert issubclass(FileLoadError, Exception)
    assert issubclass(DataValidationError, Exception)
    assert issubclass(ProcessingError, Exception)