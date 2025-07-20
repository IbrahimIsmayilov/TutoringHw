#TODO: While loops

for num in [15, 27, 38]:
    print(num)



num = 3

# Collection: 
# 1. str
# 2. list
for elem in range(0, num):
    print(elem)

# count = 0
# while count <= num:
#     print(count)
#     count = count + 1



name = ["O", "s", "m", "a", "n"]
for elem in name:
    print(elem)
    


# Question
# Print the elements of the list using while loop
index = 0
while index < len(name):
    print(name[index])
    index = index + 1


# Question (Guess the number)
# Program picks a number between 0 and 100
# User should try to guess the this number and the game whill continue until
# either the user picks the number or the user types quit

# correct_num = 38
# guess_num = int(input("Enter num between 0 and 100"))
# while guess_num != correct_num:
#     print(f"Your guess is: {guess_num}. which is wrong.")
#     guess_num = int(input("Enter num between 0 and 100"))

# print("You guessed the right number.")

# Question
# Print all the powers of the number given by the user until we hit 10000
# 1, 2, 4, 8, 16 ... < 28
num = 5
power = 0
a = 0
while a <= 28:
    a = num ** power
    power = power + 1
    if a < 28:
        print(a)

power = 0
num = 5
while num ** power < 28:
    print(num ** power)
    power += 1


# Questions
def is_sorted(lst: list[int]) -> bool:
    lst = [5, 3, 4, 2, 19, 27]
    index = 0
    while index < len(lst) - 1:
        if lst[index] > lst[index + 1]:
            # print("unsorted")
            # break
            return False
        index += 1
    return True



name = "osmana"
# a o n s a m
start_idx = 0
end = len(name) - 1
while end > start_idx:
    print(name[start_idx] + name[end])
    start_idx += 1
    end -= 1


name = "osmana"
start_idx = 0
end = len(name) - 1
while end > start_idx:
    print(name[end] + name[start_idx])
    start_idx += 1
    end -= 1
# [1,2,3,4,5]
# [2,1,3,4,5]



#TODO: For loop vs while loop

#TODO: Double for loops
# num1 = int(input("First num: "))
# num2 = int(input("Second num: "))

#  4, 3
# (0, 1)
# (0, 2)
# (0, 3)
# (1, 1)
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 2)
# (2, 3)
# (3, 1)
# (3, 2)
# (3, 3)
# (4, 1)
# (4, 2)
# (4, 3)
for i1 in range(5):
    for i2 in range(1, 4):
        print(f"({i1}, {i2})")

lst = [1, 2]
lst = ["a", "b"]
# for elem in lst:
#     print(elem)

# for idx in range(len(lst)):
#     print(lst[idx])

lst = [True, False]

# lst = [[3, 6, 9], [3, 3, 3]]
# for idx in range(len(lst)):

lst=[[1,2,3],[2,3,4]]
idx=0
for elem in lst:
    # elem = [2,3,4]
    for elem2 in elem:
        print(elem2)

for idx1 in range(len(lst)):
    for idx2 in range(len(lst[idx1])):
        print(lst[idx1][idx2])

# for idx in range(lst):

# Dictionary 

# File operations
# Working with classes