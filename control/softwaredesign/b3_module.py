# b3 module
for i in range(1, 101):                 # numbers 1 to 100 inclusive
    output = f"{i}"                     # start with the number itself
    if i % 3 == 0: output += "-Fizz"    # add Fizz if multiple of 3
    if i % 5 == 0: output += "-Buzz"    # add Buzz if multiple of 5
    print(output)                     