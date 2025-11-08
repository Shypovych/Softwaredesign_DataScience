# list of integers
my_list = [1, 3, 12, 7, 9, 11, 15]

# changing value (7>-6)
my_list[3] = -6

# max, min, sum value
print(f"max: {max(my_list)}")
print(f"min: {min(my_list)}")
print(f"sum: {sum(my_list)}")

# sorting/reverse
print(f"sort: {my_list.sort()}")
print(f"sortrevers: {my_list.reverse()}")

# slicing
print(f"slice[0:4]: {my_list[0:4]}")
print(f"slece[5:]: {my_list[5:]}")

# new list with range
my_list1 = my_list[0:4]
my_list2 = my_list[5:]
print(f"my_list1: {my_list1}")
print(f"my_list2: {my_list2}")

# range function
my_list3 = list(range(0, 21, 2))
print(f"my_list3: {my_list3}")