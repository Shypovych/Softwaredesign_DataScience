# b7 module

# b7.1 module — Function "greet" with default value "Hi" for greeting
def greet(person, greeting="Hi"):
    print(f"{greeting} {person}!")

# b7.2 module — Calls
greet("Peter")                                   # uses default "Hi"
greet(person="Peter", greeting="Hi")             # explicit arguments
greet(greeting="Hi", person="Peter")             # order swapped — same result
# All three print "Hi Peter!" — demonstrates that default values and keyword argument order both work.


# b7.3 module — Function "add_item" showing problem with mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))     # ['apple']
print(add_item("banana"))    # ['apple', 'banana'] ← same list reused — unexpected behaviour


# b7.4 module — Correct version of "add_item" using None as default
def add_item(item, items=None):
    if items is None:
        items = []           # new list created every time
    items.append(item)
    return items

print(add_item("apple"))     # ['apple']
print(add_item("banana"))    # ['banana']