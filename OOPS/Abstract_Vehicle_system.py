from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass

class Bike(Vehicle):

    def fuel_type(self):
        print("Petrol")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Battery")


b1 = Bike()
e1 = ElectricCar()

b1.fuel_type()
e1.fuel_type()

