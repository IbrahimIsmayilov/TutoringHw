# Question
# Complete the body of the function which takes a number and it needs to return
# in how many ways you can add up numbers from 1 - that number so it is equal to that number.

#sum_combination(4)
# 1 + 3
# 3 + 1

# 2 + 2
# Steps
#
def sum_combination(n: int) -> list[int]:
    lst = []
    for num in range(1, n // 2 + 1):
        lst.append((num, n - num))
    return lst

print(sum_combination(11))

#sum_combination(4)
# 1, 3
# 1, 1, 1, 1
# 2, 2
# 2, 1, 1

#[(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)]
# 11 =  1 + 10

# 10 = 8
# 2 8
# 3 5
# 1
# 2


# Dynamic programming
# You want to memorize the solution to the smaller problems as you solve them.
memory = {}
count = 0
def sum_combination(n: int):
    global memory, count
    count += 1
    if n in memory:
        return memory[n]
    print(n)
    total = 0
    # n = 3
    if n == 1:
        return total

    for num in range(1, n):
        # num = 1
        # num = 2
        total += (sum_combination(num) + sum_combination(n - num))
    memory[n] = total + 1
    return total + 1

count = 0
def sum_combination(n: int):
    global count
    count += 1
    print(n)
    total = 0
    # n = 3
    if n == 1:
        return total

    for num in range(1, n):
        # num = 1
        # num = 2
        total += (sum_combination(num) + sum_combination(n - num))
    return total + 1
# 1 + 2
# 2 + 1

# 1 - 1
#1 + 1 + 1
#2 + 1

print(sum_combination(11)) # 9
print(count)

# 1 + 1 + 1 + 1
# 1 + 2 + 1
# 1 + 3
# 2 + 2

# Question
# You are given a string of paranthesis, you need to decide if that is a valid set of paranthesis.

def is_valid(paranthesis: str) -> bool:
    pass

# You need to use stack here.
# You need to use python list to solve this problem.

print(is_valid("()"))
print(is_valid("()()"))

print(is_valid("(()())"))   # yes
print(is_valid("(()())()")) # yes

print(is_valid("(()(")) # no
print(is_valid(")())")) # no

print(is_valid("((()())"))