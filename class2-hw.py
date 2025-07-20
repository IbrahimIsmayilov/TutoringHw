# NOTES:
# - int("35") <= convers the input string into an integer object
# - learn about the following operations and experiment on what data types
# they can be applied on:
# ==, >, <, =>, <=

# Question
# Print every second letter in the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[0: len(alphabet): 2])

# Question
# In 2 different ways print the second half of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
mid_point = len(alphabet) // 2
print(alphabet[mid_point:])
print(alphabet[-1: mid_point - 1: -1])



# Question
# The funciton below is going to prompt a user to enter their age
# It will only resume when the user enters the age and store the 
# user input as a string in a variable age

# Print the users age plus 10
age = input("Enter your age")

# Question
# What will be the output of the followings?
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[3::2])  # dfhjlnprtvxz
print(alphabet[len(alphabet)::2])  # No Output
print(alphabet[:len(alphabet)])  # abcdefghijklmnopqrstuvwxyz
print(alphabet[len(alphabet):0:])  # No Output
print(alphabet[len(alphabet)-1:0:])  # No Output
print(alphabet[len(alphabet)-1:0:-1])  # zyxwvutsrqponmlkjihgfedcba

# Question
# What will be the output of the following
print(True and False)  # False
print(True and "")  # ""
print(True and 0)  # 0
print(True and [] and True) # []
print("" and False)  # ""
print(False or True and not False)  # True
print(True and "abcdefg")  # abcdefg
print(False or [] and not False or False)  # False
print(False or True and not False or False)  # True

# Question
# Write a program that asks a user for an integer input
# Print “Fizz” if an integer is divisible by three, 
# “Buzz” if an integer is divisible by five, and 
# “FizzBuzz” if an integer is divisible by both three and five.

int_input = int(input('Please provide an integer: '))
if int_input % 3 == 0 and int_input % 5 == 0:
    print('FizzBuzz')
elif int_input % 3 == 0:
    print('Fizz')
elif int_input % 5 == 0:
    print('Buzz')

