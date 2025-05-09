# Parent class
class Animal:             
    def __init__(self):
        self.eyes = 2
        self.legs = 4
    def breathing(self):
        print("Breathing")

# Child class
class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swimming(self):
        print("swimming")
    def breathing(self):
        super().breathing() # Calls all the functionality from the parent class
        print("breathes under water")


fish = Fish()
fish.swimming()
fish.breathing()
print(fish.eyes)