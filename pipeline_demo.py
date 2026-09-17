from pipeline import Pipeline
from steps import (
    LoadCSVStep,
    CleanDataStep,
    CountRecordsStep,
    UppercaseDataStep,
)


file_path = "data/sample_data.csv"


# Pipeline 1: Load → Clean → Count
pipeline_1 = Pipeline([
    LoadCSVStep(),
    CleanDataStep(),
    CountRecordsStep(),
])

result_1 = pipeline_1.run(file_path)

print("Pipeline 1:")
print(result_1)


# Pipeline 2: Load → Uppercase → Count
# CleanDataStep is swapped with UppercaseDataStep.
# Pipeline class is NOT changed.
pipeline_2 = Pipeline([
    LoadCSVStep(),
    UppercaseDataStep(),
    CountRecordsStep(),
])

result_2 = pipeline_2.run(file_path)

print("\nPipeline 2:")
print(result_2)