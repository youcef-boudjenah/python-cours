text = input("Enter a paragraph:")

# Normalize text (lowercase)
normalized = text.lower()

# Split into words
words = normalized.split()

# Total counts
word_count = len(words)
char_count = len(text)

# Frequency dictionary
freq = {}


for w in words:
    if w not in freq:
        freq[w] = 1
    else:
        freq[w] += 1


print("\nTotal Words:", word_count)
print("Total Characters:", char_count)
print("\nWord Frequency:")

for word, count in freq.items():
    print(f"word : {word} , count : {count}")
