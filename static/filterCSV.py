import csv
import json
# filter using one column
def csv_to_json(csv_file_path, json_file_path, filter_column=None, filter_value=None):
    # Read CSV file and convert to a list of dictionaries
    csv_data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Check if filtering is enabled and if the row matches the filter condition
            if filter_column is None or (filter_column in row and row[filter_column] == filter_value):
                csv_data.append(row)

    # Write JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(csv_data, json_file, indent=4)

# Example usage:
# This will filter data where the value in the 'column_name' column is 'desired_value'
#csv_to_json('styles.csv', 'women.json', filter_column='gender', filter_value='Women')
        
import csv
import json

def csv_to_json(csv_file_path, json_file_path, filter_columns=None, filter_values=None):
    # Read CSV file and convert to a list of dictionaries
    csv_data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Check if filtering is enabled and if the row matches the filter conditions
            if filter_columns is None or all(row[col] == val for col, val in zip(filter_columns, filter_values)):
                csv_data.append(row)

    # Write JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(csv_data, json_file, indent=4)

# Example usage:
# This will filter data where 'gender' column is 'Men' and 'category' column is 'Apparel'
csv_to_json('styles.csv', 'men_apparel.json', filter_columns=['gender','masterCategory'], filter_values=['Men','Apparel'])

