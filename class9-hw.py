# Question (Print keys)
# Function takes a dictionary as a parameter and prints all the keys.
def print_keys(param1: dict) -> None:
    for key in param1.keys():
        print(key)

print_keys({'ibrahim': 4, "adam": 5})  # ibrahim\n, adam\n


# Question (Print values)
# Function takes a dictionary as a parameter and prints all the values.
def print_values(param1: dict) -> None:
    for value in param1.values():
        print(value)

print_values({'ibrahim': 4, "adam": 5})  # 4\n, 5\n


# Question (Print key-values)
# Function takes a dictionary as a parameter and prints each key-value pair
# on the same line.
# param1 = {"Osman": 24, "Leyla": 22} <= should be printed like:
# Osman, 24
# Leyla, 22
def print_items(param1: dict) -> None:
    for key, value in param1.items():
        print(f'{key}, {value}')

print_items({"Osman": 24, "Leyla": 22})  # ibahim, 4\n, adam, 5\n


# Question (Most populated city)
# Function takes a dictionary as an argument. Each key in the argument
# is a city name as string and value is the list of the names of the people living in that city.
# Function should return the name of the most populated city.
# Ex. argument: population_map = {"Toronto": ["Farid", "John"], "Ottawa": ["Osman"]}
def most_populated_city(population_map: dict) -> str:
    max_pop = 0
    for key, value in population_map.items():
        if len(value) > max_pop:
            max_pop = len(value)
            max_city = key

    return max_city

print(most_populated_city({"Toronto": ["Farid", "John"], "Ottawa": ["Osman"]}))  # 2\n


# Question (Total population)
# Function takes a dictionary as an argument. Each key in the argument
# is a city name as string and value is the list of the names of the people living in that city.
# Function should return total number of people living in all cities
# Ex. argument: popuplation_map = {"Toronto": ["Farid", "John"], "Ottawa": ["Osman"]}
def total_population(population_map: dict) -> int:
    sum_pop = 0
    for population in population_map.values():
        sum_pop += len(population)
    
    return sum_pop

print(total_population({"Toronto": ["Farid", "John"], "Ottawa": ["Osman"]}))  # 3\n


# Question (Reverse key-values)
# Function takes a dictionary as an argument. Each key in the argument is a persons name
# and the value is persons age. Ex. age_mapping = {"Osman": 24, "Leyla": 22, "John": 22}
# 2 people can have the same age. 
# Complete the body of the function such that it returns
# a new dictionary where keys are ages as integers and values are list of names of people
# who are that age from the input dictionary.
def reverse(age_mapping: dict) -> dict:
    reversed_dict = {}
    for key, value in age_mapping.items():
        value = str(value)

        if not value in reversed_dict:
            reversed_dict[value] = []

        reversed_dict[value].append(key)

    return reversed_dict

print(reverse({"Osman": 24, "Leyla": 22, "John": 22}))  # {'24': ['Osman'], '22': ['Leyla', 'John']}\n

# Question (Most frequent number)
# Write a program that will keep asking a user to input numbers indefinitelly.
# At any point the user can type "Z" as a result of which your program should output
# the number that has been entered the most thus far.

def most_freq_num() -> int:
    num_count = {}
    user_input = input('Please enter a number or "Z": ')
    while user_input != 'Z':
        user_input = input('Please enter a number or "Z": ')
        if user_input not in num_count:
            num_count[user_input] = 0
        if user_input in '0123456789':
            num_count[user_input] += 1

    max_ocurrence = 0
    most_occur_num = None

    for key, value in num_count.items():
        if value > max_ocurrence:
            max_ocurrence = value
            most_occur_num = key

    return most_occur_num

print(most_freq_num())




# Question (Jumping man)
# The below function takes 3 parameters.
# islands: each index of this parameter is an island. However, number at each index is by how much a man on that island should jump to the right.
# Ex. islands = [4, 3, 2, 1, 1, 1, 7, 2]. 
#                ^           ^
#                |         This is island 4
#         This is island 0      
# If you stand at island 9, you should jump 4 islands ahead, meaning that after a jump you will be at island 4. From island 4, you will jump 1 island only.
# start: indicates the start island position of the man. 

# The below function should return at which island will the man end up after n jumps.
# Think about what is appropriate thing to do if the jump puts a man on an island that is beyond islands list.

def landing_n(islands: list[int], start: int, n: int) -> int:
    position = start
    
    for i in range(n):
        position = (position + islands[position]) % len(islands)

    return position

print(landing_n([4, 3, 2, 1, 5, 5, 7, 2], 4, 3))  #  1\n


