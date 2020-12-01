from abc import ABCMeta, abstractstaticmethod

class IShape(metaclass=ABCMeta):

    @abstractstaticmethod
    def draw():
        """Shape interface"""

class Rectangle(IShape):

    def __init__(self):
        self.height = 80
        self.width = 100
    
    def draw(self):
        return "Drawing rectangle"


class Circle(IShape):

    def __init__(self):
        self.height = self.width = 80
    
    def draw(self):
        return "Drawing circle"
        
class ShapeFactory():

    @staticmethod
    def draw_shape(shapetype):
        shapes = dict(Rectangle= Rectangle(), Circle=Circle())
        shape = shapes[shapetype]
        shape.draw()


if __name__ == "__main__":
    ShapeFactory.draw_shape("Rectangle")