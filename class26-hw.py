# Question
# Give an example of indendented for loops where time complexity is not 
# indeed n ** 2

def random_func():
    lst = [4, 3, 2, 1]
    for index in range(len(lst)):
        for other_index in range(len(lst), len(lst + 5)):
            print('f')

# Lenght of list is n. The second for loops always runs five times. So it is going to be 5N or O(N). The second for loop runs a fixed amount of times, independent of the size of the list.
    

# Question
# In your own words describe what a library is and what category of libraries exist.
# A library is a collection of built in functions in a coding language that have already been pre-coded and we cannot really change their definition. We can but it is not recommended. Some of these libraries are built-in, meanining that when you install the coding language the libraries are also installed but only usable if imported to the file. Once imported, you can use these pre-coded functions to write code faster and not have to make up your own functions at times. Most libraries are not built in and you have to install them, get their source code which includes their definitions in your system, and only then you can import them to your file. These libraries were written by other coders and the ubitiqiousness of the functions and their definitions motivates the coders to make their functions into a library that can conveniently be used by other coders. 

# Question (Using libraries)
# In the last class we learned how to use libraries.
# Explore any 2 functions in the math library
# Write code below using those 2 functions and in your own words what your
# code is indendet to do.

# This code is to round down any number with decimals to a whole number
import math
def round_down(num: int) -> int:
    return math.floor(num)

print(round_down(4.3)) # 4


# This code is intended to convert degrees to radians
def convert_degree_rad(num: int) -> int:
    return math.radians(num)

print(convert_degree_rad(180)) # pi



# Question (New library)
# We leanred about "math" and "random" libraries in our previous class.
# Find another library that is part of the standard python package.
# Explore that library and briefly decsribe what is the library is for.
# Find 2 function that you like in that library and write code that uses it and
# describe what your code is trying to do in a sentence or two.

# datetime library is used for tracking time, including the date and exact time and representing or manipulating those values. Its biggest use is to measure how long it takes for code to run and achieve a solution or present an output. 

from datetime import date
from datetime import datetime

# Returns today's date. Could be useful for a website or app that has the date on homescreen. 
def find_date() -> int:
    return date.today()

print(find_date()) # 2025-06-27

# Returns the current date and time down to the last second. 
def find_time() -> int:
    return datetime.now()

print(find_time()) # 2025-06-27 followed by the exact time.
 

# Question
# What is an array?
# An array is a sequence of elements that the computer's Random Access Memory can group together. Only arrays and integers are recognized by the computer's random access memory. Arrays reserve spaces in the RAM for a specific sequence of numbers that translate to different data types of code. They are a way to group together code in the very low level coding languages and all lists, dictionaries etc. are arrays with modified definitions that are only possible in high level programming languages. 

# Question
# In your own words, describe how lists are represented in compute memory (RAM).
# Lists are represented by a sequence of integers in the RAM. Everything in the RAM, including strings, are represented by integers. Lists are used in the RAM to group integers. For example, if the user wants to only print a desired string, their desired string will be grouped together as a list of numbers in the RAM even though they did not create a list. The RAM can only use numbers and lists or otherwise known as arrays. It translates all of our code into numbers and lists to be stored in RAM. 

# Question
# In your own words, describe how strings of multiple characters are represented 
# in computer memory.
# Strings fo multiple characters are represented as a list of numbers in computer memory, where each number translates and corresponds to a letter using the ASCII dictionary of numbers and letters. So for example if I wanted to store Ibrahim in the computer's memory, it would store it as [05, 98, 114, 105, 104, 97, 109]. It would reserve a significant amount of space for this in the memory and take up a solid amount of bytes in the memory. 