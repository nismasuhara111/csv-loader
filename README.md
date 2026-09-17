# CSV Loader

A Python project demonstrating memory-efficient CSV data processing and
object-oriented pipeline design.

## Objective

The project demonstrates how to process CSV datasets efficiently using
lazy loading, batch processing, and a reusable pipeline architecture.

The project was developed as part of an AI/ML learning track, focusing on
memory-efficient data handling and object-oriented programming for data
pipelines.

## Features

- Custom CSV iterator
- Lazy data loading
- Batch processing
- Memory-efficient data handling
- Memory usage measurement using `tracemalloc`
- Abstract base classes
- Composition over inheritance
- Interchangeable pipeline steps
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
│   ├── test_csv_iterator.py
│   └── test_pipeline.py
├── csv_iterator.py
├── memory_test.py
├── pipeline.py
├── steps.py
├── pipeline_demo.py
├── requirements.txt
├── README.md
└── .gitignore