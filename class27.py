#import random
#
## Linear search
## Binary search
#
#print("Please make a guess between 0-10000000")
#while True:
#    guess = random.randint(0, 10000000)
#    print(f"Is this guess right: {guess}")
#    user_in = input("[y]es, [n]o: ")
#    if user_in == "y":
#        break

#least = 1
#most = 1000000 # 1000001
#
## Binary search: 32
#
#while True:
#    mid = (least + most) // 2
#    print(f"Is this right: {mid}?")
#    user_in = input("Enter [y]es, [h]igher, or [l]ower: ")
#    
#    if user_in == "y":
#        print(f" The number is {mid}.")
#        break
#    elif user_in == "h":
#        least = mid + 1
#    elif user_in == "l":
#        most = mid - 1
        
        
# Worst case
# Depending of the length of the list the number of times we enter for loop will change.
# What sit the worst case scenario?: In the worst case, the number of iterations in the for loop will be equal to the length of the list (x)
# What combination of input parameters will end up in the worst case scneraion?: If target is not in the list x, we will hit the worst case.


# Best case
# What combination of input parameters will end up in the best case scneraio?: if the target is the first number in the list.
# In the best case scenario how many times we will enter the for loop: 1

# 10
# 20

#  x = [10, 20, 30, 40, 50], target = 100 # 5
#  x = [10, 20, 30, 40, 50], target = 10  # 1

#def foo(x: list[int], target: int) -> bool:
#    """ Checks if target exists in the x """
#    # x = [10, 20, 30, 40, 50]
#    count = 0
#    count += 2
#    for num in x:
#        if num == target:
#            return True
#    return False


# Worst case
# What sit the worst case scenario?: In the worst case, the number of iterations in the for loop will be equal to the length of the list (x)
# What combination of input parameters will end up in the worst case scneraio?: 

# Best case


# Best case is the same as worst case
# len(x) = 20
# Worstcase & best case are both equal to: len(x)

# Worst case& best case are both equal to: len(x) + len(x) = 2 * len(x)
def foo(x: list[int]):
    # len(x)
    for num in x:
        print(num)

    for num in x:
        print(num)
    
    # len(x)
    for num in x[::-1]:
        print(num)


# How many times for loops will execute as the size of the input parameters change?
def foo(x: list[int]) -> None:
    for i in range(5):
        print(i)
    
    
foo([10, 20, 30])