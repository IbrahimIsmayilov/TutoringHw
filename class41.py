# TODO Go over the assignment point out improvements
# TODO Warm up question
# Question
# You are given a list of numbers and a target. Decide if there are any subset of numbers in your list that add up to the 
# target value
def sum_target(lst: list[int], target) -> bool:
    pass

# Ex. sum_target([1,2,2,10], 5) True
# List is not sorted
# No negative numbers

# does 2 numbers add up to a target
# does 3 numbers add up to a target?
# does 4 numbers add up to a target?

# GREAT!!!!
# This looks like a reccursive function? Yes/No
# Ex. sum_target([1, 10, 2, 2], 5) True
# Ex. sum_target([10, 2, 2], 4) True

# Ex. sum_target([2, 2], 4) True
# Ex. sum_target([2], 2) True
# Ex. sum_target([], 0) True

# Ex. sum_target([1, 10, 2, 2], 4)
# Ex. sum_target([10, 2, 2], 3) False
# Ex. sum_target([10, 2, 2], 4) True

# True True    => True
# False True   => True
# False False  => False
# True False   => True


# Ex. sum_target([2, 2], 3)
# Ex. sum_target([2], 1)

# We use reccursion when to find an answer to our current solution there are smaller same problems to be solved.


# 1. figure out the smaller questions. 
# We see if the target is equal to the first element, we look for the target in the elements preceeding the current element.
# Target changes if the first element is smaller than the target. New target becomes the old target - the first element
# 2. when you find an answer to smaller questions, how do u use them to find the answer to the current question.
# You or the results of the smaller questions.
# 3. when do we stop? When the target reaches 0.
 
 
 
def sum_target(lst: list[int], target: int) -> bool:
    target2 = target
    first_elem_removed = False
    for elem in lst:
        if elem > target:
            lst.remove(elem)
        else:
            target -= elem
            lst.remove(elem)

def sum_target(lst: list[int], target: int) -> bool:
    if len(lst) == 1:
        if lst[0] == target:
            return True
        elif lst[0] < target:
            new_target -= lst[0]

        return False

    q1 = sum_target(lst[1:], target)
    q2 = sum_target(lst[1:], target - lst[0])

    return q1 or q2
# Ex. sum_target([1, 10, 2, 2], 4)
# Ex. sum_target([1], 4)


# Ex. sum_target([10, 2, 2], 3) False
# Ex. sum_target([10, 2, 2], 4) True
 
# TODO binary to decimal conversion
# byte & bit
# 1 byte =  8 bit

# 435748 <= decimal number
# 10101011110 <= binary number


# 1101 => <bit value> * 2 ** (nth bit) <= sum all of these up
# 1 * 2 ** (0) + 0 * 2 ** 1 + 1 * 2 ** 2 + 1 * 2 ** 3 = 1 + 0 + 4 + 8 = 13


# 1000001111010100101010

# TODO Process lifecycle in the memory
def foo(x) -> list[str, int]:
    pass