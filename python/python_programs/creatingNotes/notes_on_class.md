# Classes in Python
=====================================

## Introduction
------------

In Python, a class is a template for creating objects. Classes define a set of attributes (data) and methods (functions) that can be used to manipulate and interact with objects created from the class.

## Defining a Class
-----------------

A class is defined using the `class` keyword followed by the name of the class. The class definition is typically indented under the class name.

```python
class MyClass:
    pass
```

## Class Attributes
-----------------

Class attributes are variables that are shared by all instances of a class. They are defined inside the class definition and are accessed using the class name.

```python
class MyClass:
    class_attribute = "I'm a class attribute"

print(MyClass.class_attribute)  # Output: I'm a class attribute
```

## Instance Attributes
--------------------

Instance attributes are variables that are unique to each instance of a class. They are defined inside the `__init__` method, which is a special method that is called when an object is created from the class.

```python
class MyClass:
    def __init__(self, name):
        self.instance_attribute = name

obj = MyClass("John")
print(obj.instance_attribute)  # Output: John
```

## Methods
---------

Methods are functions that are defined inside a class. They can be used to perform actions on objects created from the class.

```python
class MyClass:
    def __init__(self, name):
        self.instance_attribute = name

    def greet(self):
        print(f"Hello, my name is {self.instance_attribute}!")

obj = MyClass("John")
obj.greet()  # Output: Hello, my name is John!
```

## Inheritance
-------------

Inheritance is a mechanism that allows one class to inherit the attributes and methods of another class. The child class inherits all the attributes and methods of the parent class and can also add new attributes and methods or override the ones inherited from the parent class.

```python
class ParentClass:
    def __init__(self, name):
        self.instance_attribute = name

    def greet(self):
        print(f"Hello, my name is {self.instance_attribute}!")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"I'm {self.age} years old.")

obj = ChildClass("John", 30)
obj.greet()
# Output:
# Hello, my name is John!
# I'm 30 years old.
```

## Encapsulation
--------------

Encapsulation is a mechanism that allows an object to hide its internal state and behavior from the outside world. This is achieved by using access modifiers such as `public`, `private`, and `protected`.

```python
class MyClass:
    def __init__(self, name):
        self.__private_attribute = name

    def get_private_attribute(self):
        return self.__private_attribute

obj = MyClass("John")
print(obj.get_private_attribute())  # Output: John
# print(obj.__private_attribute)  # This will raise an AttributeError
```

## Polymorphism
--------------

Polymorphism is a mechanism that allows objects of different classes to be treated as objects of a common superclass. This is achieved by using method overriding or method overloading.

```python
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(4), Circle(5)]
for shape in shapes:
    print(shape.area())
# Output:
# 16
# 78.5
```