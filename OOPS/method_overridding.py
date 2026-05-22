class Animal:
    
    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

d1 = Dog()
d1.sound()


class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def start(self):
        print("Car Started")

c1 = Car()
c1.start()


#Using the Super() with Overriding

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog Bark")

d1 = Dog()
d1.sound()
