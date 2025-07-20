# Question (Scale)
# Write a function that takes variable number of parameters. You know that your function will be called with at least 2 parameters
# and that all parameters will be integers. Your function should multiple the first paramater with all the reamining parameters
# and find the sum of the results.
# Ex. scale(10, 2, 3) => 10 * 2 + 10 * 3 = 50
# def scale(scaling_factor, *args):
#     total = 0
#     for num in args:
#         total += scaling_factor * num
#     return total

# print(scale(10, 2, 3, 5))

# If the scaling factor is not provided, always multiple it by 5.
# def scale(num, scaling_factor=5, dummy="Osman", people=[]):
#     return num * scaling_factor

# print(scale(10))
# print(scale(2))

def scale(num, num2, scaling_factor=5, s2=[]):
    pass


lst = ["Osman"]
scale(10, 11, s2=["Osman"])

# def dummy(num1, num2):
#     print(num1)
    
# dummy(20, num1=18)


# def bio(name, age, surname, wage): # 7 more arguments
#     pass

# bio("Afandiyev", age=23, name="Osman", wage=183)

def foo(*args, **kwargs):
    # print(args)
    # print(kwargs)

    # print(*args)
    # args = ("Osman", 183)
    # print("Osman", 183)
    pass

# foo("Osman", 183, age=18, surname="Osman")
# print(5, 6)

# lst = [10, 20, 30]
# a, b = lst

# def boo(num1, num2):
#     return num1 + num2

# print(boo(*lst))

# my_param = {"name": "Osman"}
# def foo(num2, name):
#     return num2

# foo(30, name="Osman")

# We use kwargs mostly to create decorators
# Function as variable

# def foo():
#     return 30

# a = foo
# print(a)
# print(foo)

# print(a())

def decorator(func):
    print(func)
    return func


@decorator
def dummy():
    print("hey")
    return 20
# dummy = decorator(dummy)

dummy()

# def a():
#     return 5

# a = None
# a("Hi")

# def b():
#     print(5)

# name = b()