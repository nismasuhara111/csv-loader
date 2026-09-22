from decorators import retry, timeit
from resource_manager import managed_file


def test_timeit():
    @timeit
    def sample_function():
        return "success"

    assert sample_function() == "success"


def test_retry():
    attempts = {"count": 0}

    @retry(max_attempts=3)
    def temporary_failure():
        attempts["count"] += 1

        if attempts["count"] < 3:
            raise ValueError("Temporary failure")

        return "success"

    assert temporary_failure() == "success"
    assert attempts["count"] == 3


def test_context_manager():
    with managed_file("data/sample_data.csv", "r") as file:
        first_line = file.readline()

    assert first_line.startswith("id")


def test_context_manager_closes_file():
    with managed_file("data/sample_data.csv", "r") as file:
        assert not file.closed

    assert file.closed