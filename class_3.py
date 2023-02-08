class Animal:
    def __init__(self, number_of_legs):
        self._number_of_legs = number_of_legs

    def get_leg_info(self):
        return "This animal has " + str(self._number_of_legs) + " legs."
animal = Animal(4)
print(animal.get_leg_info())
