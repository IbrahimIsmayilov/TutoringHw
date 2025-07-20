# allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ'-"
# def extract_words(sentence: str) -> list[str]:
#     current = ""
#     lst = []
#     for char in sentence:
#         if char.capitalize() in allowed_characters:
#             current = current + char

#         if (char == " " or char == '\n') and len(current) > 0:
#             lst.append(current.strip())
#             current = ""

#     if current:
#         lst.append(current)
#     return lst

# print(extract_words("I am a well-mannered - person"))

# def extract_words(sentence: str) -> list[str]:
#     current = ""
#     lst = []
    
#     for char in sentence:
        
#         current = current + char
#         if current==" ":
#             current=""
#             continue
#         if char == " ":
#              lst.append(current.strip())
#              current = ""

#     if current:
#         lst.append(current)
#     return lst

# print(extract_words("Hi there, how are you doing?"))


# def extract_words(sentence: str) -> list[str]:
#     current = ""
#     lst = []
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in sentence:
#         if char != " " and char.lower() in alphabet:
#             current += char
#         else:
#             if current:
#                 lst.append(current.strip())
#                 current = ""

#     if current:
#         lst.append(current)
#     return lst

# print(extract_words("Hi there, how are you doing?"))

# # This implementation is better
# def file_read() -> None:
#     filename = input('Please enter a filename: ')
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#     except FileNotFoundError:
#         print("SOmething went wrong")
#     print(content)
    
# # Syntactic sugar
# with open("osman.txt", 'r') as file:
#     content = file.read()
#     file.readline()

# # Equivalent to the code above
# file = open("osman.txt", 'r')
# content = file.read()
# file.close()


# def file_read() -> None:
#     filename = input('Please enter a filename: ')
#     with open(filename, 'r') as file:
#         content = file.read()
#     print(content)

# try:
#     file_read()
# except FileNotFoundError:
#     print("SOmething went wrong")


# file_name = input("Enter file name:")
# try:
#     f = open (file_name, "r")
#     content = f.read()
#     print(content)
#     f.close()
# except FileNotFoundError:
#     print(f"File {file_name} not found")

# Question (Get longest word)
# Write a code that gets the file name from the user, reads its content
# and finds the longest word in the file. Your code should not raise an error.
# def longest_word_file() -> str:
#     filename = input('Please enter a filename: ')
#     max_length = 0
#     max_length_word = ""
#     with open(filename, 'r') as file:
#         content = file.readlines()

#     lst_word = []
#     for line in content:
#         lst_word += line.strip().split()

#     for i in range(len(content)):
#       content[i] = content[i].strip()

#       if len(content[i]) > max_length:
#           max_length = len(content[i])
#           max_length_word = content[i]
#     return max_length_word
# print(longest_word_file())

# -----------------------------------------------
# words_in_file=[]
# file_name = "osman.txt"
# try:
#     f=open (file_name, "r")
#     for items in f:
#         words_in_file.append(items)
#     f.close()
# except FileNotFoundError:
#     print(f"File {file_name} not found")

# print(words_in_file)

# count=0
# words_dictionary={}
# for elem in words_in_file:
#     words_dictionary[len(elem)]= elem
#     if count < len(elem):
#         count=len(elem)
        
# print(f"Longest word:{words_dictionary[count]}")

# Question (Average age)
# Imagine you have a file where everyline is the text of the following format:
# Name, age
# Ex:
# Osman, 24
# Leyla, 22
# Murad, 17

# Write a program that finds the average of people who are over 18.
# def average_age_file() -> int:
#     filename = input('Please enter a filename: ')
#     sum_ages = 0
#     count = 0
#     with open(filename, 'r') as file:
#         content = file.readlines()
#     for i in range(len(content)):
#         name, age = content[i].strip().split(', ')
#         age = int(age)
#         if age > 18:
#             sum_ages += age
#             count += 1

#     if count == 0:
#         return 0

#     avg_age = sum_ages // count
#     return avg_age

# f = open("osman.txt")
# f2 = open("osman.txt")

# c = f.readline()
# print(c)
# print(f.readline())
# print(f2.readline())



# 0 => move that many characters from the beginning of the file
# 1 => move that many character from wherever you are in the file
# 2 => move that many characters from the end of the file
# f.seek(3, 0)
# f = open("osman.txt")
# print(f.readline())
# f.seek(3, 0)
# print(f.readline())

# f = open("osman.txt", "rb")
# print(f.readline())
# f.seek()
# f.seek(3, 1)

# f = open("osman.txt", "r")
# f.seek(0, 2)
# print(f.readline())

# f = open("osman.txt", "r+")
# print(f.readline())
# print(f.write("Osman"))

# f = open("osman.txt", "w+")
# When you try to open non existing file with r, it raises an error
# WHen you try to open a file with w permisison, it will raise its content.

# TODO: Tuples
# Tuples are non-mutable. Lists are mutable.
# my_tup = (10, 20, 30)
# empty_tup = ()
# one_elem_tupe = (5,)

# for elem in my_tup:
#     print(elem)

# print(len(my_tup))

# Tuples are just tiny bit faster than lists
# Tuples are not-mutable!
# my_dict = {(20, 30): 10}

# mapping = {(10564151658, 165848915351): "Toronto"}

# lan = int(input("Enter langitude: "))
# lat = int(input("Enter lattitude: "))
# print(mapping[(lan, lat)])
# my_tup[0] = 50
# lst = []
# lst.append(10)
# print(list(my_tup))
# print(tuple([10,20]))
# print(list("abc"))

# TODO value unpacking
# a, b = 5, "Osman"
# print(a)
# print(b)

# lst = [10, 20]
# a, b = lst
# print(a)
# print(b)

# Cannot do this. Should have the same sized list as the number of variables
# lst = [10, 20, 40]
# a, b = lst
# print(a)
# print(b)

# age, name = (10, "Osman")
# print(age)
# print(name)

# key1, key2 = {"Osman": 24, "Leyla": 15}
# print(key1)
# print(key2)

# a, b = "abc"
# print(a)
# print(b)

# def dummy():
#     return "Osman"

# Osman, 24
# Leyla, 17

# def get_eldest_name_age():
#     return ("Osman", 24)

# name, age = get_eldest_name_age()

# my_dict = {"Osman": 24, "Leyla": 15}
# for key, val in my_dict.items():

lst = [10, 20, 40]
print(max(10, 20, 40, 70))

# def dummy(param1):
#     return param1

# print(dummy(10, 20))


def dummy(param1, param2, param3, *args):
    # print(param1)
    print(args)
    
dummy(10, 20, "Osman")