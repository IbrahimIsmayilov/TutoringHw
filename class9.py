# Question (Calculator)
# Lets create a calculator!
# Write a program that will take an input from the user that would indicate the operation to perform:
# 1 for Addition
# 2 for Multiplication
# 3 for Division
# Once the user enters the number that will help us to choose an operation, ask the user to enter 2 operands that we need to perform the operation on.
# Once all the input is ready, find the result and print it to the user.
# Note that your program should never end and should keep prompting a user to input a new operation once previous operation result was calculated!

# while True:
#     operator = input("Enter an operator (+ - * /): ")
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     # Based on the operator entered, perform the correct math operation
#     if operator == '+':
#         result = num1 + num2  # Addition
#     elif operator == '*':
#         result = num1 * num2  # Multiplication
#     elif operator == '/':
#         if num2 == 0:
#             print("You cannot divide a number by 0")
#             continue
#         else:
#             result = num1 / num2  # Division
#     # elif operatore == "%":
#     else:
#         # If user entered something other than +, -, *, /
#         print(f"{operator} is not a valid operator!")
#         continue
#     print(result)
    
# GUI: Graphical User Interface

# Question (Jumping man)
# The below function takes 2 parameters.
# islands: each index of this parameter is an island. However, number at each index is by how much a man on that island should jump to the right.
# Ex. islands = [4, 3, 2, 1, 1, 1, 7, 2]. 
#                ^           ^
#                |         This is island 4
#         This is island 0      
# If you stand at island 9, you should jump 4 islands ahead, meaning that after a jump you will be at island 4. From island 4, you will jump 1 island only.
# start: indicates the start island position of the man. 

# The below function should return at which island will the man end up after 2 jumps.
# Think about what is appropriate thing to do if the jump puts a man on an island that is beyond islands list.
def jumping_man(islands: list[int], start_island) -> int:
    """ Retruns the final island after 2 jumps.
        If something goes wrong, returns -1.
    """
    # lst = [4, 3, 2, 1, 1, 1, 7, 2]
    # print(lst[start_island:4])
    if len(islands) > start_island:
        position1 = start_island + islands[start_island]
        if position1 > len(islands):
            return None
        position2 = position1 + islands[position1]
        return position2
    else:
        return None # something went wrong

print(jumping_man([4, 3, 2, 1, 1, 1, 7, 2], 0)) # result should be island 5
print(jumping_man([4, 2, 2, 1, 1, 1, 7, 2], 1)) # result should be island 4

jumping_man([2,3,4,5, 9], 4)

# Set

# Questions
# Find unique numbers in the list
def find_unique(lst: list[int]) -> int:
    unique_elements = []
    for num in lst:
        if not num in unique_elements:
            unique_elements.append(num)
    return len(unique_elements)
print(find_unique([5,5,5,2]))

# Sets
# {1, 4, 5, 7}
# {1, 4, 5, 7, 7} <= invalid set

var = set()
print(var)
var.add(5)
print(var)
var.add(8)
print(var)

var.add(8)
print(var)

var.add("Osman")
print(var)

a = set([1, 2, 4])
b = set([2, 3])
print(a | b) # union
print(a - b) # set difference
print(b - a)

print(a & b) # set intersetction
a = set([1, 2, 4])
a.remove(2)
print(a)

a = set([1, 2, 4])
# a.remove(5)
# print(a)

a = set([1, 2, 4])
a.discard(5)

b = int("123")

a = set([1,2,3,3])
print(a)

b = set("abcdaa")
print(b)
print(len(b))

def find_unique(lst: list[int]) -> int:
    return len(set(lst))

print(find_unique([5,5,5,2]))

# names = set()
# while True:
#     operation = input("Enter operation (d (delete), a (add))")
#     name = input("Enter new character name: ")
#     if operation == "d":
#         names.discard(name)
#     elif operation == "a":
#         pass


# Set questions
# Class
# Working with files