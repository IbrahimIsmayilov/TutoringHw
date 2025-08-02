# TODO There is a command line tool called "grep". Use the "man" command to learn more about grep. 
# - Give couple of examples how you would use grep command
# - Give couple of flags that you liked about grep command and describe in your own words what they do.

# TODO Create a Github repository for assignment1, make and initial commit and write down your link to the repo down below.
# Start working on your assingment ASAP. It is not trivial and needs lots of work.

# Question (Bigger right)
# We look at this quesiton during the class and said that the time complexity of the solution below is n ** 2
# However, there is a way of solving this question faster. I already gave a hint that you can solve
#  this quesiton faster by using Stack.
# Try to solve the question using stack. Describe all your steps challenges in great detail!!!!

# Step 1: Create a stack implementation list and intialize it
# Step 2: Create an empty list and intialize it to return at the end
# Step 3: Iterate through the given list and begin with adding the first element to the stack
# Step 4: Continue iterating through the list and adding the elements to the stack. After adding the first element, check if second element is greater than first element. If not, compare third element with second element and so forth. The priority with which element to compare changes as you add more elements to the stack
# Step 5: If you find a greater element than top of stack, append to the empty list len(stack) amount of times. Pop as you remove from the stack
# Step 7: Continue until the end of the list. Stop before checking the last index and append -1 to the result list
# Step 8: Return list


def bigger_right(lst: list) -> list:
    stack_lst = []
    result_lst = []
    for idx in range(len(lst) -1):
        stack_lst.append(lst[idx])
        if lst[idx + 1] > stack_lst[-1]:
            while len(stack_lst) > 0:
                result_lst.append(lst[idx + 1])
                stack_lst.pop()

    result_lst.append(-1)
    return result_lst
            
            
        


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

# Leetcode
# 1. https://leetcode.com/problems/pascals-triangle/description/