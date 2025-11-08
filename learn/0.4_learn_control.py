# Control structures: if, else
my_string = input("Please enter a number: ")
if my_string.isdigit():
    my_integer = int(my_string)
    print(f"Your number is {my_integer}")
else:
    print(f"{my_string} is not a number!")