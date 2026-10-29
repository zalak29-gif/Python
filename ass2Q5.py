# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Remove leading and trailing spaces
print("\nOriginal Sentence:",sentence)
print("After lstrip():",sentence.lstrip())
print("After rstrip():",sentence.rstrip())
print("After strip():",sentence.strip())

# Use the cleaned sentence for further operations
sentence = sentence.strip()

# (a) Search for a substring using find() and index()
word = input("Enter a word to search: ")

print("Using find():", sentence.find(word))

if word in sentence:
    print("Using index():", sentence.index(word))
else:
    print("Word not found")

# (b) Count occurrences of a specified word
word = input("\nEnter a word to count: ")
print("Occurrences of", repr(word), ":", sentence.count(word))

# (c) Replace a word or character
old = input("\nEnter the word or character to replace: ")
new = input("Enter the replacement: ")
print("After replace():", sentence.replace(old, new))

# (d) Split the sentence and join the words
words = sentence.split()
print("\nWords after split():", words)

joined_sentence = " ".join(words)
print("Sentence after join():", joined_sentence)

# (e) Demonstrate string immutability
print("\nDemonstrating String Immutability:")
if len(sentence) > 0:
    try:
        sentence[0] = 'X'
    except TypeError as error:
        print("Error:", error)
        print("Strings are immutable; characters cannot be changed by indexing.")
else:
    print("The sentence is empty, so no character can be modified.")

# (f) Sort words alphabetically
sorted_words = sorted(words, key=str.lower)
print("\nWords in Alphabetical Order:", sorted_words)