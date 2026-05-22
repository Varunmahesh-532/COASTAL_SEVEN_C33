from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

    def move(self):
        print("Running")

d1 = Dog()

d1.sound()
d1.move()