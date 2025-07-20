# Question
# Explore dicitonary "get" method

# Question
# We implemented Binary search in the previous class.
# In the worst case how many times will we enter for loop when
# the lenght of the list is:
# 6  Worst case: 3 | Best Case: 1
# 32  Worst Case: 5 | Best Case: 1
# 100  Worst Case: 7 | Best Case: 1
# 500000  Worst Case: 19 | Best Case: 1
# 1000000  Worst Case: 20 | Best Case: 1
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    condition = True
    while condition:
        middle_idx = (left + right) // 2
        middle_elem = lst[middle_idx]
        if middle_elem < target:
            left = middle_idx + 1
        elif middle_elem > target:
            right = middle_idx - 1
        else:
            condition = False
            print(f"found the element at: {middle_idx}")
            break
        
# Question
# What is the worst case and best case time complexities of the following functions:
# Worst Case: 2n | Best Case: 2n
def print_numbers(n: int):
    for i in range(n):  
        print(i)

    for j in range(n, 0, -1): 
        print(j)


# Worst Case: n^2 | Best Case: n^2
def dependent_loopsloops(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, j)

# Worst Case: n^3 | Best Case: n^3
def nested_loops(n: int):
    for i in range(1, n + 1): 
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                print(i, j, k)

# Worst Case: log2(n) | Best Case: log2(n)
def foo(n: int):
    while n > 1:
        print(n)
        n = n // 2

# Worst Case: 3n | Best Case: 3n
def zoo(n: int):
    for i in range(n):
        print(i)

    for i in range(2*n):
        print(i)

# Worst Case: n^2 | Best Case: n^2
def boo(n: int):
    for i in range(n ** 2):
        print(i)
        
# Worst Case: 2^n | Best Case: 2^n
def goo(n: int):
    for i in range(2 ** n):
        print(i)

