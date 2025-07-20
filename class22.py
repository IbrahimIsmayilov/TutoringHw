# def dependent_loops(n: int): # n *n == n ** 2
#     for i in range(1, n + 1): # n
        
#         for j in range(1, n + 1): # n
#             print(i, j)

# dependent_loops(2)

# def zoo(n: int): 
#     for i in range(n): # n
#         print(i)

#     for i in range(2*n): # 2n
#         print(i)
# zoo(4)


# # TODO Same hw
# def foo(n: int):
#     while n > 1:
#         print(n)
#         n = n // 2
        
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
        
# #     def __lt__(self, other):
# #         # self is the left operand
# #         # other is the right operand
# #         return self.age < other.age
#         # return "aueirghaieurbgaeiuyr"
#         # return len(self.name) < len(other.name)

# # lst = [70, 10, 20, 30, 50, 40]
# # result = sorted(lst)
# # print(result)
# # # print(result)
# # # p1 = Person("Osman", 18)
# # # p2 = Person("John", 20)
# # # print(p1 < p2)

# # lst = [Person("Osman", 24), Person("John", 20), Person("Jane", 22)]
# # result = sorted(lst)
# # print(result)
# # for p in result:
# #     print(p.name, p.age)
# # print(result)

# new_lst = []
# lst = [70, 10, 20, 30, 50, 40]
# minimum = lst[1]
# new_lst.append(minimum)

# # TODO implement the function based on the steps
# # Steps
# # 1. Are we sorting in ascending or descending orders? (Ascending)
# # 2. Let's find list minimum: 10
# # 3. add that minimum to the new list new_lst = [10]
# # 4. Delete the minimum from the origian lst
# # 5. Repeat the process until the original list is emptys

# def my_sort(lst):
#     new_lst = []
    
#     return new_lst

# my_sort(lst)


# lst = [70, 10, 20, 30, 50, 40]
# # Steps
# # 1.Find the biggest in the list

# # Removing from the list can be very expensive in terms of time complexity
# # We can decrease the size of the list from the end in a constant run time (time complexity) 1.
# # We can only remove an element from the end of the list

lst = [70, 10, 20, 30, 50, 40]

lst = [70, 10, 30, 50, 40]


# Question
# How would you remove from the list in constant time?
def remove(lst, idx):
    lst[idx], lst[-1] = lst[-1], lst[idx]
lst = [70, 10, 20, 30, 50, 40]
remove(lst, 2)


lst[-1], lst[0] = lst[0], lst[-1]
print(lst)



# lst[0] # 70
# lst[1] # 10

# lst.remove(70)

# lst = [10, 20, 30, 50, 40]
# lst[0] # 10
# lst[1] # 20

# # The number of lines of code does not say much about time complexity

# # Worst case time complexity: len(lst)
# def contains(lst, n):
#     return n in lst

# contains([10, 20, 30, 40, 50])



# # Question
# def my_sort_in_place(lst):
#     pass



# Question
# How would you remove from the list in constant time?
def remove(lst, idx):
    lst[idx], lst[-1] = lst[-1], lst[idx]
    lst.pop()
    
def num_remove(lst, num_to_remove):
    # 1. We should find the index of the number first
    # 2. The do the procedure below
    
    # lst[idx], lst[-1] = lst[-1], lst[idx]
    # lst.pop()
    pass
# lst.pop() removes the last element from the end of the list

print("removing")
lst = [70, 10, 20, 30, 50, 40]
remove(lst, 2)
print(lst)

lst = [70, 10, 20, 30, 50, 40]
lst.remove(20)


print(lst)

# This list is sorted
lst = [10, 20, 30, 40, 50, 60]
remove(lst, 2)
print(lst)

# Write a remove function

lst = [10, 20]
lst[-1], lst[1] =  lst[1], lst[-1]
print(lst)
lst.pop()
print(lst)

4 in lst