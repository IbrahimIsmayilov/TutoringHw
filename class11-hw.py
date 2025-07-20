# Question (Fix split_str)
# Note that there are some cases where split_str function that we wrote in
# class10 does not work.
# The function should provide a list of strings that are whitespace separated
# in the given sentence.
# Ex.
# sentence = "Hi there, how are you doing?"
# Expected list: ["Hi", "there,", "how", "are", "you", "doing?"]
# Your job:
# 1. Find an example where the function does not work properly
# 2. Fix the function 

# Question (Extract words)
# Complete the body of the function to create a list of words from the given
# sentence. (Do not use split function!)
# Ex.
# sentence = "Hi there, how are you doing?"
# returned lst should be: ["Hi", "there", "how", "are", "you", "doing"]

allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ'-"
def extract_words(sentence: str) -> list[str]:
    current = ""
    lst = []
    for char in sentence:
        if char.capitalize() in allowed_characters:
            current = current + char

        if (char == " " or char == '\n') and len(current) > 0:
            lst.append(current.strip())
            current = ""

    if current:
        lst.append(current)
    return lst

print(extract_words("Paul Atreides is the villain of Dune, argued a critic."))  # ['Paul', 'Atreides', 'is', 'the', 'villain', 'of', 'Dune', 'argued', 'a', 'critic']\n['Paul', 'Atreides', "isn't", 'an', 'interesting', 'character']\n
print(extract_words("Paul     Atreides isn't an interesting character"))  # ['Paul', 'Atreides', "isn't", 'an', 'interesting', 'character']\n


# Question (Divisibles)
# Write a function that takes an integer and returns a list of integers
# that the number can be divided by without any remainder.
# Ex:
# Input: 10
# Expected return: [1, 2, 5, 10]
def find_divisibles(number: int) -> list:
    divisibles = []
    for potential_divisible in range(1, number + 1):
        if number % potential_divisible == 0:
            divisibles.append(potential_divisible)

    return divisibles

print(find_divisibles(25))  # [1, 5, 25]\n


# Question (Print content)
# Write a code that gets the file name from the user, reads its content
# and prints it. Your code should not raise an error.

def file_read() -> None:
    filename = input('Please enter a filename: ')
    with open(filename, 'r') as file:
        content = file.read()
    print(content)


# Question (Get longest word)
# Write a code that gets the file name from the user, reads its content
# and finds the longest word in the file. Your code should not raise an error.
def longest_word_file() -> str:
    filename = input('Please enter a filename: ')
    max_length = 0
    max_length_word = '' 

    with open(filename, 'r') as file:
        content = file.readlines()
    for i in range(len(content)):
      content[i] = content[i].strip()
      if len(content[i]) > max_length:
          max_length = len(content[i])
          max_length_word = content[i]
    

    return max_length_word


# Question (Most common word)
# Write a code that gets the file name from the user, reads its content
# and finds the most common word in the file. Your code should not raise 
# an error.

def count_file() -> str:
    filename = input('Please enter a filename: ')
    word_count_dict = {}
    with open(filename, 'r') as file:
        content = file.readlines()
    for i in range(len(content)):
        content[i] = content[i].strip()
        if content[i] not in word_count_dict:
            word_count_dict[content[i]] = 0

        word_count_dict[content[i]] += 1

    max_occur = 0

    for key, value in word_count_dict.items():
        if value > max_occur:
            max_occur_word = key
    
    return max_occur_word


# Question (Average age)
# Imagine you have a file where everyline is the text of the following format:
# Name, age
# Ex:
# Osman, 24
# Leyla, 22

# Write a program that finds the average of people who are over 18.
def average_age_file() -> int:
    filename = input('Please enter a filename: ')
    sum_ages = 0
    with open(filename, 'r') as file:
        content = file.readlines()
    for i in range(len(content)):
        name, age = content[i].strip().split(', ')
        if age > 18:
            sum_ages += age

    avg_age = sum_ages // len(content)

    return avg_age

# Question (Reverse content)
# Write a program that reverse the content of the file.
# Ex.
# Original File content:
# Osman says hi
# Osman says bye

# After your program runs, the content should be as following:
# Osman says bye
# Osman says hi

# The above example was only for a file with 2 lines but your program
# should work with a file of an arbitrary number of lines.

def reverse_file() -> None:
    filename = input('Please enter a filename: ')
    with open(filename, 'r') as file:
        content = file.readlines()
    for i in range(len(content[::-1])):
        content[i] = content[i].strip()
        print(content[i])
    