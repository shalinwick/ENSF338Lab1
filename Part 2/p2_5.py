import json
import timeit


def alter_size():
    
    global data

    for record in data:
        
        record['size'] = 42


file_path = "large-file.json"

with open(file_path, 'r', encoding='utf-8') as file:
    
    data = json.load(file)


time_measured = timeit.timeit(alter_size, number=10) 


calculate_average_time = time_measured / 10

print("Average time taken to change the size across 10 iterations is:", calculate_average_time, "seconds")
