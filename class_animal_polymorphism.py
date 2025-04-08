class Animal:
    def move(self):
        print("This animal moves in some way.")

class Bird(Animal):
    def move(self):
        print("Flying ✈️")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

class Dog(Animal):
    def move(self):
        print("Running 🐕")
#usage
animals = [Bird(), Fish(), Dog()]

for animal in animals:
    animal.move()
