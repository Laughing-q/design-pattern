from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color) -> None:
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        # 长方形逻辑
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        # 圆形逻辑
        self.color.paint(self)


class Line(Shape):
    name = "直线"

    def draw(self):
        # 直线逻辑
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print(f"Red {shape.name}")


class Green(Color):
    def paint(self, shape):
        print(f"Green {shape.name}")


class Blue(Color):
    def paint(self, shape):
        print(f"Blue {shape.name}")


shape = Line(Red())
shape.draw()

shape2 = Circle(Blue())
shape2.draw()
