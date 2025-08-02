# Go over the assignment
# Go over a question
# Question
# We are given a list of numbers
# We need to create a new list of the same size as original where every elment of the new list
# maps to the other list in the following manner:
# [2, 4, 9, 6, 2, 1, 7 ,0]
# [4, 9,-1, 7, 7, 7, -1, -1]

# Steps
# - create an empty list
# - we need to go over each element of the list
# - for each element we need to start looking at each element to its right
# - when we find the first bigger element than the current element, we can add it to the list. Stop when u find the element
# - Add -1 to the result list
# - At the end return the list

def bigger_right(lst: list[int]) -> list[int]:
    curr_idx = 0
    lst = []
    for i in range(curr_idx + 1, len(lst)):
        if lst[i] > lst[curr_idx]:
            lst.append(lst[i])

[2, 1, 0, 5]
# Dynamic programming: u need to memorize only if it makes sense to search for what u memorized
# The time complexity is n**2
def bigger_right(lst):
    result = []
    for i in range(len(lst)):
        original_len = len(result)
        # i = 7
        for j in range(i+1,len(lst)):
            if lst[i] < lst[j]:
                result.append(lst[j]) 
                break 
        if original_len == len(result): 
            result.append(-1)
    return result

print(bigger_right([2, 1, 7 ,0]))
[2, 1, ]
# Look back at dynamic programming question
# learn about grep command