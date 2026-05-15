x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")


# This code will raise a ZeroDivisionError if y is zero, and a ValueError if the user enters a non-integer value for x or y. We can use a try-except block to handle these exceptions and provide a more user-friendly error message.

import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("You can't divide by zero!")
    sys.exit(1)
except ValueError:
    print("You must enter a valid integer!")
    sys.exit(1)

print(f"{x} / {y} = {result}")
