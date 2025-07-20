# List operations revisited
# Mutability
# Passing by reference vs passing by value
#     - # Replace all negative numbers in the list by 0
#     - # replace the third letter of the string by "a"
# Working on questions
# Double lists
# Working on questions about double lists
# While loops?


# What is the difference between method and functions?

# def my_func(param1):
#     print("Osman")
#     return
# my_func([1,2,3])

# print(lst1)
# print(lst2)

# lst1.append(1)
# lst1 + [1]
lst1 = [1, 2, 3]
# lst1.pop()
# print(lst1)
# lst1.pop()
# print(lst1)
lst2 = lst1 + [4]
# print(lst1 + "" + lst2)
print(lst2)
lst2.pop()
print(lst2)

# Empty list
lst1 = []
print(lst1)
lst1 = [1,2,3]
lst1.pop(0)
# lst1.pop
print(lst1)

print("Learning mutabilty")
# Indexible data structures/types
# 1. String
# 2. List

# Strings are non-mutable
name = "Osman"
# name[0] = "q" <= Cannot do this

lst1 = ["Osman", "Habil", "Dilara"]
lst1[0] = "Huseyn"

print(lst1)

lst = [0, -1, 19, 23, -3]
# 1. Go over each elemnt
# 2. Decide if that element in negative
# 3. If it is nagetive, change it to 0

lst=[0,-1,19,23,-23]

def change_to_zero(lst):
    for index in range(len(lst)):
        # print(index)
        if lst[index] < 0:
            lst[index] = 0
    # return lst

change_to_zero(lst)
print(lst)
#       012345678
name = "ad;fogjaeriopfjEWPOF"
name = name[:3] + "l" + name[4:]

# def replace(my_str: str, idx: int, char: str) -> str:
    

# print(name[3])

def replace(my_str: str, idx: int, char: str) -> str:
    return my_str[0:idx] + char + my_str[idx + 1:]
#   return "Os" +                "l" + "an"
#       012345
name = "Osman"
#       Olan
print(replace(name, 2, 'l'))

# for idx in range(len(name)):
    

# [0, -1, 23, 19, -3]
# [0, 0, 23, 19, 0]

print("Passing by reference vs passing by value")

# Passing by reference
# lst2 = lst
# lst[-1] = "z"
# print(lst)
# print(lst2)


def func(param_lst):
    # param_lst = lst
    param_lst[-1] = "q"
    
lst = ["a", "b", "c"]
func(lst)
print(lst)

# Assume list is mutable but not passed by reference
func(lst)
lst = [1,2,3]
lst2 = lst

def add_ten(num: int) -> None:
    # num = b
    num = 38

b = 19
add_ten(b)
print(b)

lst = ["a", "b", "c"]
lst2 = lst
lst2[-2] = "t"
print(lst)

lst = ["a", "b", "c"]
lst2 = list(lst)
lst2[-1] = 19

print(lst)
print(lst2)
# print(19 + "28") <= gives error

string_lst = ["a", "b", "c"]
int_lst = [1, 2, 3]
print(string_lst + int_lst)

# def my_func():
#     """ Bu funksiya nese edir
#     """
# Print all even numbers from a list.
# Count how many even numbers are in a list.
# Find the average of numbers in the list
# From a list of strings, print only the ones that start with “A”.

# Print all elements in a 2D list row by row.
# Sum all the elements in a 2D list.
# Count how many even numbers are in the 2D list.

lst = [1,2,3,4,5,6,7,8]

# 3 % 2 = 1
# 4 % 2 = 0

# 25 % 5 = 0

# print("Divisble by 5")
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# def dividing_5(lst2):
#     for index in range(len(lst2)):
#         if lst2[index] % 5 == 0:
#             print(lst2[index]) 
# dividing_5(lst)

# if 25 % 6 == 0:
#     print("Helloi world")

lst=[1,2,3,4,5,6,7,8]
new_lst=[]

for elements in lst:
    if elements%2==0:
        new_lst.append(elements)

print(new_lst)