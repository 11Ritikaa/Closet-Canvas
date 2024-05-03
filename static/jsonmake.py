import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read CSV file and convert to a list of dictionaries
    csv_data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            csv_data.append(row)

    # Write JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(csv_data, json_file, indent=4)

# Example usage:
csv_to_json('styles.csv', 'style.json')
