from resource_manager import managed_file


print("Normal file operation:")

with managed_file("data/sample_data.csv", "r") as file:
    first_line = file.readline()
    print("First line:", first_line.strip())


print("\nTesting cleanup after exception:")

try:
    with managed_file("data/sample_data.csv", "r") as file:
        print("Reading file...")
        raise ValueError("Something went wrong while processing the file")

except ValueError as error:
    print("Caught error:", error)