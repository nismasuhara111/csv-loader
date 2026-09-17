# CSV Loader

A Python project demonstrating memory-efficient CSV data processing using a custom lazy iterator.

## Objective

The goal of this project is to process large CSV datasets without loading the entire dataset into memory at once.

The custom `CSVBatchIterator` reads the CSV file lazily and yields one batch of rows at a time.

## Features

- Custom CSV iterator
- Lazy data loading
- Batch processing
- Memory-efficient data handling
- Memory usage measurement using `tracemalloc`
- Automated testing using `pytest`

## Project Structure

```text
csv-loader/
├── data/
│   ├── sample_data.csv
│   ├── data_100.csv
│   └── data_10000.csv
├── scripts/
├── tests/
│   └── test_csv_iterator.py
├── csv_iterator.py
├── memory_test.py
├── requirements.txt
├── README.md
└── .gitignore