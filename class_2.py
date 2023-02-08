class Animal:
    def __init__(self, legs=4):
        self.legs = legs
        print("Animal object was created")

    def run(self):
        print("Running started")

    def count_legs(self):
        print("The number of legs is:", self.legs)

    def return_legs(self):
        return self.legs

animal = Animal()
animal.run()
animal.count_legs()
print("Number of legs:", animal.return_legs())
print("Number of legs:", animal.legs)