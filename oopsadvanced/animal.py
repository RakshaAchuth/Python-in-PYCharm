from abc import ABC, abstractmethod

class AbstractAnimal:
    #abstract
    @abstractmethod
    def bark(self): pass

class Dog(AbstractAnimal):
    def bark(self):
        print("bow bow")

print(Dog().bark())