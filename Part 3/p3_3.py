import json
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

def modify_size():
    global data
    for record in data:
        record['size'] = 42

# Measure processing time for the first 1000 records 1000 times
file_path = "Part 2/large-file.json"  # Adjust the file path as needed
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    data_copy = data[:1000]  # Extract the first 1000 records for processing

def measure_time():
    global data
    data = data_copy  # Restore the data to the first 1000 records for each repetition
    return timeit.timeit(modify_size, number=1)

timings = [measure_time() for _ in range(1000)]

# Plot a histogram of the measured times
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(timings, edgecolor='k', alpha=0.7)
ax.set_xlabel("Processing Time (seconds)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Processing Times (First 1000 Records)")

# Save the histogram plot to a file
plt.savefig("output.3.3.png")
plt.show()
