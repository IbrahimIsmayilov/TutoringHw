# Question (check if the character is a letter of the alphabet)
# HINT: You can use "in" functionality
import string
alphabet = string.ascii_lowercase
def is_alphabet_character(letter: str) -> bool:
    if letter.lower() in alphabet:
        return True
    
print(is_alphabet_character('A'))  # True\n
    

# Question (Get sum of the digits)
# You are given a numerical string (a string that only consists of numbers).
# Complete the body of the function below to find the sum of the digits in the string
# Ex. "10" -> 1 + 0 = 10
# Ex. "1241345" -> 1 + 2 + 4 + 1 + 3 + 4 + 5 = 20 

def digit_sum(input: str) -> int:
    sum = 0
    for number in input:
        sum += int(number)
    return sum

print(digit_sum('2394'))  # 18\n


# Question (What is the goal?)
# 1. Describe with words what this code is trying to do.
# It is trying to find the product of all the numbers in the a list full of floats, or numbers with decimals, when multiplied by each other. 
# 2. Does it work correctly. If not, why? The code does not work correctly because the product, n, will always remain 0 no matter what is multiplied with. To get the correct product of all the numbers in the list, n needs to be updated to equal = 1. 
# 3. Fix the code to work correctly
def dummy(lst: list[float]) -> float:
    n = 1
    for i in lst:
        n *= i
    return n

print(dummy([5, 2, 3, 9]))  # 270\n

# Question (Max length string)
# Write a function that takes a list of strings and returns the size of the biggest string in the list
def max_len_str(lst: list[str]) -> int:
    max_str_size = 0
    for index in range(len(lst)):
        if len(lst[index]) > max_str_size:
            max_str_size = len(lst[index])

    return max_str_size  

print(max_len_str(['something', 'ibrahim', 'john']))  # 9\n

# Question (Filter)
# Write a function that takes a list of strings and prints only the ones that start with "abc"
def filter_abc(lst: list[str]) -> None:
    for string in lst:
        if string[:3] == 'abc':
            print(string)

filter_abc(['ibrahim', 'abcertygergre', 'abcibrahim'])  # abcertygergre\n, abcibrahim\n


# Question (Print stars)
# Write a function that takes integer as a parameter and prints the following:
# if input is 3:
# *
# **
# ***

# if input is 6:
# *
# **
# ***
# ****
# *****
# ******

def print_stars(star_count: int) -> None:
    for star_amount in range(1, star_count + 1):
        print("*" * star_amount)

print_stars(5)  # *\n, **\n, ***\n, ****\n, *****\n

# Question (Integers digits)
# Write a function that takes integer as an input parameter and prints all of its digits from right to left
# Ex. 5789 should print:
# 9
# 8
# 7
# 5

def right_to_left(number: int) -> None:
    str_num = str(number)
    for number in str_num[::-1]:
        print(int(number))

right_to_left(540) # 0\n, 4\n, 5\n

# Question (Hard)
# Can you do the above question without calling any function except print to peform the printing!

def mod_right_to_left(number: int) -> None:
    while number > 0:
        print(number % 10)
        number = number // 10

mod_right_to_left(2600) # 0\n, 0\n, 6\n, 2\n


# Question (Password checker)
# Write a program that takes a user input which would be a new password for user's account. 
# For a new password to be a valid password, it should be:
# 1. at least 8 characters long
# 2. have both numbers and letters in it
# 3. Should not have any character that is not either a digit (0,1,2,3,4,5,6,7,8,9) or a letter.  
# Your program should keep asking a user to enter a valid new password until they enter a password that matches our criteria.

def password_checker() -> str:
    new_pass = input('Please enter a valid password: ')
    valid = False
    while valid == False:
        
        letter_req = False
        digit_req = False
        special_char = False

        if len(new_pass) >= 8:
            for char in new_pass:
                if char.lower() in alphabet:
                    letter_req = True
                elif char in '0123456789':
                    digit_req = True
                else:
                    special_char = True
        
        if letter_req and digit_req and not special_char:
            valid = True
        else:
            new_pass = input('Invalid. Please enter a new password: ')

    return new_pass

print(password_checker())
            

# Question (Calculator)
# Lets create a calculator!
# Write a program that will take an input from the user that would indicate the operation to perform:
# 1 for Addition
# 2 for Multiplication
# 3 for Division
# Once the user enters the number that will help us to choose an operation, ask the user to enter 2 operands that we need to perform the operation on.
# Once all the input is ready, find the result and print it to the user.
# Note that your program should never end and should keep prompting a user to input a new operation once previous operation result was calculated!

def calculator() -> None:
    while True:
        operation = input('Please enter 1 for Addition, 2 for Multiplication, 3 for Division: ')

        num1 = int(input('Please enter first operand: '))
        num2 = int(input('Please enter second operand: '))
    
        if operation == "1":
            print(num1 + num2)
        if operation == '2':
            print(num1 * num2)
        if operation == '3':
            print(num1 / 3)



# Question (Jumping man)
# The below function takes 2 parameters.
# islands: each index of this parameter is an island. However, number at each index is by how much a man on that island should jump to the right.
# Ex. islands = [4, 3, 2, 1, 5, 5, 7, 2]. 
#                ^           ^
#                |         This is island 4
#         This is island 0      
# If you stand at island 9, you should jump 4 islands ahead, meaning that after a jump you will be at island 4. From island 4, you will jump 1 island only.
# start: indicates the start island position of the man.

# The below function should return at which island will the man end up after 2 jumps.
# Think about what is appropriate thing to do if the jump puts a man on an island that is beyond islands list.

def landing(islands: list[int], start: int) -> int:
    position = start
    
    for i in range(2):
        position = (position + islands[position]) % len(islands)

    return position

print(landing([4, 3, 2, 1, 5, 5, 7, 2], 4)) #  4\n


# Question (Reverse)
# You are given a list. Write a function that will print all the numbers in reverse.
# Ex. [[1,2],[3,4]] should print:
# 4
# 3
# 2
# 1
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

def reverse_num(lsts: list[list[int]]) -> None:
    for list in lsts[::-1]:
        for number in list[::-1]:
            print(number)
    
reverse_num(lst)  # 9\n, 8\n, 7\n, 6\n, 5\n, 4\n, 3\n, 2\n, 1\n


param1 = [6,5,1,1,7,11,12]
def get_number(param1: list[int], param2: int) -> int:
    # Check if two numbers within param1 can equal second param
    for index1 in range(len(param1)):
        for index2 in range(len(param1)):
            sum = param1[index1] + param1[index2]
            if sum == param2:
                return sum
            
print(get_number(param1, 11)) # 11
            
        

        
    
    
