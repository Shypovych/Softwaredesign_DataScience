# b4 module
import copy

list1 = [[1, 2, 3], [4, 5, 6], ["a", "b", "c"], 2]
list2 = list1                      # assignment to same object
list3 = copy.copy(list1)           # shallow copy to new list, same inner objects
list4 = copy.deepcopy(list1)       # deep copy to full independent clone

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

# list2 — це лише інше ім’я тієї ж самої пам’яті, тому всі зміни в list1 з’являються й у list2
# list3 — shallow copy: створює новий зовнішній список, але внутрішні елементи залишаються спільними
# list4 — deep copy: повна незалежна копія, усі рівні структури дублюються в пам’яті
# Використання функції Id показує різні адреси для list1–list4, що демонструє різницю між копіюваннями