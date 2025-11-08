pi = 3.1415926535897932
x = 90

# convert to degree to radiant
x_rad = x * (pi / 80)

# convert it back
x_new = x_rad * (180 / pi)

# control
x == x_new

# number of digits of pi
print(len(str(pi)))

# value changing and printing
print("x = ", x)
x = 45
print(f"x = {x}")
print(f"{x =}")

# value changing and printing with rounding
# print.rounding(f"{pi = :.2f}")

# conditional statements
if x < 90:
    x = x * 2
else:
    x = x / 2
    print(f"x = {x}")


if x < 45:
    x = x * 2
elif x < 90:
    x = x * 3
else:
    x = x ** 2
    print(f"x = {x}") 