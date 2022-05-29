from abc import ABCMeta, abstractmethod


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a) -> None:
        self.a = a

a = MyClass(10)
b = MyClass(20)
print(a.a, b.a)
print(id(a), id(b))
