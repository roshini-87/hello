import re

def LongestWord(sen):
    # Remove punctuation and numbers, keeping only letters and spaces
    sen = re.sub(r'[^a-zA-Z\s]', '', sen)
    
    words = sen.split()

    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word

sen = input()
result = LongestWord(sen)
print("Longest word:", result)
