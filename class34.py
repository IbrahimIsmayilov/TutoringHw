# TODO Go over the homework
# TODO Go over the assignment
# TODO Learn about Abstract data types (Stack)
# TODO Learn about Recursion
# TODO Intro to Computer Architecture

# Main dictionary operations: adding, removing, updating
class Dictionary():
    # Time complexity O(1), constant time complexity
    HASH_TABLE_SIZE = 1500
    def __init__(self):
        self.hash_table = [[]] * Dictionary.HASH_TABLE_SIZE
        self.total_count = 0

    # Time complexity O(1), constant time complexity
    @staticmethod
    def __hash__(unhashed_key):
        return hash(unhashed_key) % Dictionary.HASH_TABLE_SIZE
    
    def change_hash_size(self, new_size):
        Dictionary.HASH_TABLE_SIZE = new_size
    
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def find_kv_idx(self, hashed_idx, key_target):
        for kv_idx in range(len(self.hash_table[hashed_idx])):
            if self.hash_table[hashed_idx][kv_idx][0] == key_target:
                return kv_idx
        return -1
    
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def check_key_existence(self, key):
        hashed_idx = Dictionary.__hash__(key)
        kv_idx = self.find_kv_idx(hashed_idx, key)
        if kv_idx == -1:
            raise KeyError
        else:
            return hashed_idx, kv_idx

    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def add(self, key, value):
        try:
            self.check_key_existence(key)
        except KeyError:
            hashed_idx = Dictionary.__hash__(key)
            self.hash_table[hashed_idx].append((key, value))

    
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def remove(self, key):
        hashed_idx, kv_idx = self.check_key_existence(key)
        self.hash_table[hashed_idx][kv_idx], self.hash_table[hashed_idx][-1] = self.hash_table[hashed_idx][-1], self.hash_table[hashed_idx][kv_idx]
        self.hash_table[hashed_idx].pop()

        
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def update_key(self, key, value):
        hashed_idx, kv_idx = self.check_key_existence(key)
        self.hash_table[hashed_idx][kv_idx] = (key, value)

    def print_kv_pair(self, key):
        hashed_idx, kv_idx = self.check_key_existence(key)
        print(self.hash_table[hashed_idx][kv_idx])

    # Time complexity O(1), constant time complexity
    def __str__(self):
        return f'{self.hash_table}'
    
#["Osman"] * 3
#[[]] * 3


class Circle:
    def __init__(self, r: int):
        self.radius = r
    
    def find_area(osman):
        return 3.14 * osman.radius ** 2
   
    @classmethod 
    def create_from_str(clss, my_str: str):
        """ Creates an instance of Circle from a string """
        return clss(int(my_str))

    @classmethod
    def create_from_file(cls, filename: str) -> list["Circle"]:
        # 1. read a line at a time fromt he file.
        # 2. use cls word to create a circle for each line in the file
        # 3. add that to result list
        # 4. return the list.

        pass

c = Circle(8)
print(c.find_area())
#{c: "Osman"}


# ADT (Abstract Data Type)
# Is a concept that we create to reason about things that can be implemented in different ways with concrete data
# types.
# Stack

# What is on top of stack? Glass

# pan3
# pan2
# pan
# plate

# We can add to stack and we can remove from stack.
# When we add to stack we add to the top of the stack
# When we remove from stack we remove from the top of the stack.

# LIFO (Last In First Out)
class Stack:
    def __init__(self):
        self.elements = []
    
    def add(self, element):
        self.elements.append(element)
    
    def remove(self):
        if len(self.elements) == 0:
            return -1
        self.elements.pop()

s = Stack()
s.add("Plate")
s.add("pan")
s.add("pan2")
s.remove()

# Normal Data Types
# list, int, float, str, bool, tuple, dict

def is_valid(parantheses: str) -> bool:
    opening_parantheses_stack  = Stack()
    for paranthesis in parantheses:
        if paranthesis == "(":
            opening_parantheses_stack.add(paranthesis)
        else:
            if opening_parantheses_stack.remove() == -1:
                return False
    return len(opening_parantheses_stack.elements) == 0
    #return not opening_parantheses_stack.elements

# What if we count how many left and right facing parantheiss there are and based on that tell if this is valid or not.
is_valid(")(")
is_valid("(())")
is_valid("(()")

is_valid("(()")
is_valid("())")


# You need to use stack here.
# You need to use python list to solve this problem.


# Examples:
#print(is_valid("()"))  # True
#print(is_valid("()()"))  # True
#
#print(is_valid("(()())"))   # True
#print(is_valid("(()())()")) # True
#
#print(is_valid("(()(")) # False
#print(is_valid(")())")) # False
#print(is_valid("(()))")) # False

#print(is_valid("")) # True
                            
                            
# Question
# Steps 1: To create a dynamic implementation that uses recursion, a function to find all sum combination should be created that considers both 1 + 3 and 3 + 1 as different solution to get 4. 
# Step 2: Add base case to stop recursion and recursively call function
# Step 3: Create a dictionary to keep a record of all summing combinations, so the summing combinations of 3 in 3 + 6 and 3 + 3 + 3 are not recounted. Also put these different combos in a set so that (1 + 1 + 1 + ...1) is not recounted. 
# Step 4: Just get len(set) to




# For number n count the number of ordered sums till n.


# combos_dict = {}
# combos_dict[1] = set()
# combos_dict[2] = {(1, 1)}
# combos_dict[3] = {(1, 1, 1), (1, 2), (2, 1)}

#def ordered_sums(n: int) -> int:
#    total = 0
#    if n in combos_dict:
#        return combos_dict[n]
#    
#    for num in range(1, n):
#        combos_dict[n] = combos_dict.get(n, set())
#        combos_dict[n].add((num, (n - num)))
#        combos_dict[n].add((ordered_sums(num) | ordered_sums(n - num)))
#    
#    
#    return combos_dict[n]

# def ordered_sums(n: int) -> int:
#     result = {}

#     for i in range(1, n + 1):
#         result[i] = 0
#         for j in range(1, i + 1):
#             result[i] += result[i - j]
            

# print(ordered_sums(4))
# # 1 + 1 + 1
# # 1 + 2
# # 2 + 1
        
# 1, 1

# # Ex: 
# ordered_sums(4) # -> 7
# ordered_sums(4) # -> 7
# ordered_sums(4) # -> 7
#1+1+1+1
#1+1+2
#1+2+1
#2+1+1
#2+2
#1+3
#3+1

# ordered_sums(3) 

# Use reccursion
# We have not covered reccursion.
# Recursion is bad (never user it!)

# There is a concept of a reccursion depth.

# 1001

# Recurrsion is extremely slow!!!

# System programming.
# Function calls are expensive.
# Each function call creates a stack in memory.

# Bottom up/top down.
# U almost always can avoid recursion.

# Recursive thinking is good.


# ordered_sums(7)

# ordered_sums(6) + ordered_sums(1)
# ordered_sums(5) + ordered_sums(2)
# ordered_sums(4) + ordered_sums(3)

# n = 0

def bigger_right(lst:list[int]) ->list[int]:
    curr_idx = 1
    new_lst = []
    for idx in range(len(lst)):
        for new_idx in range(idx + 1, len(lst)):
            if lst[new_idx] > lst[idx]:
                new_lst.append(lst[new_idx])
                break
            break
        new_lst.append(-1)
        curr_idx += 1

    return new_lst







print(bigger_right([2, 3, 4, 9, 1, 3]))

        

        



