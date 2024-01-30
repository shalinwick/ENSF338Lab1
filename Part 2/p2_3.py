import json

# Load the JSON file
file_path = "Part 2/large-file.json"

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Change the size field in every record to 42
for record in data:
    record['size'] = 42

# Write back the result in reverse order to a new JSON file
output_data = data[::-1]  # Reverse the list

output_file_path = "output.2.3.json"

with open(output_file_path, 'w') as output_file:
    json.dump(output_data, output_file, indent=4)

print("Output file 'output.2.3.json' has been generated with modified data.")
