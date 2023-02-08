class Animal:
    def __init__(self, number_of_legs):
        self._number_of_legs = number_of_legs

    def get_leg_info(self):
        return "This animal has " + str(self._number_of_legs) + " legs."
animal = Animal(4)
print(animal.get_leg_info())

class Dog(Animal):
    def __init__(self, name, number_of_legs):
        Animal.__init__(self, number_of_legs)
        self._name = name

    def bark(self):
        print("Woof woof!")

# Create an instance of the Dog class
dog = Dog("Lollipop", 4)

# Print the name of the dog
print("Name of dog:", dog._name)

# Make the dog bark
dog.bark()

# Count the legs of the dog
print(dog.get_leg_info())