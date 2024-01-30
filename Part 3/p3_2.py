import json
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

def modify_size():
    global data
    for record in data:
        record['size'] = 42

avgtimes = []

record_counts = [1000, 2000, 5000, 10000]
repetitions = 100

fig, ax = plt.subplots(figsize=(10, 5))

for count in record_counts:
    file_path = "Part 2/large-file.json"  # Adjust the file path as needed
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_copy = data[:count]  # Extract a subset of records for processing
        
    def measure_time():
        global data
        data = data_copy  # Restore the data to the subset for each repetition
        return timeit.timeit(modify_size, number=repetitions)

    average_time = measure_time() / repetitions
    avgtimes.append(average_time)
    print("Average time for %d records: %.6f seconds" % (count, average_time))

# Now, compute linear regression using NumPy, similar to the reference code
x = np.array(record_counts)
y = np.array(avgtimes)

mean_x = np.mean(x)
mean_y = np.mean(y)

numerator = sum((x - mean_x) * (y - mean_y))
denominator = sum((x - mean_x) ** 2)

slope = numerator / denominator
intercept = mean_y - slope * mean_x

# Calculate the line values for the linear regression line
linevalues = slope * x + intercept

# Plot the data points and the linear regression line
ax.scatter(x, y, label="Actual Data")
ax.plot(x, linevalues, 'r', label="Linear Regression")
ax.set_xlabel("Number of Records")
ax.set_ylabel("Average Processing Time (seconds)")
ax.legend()

# Print the linear relationship
print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))

# Save the plot to a file
plt.savefig("output.3.2.png")
plt.show()
