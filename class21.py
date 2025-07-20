# Question (Fix Binary Search)
# The function below does not work when called with binary_search([10, 20], 20). Why? What is the problem? 
# Identify the reason and fix the implementation of the binary search.
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1
#     while True:
#         middle_idx = (left + right) // 2
#         middle_elem = lst[middle_idx]
#         if middle_elem < target:
#             left = middle_idx
#         elif middle_elem > target:
#             right = middle_idx
#         else:
#             print(f"found the element at: {middle_idx}")
#             break
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1
#     condition = True
#     while condition:
#         middle_idx = (left + right) // 2
#         middle_elem = lst[middle_idx]
#         if middle_elem < target:
#             # lst = lst[middle_idx:]
#             left = middle_idx + 1
#             # we go to the right
#         elif middle_elem > target:
#             # we go to the left
#             # lst = lst[:middle_idx]
#             right = middle_idx - 1
#         else:
#             # We found the element
#             condition = False
#             print(f"found the element at: {middle_idx}")
            # break
# binary_search([10, 20], 20)
# binary_search([10, 20, 30, 40, 50, 60], 60)

# TODO
# Fix the Binary Search
# Do anagram question

def find_freq(param1: str) -> dict:
    """ Takes a string and generates a dictionary of letter -> count pairs"""
    empty_dict = {}
    for letter in param1:
        empty_dict[letter] = empty_dict.get(letter, 0) + 1
        # if letter not in param1:
        #     empty_dict[letter] = 0
        # empty_dict[letter] += 1
    return empty_dict

def is_anagram(param1: str, param2: str) -> bool:
    """ Given 2 strings, decide if they have exactly same number of letters of the same letters """    
    return find_freq(param1) == find_freq(param2)
    # if len(param1) == len(param2):
    #     for letter in param1:
    #         if letter not in param2:
    #             return False

    #     for letter in param2:
    #         if letter not in param1:
    #             return False
    #     return True
    # return False

# Test cases
print(is_anagram("abc", "bca")) #  True
print(is_anagram("aaa", "bca")) #  False
print(is_anagram("aab", "bba")) #  False

# Question
# Write a function that given a list of words, group them into list of lists where each work in each inner list has the same letters but maybe in different order.
# Example:
# Input: ['eat', 'tea', 'tea', 'tan', 'ate', 'nat', 'bat']

# Output: [['eat', 'tea', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Steps
# 1. Write a helper function to decide if 2 words should be grouped together in the first place.
# 2. Group the words into individual lists

# Interview process/problem solving process
# 1. Familirize ourselves with the question. Clairfy things from the interviewer
# 2. Create a rough plan/steps
# 3. Start coding the steps 


# Questions to contemplate over.
# What should be added to result? [word]
# When should it be added? Only when we know that there is not a single list in result where the current word belongs to.

# Input: ['eat', 'tea', 'tea', 'tan', 'ate', 'nat', 'bat']
# def generate_anagram_list(words: list) -> list[list[str]]:
#     result = [["eat"], ["boo"]]
#     for word in words:
#         for inner_list in result:
#             if is_anagram(word, inner_list[0]):
#                 inner_list.append(word)
#             # else:
#             #     result.append([word])
#     return result


# Are we going to have multiple groups in result that are anagrams?
[["eat"], ['tea']]
[["eat", "ate"], ['tea', "ate"]]

def generate_anagram_list(words: list) -> list[list[str]]:
    result = []
    for word in words:
        was_grouped = False
        
        for inner_list in result:
            if is_anagram(word, inner_list[0]):
                inner_list.append(word)
                was_grouped = True
        
        if not was_grouped:
            result.append([word])
    return result

print(generate_anagram_list(['eat', 'tan', 'ate', 'nat', 'bat']))

    # my_dict = {}
    # for word in words:
    #     if word not in my_dict.keys():
    #         my_dict[key] = []
            
    #     for key, val in my_dict.items():
    #         if is_anagram(key, word):
    #             my_dict[key].append(word)



# Introduction to command line


# Introduction to version control

# Go over Insertion sort/Bubble sort
# TODO HW explore dicitonary get method

# Command line
# pwd (point working directory)
# ls (list s)