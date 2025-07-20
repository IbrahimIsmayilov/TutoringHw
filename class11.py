# Global scope vs Local scope

name = "Osman"

def dummy():
    # name = "Bilal"
    global name
    name = "Bilal"
    print(name)

dummy()
print(name)
# print(a)

# for l in "abc":
#     print(l)
# print(l)

for l in "":
    print(l)
print("Hello world")

for l in []:
    print(l)
print("Hello world")

for l in "abc":
    print(l)

print(l)

# name2 = 5
# print(name2)

# Question 
# Write a function that takes a string as a parameter and creates a list containing each word in that string as an individual element
# sentence = "Hi there, how are you?"
# lst = ["Hi", "there,", "how", "are", "you?"]
# DO NOT USE .split function!!!!
def split_str(sentence: str) -> list[str]:
    # sentence = "Hi there, how are you?"
    current = ""
    lst = []
    for char in sentence:
        # current = "Hi"
        # char = " "
        # We should add current to the list only when current is equal to an entire word in the sentence
        # if char != " ":
        current = current + char

        if char == " ":
            lst.append(current.strip())
            current = ""

    if current:
        lst.append(current)
    return lst

# print(split_str("Hi there, how are you? "))
# print("hi")
# print("Hi there, how are you? ".split("h"))
# ["Hi t", "ere"]

# print(len("    O "))

# TODO: Exceptions
# 5 / 0
# print("Osman is cool")
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num1: "))
# if num2 != 0:
#     print(num1 / num2)

try:
     print("Azerbaijan is cool")
     f = open("asdfasd", "r")
     print("Azerbaijan2 is cool")
except ZeroDivisionError:
     print("Canada is cool")
except FileNotFoundError:
     print("File not found")
     try:
         5 / 0
     except ZeroDivisionError:
         print("byte")
        

try:
    5 / 0
    print("hi")
except ZeroDivisionError:
    print("Canada is cool")
finally:
    print("bye")


# TODO: Continue with files.

# def dummy() -> str:
#     return "ab"

# try:
#     print(dummy()[2])
# except IndexError:
