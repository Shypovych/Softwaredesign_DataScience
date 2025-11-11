# b4 module
import copy

list1 = [[1, 2, 3], [4, 5, 6], ["a", "b", "c"], 2]
list2 = list1                     
list3 = copy.copy(list1)           # shallow copy (same inner objects)
list4 = copy.deepcopy(list1)       # deep copy (independent clone)

print("List # \tID\t\tEntries")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)

# modify outer element
list1[3] = -2

print("\nAfter list1[3] = -2:")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)

# modify inner element
list2[2][2] = 9

print("\nAfter list2[2][2] = 9:")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)

# append new element
list1.append([0, 8, 15])

print("\nAfter list1.append([0, 8, 15]):")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)