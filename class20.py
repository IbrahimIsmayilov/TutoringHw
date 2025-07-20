# lst = [10, 20] # 11
# # left = 0, right = 10, # 5

# # left = 5, right = 10 #

# target = 20

# left = 0
# right = len(lst) - 1
# condition = True

# while condition:
#     middle_idx = (left + right) // 2
#     middle_elem = lst[middle_idx]
#     if middle_elem < target:
#         # lst = lst[middle_idx:]
#         left = middle_idx
#         # we go to the right
#     elif middle_elem > target:
#         # we go to the left
#         # lst = lst[:middle_idx]
#         right = middle_idx
#     else:
#         # We found the element
#         condition = False
#         print(f"found the element at: {middle_idx}")
#         # break
# # while 
# # print(lst[4.0])


# Sorting

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __lt__(self, other):
        # self is the left operand
        # other is the right operand
        return self.age < other.age
        # return "aueirghaieurbgaeiuyr"
        # return len(self.name) < len(other.name)

# lst = [70, 10, 20, 30, 50, 40]
# result = sorted(lst)

# print(result)
# p1 = Person("Osman", 18)
# p2 = Person("John", 20)
# print(p1 < p2)

lst = [Person("Osman", 24), Person("John", 20), Person("Jane", 22)]
result = sorted(lst)
for p in result:
    print(p.name, p.age)
# print(result)


# These ones are taught
# Insertion sorting
# Bubble sort
# Selection sort

# These ones are used
# Merge sort
# Quick sort