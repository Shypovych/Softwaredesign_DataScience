# b2 module
list1 = list(range(1, 6))  
list2 = list(range(11, 16))  

list_zip = []              
for i in range(len(list1)):  # iterate over the indices of the list
    list_zip.append(list1[i])  # append elements from the first list
    list_zip.append(list2[i])  # append elements from the second list

list_odd = []  
for i in list1 + list2:  # iterate through the combined list
    if i % 2 == 1:  # check if the number is odd
        list_odd.append(i)  # add the odd number to the list

list_zip_reverse = []  
for i in range(len(list1) - 1, -1, -1):  # iterate over the indices in reverse order
    list_zip_reverse.append(list1[i])  # append elements from the first list
    list_zip_reverse.append(list2[i])  # append elements from the second list

print(f"list_zip: {list_zip}")
print(f"list_odd: {list_odd}")
print(f"list_zip_reverse: {list_zip_reverse}")