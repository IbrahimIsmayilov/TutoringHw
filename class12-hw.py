# Question (Guess)
# Guess what will be printed without running the program.
# 38 48 Osman
def question(a, *args):
    print(args) 
    
question(10, 38, 48, "Osman")



# Question (Identify types)
x = {"Osman": ["Book", "Phone"]}  # Type: Dict
y = {"Toronto": [23, 28, 37]}  # Type: Dict
z = [{"Osman": 52}, {"Leyla": 73}]  # Type: List

# For each line below, what will be the type of variable guess and what would be printed if i try to print it.
# DO NOT USE PRINT FUNCTION, MAKE A GUESS FIRST!!! 
guess = x  # Type: Dict, Value: Osman: [Book, Phone]
print(guess)
guess = x["Osman"]  # Type: List, Value: [Book, Phone]
print(guess)
guess = x["Osman"][1]  # Type: Str, Value: Phone
print(guess)
guess = x["Osman"][0][-1] # Type: Str, Value: k
print(guess)
guess = len(x)  # Type: Int, Value: 1
print(guess)
guess = len(x["Osman"])  # Type: Int, Value: 2
print(guess)
guess = len(x["Osman"][-1])  # Type: Int, Value: 5
print(guess)
guess = len(x["Osman"][-1][-2])  # Type: Int, Value: 1
print(guess)
guess = len(y["Toronto"])  # Type: Int, Value: 3
print(guess)
guess = z  # Type: List, Value: [Osman: 52, Leyla: 73]
print(guess)
guess = z[-1]  # Type: Dict, Value: Leyla: 73
print(guess)
guess = len(z[-1])  # Type: Int, Value: 1
print(guess)
guess = z[-1]["Leyla"]  # Type: Int, Value: 73
print(guess)

# Question (Scale)
# Write a function that takes variable number of parameters. You know that your function will be called with at least 2 parameters
# and that all parameters will be integers. Your function should multiple the first paramater with all the reamining parameters
# and find the sum of the results.
# Ex. scale(10, 2, 3) => 10 * 2 + 10 * 3 = 50

def scale_num(first_num: int, *args: tuple) -> int:
    total_num = 0

    for num in args:
        total_num += num * first_num
    
    return total_num


print(scale_num(3, 2, 3, 4, 5))

# Question (Value unpacking)
# Complete the body of the function such that the code below works
def square_and_cube(num: int) -> tuple[int, int]:
    return num ** 2, num ** 3

square, cube = square_and_cube(5)
print(square) # should print 25 with the above example
print(cube)   # should print 125 with the above example