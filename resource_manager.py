from contextlib import contextmanager


@contextmanager
def managed_file(file_path, mode="r"):
    """
    Opens a file and guarantees that it is closed
    when the operation finishes, even if an exception occurs.
    """

    file = None

    try:
        file = open(file_path, mode, newline="", encoding="utf-8")
        print(f"Opened file: {file_path}")

        yield file

    finally:
        if file is not None:
            file.close()
            print(f"Closed file: {file_path}")