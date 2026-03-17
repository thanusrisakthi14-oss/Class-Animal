# Write a program to implement abstraction on animal class (base class).
#  The abstract method will be move will display what subclasses can do.
#  Subclasses can be something like - Human, Dog.

from abc import ABC

class animal(ABC):
    def move(self):
        pass

class Dog(animal):
    def move(self):
        print("Dog barks")

class human(animal):
    def move(self):
        print("Human Walk")

ob1=Dog()
ob1.move()
ob2=human()
ob2.move()