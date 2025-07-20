# empty list is false
# empty string is false


print(False or ("" and not False) or False)


# True = 1
# False = 0
# and-e vurma
result = True and True
result = False and True
result = False and False
result = True and False

# or addition
result = True or True
result = False or False


# Evaluates to boolean
value = 5
# ==
print(7 == 9)
print(7 == 7)
print("abc" == "abc")
print("abc" == "cba")
# !=
print(7 != 9)
# >, <
print(10 > 8)
print(10 < 8)
# >=, <=
print(10 >= 8)
print(8 > 8)
print(8 >= 8)

# Scope of the variable
print("Variable Scope")
if 5 < 2:
    name = "Osman"
else:
    name = "Dilara"

print(name)
int("5")
str(555)
print("Salam necesen?")

# f(x) = 5x
# f(2) = 10

# f(x) = 19
# f(2) =

# def print(name, surname):
#     # function body
#     pass

def dummy_function(x):
    print(x)
    print(x * 2)
    return 19

a = dummy_function(100)
print(a)

def multiply(x, y):
    # print(x * y)
    result = x * y
    return result

def find_percentage(amount, percentage):
    result =  multiply(amount, percentage) / 100
    return result

# a = 10 * 5
# print(a)
# result = None
# int(input("Enter number"))
second_result = find_percentage(100, 20)
print(second_result)

# Global scope
name = "Osman"

def print_name():
    # name is a local variable
    global name
    name = "Ibrahim"
    print(name)
    return 28

foo = print_name()
print(name)
print(foo)

def multiply(x, y):
    return x * y

print(multiply(5, 9))
# print(x)

# If the user gave input that is greater than 10 and less than 100
# it is a valid input, return True
# def validate_user_input(usr_input):
#     if usr_input > 10:

# usr_input = int(input("Get user input: "))
# validate_user_input(usr_input)

# def validate_user_input(usr_input):
#     if usr_input > 10 and usr_input < 100:
#         return True
#     else: 
#         return False

# If the user gave input that is greater than 10 and less than 100
# it is a valid input, return True
# def validate_user_input(usr_input):
#     if usr_input > 10:
#         print("Valid Input")
        
# usr_input = int(input("Get user input: "))
# validate_user_input(usr_input)

# def validate_user_input(usr_input):
#     if usr_input > 10 and usr_input < 100:
#         return True
#     else:
#         return False
    
# def validate_user_input(usr_input):
#     if usr_input > 10 and usr_input < 100:
#         return True
#     return False

def is_valid_input(usr_input:int, second_param:bool) -> None:
    # becomes docstring of the function
    """ This function validates user input
    """
    print("Osman")
    # return 10 < usr_input < 100
# user_input = int(input("Enter the number: "))
# if is_valid_input(user_input):
#     # do something with user input
#     print("Valid")
# else:
#     print("Your user input is  (it must be between 10 and 100)")
    
name = "Osman"
new_name = name.lower()
# name.
print(new_name)
print(name == new_name)

name = "Osman"
for letter in name:
    print(f"{letter}\n++")
    
# Get the user input and output the number of character a's in the input
# name="Dilara”

# for letter in name:
#    if letter ==“a”:
#        print (letter)

sentece = input('Please enter a sentece: ')
required_letter = input("Enter a letter to search for: ")
if len(required_letter) == 1:
    print("You have to only use one letter")

count = 0
for letter in name.lower():
    if letter == required_letter:
        count = count + 1

print(count)