import json
import timeit

# Define the function to modify the size value in each record
def modify_size():
    global data
    for record in data:
        record['size'] = 42

# Load the JSON file
file_path = "Part 2/large-file.json"

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Time the modification operation
time_taken = timeit.timeit(modify_size, number=10)  # Run 10 repetitions

# Calculate the average time across the 10 repetitions
average_time = time_taken / 10

print("Average time taken to modify the size value across 10 repetitions:", average_time, "seconds")
