# TODO Wramp up
# Time complexity explanation class 31
# n ** 2, what is n? n = len(lst)

# n = 10
# How many for loop iterations will we run? 5 * 10  = 50
# if time complexity was n ** 2, then we would expect 100 iterations.

# n = 30
# how many for loop iterations will we run? 5 * 30 = 150
# if time complexity was n ** 2, then we would expect 900 iterations.

# What is the definiton of time complexity?
# Time complexity proqram daxilindeki her bir funksiyanin 
# nece defe dovr etdiyini gosterir. 

# There are 2 parts to a definition of time complexity
# 1. how many for loops are we going to have
# 2. as the size of the input parameters grow.

def foo(lst: list[int]) -> None:
    for i in range(len(lst)):
        for j in range(5):
            print("Osman")

# 5 * n => O(n)


# n ** 2 - 1
# n ** 2 - n
# First loop goes n times
# How many times second loops goes depends on the first loop.

# n ** 2

def foo2(lst: list[int]) -> None:
    # lst = [10, 20, 30, 55, 77]
    for i in range(len(lst)):
        # i = 4
        for j in range(i + 1, len(lst)):
            print(i)
            
# n - 1 + n - 2 + n - 3 + n - 4 . . . + 0 = ?

# n = 10
# 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0
# Arithmetic sequence formula: n ** 2

# Stack related questions
# ADT (Abstract data types)
# ADT gives us a definition of a data type but not the implementation details.
# The door is something that you can open and close.
# Stack is a data type where you can add elements and also you can remove elements. THe only thing is the latest added element should be removed first
# Is by using lists.

# Glass, wood, not open and closing but a sliding door.

# TODO Wramp up assignment
# 5 times the load that we have in this course.

# TODO Solve a palindrome question
# What is the palindrome. It is a string that reads same forward and backward.
# "aaa"
# "aba"
def is_palindrome(word: str) -> bool:
    return word == word[::-1]

def is_palindrome(word: str) -> bool:
    if len(word) == 2:
        return word[0] == word[1]
    elif len(word) == 1:
        return True

    result = is_palindrome(word[1:-1])
    return word[0] == word[-1] and result

print(is_palindrome("abccba"))
print(is_palindrome("qbccba"))
print(is_palindrome("abtcba"))
    
"abccba"
# 1. Start and ends are equal
# 2. Smaller question should also be palindrome
"bccb"
"cc" # whent the length of the string is 2 just make sure they are equal, when it is 1, defacto accept it as a palindrome

#"a"

# What type of questions can we use reccrusion for?
# Reccursion should eventually stop.

# We use reccursion when to find an answer to our current solution there are smaller same problems to be solved.

# Reccursion
# 1. figure out the smaller questions
# 2. when you find an answer to smaller questions, how do u use them to find the answer to the current question.
# 3. when do we stop? Hitting the bottom of the reccursion.

# To find if the above string is a poindrome, is there a smaller string that we can first find if that smaller string is palindrome or not
# and then use that answer to find the answer to our oiriginal question.

# Try to solve the palindrome question through the reccursion lens.
# Reccursion are the functions that call themselves within the body of the function.


# TODO Architecture
# How does python program gets executed in the computer?
# Python code gets run through interpreter that converts/translates the human readable python code into a binary code (the only language that
# computers understand)

# When we say program is being run in a computer what does that mean?

# There is another program that runs our code (Operating System)

# What is a program? WHere is program in a computer?

# CPU, RAM, Storage.

# Program vs Process
# A process is a running instance of a program

# An example of Python code that interpreter can convert in to 1 line binary code
(5 + 10)

if 10 > 20 and []: # 9 binary code
    pass

