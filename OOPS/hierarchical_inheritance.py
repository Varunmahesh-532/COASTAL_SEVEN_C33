class Vehicle:

    def start(self):
        print("Vehicle Started")
    
class Car(Vehicle):
    
    def drive(self):
        print("Car Driving")

class Bike(Vehicle):

    def ride(self):
        print("Bike riding")

c1 = Car()
b1 = Bike()

c1.start()
c1.drive()

b1.start()
b1.ride()