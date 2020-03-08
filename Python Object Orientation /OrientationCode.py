# OBJECT ORIENTED PROGRAMMING


# INHERITANCE EXAMPLE CODE


class Polygon:
    width_ = None
    height_ = None

    def set_values(self, width, height):
        self.width_ = width
        self.height_ = height


class Rectangle(Polygon):
    def area(self):
        return self.width_ * self.height_


class Triangle(Polygon):
    def area(self):
        return self.width_ * self.height_ / 2


# ENCAPSULATION EXAMPLE CODE
class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value


audi = Car(200, 'red')
honda = Car(250, 'white')
audi.set_speed(400)

# ABSTRACT EXAMPLE CODE
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Square(Shape, ABC):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


# POLYMORPHISM EXAMPLE CODE OVERWRITING VARIABLE
class Parent:
    name = "Bob"


class Child(Parent):
    pass


obj = Child()
