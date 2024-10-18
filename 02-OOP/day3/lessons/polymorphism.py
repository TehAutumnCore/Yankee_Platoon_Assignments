"""
Ability of different to response to the *same* method in different ways.

-Abstract base class / abstract method
"""
# #abstract base class
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod #enforces every class must have speak class
#     def speak(self):
#         pass
        
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# class Duck(Animal):
#     def speak(self):
#         print("Why, oh why must i quack")
#         return "Quack!"

# donald = Duck()
# garfield = Cat()
# lassie = Dog()
# clifford = Dog()

# my_animals = [donald,garfield,lassie,clifford]
# for animal in my_animals:
#     print(animal.speak())

from abc import ABC, abstractmethod
import math



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    PI = math.pi
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

print(Circle.PI)

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5

my_circle = Circle(5)
my_triangle = Triangle(5,4)
my_rectangle = Rectangle(4,4)
print(my_circle.area())

for a_shape in [my_circle,my_triangle,my_rectangle]:
    print(a_shape.area())