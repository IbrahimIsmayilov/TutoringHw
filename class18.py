# # class Human:
# #     def __init__(self, name, age, height):
# #         self.name = name
# #         self.age = age

# #     def __str__(self):
# #         return f"{self.name} is {self.age} years old"
    
# #     @classmethod
# #     def foo(cls):
# #         print("Hi")
    
# #     @classmethod
# #     def zoo(cls):
# #         # Human.foo()
# #         cls.foo()

# # class Manager(Human):
# #     def __init__(self, salary, *args):
# #         self.salary = salary
# #         super().__init__(*args)
        
# #     # def boo(self):
# #     #     super().foo()

# #     @classmethod
# #     def foo(cls):
# #         print("Bye")

# # Manager.foo()
# # Human.foo()

# # Human.zoo()
# # Manager.zoo()

# # # m = Manager(100, "Stewart", 199, 47)
# # # # m.foo()
# # # print(m)

# # # h = Human("Osman", 24, 186)
# # # print(h.height)

# # # # def foo(a):
# # # #     return 15

# # # # foo(20)


# class Book:
#     TOTAL_BOOK_CNT = 0
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.TOTAL_BOOK_CNT += 1
    
#     def foo(self):
#         print("Hi")
   
#     def chage_author(self, new_author):
#         self.author = new_author

#     # @classmethod
#     # def change_author(cls, new_author):
#     #     pass

#     @classmethod
#     def from_string(cls, string):
#         title, author = string.split(",")
        
#         new_book = cls(title, author)
        
#         return new_book

# # # 1. Instance methods: the mandatorly take self as a parameter
# # # 2. Class methods: THey do not need an instance to be called. They can be called purely with the name of the class.
# # # 3. Static method: Static method neither takes a cls object nor it takes an instance (self).

# # def find_area_square(side):
# #     print("bye")
# #     return side ** 2

# # def find_area_circle(side):
# #     print("bye")
# #     return side ** 2

# class Square:
#     DUMMY = 0
#     def __init__(self, side):
#         self.side = side

#     def find_area(self):
#         return self.side ** 2

#     @classmethod
#     def find_area(cls, side):
#         cls.DUMMY += 1
#         print("hi")
#         return side ** 2

#     @staticmethod
#     def find_area(side):
#         DUMMY += 1
#         print("bye")
#         return side ** 2


# # class Cicrcle:
# #     def __init__(self, radius):
# #         self.r = radius
    
# #     @staticmethod
# #     def find_area(radius):
# #         return 3.14 * (radius ** 2)

# # s = Square(10)
# # print(s.find_area())

# # print(Square.find_area(20))

# # Cicrcle.find_area(15)
# Square.find_area(30)


# # b = Book("zoo", "Osman")


# # # b.foo()
# # # Book.foo(b)


# # # my_str = "War and Peace, Leo"
# # # Book.from_string(my_str)

# # To comment/uncomment multiple lines use: Ctrl + /
# # To indent/deindent multiple lines use: Ctr + [ or Ctr + ]


# # Question
# # Given a list of number create a new list. For each positive number in the original list add a "p" in the new list. For every negative number in the original list add "n" to the old list. The order should be preserved
# lst = [10, -5, -5, 7]
# lst = ["p", "n", "n", "p"]

# TODO: HW do this in place

def convert(lst: list[int]) -> list[str]:
    # A list compression
    # Syntactic sugar
    new_lst = ["p" if num > 0 else "n" for num in lst]
    # lst = ["p" if num > 0 for num in lst]

    print(new_lst)

    # new_lst = []
    # for num in lst:
    #     if num < 0:
    #         new_lst.append("n")
    #     else:
    #         new_lst.append("p")
    # return new_lst

# Python 3.11
# There are different Python versions. 2.7, 3.11, 3.19
# Backward compatibility

# 3.11: "A list compression" was introduced 
# 2.7: Error

convert([10, -5, -5, 7])

# TODO: Basic complexity
# Speed of a program
# 1. For one program to be faster than the other, it should have less lines of instructions.
# a = 10
# print(a)

# a = 20
# b = 30
# print(a * b)

# def zoo():
#     a = 20
#     b = 30
#     return a * b
    
# zoo()


# a = 10
# print(a)

# To answer which program runs faster, we need to figure out how many lines in total will program execute?

# n <= we describe the speed of the program execution with n


# n is same as num
def print_nums(num: int):
    for i in range(num):
        print(i)


print_nums(50)
print_nums(20)
print_nums(1)

# How does the number of times print is executed is related to the lst variable.
# n is len(lst)
def print_lst_elements(lst):
    for num in lst:
        print(num)
# print_lst_elements([10, 20, 30]) # 3
# # print_lst_elements([10, 20, 30,10, 20, 30,10, 20, 30,10, 20, 30,10, 20, 30,10, 20, 30]) # 15


# How does the number of times print is executed is related to the lst variable.
# n: len(lst) ** 2
def double_loop(lst):
    for num in lst:
        for num2 in lst:
            print(num2)
            
double_loop([10, 20, 30]) # 9
double_loop([10, 20])     # 4
double_loop([10, 20, 30, 40]) # 16



# Code block # 2
# a = 20
# b = 30
# a = 20
# b = 30
# a = 20
# b = 30
# a = 20
# b = 30
# a = 20
# b = 30
# a = 20
# b = 30

# # Code block # 3
# for num in range(50):
#     print(num)





# Sorting 
# Binary search