# b11 module
# Loop with key, value pair and index-value enumeration

# b11.1 Loop through dictionary from B.10 
roman_values = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400,
    "C": 100, "XC": 90, "L": 50, "XL": 40,
    "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
}

print("------------- Roman dictionary keys and values:") 
for key, value in roman_values.items():       # extract key and value directly
    print(f"Roman: {key:>2} → Arabic: {value}")

# b11.2 Enumerate list with index and value ---
print("\n-------------Enumerating a list:")
words = ["first", "second", "third"]
for index, value in enumerate(words):         # enumerate gives both index and item
    print(f"index = {index}, value = '{value}'")