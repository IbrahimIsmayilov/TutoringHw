# # # TODO Talk more about complexity (Time Complexity and Space complexity)

# # # len(lst) is how many times we will run the print statement

# # # Worst case: len(lst)
# # # Best  case: len(lst)
# # # def foo(lst):
# # #     for num in lst:
# # #         print(num)

# # # foo([10, 20, 30, 40, 50])
# # # foo([10, 20, 30])


# # # def find_num(lst: list[int], n: int) -> bool:
# # #     "Check if n exists in lst"
# # #     for num in lst:
# # #         if num == n:
# # #             return True
# # #     return False

# # # find_num([10, 20, 30, 40], 5)                                             # Worst case: len(lst)
# # # find_num([5, 20, 30, 40,5, 20, 30, 40,5, 20, 30, 40,5, 20, 30, 40], 150)  # Best case: 1


# # # # Worst case: len(lst) * len(lst) == len(lst) ** 2
# # # # Best  case: 1

# # # # len(lst) is same as len of each element in lst
# # # def find_num_indented(lst, n) -> bool:
# # #     for inner_list in lst: # 4
# # #         for num in inner_list: # 4
# # #             if num == n:
# # #                 return True
# # #     return False


# # # find_num_indented([[10,20,30, 50], [10,20,30, 50], [10,20,30, 50], [10,20,30, 50]], 10) # Best case

# # # find_num_indented([[10,20,30], [10,20,30], [10,20,30]], 80)                             # Worst case: 9
# # # find_num_indented([[10,20,30, 50], [10,20,30, 50], [10,20,30, 50], [10,20,30, 50]], 80) # Worst case: 16


# # # Time complexity: n ** 2 == n * n
# # # Best case time complexity : n * n
# # # Worst case time complexity: n * n
# # def foo(n: int):
# #     for i in range(1, n + 1): # n
# #         for j in range(1, n + 1): # n
# #             print(i, j)
# # foo(5)

# # # Time complexity: n + n == 2 * n
# # # Best case time complexity : 2 * n
# # # Worst case time complexity: 2 * n
# # def boo(n: int):
# #     for i in range(1, n + 1):
# #         print(i)

# #     for j in range(1, n + 1):
# #         print(j)
# # boo(10)

# # # Time complexity: n * n * n
# # def fa(n: int):
# #     for i in range(1, n + 1): # n
# #         for j in range(1, n + 1): # n
# #             for z in range(1, n + 1): # n
# #                 print(i, j, z)

# # # Time complexity: n * 2n == 2 * (n ** 2)
# # def foo(n: int):
# #     for i in range(1, n + 1): # n
# #         for j in range(1, n + 1): # n
# #             print(i, j)
# #         for z in range(1, n + 1): # n
# #             print(i, z)


# # # If you another function that runs in 3n or 10000n, as far as programming is concerned, we say that all those functions run with the same speed.  O(n)
# # # 3 * n ** 2, 50 * n ** 2, these 2 programs run with the same speed as far as the programming is concerned.

# # # These functions have different speeds.
# # # n, n**2
# # # n ** 2, n**3

# # # n = 5
# # # 2n = 10
# # # n ** 2 = 25

# # # What programmers are interested in when they talk about the speed of the program is the rate of the change with regards to input.
# # # n = 5
# # # n = 10
# # # 4n = 20, 40 
# # # 
# # # 2n = 10, 20

# # # n = 5
# # # n = 6
# # # n ** 2 = 25, 36 
# # # n      = 5,  6


# # # n ** 2
# # # 2 ** n


# # # Time complexity: 2n
# # def boo(n: int):
# #     for i in range(1, n + 1):
# #         print(i)

# #     for j in range(1, n + 1):
# #         print(j)

# # # Time complexity: 3n
# # def boo2(n: int):
# #     for i in range(1, n + 1):
# #         print(i)

# #     for j in range(1, n + 1):
# #         print(j)
    
# #     for z in range(1, n + 1):
# #         print(z)

# # boo(10)
# # boo2(10)


# # # foo1, foo2, that do exactly the same thing. But one runs in n time complexity, another one runs in n ** 2. We will take the one that runs with n time complexity cause we want our program to exectue as little lines of code as possible
# # # while working correctly.


# # # The same problem is computer science can be solved multiple ways. Not all of them are the same.

# # # 2n 4n
# # # 4 1 3 Constant complexity

# # # Space complexity: 3
# # # Time complexity : n
# # def find_sum(n):
# #     result = 0
# #     result2 = 0
# #     for i in range(1, n + 1):
# #         result += i
# # find_sum(10)
# # find_sum(10000000)


# # # Time complexity: n
# # # Space compleity: 
# # def generate_lst(n):
# #     lst = []
# #     for i in range(1, n + 1):
# #         lst.append(i)


# # # TODO Talk about worst case and best case time complexities
# # # TODO Binary search


# # # Worst case time complexity: len(lst)
# # # Best case time complexity: 1
# # def find_num_unsorted(lst: list[int], n: int) -> bool:
# #     "Check if n exists in lst"
# #     for num in lst:
# #         if num == n:
# #             return True
# #     return False

# # # Worst case time compleixty is len(lst)
# def find_num_sorted(lst: list[int], n: int) -> bool:
#     "Check if n exists in lst"
#     for num in lst:
#         if num == n:
#             return True
#     return False

# n = 70
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# [60, 70, 80, 90, 100, 110]
# [60, 70, 80]

# # # 1 ... 100
# # # guess = 42

# # # 50
# # # 0 ... 50

# # # 25
# # # 25 .. 50
# # # 
# # # 37
# # # 37 ... 50
# # # 
# # # 44
# # # 37 ... 44 

# # # 1 ... 1000000
# # # 1 ... 500000
# # # 250000 ... 500000
# # # 375000 ... 500000

# num = 1000000

# while num > 1:
#     print(num)
#     num = num // 2


# num = 1000000
# # Binary search: 32
# # Linear search: 1000000


# # # The numbers that we are searching withing is our search space.


# # # Write a function that tells if the number is in the list that is sorted





# # # This list is sorted in ascending order (choxalan sira ile)
# # lst = [10, 20, 30]

# # # This is not a sorted list
# # lst = [10, 30, 20]




# # # TODO Sorting

def my_decorator(func):
    print(func)
    def wrapper(*args):
        print("Wrapper execution")
        print(func, args)
        return func(*args)
    return wrapper("Osman")
    
@my_decorator
def greet(name):
    return f"Hello, {name}!"

# greet = my_decorator(greet)

message = greet("John")
print(message.upper())