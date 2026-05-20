people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Luna", "house": "Ravenclaw"},
]

def f(person):
    return person["house"]
people.sort(key=f)

print(people)  # [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Luna', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}]

# Using a lambda function to sort the list of people by their house
people.sort(key=lambda person: person["house"])
print(people)  # [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Luna', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}]