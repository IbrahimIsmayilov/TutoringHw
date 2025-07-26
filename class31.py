# Question
# complete the body of the function such that it finds the missing number in
# a list within which numbers go from 1 to len(lst) + 1. There will be only one number missing in an input
# list.
# Your solution must have linear time complexity (linear time complexity means "n" time complexity)
# MAKE SURE TO SPECIFY TIME COMPLEXITY

# O(n)
def find_missing_numer(lst: list[int]) -> int:
    s = set() # 1
    for i in range(1, len(lst) + 2): # len(lst)
        s.add(i) 
    
    for num in lst: #O(n)
        s.discard(num)
    return s

# O(n)
def find_missing_non_sorted(lst: list[int]) -> int:
    all_list_len = len(lst) + 1.
    all_list_elem_sum = all_list_len * (1 + all_list_len) // 2
    
    # The numbers in our list ends up forming an arithmetic sequence. 1 ... len(lst) + 1, by 1.
    # We can find the sum of arithmetic sequence.
    missing_list_sum = sum(lst) # O(n)

    return int(all_list_elem_sum - missing_list_sum)

# What do we choose our solutions by?
# 1. Time complexity: CPU (Centeral Processing Unit)
# 2. Space complexity: RAM (Random Access Memory)
# 3. Elegance/cleanliness/readibility/maintanibility.

1, 2, 3, 4, 5 # => 15
1, 2, 3, 4 # => 10

def find_missing_non_sorted(lst: list[int]) -> int:
    num_set = set()

    # O(N), where N = len(lst)
    for index in range(len(lst)):
        # All of these are O(1), constant time
        if lst[index] != len(lst) + 1:
            if lst[index] + 1 in num_set:
                num_set.remove(lst[index] + 1)
            else:
                num_set.add(lst[index] + 1)

        # All of these are also O(1), constant time
        if lst[index] != 1:
            if lst[index] in num_set:
                num_set.remove(lst[index])
            else:
                num_set.add(lst[index])  
    return min(num_set)  # O(2), constant time

find_missing_non_sorted([1,5,4,2])


# We can go over the list, for each number check what number do we expect to come after that.
# If that number is not there, we add to the set, as we go, if we see that number, we will remove it
# from the set. 
# there will be a number that is in the set.


# SPECIAL CASES ARE OUR ENEMIES!!!
# if we have too many special cases, we can probably simplify the solution.


# 1. 1 ... len(lst) + 1
# 2. Add all the numbers that we expect in the list to the set.
# 3. Go over the list, remove the existing numbers.
def find_missing_numer(lst: list[int]) -> int:
    s = set() # 1
    for i in range(1, len(lst) + 2): # len(lst)
        s.add(i) 
    
    for num in lst: #O(n)
        s.discard(num)
    return s

# Sets are implemented using hash table. Time complexity of removing and adding to the has table is constant.
# Hash table operations are not really a constant time but for all practical reasons we can assume so.

#print(foo([1,5,4,2]))


def isPalindrome(x:int) -> bool:   # Time complexity len(lst)
    return str(x)[::-1] == str(x)

# 1. what are we trying to do in this piece of code. 
# 2. Is there another way of doing this?

# 2n + log(n) = O(n)
# What is n in this context anyways? n is the number of digits in the parameter.
def foo(n):
    for i in range(n):
        print(n)

def plusOne(digits:list) -> list:  #Time complexity - len(lst)
    result = 0
    for i in digits:
        result = result * 10 + i
    result = 129

    result += 1   
    # TODO Conversion time complexity
    new_digits = str(result)  # log(n)

    result_digits = []
    for elem in new_digits:
        result_digits.append(int(elem))

    return result_digits
plusOne([1,2,9])


def plusOne(digits: list[int]) -> list[int]:
    checked_index = -1
    digits[checked_index] += 1
    while digits[checked_index] == 10:
        digits[checked_index] = 0

        if checked_index == -len(digits):
            digits.append(0)

        checked_index -= 1 
        digits[checked_index] += 1
    
    return digits
