file_path = 'Part 2/pg2701.txt'  
with open(file_path, 'r', encoding ='utf-8') as file:
    text = file.read()

    

start_index = text.find("CHAPTER 1. Loomings.")
text = text[start_index:]
words = text.split()
total_vowels = sum(char.lower() in "aeiouy" for word in words for char in word)
average_vowels = round(total_vowels / len(words) )
print("Average number of vowels per word:", average_vowels)
