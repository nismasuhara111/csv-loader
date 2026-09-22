from functools import lru_cache


@lru_cache(maxsize=3)
def get_file_size(file_path):
    """
    Returns the size of a file in bytes.
    The result is cached for repeated calls.
    """

    print(f"Reading file information: {file_path}")

    with open(file_path, "rb") as file:
        file.seek(0, 2)
        return file.tell()


file_path = "data/sample_data.csv"


print("First call:")
print(get_file_size(file_path))

print("\nSecond call:")
print(get_file_size(file_path))

print("\nCache information:")
print(get_file_size.cache_info())