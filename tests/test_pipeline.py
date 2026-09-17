from pipeline import Pipeline
from steps import (
    LoadCSVStep,
    CleanDataStep,
    CountRecordsStep,
    UppercaseDataStep,
)


def test_pipeline_clean_count():
    pipeline = Pipeline([
        LoadCSVStep(),
        CleanDataStep(),
        CountRecordsStep(),
    ])

    result = pipeline.run("data/sample_data.csv")

    assert result["record_count"] == 10


def test_pipeline_uppercase_count():
    pipeline = Pipeline([
        LoadCSVStep(),
        UppercaseDataStep(),
        CountRecordsStep(),
    ])

    result = pipeline.run("data/sample_data.csv")

    assert result["record_count"] == 10