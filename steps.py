import csv

from pipeline import Step


class LoadCSVStep(Step):
    """
    Loads records from a CSV file.
    """

    def run(self, data):
        file_path = data

        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            records = list(reader)

        return records


class CleanDataStep(Step):
    """
    Removes empty rows and whitespace from CSV values.
    """

    def run(self, data):
        cleaned_data = []

        for row in data:
            cleaned_row = {
                key: value.strip() if isinstance(value, str) else value
                for key, value in row.items()
            }

            if any(value for value in cleaned_row.values()):
                cleaned_data.append(cleaned_row)

        return cleaned_data


class CountRecordsStep(Step):
    """
    Counts the number of records.
    """

    def run(self, data):
        return {
            "record_count": len(data)
        }


class UppercaseDataStep(Step):
    """
    Alternative transformation step.
    Converts text values to uppercase.
    """

    def run(self, data):
        uppercase_data = []

        for row in data:
            uppercase_row = {
                key: value.upper() if isinstance(value, str) else value
                for key, value in row.items()
            }

            uppercase_data.append(uppercase_row)

        return uppercase_data