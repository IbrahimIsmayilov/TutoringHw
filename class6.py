# 1. HW review
# 2. For loop (break and continue)
# 3. While loops
# 4. Double lists

# 5 + \
# 5
# 5 + 5

# print("Osman") 5


import random


#TODO HW Review
#Q1

# Write a function that takes integer list and prints all the even numbers in the list
lst=[1,2,3,4,5]


# Functions should always return the same type
def give_even_numbers(in_lst:int) -> list:
    lst2 = []
    for elem in in_lst:
        if elem % 2 == 0:
            lst2.append(elem)
    return lst2

    # if len(lst2) == 0:
    #     return "no even number found" 
    # else:
    #     return lst2
print(give_even_numbers(lst)) 

#------------------------
#Q2
def give_even_numbers_count(lst:int):
    a = give_even_numbers(lst)
    return len(a)

#print (give_even_numbers_count(lst))



#------------------------
#Q3

def average_of_even_numbers(lst: list[int]) -> float:
    a = give_even_numbers(lst)
    count = 0
    for elem in a:
        count += elem

    if len(a) != 0:
        return count / len(a)
    return 0.0


#print(average_of_even_numbers(lst))

#---------------------------
#Q5

def sum(a: int, b:int) -> int:
    # print("Osman")
    return a + b

def print_all_number_till_given_number(num):
    for count in range(num):
        print(count)

print_all_number_till_given_number(8)

#num=5         
#print_all_number_till_given_number(num)

#---------------------------
#Q7

lst=[1,2,-6,2,-9,7,1,-3]
def merge_all_positive_and_negative_numbers(lst):
    count_positive=0
    count_negative=0
    for i in lst:
        if i>0:
           count_positive = count_positive + i 
        else:
            count_negative=count_negative+i
    return count_negative * count_positive


#merge_all_positive_and_negative_numbers(lst)

#----------------
#Q8

lst=["books", "pen", "table","ant","ad"]

def create_new_list_min3_character(lst):
    new_lst = []
    for i in lst:
        if len(i) >= 3:
            new_lst.append(i)

    return new_lst

#----------------
#Q11

lst_str=["a","b","c","d"]
string=""

def concatination_strings(lst):
    for letter in lst:
        global string
        string=string+letter

    return string
#print(concatination_strings(lst_str))

# Question (remove all occurences)
# Write a function that takes a string and a letter string as params. The function should return a new string
# with all the occurences of letter string removed from the first parameter.

in_str = "Osmans"
letter = "s"

def remove_all_occurences(in_str: str, letter: str) -> str:
    result = ""
    for l in in_str:
        if l != letter:
            result = result + l

    # return "".join(lst)
    return result

print(remove_all_occurences("Osmans", "s"))
print(remove_all_occurences("", "s"))
print(remove_all_occurences("Oman", "s"))
# print(remove_all_occurences("Os12351345s", "s"))


print("Hello world")



#TODO: For loop (break and continue) 

# Question
# Print the sum of all the numbers in the list up until the first 0 
lst = [1,2,3,0,5,9,11,12]
total = 0
for num in lst:
    if num == 0:
        break
    else:
        total = total + num
        
for num in lst:
    if num == 0:
        break
    total = total + num
print(total)

# Question
# Given a list find sum of all numbers in the list. howevre, if the number is not even instead of adding that number to the sum
# add 1
lst = [5, 6, 8, 9] 
my_sum = 0
for num in lst:
    if num % 2 == 0:
        my_sum += num
    my_sum += 1

for num in lst:
    if num % 2 == 0:
        my_sum += num
    else:
        my_sum += 1
    

for i in range(10):
    if i == 7:
        break
        print("Dilara")
    print(i)

for i in range(10):
    print("Osman")
    break


#TODO: While loops

# Question
# Print the elements of the list using while loop
index = 0
while index < len(lst):
    print(lst[index])
    index += 1

# Question (Guess the number)
# Program picks a number between 0 and 100
# User should try to guess the this number and the game whill continue until
# either the user picks the number or the user types quit
random_num = random.randint(0, 100)
correct_number = False
while correct_number == False:
    user_guess = input('Guess random number or quit: ')
    if user_guess == 'quit':
        correct_number = True
        print('Next Time')
    elif user_guess == int(user_guess):
        correct_number = True
        print("Good Job")

# Question
# Print all the powers of the number until we hit 10000
def print_powers(number):
    power_counter = 1
    while number ** power_counter < 1000:
        print(number ** power_counter)
        power_counter += 1


#TODO: For loop vs while loop