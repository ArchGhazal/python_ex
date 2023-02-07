class Animal:
    def __init__(self, legs=4):
        self.legs = legs
        print("Animal object was created")

    def run(self):
        print("Running started")

    def count_legs(self):
        print(f"the animal has {self.legs} legs")

animal = Animal()
animal.run()
animal.count_legs()