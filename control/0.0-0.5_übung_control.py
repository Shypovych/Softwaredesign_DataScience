list1 = list(range(1, 6)) # створюємо список від 1 до 5
list2 = list(range(11, 16)) # створюємо список від 11 до 15

list_zip = [] # створюємо порожній список
for i in range(len(list1)): # ітеруємося по індексах списку
    list_zip.append(list1[i]) # додаємо кортежі з елементів обох списків
    list_zip.append(list2[i]) # додаємо кортежі з елементів обох списків

list_odd = [] # створюємо порожній список
for i in list1 + list2: # ітеруємося по об'єднаному списку
    if i % 2 == 1: # перевіряємо, чи є число непарним
        list_odd.append(i) # додаємо непарне число до списку

list_zip_reverse = [] # створюємо порожній список
for i in range(len(list1)-1, -1, -1): # ітеруємося по індексах списку у зворотньому порядку
    list_zip_reverse.append(list1[i]) # додаємо кортежі з елементів обох списків
    list_zip_reverse.append(list2[i]) # додаємо кортежі з елементів обох списків

print(f"list_zip: {list_zip}")
print(f"list_odd: {list_odd}")
print(f"list_zip_reverse: {list_zip_reverse}")  