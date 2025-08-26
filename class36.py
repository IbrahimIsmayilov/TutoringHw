# TODO grep
# TODO More command line

# TODO Reccursion

# Question
# Write a function to find a fibonacci number
#1, 1, 2, 3, 5, 8 ... 

def fib(n: int) -> int: ...

# fib(3) => 2
# fib(6) => 8

def fib(n):
    fib_list=[1]
    fib_element=0
    for i in range(n-1):
        fib_element = i + (i+1)
        fib_list.append(fib_element)
    return fib_list

print(fib(3))

# Time complexity: O(n) where n is size of fib index.
# Space complexity: O(n) where n is size of fib index.


# n, n -1, n-2, n-3, n-4

# Space complexity: O(1)
# How muc memory will we occupe  as the size of input parameters change.

# Time complexity: O(1)
# How many iterations of loops will we do as the size of input parameters change.
def foo3(n: int):
    for i in range(20):
        print(i)

def foo2(n: int):
    a = 28
    b = a * n
    return b

def fib(n: int):
    fibonacci_seq = [1, 1]
    while len(fibonacci_seq) < n:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq[-1]

def fib_ibrahim(n: int):
    count = 0
    first_num = 0
    second_num = 1
    fib_num = 1
    while count != n:
        count += 1
        fib_num = first_num + second_num
        second_num = first_num
        first_num = fib_num
    return fib_num

def fib_osman(n: int) -> int:
    prev, curr = 1, 1
    count = 2
    while count < n:
        prev, curr = curr, prev + curr
        count += 1
    return curr

# You can find the fib number in a constant time.


# What is reccursion? When do we use it? How do we use it?

# if we are solving a question answer of which depends on same smaller questions. THen we can find the answer
# to smaller questions first, use them to find the answer to current question.

# n , n -1, n - 2, n - 3, n -4

# Reccursion
# 1. figure out the smaller questions
# 2. wen you find an answer to smaller questions, how do u use them to find the answer to the current question.
# 3. when do we stop? Hitting the bottom of the reccursion.

# Do not try to walk thorugh the code of reccursion.
# Do not try to go through the function call chain.

# fib(1) = 1
# fib(2) = 1
def fib(n: int) -> int:
    # n = 2
    if n == 1:
        return 1

    if n == 2:
        return 1

    fib1 = fib(n - 1)
    fib2 = fib(n - 2)

    return fib1 + fib2

print(fib(4))
#print(fib(29))
# TODO Compute architecture