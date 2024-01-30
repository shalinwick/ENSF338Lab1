def count_vowels(word):
    vowels = "aeiouy"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

def main():
    # Read the text from the file
    with open("Part 2/pg2701.txt", "r") as file:
        text = file.read()

    words = text.split()
    
    total_vowels = 0
    total_words = len(words)
    
    for word in words:
        total_vowels += count_vowels(word)
    
    if total_words > 0:
        average_vowels_per_word = total_vowels / total_words
    else:
        average_vowels_per_word = 0
    
    print("Average number of vowels per word:", average_vowels_per_word)

if __name__ == "__main__":
    main()
