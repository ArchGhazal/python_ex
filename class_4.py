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

dog = Dog("Lollipop", 4)
print("Name of dog:", dog._name)
dog.bark()
print(dog.get_leg_info())