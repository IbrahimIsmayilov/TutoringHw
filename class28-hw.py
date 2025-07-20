# Question
# What is a hash function? What are the key constaints when it comes to the hash function? A hash function is a program that takes a file and converts it to a different format that always has a definite size regardless of the input. The outputs differ depending on the input in 99 percent of the cases and the same input will always get you the same output. The hashed value is used as an index to determine where to place an element in a hash table. The key constraints of a hash function is that the hashed value is unable to be reversed to find the initial value since multiple inputs can result in the same output. The mapped output scope must be the same or greater than the input scope. 

# Question
# In your own words, describe what are the key differences between decoding/ecoding vs hashing?
# When would you use one over the other? Decoding and encoding is taking a piece of data and not necesarrily converting it to a different format but hiding the message of the initial input with a program. The message can be unhidden or decoded and the existence of an encoding function depends entirely that there is a decoding function. However, this is entirely different from hashing where the mapped output value can never be used to get the initial input value. That is the main difference conceptually between the 2 functions. Moreover, hashing is not used to hide data but rather get an associated piece of data in a different format. If you are trying to create a message that will be unable to deciphered unless it is the intended audience then you should encode it. If you are trying to simply map your input value to a smaller output value in a different format consistently, then you should use a hashing function. 

# Ceasar's cipher
# In our previous class we have briefly discussed how to use Ceaser's cipher.
# Ceaser's cipher will take each letter of your text and shift it alphabetically to the right by 3 during encoding process.
# Complete the encode and decode functions for ceaser's cipher algorithms.
# Note that special characters (,!? etc) should remain as they are. Moreover, you should retain, lover and upper case
# sensitivity.
# Make sure to specify the time complexities of both of the functions!!!

# Time complexity: O(N) time complexity

import string  # O(1)
all_letters = string.ascii_letters  # O(1)

def ceaser_encode(original: str) -> str:
    encoded_word = ''  # O(1)
    
    for letter in original:  # O(n)
        initial_pos = all_letters.index(letter)  # O(52)
        if letter.isupper():  # O(1)
            encoded_word += all_letters[((initial_pos + 3) % 26) + 26]  # O(1)
        if letter.islower():  # O(1)
            encoded_word += all_letters[((initial_pos + 3) % 26)]  # O(1)
    
    return encoded_word  # O(1)

print(string.ascii_letters)
print(ceaser_encode('abcABCzZyY'))  # defDEFcCbB
print(ceaser_encode('Ibrahim'))  # Leudklp



# Time Complexity: O(N)       

def ceaser_decode(encoded_txt: str) -> str:
    decoded_word = '' # O(1)

    for letter in encoded_txt:  # O(n)
        initial_pos = all_letters.index(letter)  # O(52)
        if letter.isupper():  # O(1)
            decoded_word += all_letters[((initial_pos - 3) % 26) + 26]  # O(1)
        if letter.islower():  # O(1)
            decoded_word += all_letters[((initial_pos - 3) % 26)]  # O(1)
    
    return decoded_word  # O(1)

print('\n' + string.ascii_letters)    
print(ceaser_decode('defDEFcCbB'))  # abcABCzZyY
print(ceaser_decode('Leudklp'))  # Ibrahim
print(ceaser_decode('A'))  # X

# Question
# Why this code does not work: It returns indexes, not the letters of the original word. Also for decoding words in which letters are repeated more than twice, say 4 times, the decoded text will contain 3 instances of that letter instead of 2 that the original text had. Instead of checking every adjacent letter, it needs to divide the string in groups of 2 and check thus. 
#def my_decode(param):
#    my_decode=""
#    for i in range(len(param)):
#        if param[i]==param[i+1]:
#            my_decode += i
#
#    return my_decode
#
#print(my_decode("oossmmaann"))

# Question
# How does hash table handle collisions? When a collision occurs, the program searches for the next available place in a hash table and this can take very long at times when most of the hash table is full. It searches for the available space in a linear fashion. 

# Question
# Complete the body of the function that takes 2 sorted lists and needs to return a new list containing the elements
# in both input lists in sorted order.
def merge(lst1: list[int], lst2: list[int]) -> list[int]:
    result_lst = []
    lst1_index = 0
    lst2_index = 0

    while len(result_lst) != (len(lst1) + len(lst2)):
        if lst1[lst1_index] <= lst2[lst2_index]:
            result_lst.append(lst1[lst1_index])
            lst1_index += 1
        else:
            result_lst.append(lst2[lst2_index])
            lst2_index += 1

        if lst1_index == len(lst1):
            result_lst += lst2[lst2_index:]
        
        if lst2_index == len(lst2):
            result_lst += lst1[lst1_index:]
            

        
    return result_lst

print(merge([1, 1, 3, 6], [2, 8, 9]))  # [1, 1, 2, 3, 6, 8, 9]

            
    

# Introduction to Leetcode.
# Leetcode is a web platform where there exist lots of programming questions. You can pick a question, write
# code against it and the submit it. Leetcode in turn will run certain predefined tests to check if your functions work
# correctly. Concept of correctness has 2 meanings>
# 1. Given the input function should produce the correct output based on the question's description.
# 2. Program should run fast. For instance, if there is a way of solving a problem in len(lst) time but your solution does it
#    in len(lst) ** 2. Your solution might be considered "incorrect" - too slow, and not be accepted as a valid solution.
# Starting from now, i will provide you with a couple of leetcode questions from class to class. I expect you to attempt doing them
# and provide solutions to me as well under your HW subimission (just copy paste what you submitted in the leetcode).
# It would also be useful if you write if your code has passed leetcode or not as it will be easier for me to skim over the questions.

# Question Leetcode (Remove Duplicates from Sorted Array)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# It passed the leetcode

def remove_duplicates(nums: list) -> list:
        track_index = 0
        pos_index = 0
        while True:
            if track_index == len(nums) - 1:
                nums[pos_index], nums[track_index] = nums[track_index], nums[pos_index]
                return pos_index + 1
            elif nums[track_index] == nums[track_index + 1]:
                track_index += 1
            else:
                nums[pos_index], nums[track_index] = nums[track_index], nums[pos_index]
                track_index += 1
                pos_index += 1
        
                   
                
print(remove_duplicates([1, 1, 1, 2, 2, 3, 4, 4, 5]))
