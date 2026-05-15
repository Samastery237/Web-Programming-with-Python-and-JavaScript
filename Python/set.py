#Create an empty set
s = set()

# Adding elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)  # {1, 2, 3, 4, 5}

# removing an element from the set
s.remove(3)

print(s)  # {1, 2, 4, 5}

# checking if an element is in the set
print(3 in s)  # False
print(f"The set has {len(s)} elements") # The set has 4 elements    