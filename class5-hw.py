# Question (Print evens)
# Write a function that takes integer list and prints all the even numbers in the list
def print_evens(int_list):
    for number in int_list:
        if number % 2 == 0:
            print(number)

# Question (Even num count)
# Write a function that takes integer list and counts how many even numbers are in a list
def count_evens(int_list):
    count = 0
    for number in int_list:
        if number % 2 == 0:
            count += 1
    return count

# Question (List average)
# Write a function that takes integer list and finds the average of numbers in the list
def find_avg(int_list):
    sum = 0
    for number in int_list:
        sum += number
    return sum / len(int_list)
        
# Question ("A" starters)
# Write a function that takes string list as an input and prints those strings in the list that
# start with "A".
def string_list(str_list):
    for string in str_list:
        if string[0] == "A":
            print(string)
        

# Question (print all numbers)
# Write a function that takes an integer as an input and prints all numbers from 0 up until that integer.
def print_all_leading_numbers(integer):
    for number in range(integer):
        print(number)

# Question (4 divisible)
# Write a function that takes an integer as an input and prints all numbers divisible by 4 from 0 
# up until the integer.
def get_div_by_4(integer):
    for number in range(0, integer, 4):
        print(number)

# Question (Positive/Negative multiple)
# Write a function that take integer list as an input, adds all negative numbers together.
# Then adds all the positive numbers together.
# Then returns the multiple of the sum of positive numbers and the sum of negative numbers
def get_sums(int_list):
    negative_sum = 0
    positive_sum = 0
    for number in int_list:
        if number > 0:
            positive_sum += number
        else:
            negative_sum += number

    return negative_sum * positive_sum

# Question (Min length filter)
# Write a function that takes string list as an input and returns a new list with all the strings
# from the input list that has at least 3 characters in it.
def min_3_char(str_list):
    new_list = []
    for string in str_list:
        if len(string) == 3:
            new_list.append(string)

    return new_list

# Question (remove at index)
# Write a function that takes string and integer as inputs. The function should return a new string
# that has character at input integer index removed.

def remove_char(string, integer):
    new_string = string[:integer] + string[integer + 1:]
    return new_string

# Question (remove all occurences)
# Write a function that takes a string and a letter string as params. The function should return a new string
# with all the occurences of letter string removed from the first parameter.
def new_str(string, letter_input):
    new_string= ''
    for letter in string:
        if letter != letter_input:
            new_string+= letter

    return new_str

# Question (String concatination)
# Write a function that takes a string list and returns a single string that is a concatination
# of all strings in the input list.
# Ex. input: ["a", "b", "c"]
def concatenate_str(str_list):
    new_string= ''
    for string in str_list:
        new_string += string
    
    return new_string