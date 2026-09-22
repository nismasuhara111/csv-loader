import time
from functools import wraps


def timeit(func):
    """
    Measures and prints the execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(f"{func.__name__} took {elapsed_time:.6f} seconds")

        return result

    return wrapper


def retry(max_attempts=3):
    """
    Retries a function when it raises an exception.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception as error:
                    last_error = error

                    print(
                        f"{func.__name__} failed "
                        f"(attempt {attempt}/{max_attempts})"
                    )

            raise last_error

        return wrapper

    return decorator