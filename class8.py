# Question (Integers digits)
# Write a function that takes integer as an input parameter and prints all of its digits from right to left
# Ex. 5789 should print:
# 9
# 8
# 7
# 5

# def integers_digits(num:int):
#     num = str(num)
#     num = num[::-1] #"316784"
#     for digit in num:
#         print(digit)
        
# integers_digits(18)

# num = "487613"
# num = num[::-1] #"316784"

# for digit in num:
#     print(digit)

# 487613

# num = 487613
# num % 10 => 3 
# num // 10 = 48761

# num = 48761
# num % 10 => 1

# num = 4876
# num % 10 => 6

# def integers_digits(num: int):
#     pass

# def find_number(number):
#     for i in range(5):
#         print(number % 10)
#         number = number // 10

# find_number(41)

# def digit_func(num:int):
#     global num_mod
#     while num>0:
#         num_mod=num%10
#         print(num_mod)
#         num=num//10

# def integers_digits(num: int):
#     while num > 0:
#         print(num % 10)   
#         num = num // 10   
# integers_digits(5789)

# digit_func(1234)

# Dictionaries
# key, val
# word, definition

# print(people["Osman"])
# print(people["Habil"])

lst = ["a", "b"]
lst.append('c')

name = "Osman"
# name[0] = "c"

people = {"Osman": 24, "Habil": 24}
people["Leyla"] = 20

# print(people["Ibrahim"]) Errors
del people["Leyla"]
print(people)

people['Osman'] = 30
print(people)

people = {"Osman": 24, "Habil": 24}
for key in people.keys():
    print(key)
    

for value in people.values():
    print(value)
    
for key, value in people.items():
    print(key)
    print(value)

people[1] = 20

# Dictionary keys should be non mutable

# people[[1]] = 3

def generate_frequencies(sentence: str) -> dict:
    pass

result = generate_frequencies('asduhbguiahegrioeurhgiueirhg')
print(result["a"])
print(result["g"])

p = {"b": 3, "a": 8}
print("a" in p)

"a" in "asdfhgwoiurthwro"

1 in [1,5,6,87]

def generate_frequencies(sentence: str) -> dict:
    count = 0
    dictionary = {}
    for character in sentence:
        if character in dictionary:
            count += 1

# result = generate_frequencies("asdsfgjkgjflkkasaskalsklaks")
# print(result['a'])
# print(result["g"])

def generate_frequencies(sentences):
    results = {}
    for letter in sentences:
        # letter = "a"
        # results = {"a": 1, "b": 1, "c": 1}
        if not letter in results:
            results[letter] = 0
        results[letter] = results[letter] + 1
        
        results[letter] = results.get(letter, 0) + 1
    return results

generate_frequencies("abca")

# {"a": 2, "b": 1, "c": 1}

people = {}
people["osman"] = 28