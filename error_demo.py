from error_handler import run_pipeline
from exceptions import (
    FileLoadError,
    DataValidationError,
    ProcessingError,
)


print("Test 1: File Load Error")

try:
    run_pipeline("data/not_found.csv")

except FileLoadError as error:
    print(f"Caught FileLoadError: {error}")


print("\nTest 2: Data Validation Error")

try:
    run_pipeline("data/empty_data.txt")

except DataValidationError as error:
    print(f"Caught DataValidationError: {error}")


print("\nTest 3: Processing Error")

try:
    run_pipeline("data/error_data.txt")

except ProcessingError as error:
    print(f"Caught ProcessingError: {error}")