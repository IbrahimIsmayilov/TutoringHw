# count = 0

# def my_decorator(func):
#     print("hi")

#     def wrapper(*args):
#         args = (17,)
#         global count
#         count += 1
#         print("Before function execution")
#         dummy(*args)
#         print("After function execution")
#         return "Osman"
    
#     return wrapper

# @my_decorator
# def foo(num, num2):
#     print(num)

# @my_decorator
# def dummy(num1):
#     return 18

# foo(20, 10)
# dummy(17)

# @my_decorator
# def boo(dummy):
#     return 17


# def zoo(a):
#     return 5

# zoo(7)
# foo(20)
# foo(174)
# boo(75)
# foo(5)
# print(f"Count is: {count}")


# print(wrapper(20))

# foo = foo
# print(foo)

# for num in [10, 20]:
#     # num = 10
    



# def boo():
#     def doo():
#         return 20
#     a = doo()
#     print(a)
#     return 17

# def boo():
#     return 17
# z = boo
# z()
# # doo()
# print(boo())

# boo = boo

# boo = 15
# print(boo())
# boo = 10
# boo = "Osman"
# print(boo)
# boo2 = 15
# print(boo2())

# TODO classes in Python


# Primitive date types
# int, bool, str, list, set, tuple


# 1. How to create our own data types?
# 2. Why and when to create our own data types?

# class Human:
    
#     # Init method
#     def __init__(self, name, age):
#         # Fields of the class instance
#         self.name = name
#         self.age = age
#         self.height = 186
    
    
    
# lst = []

# Human class object/variable. 
# An instance of class Human
# Variable h1 is an instance of class Human

# We refer to class functions as methods
# lst = []


# When we call __init__ method, we return the self parameter
# h1 = Human("Osman", 24)
# print(h1.name)
# h1.name = "Turan"
# print(h1.name)
# h1.height = 5
# print(h1.height)
# # print(h1.name)
# # print(h1.age)
# # print(h1.height)

# h2 = Human("Leyla", 77)
# print(h2.height)
# print(h2.name)
# lst.append()

class Human:
    
    # Init method
    def __init__(self, name, age):
        # Fields of the class instance
        self.name = name
        self.age = age
        self.height = 186
        
    def make_older(self, age_to_add) -> int:
        self.age = self.age + age_to_add
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    # def __lt__(self, other)

lst = []
# print()
# lst.append()

h1 = Human("Osman", 24)
print(h1)

# print(h1.make_older(27))
# print(h1.age)