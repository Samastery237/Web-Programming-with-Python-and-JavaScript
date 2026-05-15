people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Luna", "house": "Ravenclaw"},
]

# Using a lambda function to sort the list of people by their house

def f(person):
    return person["house"]
people.sort(key=f)

print(people)  # [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Luna', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}]