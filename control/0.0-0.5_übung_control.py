list1 = list(range(1, 6))  # create a list from 1 to 5
list2 = list(range(11, 16))  # create a list from 11 to 15

list_zip = []  # create an empty list
for i in range(len(list1)):  # iterate over the indices of the list
    list_zip.append(list1[i])  # append elements from the first list
    list_zip.append(list2[i])  # append elements from the second list

list_odd = []  # create an empty list
for i in list1 + list2:  # iterate through the combined list
    if i % 2 == 1:  # check if the number is odd
        list_odd.append(i)  # add the odd number to the list

list_zip_reverse = []  # create an empty list
for i in range(len(list1) - 1, -1, -1):  # iterate over the indices in reverse order
    list_zip_reverse.append(list1[i])  # append elements from the first list
    list_zip_reverse.append(list2[i])  # append elements from the second list

print(f"list_zip: {list_zip}")
print(f"list_odd: {list_odd}")
print(f"list_zip_reverse: {list_zip_reverse}")
