# Using classes to create a Point object with x and y coordinates, and a method to move the point by a certain amount
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(2, 8)
print(p)  # (2, 8)
print(p.x)  # 2
print(p.y)  # 8

# Using classes to create a Flight object with a capacity and a list of passengers, and methods to add passengers and check for open seats
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")