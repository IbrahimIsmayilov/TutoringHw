# Question
# We have covered a reccursive quesiton sum_target in the class.
# Complete the reccursive implementation.

# 1. figure out the smaller questions. 
# We see if the target is equal to the first element, we look for the target in the elements preceeding the current element.
# Target changes if the first element is smaller than the target. New target becomes the old target - the first element
# 2. when you find an answer to smaller questions, how do u use them to find the answer to the current question.
# You or the results of the smaller questions.
# 3. when do we stop? When the target reaches 0.1

def sum_target(lst: list[int], target: int) -> bool:
    
    if target == 0:
        return True
    elif target < 0:
        return False
    elif len(lst) == 0 and target > 0:
        return False
         
        
    
    q1 = sum_target(lst[1:], target)
    q2 = sum_target(lst[1:], target - lst[0])

    return q1 or q2


print(sum_target([10,1,1,4], 5))  # True

    





# Question
# How many bits in a byte? There are 8 bits in a byte. 

# Question
# How many bits in 7 bytes? There are 56 bits in 7 bytes. 

# Question
# How many bytes are needed to store a string in memory?
# 
# How many bytes are needed to store an integer in memory?
# How many bytes are needed to store a boolean in memory?
# How many bytes in memory does each of the following variables occupy?
a = "Osman"
a = 19
a = [66, 20]
a = ["Osman", "Leyla"]
a = ["Osman", 54, 61]

# Question
# Which one is faster: RAM or Storage?
# RAM is much faster, has to deal with less data and can search through much faster. 

# Question
# Why do we have memory and storage in the system?

# Question
# Convert following binary numbers into a decimal numbers.
# 0001
# 0010
# 0100
# 1000

# 1011
# 1111
# 1101

# Leetcode