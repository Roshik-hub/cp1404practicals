"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

# Ask the user for a string of text
text = input("Text: ")

# Create an empty dictionary to count words
word_to_count = {}

# Split text into words and count occurrences
for word in text.split():
    word = word.lower()  # make it case-insensitive
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# Find the length of the longest word
max_length = max(len(word) for word in word_to_count)

# Print sorted results neatly aligned
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
