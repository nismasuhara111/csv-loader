from pydantic import ValidationError

from config import PipelineConfig


# 1. Invalid batch size
print("Test 1: Invalid batch size")

try:
    PipelineConfig(
        file_path="data/sample_data.csv",
        batch_size=-5,
        mode="clean",
    )
except ValidationError as error:
    print(error)


# 2. Invalid mode
print("\nTest 2: Invalid mode")

try:
    PipelineConfig(
        file_path="data/sample_data.csv",
        batch_size=10,
        mode="invalid_mode",
    )
except ValidationError as error:
    print(error)


# 3. Non-existent file path
print("\nTest 3: Non-existent file")

try:
    PipelineConfig(
        file_path="data/not_found.csv",
        batch_size=10,
        mode="clean",
    )
except ValidationError as error:
    print(error)

# 4. Missing required field
print("\nTest 4: Missing required field")

try:
    PipelineConfig(
        file_path="data/sample_data.csv",
        batch_size=10,
        # mode is missing
    )
except ValidationError as error:
    print(error)