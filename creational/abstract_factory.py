import random
from abc import ABCMeta, abstractstaticmethod

class ITable(metaclass=ABCMeta):
    @abstractstaticmethod
    def dimensions():
        """Table interface"""

class TableFactory:

    @staticmethod
    def get_table(furniture):
        if furniture == "SmallTable":
            return SmallTable()
        else:
            return BigTable()

class BigTable(ITable):
    def dimensions(self):
        return "80x80"

class SmallTable(ITable):
    def dimensions(self):
        return "40x40"

class IChair(metaclass=ABCMeta):
    @abstractstaticmethod
    def dimensions():
        """Chair interface"""

class ChairFactory:
    @staticmethod
    def get_chair(furniture):
        if furniture == "BigChair":
            return BigChair()
        else:
            return SmallChair()

class BigChair(IChair):
    def dimensions(self):
        return "80x80"

class SmallChair(IChair):
    def dimensions(self):
        return "40x40"

class IFurnitureFactory(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_furniture():
        """Returns a furniture"""

class FurnitureFactory(IFurnitureFactory):
    
    @staticmethod
    def get_furniture(furniture):
        try:
            if "Chair" in furniture:
                return ChairFactory().get_chair(furniture)
            elif "Table" in furniture:
                return TableFactory().get_table(furniture)
            else:
                raise AssertionError("No Furniture Factory Found")
        except AssertionError as e:
            print(e)

if __name__ == "__main__": 
  
    furniture = FurnitureFactory().get_furniture("SmallChair") 