# TODO: Libraries +
# TODO: target question
# TODO: Fundamental data structures
# TODO: Dictionaries and hash tables
# TODO: Command line more
# TODO: Git branching:

import math
import random

def foo2():
    return 7

foo2()
#foo()
a = 5
print("Osman")


# Pygame
# Pytorch
# Numpy


# Question
# Write a function that takes a list of integers and a number as a parameter and it  should return the list of tupe pairs where each pari sum adds up to the
# target number.

# Ex.: two_sum([1, 2, 3, 4], 5) => [(1, 4), (2, 3)]

# Solve the question by using sets. Duplicate pairs are allowed and 1 number can be matched with another number multiple times.
# No duplicate numbers will exit
# target = 6
# [1, 2, 3, 4, 5] => [(1, 5), (2, 4)]


# To solve this with only 1 loop!
# s = set()
# do not turn your list into a set. You can create a new empty set.
# you can use: 5 in s

def two_sum(lst: list[int], target: int) -> list[tuple[int]]:
    combinations = []
    for index in range(len(list)):
        new_target = target-lst[index]
        for other_index in range(index + 1, len(lst)):
            if lst[other_index] == new_target and other_index != index:
                combinations.append((lst[index], lst[other_index]))
    return combinations

def two_sum(lst: list[int], target: int) -> list[int]:
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                result.append(tuple(lst[i], lst[j]))
    return result

# Arithmetic sequence
# 2  4  6  8  10 12 14
# by how much numbers are increasing = 2
# 
# n - 1  +  (n - 2) +  (n - 3) + (n - 4) + ... + 0 = (n (0 + n - 1)) / 2 = (0 + n ** 2 - n) / 2 = (n ** 2 - n) / 2  = n ** 2
#  


# n * (n - 1) = n * n - n = n**2 - n = n**2

# HW Question: give an example of indendented for loops where time complexity is not indeed n ** 2

# n ** 2
def two_sum(lst: list[int], target: int) -> list[tuple[int]]:
    result = []
    for i in range(len(lst)):
        if (target - lst[i]) in lst[i + 1:]:
            result.append((lst[i], target - lst[i]))
    return result



# 100: 100,  10000

# 1000: 1 day, 1000 days, 1000000

# 1000: 1000, 1000000
# 
# Time complexity: n
def two_sum(lst: list[int], target: int) -> list[tuple[int]]:
    result = []
    s = set()
    for i in range(len(lst)):
        if (target - lst[i]) in s:
            result.append((lst[i],target - lst[i]))
        else:
            s.add(lst[i])
    return result


# Searching in a list takes: len(lst)
# Searching in a set takes: constant time: 1

class Dummy:
    def __init__(self):
        pass

print(type(Dummy()))
print(type([]))
print(type({"a": 2}))