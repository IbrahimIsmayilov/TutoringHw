# TODO count_occurence with reccrusion

def count_occurece(lst: list[int], target: int) -> int:
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count

#def count_
a = 10
a = 5
print(a)

count_occurece([10, 20, 10, 30, 10, 70], 10) # => 3
#[10, 20, 10]
#[10]
#[20, 10]
#
#[30, 10, 70]
# We use reccursion when to find an answer to our current solution there are smaller same problems to be solved.

# Reccursion
# 1. figure out the smaller questions
# 2. when you find an answer to smaller questions, how do u use them to find the answer to the current question.
# 3. when do we stop? Hitting the bottom of the reccursion.


# 1 listi yariya boluruk, her bolunmus listde axtardigimiz ededin sayini tapiriq
# 2 butun bolunmus listlerdeki axtarilan ededlerin sayini toplayiriq
# 3 bolunen listin olcusu 1-e beraberdise dayaniriq

# 1. figure out the smaller questions. The smaller question is, how many occurences of the target occurs in the first and second half 
# of the given list. Instead of checking a list by itself, divide into 2 lists or 2 smaller problems.
# 2. when you find an answer to smaller questions, how do u use them to find the answer to the current question. # 
# Add the occurrences to return the total amount of occurences in the list.
# 3. when do we stop? Hitting the bottom of the reccursion. When the length of the given list is 1: Check if it is the 
# target, if so return 1. Else return 0. If we continue dividing a list with a length of 1 element into 2 elements, we will run into an error.


# 1. How many times does target occur in the rest of the list after the first element?
# 2. Add 1 if the first element matches the target, otherwise 0, to the answer from the smaller question.
# 3. When the list is empty, return 0