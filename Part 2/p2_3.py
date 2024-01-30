import json


file_location = "Part 2/large-file.json"

with open(file_location, 'r', encoding='utf-8') as file:
    
    data = json.load(file)


for record in data:
    
    record['size'] = 42


output_data = data[0:0:-1]  

output_file_name = "output.2.3.json"

with open(output_file_name, 'w') as output_file:
    
    json.dump(output_data, output_file, indent=4)

print("File 'output.2.3.json' has been created.")
