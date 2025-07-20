# Question
# What will be the ouptut of these? 
print(10 < 20 <= 39)  # True
print(38 == 25)  # False
print(38 != 25)  # True 
print(int("5") + str(13))  # TypeError
print(f"Hi {int("Leyla")}")  # Type Error

# Question
# What will be the ouptut of these?
name = "Osman"
if name == "Osman":
    name = "Ali"
elif name == "Ali":
    name = "Osman"
else:
    print("Josh")
print(name)  # Ali  

# Question
def dummy(in1: int, in2: int):
    print(in1 + in2) 

result = dummy(1, 19)  # 20
print(result + result ** 2)  # None

# Question
# What will be the output of this
def is_valid_msg(msg):  
    return msg[0] == "A" and len(msg) > 4
print(is_valid_msg("Abbaslar"))  # True
print("") # \n

# Question
# What will be the output of this
def is_valid_msg(msg):
    return len(msg) > 4 and msg[0] == "A"
print(is_valid_msg("Abbaslar"))  # True
print("")  # \n

# Question
# Write a function that checks if the legnth of the string
# is a multiple of 3
def length_string(string):
    return len(string) % 3 == 0


# Question
# Zero checksum of 2 numers is defined as:
# Adding two numbers reults in a number that is divisible by 
# 256 without any remainder.
# Write a function that takes 2 numbers and checks if they have zero checksum

def checksum(num1, num2):
    return (num1 + num2) % 256 == 0

# Question
# Write a function that takes a string and returns it in reverse
# Ex. "abcdef" -> "fedcba"

def reverse_string(string):
    reverse_string = string[len(string): : -1]
    return reverse_string

# Question
# Palindrome is defined as if the string reads the same in reverse
# as it reads from the front.
# Ex. "abc" <= not a polyndrome
# Ex. "aaa" <= is a polyndrome

def palindrome(string):
    return string == reverse_string(string)

# Question
# Write a function that takes a string input and checks if
# all the characters in the input string is numeric without using
# any of the string builtin functions

def check_int_in_str(string):
    integers = '0123456789'
    for character in string:
        if character not in integers:
            return False
    return True

# HINT: "ca" in "cabdef" <= returns a boolean value that checks
# if "ca" is a substring of "cabdef".

# Question
# Copmlete the following functions based on their docstring
# and test if they behave as expected.
alphabet = "abcdefghijklmnopqrstuvwxyz" 
def is_valid_arg(arg: str) -> bool:
    """ Argument is only valid if it is a letter in the 
        alphabet
    """
    return arg in alphabet

def does_contain_same(msg1, msg2, letter):
    """ Return True if the msg1 and msg2 has the same
        number of occurences of character 'letter'
    """
    count1 = 0
    count2 = 0

    for char in msg1:
        if char == letter:
            count1 += 1

    for char in msg2:
        if char == letter:
            count2 += 1

    if count1 == count2:
        return True

def main():
    """ - Get 3 inputs from the user.
        - Make sure all the necessary arguments are verified
        - In the case in1 and in2 has the same number of occurences
          of letter in3, let the user know about it. Otherwise,
          handle the function's body as you deem needed.
    """
    
    input1 = input('First Input, word: ')
    while is_valid_arg(input1) !=  True:
        input1 = input('First Input, word: ')

    input2 = input('Second Input, word: ')
    while is_valid_arg(input2) !=  True:
        input2 = input('Second Input, word: ')

    input3 = input('Third Input, letter: ')
    while is_valid_arg(input3) !=  True:
        input3 = input('Third Input, letter: ')

    if does_contain_same(input1, input2, input3):
        print('Same number of occurences!')
    else:
        print('Not the same amount of occurences')


    


    