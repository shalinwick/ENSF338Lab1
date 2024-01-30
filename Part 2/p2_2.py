import numpy as np

def count_vowels(word):
    vowels = "aeiouy"
    return sum(letter in vowels for letter in word.lower())

with open('Part 2/pg2701.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
start_index = lines.index("CHAPTER 1. Loomings." + '\n')
lines = lines[start_index:]
lines = [line.strip() for line in lines]
arr1 = np.array(lines)

total_num_of_vowels = 0
total_num_of_words = 0

for line in arr1:
    words = line.split()
    total_num_of_words += len(words)
    total_num_of_vowels += sum(count_vowels(word) for word in words)

average_vowels = round(total_num_of_vowels / total_num_of_words )
print(f"Average number of vowels per word: {average_vowels}")