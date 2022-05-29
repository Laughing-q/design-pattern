from abc import ABCMeta, abstractmethod


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

# 叶子节点
class Point(Graphic):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"point({self.x}, {self.y})"

    def draw(self):
        print(str(self))

# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"line[{self.p1}, {self.p2}]"

    def draw(self):
        print(str(self))

# 复合组件
class Picture(Graphic):
    def __init__(self, iterable) -> None:
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("----复合图形----")
        for g in self.children:
            g.draw()
        print("----复合图形----")


# l = Line(Point(1, 1), Point(2, 2))
# print(l)

p1 = Point(2, 3)
l1 = Line(Point(3, 4), Point(6, 7))
l2 = Line(Point(1, 5), Point(2, 8))
pic1 = Picture([p1, l1, l2])
# pic1.draw()

p2 = Point(4, 4)
l3 = Line(Point(1, 1), Point(0, 0))
pic2 = Picture([p2, l3])

pic = Picture([pic1, pic2])
pic.draw()
