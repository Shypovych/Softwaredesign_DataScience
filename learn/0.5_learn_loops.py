# average calculation
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0 
for i in integers:
    total = total + i
mean = total / len(integers)
print(f"mean: {mean}")

# even und odd counting
odd = 0
even = 0
for i in integers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f"odd: {odd}, even: {even}")

# exponentiation calculation 1
a = 5 # скільки разів множимо
b = 2 # число, яке множимо
c = 1 # початковий результат
while a > 0:
    a = a - 1
    c = c * b
print(f"b^5 = {c}")

# exponentiation calculation 2
import math
mean = math.fsum(integers) / len(integers)
print(f"mean: {mean}")

c = math.pow(2, 5)
print(f"2^5 = {c}")