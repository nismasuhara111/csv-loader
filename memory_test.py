import tracemalloc
from csv_iterator import CSVBatchIterator


def create_csv(file_path, rows):
    with open(file_path, "w") as file:
        file.write("id,name,score\n")

        for i in range(1, rows + 1):
            file.write(f"{i},Student{i},{50 + (i % 50)}\n")


def measure_memory(file_path, batch_size):
    tracemalloc.start()

    iterator = CSVBatchIterator(file_path, batch_size)

    for batch in iterator:
        pass

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return peak / 1024


# Create test datasets
create_csv("data/data_100.csv", 100)
create_csv("data/data_10000.csv", 10000)


# Measure memory usage
memory_100 = measure_memory("data/data_100.csv", batch_size=10)
memory_10000 = measure_memory("data/data_10000.csv", batch_size=10)


# Display results
print(f"100 rows    → Peak memory: {memory_100:.2f} KB")
print(f"10,000 rows → Peak memory: {memory_10000:.2f} KB")