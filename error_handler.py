from exceptions import (
    FileLoadError,
    DataValidationError,
    ProcessingError,
)


def load_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError as error:
        raise FileLoadError(
            f"Unable to load file: {file_path}"
        ) from error


def validate_data(data):
    try:
        if not data:
            raise ValueError("Data cannot be empty.")

        return True

    except ValueError as error:
        raise DataValidationError(
            "Input data validation failed."
        ) from error


def process_data(data):
    try:
        if "ERROR" in data:
            raise RuntimeError("Processing failed.")

        return data.upper()

    except RuntimeError as error:
        raise ProcessingError(
            "An error occurred while processing data."
        ) from error


def run_pipeline(file_path):
    try:
        data = load_file(file_path)
        validate_data(data)
        result = process_data(data)

    except FileLoadError:
        raise

    except DataValidationError:
        raise

    except ProcessingError:
        raise

    else:
        return result

    finally:
        print("Pipeline execution finished.")