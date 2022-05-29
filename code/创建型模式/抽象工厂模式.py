"""
下面是生产厂商生产一部手机的例子：
生产一部手机如果说只需要手机壳、CPU和操作系统这三个类对象，
其中每个类对象都有不同的种类。
对每个具体工厂，分别生产一部手机需要的三个对象：
"""

from abc import abstractmethod, ABCMeta

# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    def make_cpu(self):
        pass

    def make_os(self):
        pass


# 具体产品
