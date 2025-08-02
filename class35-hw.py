# TODO There is a command line tool called "grep". Use the "man" command to learn more about grep. 
# - Give couple of examples how you would use grep command
# - Give couple of flags that you liked about grep command and describe in your own words what they do.

# TODO Create a Github repository for assignment1, make and initial commit and write down your link to the repo down below.
# Start working on your assingment ASAP. It is not trivial and needs lots of work.

# Question (Bigger right)
# We look at this quesiton during the class and said that the time complexity of the solution below is n ** 2
# However, there is a way of solving this question faster. I already gave a hint that you can solve this quesiton faster by using Stack.
# Try to solve the question using stack. Describe all your steps challenges in great detail!!!!
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