# import from functions.py
from functions import square
for i in range(10):
    print(f"the square of {i} is {square(i)}")

# Another way to import from functions.py
import functions
for i in range(10):
    print(f"the square of {i} is {functions.square(i)}")