from csv_iterator import CSVBatchIterator


def test_csv_iterator_batches():
    iterator = CSVBatchIterator("data/sample_data.csv", batch_size=3)

    batches = list(iterator)

    assert len(batches) == 4
    assert len(batches[0]) == 3
    assert len(batches[1]) == 3
    assert len(batches[2]) == 3
    assert len(batches[3]) == 1