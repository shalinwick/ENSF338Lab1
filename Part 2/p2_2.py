import numpy as np

def read_from_chapter(file_path, start_line):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    start_index = lines.index(start_line + '\n')
    lines = lines[start_index:]
    lines = [line.strip() for line in lines]
    return np.array(lines)

def count_vowels(word):
    vowels = "aeiouy"
    return sum(letter in vowels for letter in word.lower())

total_vowels = 0
total_words = 0

file_path = 'Part 2/pg2701.txt'
start_line = "CHAPTER 1. Loomings."
lines_array = read_from_chapter(file_path, start_line)

for line in lines_array:
    words = line.split()
    total_words += len(words)
    total_vowels += sum(count_vowels(word) for word in words)

average_vowels = round(total_vowels / total_words if total_words else 0)
print(f"Average number of vowels per word: {average_vowels}")