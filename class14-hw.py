# Question (Calculator)
# What will happen after the following code is executed? (Predict before running and see if the behvaior is as expected)
# Prediction: There will be an error because the class has not been intialized with a def __init__ function, leading to nothing being executed.
class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        return a / b

calc = Calculator()
result1 = calc.add(7, 5)
result2 = calc.divide(15, 0)


# Question 
# What will happen after the following code is executed? (Predict before running and see if the behvaior is as expected)
# Prediction: my_decorator returns nothing and wrapper is never executed so greet() will always return None, leading to an error when trying to call None("John")
def my_decorator(func):
    def wrapper(*args):
        print("Wrapper execution")
        return func(*args)

@my_decorator
def greet(name):
    return f"Hello, {name}!"

message = greet("John")
print(message.upper()) 

# Question 
# What will happen after the following code is executed? (Predict before running and see if the behvaior is as expected)
# Prediction: Due to the decorator, greet will become equal to the word wrapper and the function wrapper will try to execute with the arguement "John". However due to the scope of the wrapper function, it is only callable inside the my_decorator function and thus will return an error when it is called on line 44.
def my_decorator(func):
    def wrapper(*args):
        print("Wrapper execution")
        return func(*args)
    return wrapper
    
@my_decorator
def greet(name):
    return f"Hello, {name}!"

message = greet("John")
print(message.upper()) 

# Question
# What will happen after the following code is executed? (Predict before running and see if the behavior is as expected)
# Prediction: Greet will become equal to my_decorator(func) which will return what wrapper(Osman) returns. However, wrapper(Osman) will loop back to calling the greet function with the arguement "Osman" regardless of the intial arguement, returning "Hello Osman". This will cause message to equal "Hello, Osman!" and raise an error again where it does not realize that the string is meant to be a function.  Thus, only an error will be printed. 
def my_decorator(func):
    def wrapper(*args):
        print("Wrapper execution")
        return func(*args)
    return wrapper("Osman")
    
@my_decorator
def greet(name):
    return f"Hello, {name}!"

message = greet("John")
print(message.upper()) 

# Question 
# What will happen after the following code is executed? (Predict before running and see if the behvaior is as expected)
# Prediction: h1 will be intialized without any error. h2 will also be intialized without any error. h1's name, "Emily" will be printed first. However, the program will then encounter an error when trying to print h2's age as the age variable is never intialized within the Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name

    def display_name(self):
        print(self.name)

h1 = Human("Emily", 30)
h2 = Human("Ryan", 45)
print(h1.name)
print(h2.age)

# Question (Design)
# Imagine you are tasked with designing a system for a bank. The bank needs to manage its customers' 
# accounts through a simple program, and you’ve been asked to write part of the solution. Your task 
# is to represent a bank account as a single Python class. Each bank account should store the name 
# of the account owner and the current balance in the account.

#The users of your program (bank customers) will interact with their account in the following ways:

# 1. They can open an account by providing their name and an initial deposit (if they don't provide an initial deposit, the balance should start at 0).
# 2. Customers should be able to deposit money into their account. This will increase their balance by the deposit amount.
# 3. Customers also need the ability to withdraw money from their account. However, the account should never allow a 
#    customer to withdraw more than the current balance, as negative balances are not permitted.
# 4. Customers should be able to check their account details, like the owner’s name and the current balance. 
#    When printing the account, it should display these details in a clear and readable format.


class Bank_Account():
    def __init__(self, name, initial_deposit):
        self.name = name
        if initial_deposit > 0:
            self.initial_deposit = initial_deposit
        else:
            self.initial_deposit = 0
        self.bank_balance = self.initial_deposit

    def deposit(self, deposit_amount):
        print(f'${deposit_amount} has been deposited into your account!')
        self.bank_balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.bank_balance - withdraw_amount >= 0:
            self.bank_balance -= withdraw_amount
            print(f'${withdraw_amount} has been withdrawn from your bank account!.')
        else:
            print('Withdraw attempt denied due to insufficient funds!')

    def __str__(self):
        return f'|Account Name: {self.name} |Account Balance: {self.bank_balance}'
    
test_balance = Bank_Account('John', -20)
print(test_balance)
test_balance.deposit(60)
test_balance.withdraw(20)
print(test_balance)


# Question
# Answer 1-3 questions before first!
# 1. What does the `print_all` function do when called with multiple arguments versus a single argument?
# Prediction: It prints every element in that arguement seperately as they are in a tuple format. If it is a single arguement, it just prints the only element in that tuple. 
# 2. Does it work differently for different types of arguments (e.g., integers, strings)? 
# Prediction: No, they are all put in a tuple, so the data type of *args is always the same. 
# 3. What happens when you `print_all` is called with no arguments?
# If there are no arguements, then the program will not print anything as it cannot traverse through an empty tuple. 
def print_all(*args):
    for i in args:
        print(i)

# Question
# What will happen after the following code is executed? (Predict before running and see if the behvaior is as expected)
# Prediction: 1 is printed as a, (2, 3) is printed as args, and name: "Alice" is printed as kwargs
def tricky_func(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

tricky_func(1, 2, 3, name="Alice")
# tricky_func(name="Alice", 1, 2)

