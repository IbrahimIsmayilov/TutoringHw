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
# Step 2: Create an empty list and intialize it to return at the end. 
# Step 3: Iterate through the given list and begin with adding elements to the stack and the created list
# Step 4: Continue iterating through the list and adding the indexes of elements to the stack and list. After adding the first element, check if second element is greater than first element. If not, compare third element with second element and so forth. The priority with which element to compare changes as you add more elements to the stack.
# Step 5: If you find a greater element than the index at the top of the stack, pop from the stack. Catch the returned index value and replace the index in the created list with the greater element until the stack is empty or the element referenced by the index at the stack is greater. If the element referenced by the stack is greater, break the while loop as logically it means that all other elements referenced by the stack are greater too.
# Step 7: Continue until the end of the loop. Stop before checking the last index.
# Step 8: Add a -1 to the created list because the last value in the list will never find any element greater.
# Step 9: To ensure all elements that did not have greater elements to their right are assigned -1, pop from the stack until it is empty, catch the returned indexes and replace them with -1. 
# Step 8: Return the created list


# Time Complexity: O(N), where N = length of the given list. Linear time complexity. Worst Case: Roughly O(2N).
def bigger_right(lst: list) -> list:
    stack_lst = []
    result_lst = []
    for idx in range(len(lst) -1):
        stack_lst.append(idx)
        result_lst.append(lst[idx])
        while len(stack_lst) > 0 and lst[idx + 1] > lst[stack_lst[-1]]:
            result_lst[stack_lst.pop()] = lst[idx + 1]

                    
    result_lst.append(-1)
    while len(stack_lst) != 0:
        result_lst[stack_lst.pop()] = -1
            

    return result_lst 


        
print(bigger_right([5, 4, 3, 2, 1, 6]))  # [6, 6, 6, 6, 6, -1]
print(bigger_right([1, 4, 3, 2, 9, 0, 3, 1, 10, 4, 1]))  # [4, 9, 9, 9, 10, 3, 10, 10, -1, -1, -1]

            
        


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