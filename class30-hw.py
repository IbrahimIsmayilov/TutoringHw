# NOTE: For all the function that you write for all the HWs, MAKE SURE TO SPECIFY THE TIME COMPLEXITY
# AS PART OF YOUR SOLUTION. I will remind it for couple of classes and later I expect you just do it
# for all the functions that you write.

# We will learn more about Git and command line in upcoming classes so please make sure:
# TODO: Make sure you have Git installed and comfortable with Git "add", "commit", "checkout" workflows.
# TODO: Make sure you have access to command line and are comfortable with commands that we have covered so far.

# Question
# complete the body of the function such that it finds the missing number in
# a list within which numbers go from 1 to len(lst) + 1. There will be only one number missing in an input
# list.
# Your solution must have linear time complexity (linear time complexity means "n" time complexity)
# MAKE SURE TO SPECIFY TIME COMPLEXITY

# Linear time complexity
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

print(find_missing_non_sorted([4, 3, 5, 1, 6, 7, 10, 9, 8]))  # 2
print(find_missing_non_sorted([4, 5, 2, 1, 6, 7, 10, 9, 8]))  # 3
print(find_missing_non_sorted([4, 5, 2, 1, 6, 7, 3, 9, 8]))  # 10
print(find_missing_non_sorted([1]))  # 2


# Question
# Complete the body of the function such that it finds the missing numbers in
# a sorted list within which numbers go from 1 to len(lst) + 1. Your function should return the 
# list of missing numbers.
# MAKE SURE TO SPECIFY TIME COMPLEXITY

# Linear time complexity O(N) where N = len(lst)
def find_missing_list(lst: list[int]) -> list[int]:
    missing_nums = []
    for index in range(len(lst) - 1):
            
        if lst[index + 1] != lst[index] + 1:
            missing_nums.append(lst[index] + 1)

    if lst[-1] != len(lst) + 1:
        missing_nums.append(len(lst) + 1)

    return missing_nums

print(find_missing_list([1, 2, 3]))  # 4
print(find_missing_list([1, 3, 4]))  # 2
print(find_missing_list([1, 2, 3, 4, 6]))  # 5
    

# For each function below tell its time complexity.
# Make sure to explain your rational (how you came up with that time complexity) in great detail!!!
# Time Complexity: Outer loop requires us to traverse N, where N = len(lst) amount of times. Inner loop requires us to iterate 4 times. For every element in the lst, we have to iterate through the inner loop 4 times. Therefore, the answer would be just O(N) where N = len(lst) or linear time complexity.
def foo(lst: list[int]) -> None:
    for num in lst:
        for j in range(4):
            print(num)

# Time Complexity: Outer loop requires us to traverse N, where N = len(lst) amount of times. Inner loop requires us to iterate 4 times. For every element in the lst, we have to iterate through the inner loop 4 times. Therefore, the answer would be just O(N) where N = len(lst) or linear time complexity.
def foo2(lst: list[int]) -> None:
    for num in lst:
        for j in range(4):
            print(j)

# Time Complexity: i start out as 0 and concatenates until it is the same size of the len(lst). Therefore this function will iterate a len(lst) amount of times or O(N) amount of times where N = the size of the list. This function has linear time complexity.
def foo3(lst: list[int]) -> None:
   i = 0 
   while i < len(lst):
       print(lst[i])
       i += 1

# Time Complexity: This function has infinite time complexity. i intially starts out as 0, j then equals i or 0 and the second while loop guarantees that the function causes the program to repeat lst[j] endlessly as both variables remain unchanged. Therefore, O(∞) time complexity.
def foo4(lst: list[int]) -> None:
   i = 0 
   while i < len(lst):
       j = i
       while j < len(lst):
           print(lst[j])
           
# NOTE That for leetcode questions too, I expect you to write down time complexities as part of your solution.
# As well as, make sure to provide your leetcode answer in your homework submission to since I cannot view
# your submissions on leetcode.
# Leetcode:
# 1. https://leetcode.com/problems/palindrome-number/description/
#    There is also a follow up part to the question. Make sure you to do that too!
# 2. https://leetcode.com/problems/length-of-last-word/description/
# 3. https://leetcode.com/problems/plus-one/description/

# First Leetcode
# Passed, time complexity is O(N) due to the string reversal, where N = length of the string form of x. Linear time complexity
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

print(isPalindrome(121))  # True



# The follow up where I cannot convert to a string, passed Leetcode.
# Time complexity: Logarithmic Time complexity, O(log(N), base = 10), where N = x
import math
def isPalindrome(x: int) -> bool:
    palindrome_num = 0
    counter = 0
    while 10 ** counter <= x:
        last_digit = (x // (10 ** counter)) % 10
        palindrome_num += 10 ** (math.floor((math.log(x, 10))) - counter) * last_digit
        counter += 1

    return palindrome_num == x

print(isPalindrome(121))  # True


# Second Leetcode 
# Passed Leetcode
# Time complexity: Linear time complexity, O(N) where N is the length of the string. I say this because the spaces after the last word could be almost endless making the remaining length of the string insignificant. 
def lengthOfLastWord(s: str) -> int: 
    index = -1
    letter_count = 0
    while s[index] == ' ':
        index -= 1

    while s[index] != ' ':
        letter_count += 1
    
        if index == -len(s):
            break
        else:
            index -= 1
    
    return letter_count

print(lengthOfLastWord('John '))  # 4
print(lengthOfLastWord('Ibrahim wrote some stuff  '))  # 5


# Third Leetcode
# Passed
# Time Complexity: I am very unsure about this. Since time complexity usually covers the worst case, it would be linear time complexity because all of those 9s in the digits list would eventually become 0 and an additional appending of 0. Therefore, I am guessing O(N) time complexity where N is the length of the digits. 
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

print(plusOne([9, 9, 9]))  # [1, 0, 0, 0]
        

    
    
    


    
        
    

        