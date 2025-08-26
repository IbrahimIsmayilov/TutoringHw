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
    """
    Check whether or not the elements in a list could sum up to a given target. 
    """
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
# How many bytes are needed to store a string in memory?  # It depends on the length of the string. The length of the string dictates the continous amount of bytes needed in the memory. 1 character occupies one byte. 
# How many bytes are needed to store an integer in memory?  # 4 Bytes
# How many bytes are needed to store a boolean in memory?  # 1 Bit, 1 Byte.
# How many bytes in memory does each of the following variables occupy?
a = "Osman"  # 5 Bytes
a = 19  # 4 Bytes
a = [66, 20]  # 8 Bytes
a = ["Osman", "Leyla"]  # 10 Bytes
a = ["Osman", 54, 61]  # 13 Bytes

# Question
# Which one is faster: RAM or Storage?
# RAM is much faster, has to deal with less data and can search through much faster. 

# Question
# Why do we have memory and storage in the system?
# Memory communicates between the CPU and the Storage the necessary data regarding a program being run, like variables. Memory is a temporary storage that gets deleted after a session and allows a program to execute quicker. It achieves this through not having to iterate through the storage to find any variables or any other data it needs and only through a smaller, temporary storage known as the RAM. Storage allows files to be saved even if a session ends, allowing for a permanent preservation of files.

# Question
# Convert following binary numbers into a decimal numbers.
# 0001 = 1 * 2 ** 0 = 1
# 0010 = 1 * 2 ** 1 = 2
# 0100 = 1 * 2 ** 2 = 4
# 1000 = 1 * 2 ** 3 = 8
# 1011 = (1 * 2 ** 0) + (1 * 2 ** 1) + (1 * 2 ** 3) = 11
# 1111 = (1 * 2 ** 0) + (1 * 2 ** 1) + (1 * 2 ** 2) + (1 * 2 ** 3) = 15
# 1101 = (1 * 2 ** 0) + (1 * 2 ** 2) + (1 * 2 ** 3)  = 13

# Leetcode