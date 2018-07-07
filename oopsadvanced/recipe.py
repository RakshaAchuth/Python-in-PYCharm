
from abc import ABC,abstractmethod


class AbstractRecipe(ABC):

    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def recipe(self): pass


    @abstractmethod
    def cleanup(self): pass

class Recipe1(AbstractRecipe):


    def prepare(self):
         print('dishes')

    def recipe(self):
         print('reci')

    def cleanup(self): pass


Recipe1().execute()



class MicrowaveRecipe1(AbstractRecipe):


    def prepare(self):
         print('dishes')

    def recipe(self):
         print('reci')

    def cleanup(self):
         print('clean microwave')


MicrowaveRecipe1().execute()
#prepare - rawmaterials
#recipe
#cleanup