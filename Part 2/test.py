# Define the file path
file_path = 'Part 2/pg2701.txt'

# Function to count vowels in a word
def count_vowels(word):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Read the file and store each line in an array
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Flag to start counting
start_counting = False
word_count = 0
vowel_count = 0

# Iterate over the lines to count vowels
for line in lines:
    # Check if the line marks the starting point for counting
    if "CHAPTER 1. Loomings." in line or "Part 2.2. - Continued" in line:
        start_counting = True

    # Start counting vowels after the designated line
    if start_counting:
        # Split the line into words
        words = line.split()
        for word in words:
            word_count += 1
            vowel_count += count_vowels(word)

# Calculate the average number of vowels per word
if word_count > 0:
    average_vowels_per_word = round(vowel_count / word_count)
    print("Average number of vowels per word:", average_vowels_per_word)
else:
    print("No words found to count.")
