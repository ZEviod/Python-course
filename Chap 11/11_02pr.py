class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow,Bow!")

d = Dog()
d.bark()