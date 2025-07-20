class Human:
    def __init__(self, name, age=0):
        self._internal_name = name
        self.age = age
    
    def increment_age(self):
        print(self._internal_name)
        self.age += 1
    
    def __str__(self):
        return f"{self._internal_name} is {self.age} y.o."
    
# Methods with underscore in them behave exactly like regular methods
# Sometimes they get automatically called by Python
# # a.increment_age

# BUG definition: something does not work as expected.
# Debugger

for num in [1,2,3,4]:
    if num % 2 != 0:
        print(num)

# print(a)
a = Human("Osman")
a.__str__()

Human.__str__(a)

# TODO Inheritance
# class Human
# class Manager

# every manager is a human: True
# is every human a manager?: False

# Every manager will have the same attributes as a Human
# Not every human will have the same attributes as a manager.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def foo(self):
        print("Human1 foo")

class Human2:
    def __init__(self):
        pass

    def dummy(self):
        print("Human2 dummy")

    def foo(self):
        print("Human2 foo")

class Manager(Human, Human2):
    def __init__(self, name, salary, age):
        self.salary = salary
        super().__init__(name, age)
        
    # def boo(self):
    #     super().foo()

    def foo(self):
        super().dummy()
        super().foo()
        # Human.foo(self)
        print("Bye")

m = Manager("Stewart", 100, 47)
m.foo()
print(m)
# Manager is a child class
# Human is a parent class

a = Human("Osman", 24)
# a.foo()
# print(a)

# 1. Human is parent, manager child.
# 

# print(m.salary)
# print(m.name)

# Front end and back end
# Class design question

# Concept of inheritance A B. B has all the same attributes as A.

# Front-end
# *********
# *       *
# *       *
# *       *
# *       *
# *********


# Back-end
# *********
# *       *
# *       *
# *       *
# *       *
# *********

# Calculator
# It was taking an input from the console
# input("Please enter num1")