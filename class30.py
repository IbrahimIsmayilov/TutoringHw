# TODO Upload class 29 recording.

# TODO Go over homework
# TODO Warm up exercise
# TODO Wrap with Git and Github
# TODO Process life cycle


# A hash function is a function that takes an input and converts it to a different format

# The hashed value is used as an index to determine where to place an element in a hash table.

# What are the use cases for hashing?
# 1. Converting arbitrary formated input to an index in a hash table.
# 2. Be able to verify if the file has been tempered with.
# 3. Hash trees.


# File related operations
# 1. encoding/decoding
#    to prevent malicious actors from reading the content of my file
# 2. hash
#    to be able to verify if the file has been tempered with/changed.
#    osman.txt => "abc"
#    osman.txt => "abc"
#    Malicious actor has changed the file
#    osman.txt => not be "abc"
# 3. decompress/compress
#    archive file: .zip .tgz
def hash(my_str: str) -> str:
    """ Convers my_str parameter to a string that has length of 4 """
    if len(my_str) == 0:
        return "aaaa"
    if len(my_str) >= 4:
        return my_str[0:4]
    return (my_str * 4)[0:4]

def ht_hashing(my_str: str) -> int:
    pass

def ht_hashing(my_int: int) -> int:
    pass

class Employee:
    def __init__(self, name):
        self.name = name
    
    def __lt__(self, other):
        return True
    
    def __str__(self):
        return self.name
    
    def __iter__(self):
        pass
    def __next__(self):
        pass
    
    #def __hash__
# What is the restiriction on the keys for the dicitonary?
# The dicitonary keys must be immutable
Employee("Osman") < Employee("Leyla")

e = Employee("Osman")
my_dicitonary = {20: "Osman", "Leyla": 40}

#f = open("asdhifa", "r")


# Question
# Complete the body of the function such that it finds the missing number in
# a sorted list within which numbers go from 1 to len(lst) + 1
[1,2,3,5,6]
# len(lst)
# O(n) => what is n? 
def missing_number(lst: list[int]) -> int:
    for index in range(len(lst) - 1):
        if lst[index + 1] != lst[index] + 1:
            return lst[index] + 1
    return lst[-1] + 1 
    #return len(lst) + 1
print(missing_number([1,2,3,5,6]))
print(missing_number([1,2,3,4,5]))

# HW TODO: reutrn the list  of missing numbers.

# Question
# Complete the body of the function such that it finds the missing number in
# a list within which numbers go from 1 to len(lst) + 1

# 1. Sort the list
# 2. Do the same thing as above
# n * log(n) + n = n * log(n)
def find_missing_non_sorted(lst: list[int]) -> int:
    lst = sorted(lst) # len(lst) = n: n * log(n), Base 2.
    return missing_number(lst) # len(lst): n

# 1 < n < n * log(n) < n ** 2 < 2 ** n
# n ** 3
# What would my time complexity be if the list was sorted?
# 1. n ** 3: n * log(n) + n**3
# n**2
def find_missing_non_sorted(lst: list[int]) -> int:
    for i in range(1, len(lst) + 2):
        if not i in lst: #len(lst): n + n - 1 + n - 2 + n - 3 ... 1 = n*(n-1)/2 
            return i

find_missing_non_sorted([5,4,3,2,1])

def find_missing_non_sorted(lst: list[int]) -> int:
    for i in range(0, -1 * (len(lst) + 2), -1):
        if not i in lst: #len(lst)
            return i
    
# you can solve this in n time complexity.