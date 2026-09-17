import csv


class CSVBatchIterator:
    def __init__(self, file_path, batch_size):
        self.file_path = file_path
        self.batch_size = batch_size

    def __iter__(self):
        with open(self.file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            batch = []

            for row in reader:
                batch.append(row)

                if len(batch) == self.batch_size:
                    yield batch
                    batch = []

            if batch:
                yield batch