file_path = 'your_text_file.txt'  
with open(file_path, 'r') as file:
    text = file.read()

start_line = "CHAPTER 1. Loomings."
start_index = text.find(start_line)
if start_index != -1:
    relevant_text = text[start_index:]
    words = relevant_text.split()
    vowel_count = sum(char.lower() in "aeiouy" for word in words for char in word)
    average_vowels = vowel_count / len(words) if words else 0
    print("Average number of vowels per word:", average_vowels)
else:
    print("Start line not found in the text.")
