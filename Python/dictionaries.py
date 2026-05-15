houses = {"Harry": "Gryffindor", "Draco": "Slytherin", "Luna": "Ravenclaw", "Cedric": "Hufflepuff"}

houses["Hermione"] = "Gryffindor"

# First: Accessing values in a dictionary using keys
print(houses)  # {'Harry': 'Gryffindor', 'Draco': 'Slytherin', 'Luna': 'Ravenclaw', 'Cedric': 'Hufflepuff'}
print(houses["Harry"])  # Gryffindor

# Second: Adding a new key-value pair to the dictionary and accessing the value using the new key
print(houses["Hermione"])  # Gryffindor