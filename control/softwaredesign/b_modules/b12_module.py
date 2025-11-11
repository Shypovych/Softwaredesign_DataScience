# b12 module
# Set, List and Dictionary Comprehensions

# b12.1 Flatten a list of tuples into one list
list_of_sets = [(1, 2, 3), (4, 5, 6), (7, 8)]
flat = [num for group in list_of_sets for num in group]
print("1.", flat)

# b12.2 Single-entry tuples
list_of_sets = [(1, 2, 3), (4, 5, 6), (7, 8), (9,)]
flat = [num for group in list_of_sets for num in group]
print("2.", flat)

# b12.3 Explicit sets
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8}, {9}]
flat = [num for group in list_of_sets for num in group]
print("3.", sorted(flat))  # sorted for consistent order

# b12.4 Using lists instead of sets
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8], [9]]
flat = [num for group in list_of_lists for num in group]
print("4.", flat)

# b12.5 Split two separate sentences into words
sentence1 = "I spy with my little eye a tricky"
sentence2 = "List and dict comprehension coming up"

words1 = sentence1.split()
words2 = sentence2.split()

print("5.1 Sentence 1 words:", words1)
print("5.2 Sentence 2 words:", words2)

# b12.6 Sets of unique word lengths for each sentence
lengths1 = {len(word) for word in words1}
lengths2 = {len(word) for word in words2}

print("6.1 Lengths (sentence 1):", lengths1)
print("6.2 Lengths (sentence 2):", lengths2)

# b12.7 Dictionaries: word length -> set of words (for each)
word_dict1 = {length: {w for w in words1 if len(w) == length} for length in lengths1}
word_dict2 = {length: {w for w in words2 if len(w) == length} for length in lengths2}

print("7.1 Dictionary (sentence 1):", word_dict1)
print("7.2 Dictionary (sentence 2):", word_dict2)

# b12.8 Combine both sentences and analyze together
all_words = words1 + words2
combined_dict = {
    length: {w for w in all_words if len(w) == length}
    for length in {len(w) for w in all_words}
}
print("8. Combined dictionary (both sentences):", combined_dict)