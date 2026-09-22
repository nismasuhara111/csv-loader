from decorators import timeit, retry
from pipeline import Pipeline
from steps import (
    LoadCSVStep,
    CleanDataStep,
    CountRecordsStep,
)


class DecoratedPipeline:
    """
    Pipeline wrapper using reusable decorators.
    """

    def __init__(self, steps):
        self.pipeline = Pipeline(steps)

    @timeit
    @retry(max_attempts=3)
    def run(self, data):
        return self.pipeline.run(data)


pipeline = DecoratedPipeline([
    LoadCSVStep(),
    CleanDataStep(),
    CountRecordsStep(),
])


result = pipeline.run("data/sample_data.csv")

print("Pipeline Result:")
print(result)