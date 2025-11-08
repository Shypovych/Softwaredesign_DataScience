element0 = "chery"
element1 = "apple"
element2 = "banana"
element3 = "kiwi"
element4 = "mango"
element5 = "orange"

# grouping elements in a list
my_fruits = [element0, element1, element2, element3, element4, element5]

# adding new elements
my_fruits.append("pear")

# changing value (banana>grape)
my_fruits[2] = "grape"
my_fruits[2], my_fruits[4] = my_fruits[4], my_fruits[2]

# removing elements
my_fruits.pop(4)
print(f"my_fruits: {my_fruits}")