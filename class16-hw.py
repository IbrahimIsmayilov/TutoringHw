# Do not run the code. For each "What will happen" try to predict. Take your time. 
# Before looking at questions, spend time to familirize yourself with class, all the attributes and the methods.
# Comment everything out except specific "What will happen" when you want to test.

# NOTE: There are different definitions of class Human
# When new class of Human is defined, all the questions under that should be answered based on 
# the latest definition of class Human.

# Question (Human class 1).
# Answer all "What will happen" questions based on the following class.
class Human:
    def __init__(self, name, age=0):
        self._internal_name = name
        self.age = age
    
    def increment_age(self):
        print(self._internal_name)
        self.age += 1
    
    def __str__(self):
        return f"{self._internal_name} is {self.age} y.o."

# What will happen?
# Prediction: It will print Osman is 0 y.o
a = Human("Osman")
print(a)

# What will happen?
# Prediction: It will print Osman is 0 y.o
a = Human("Osman")
b = a.__str__()
print(b)

# What will happen?
# Prediction: It will print Osman is 1 y.o
a = Human("Osman")
a.increment_age()
print(a)

# What will happen?
# Prediction: It will print Leyla is 1 y.o
a = Human("Osman")
a._internal_name = "Leyla"
a.increment_age()
print(a)

# What will happen?
# Prediction: It will print "Osman is 0 y.o". It will then provide the instance "a" to the increment method and then print "Osman is 1 y.o"
a = Human("Osman")
print(a)
Human.increment_age(a)
print(a)

# Can i do this? Why or why not?
# Prediction: You can do this because you provided an instance for the instance method even though you called it from the general class Human. It will print "Osman is 0 y.o"
a = Human("Osman")
b = Human.__str__(a)
print(b)

# Can i do this? Why or why not?
# You cannot do this because the string method of Human requires an instance and b is not intialized as an instance. It is an instance method, not a class method. Thus, printing this will generate an error. 
b = Human.__str__()
print(b)
print(b)


# Question (Human class 2)
# Answer all "What will happen" based on the following class.
class Human:
    def __init__(self, name, age=0):
        self._internal_name = name
        self.age = age
    
    def increment_age(self):
        self._internal_name = "Dummy"
        self.height = 186
    
    def dummy(self):
        print(self.salary)
    
    def __str__(self):
        return f"{self._internal_name} is {self.age} y.o."

# What will happen?
# Prediction: It will run into an error when trying to access the "surname" attribute of Human as it does not exist. Thus, the console will only report the error and not print anything. 
a = Human("Osman")
b = Human("Leyla")
a.surname = "Afandiyev"
print(a.surname)
print(b.surname)

# What will happen?
# Prediction: It will print "Osman is 0 y.o". It will then print "Osman is 1 y.o".
a = Human("Osman")
print(a)
a.increment_age()
print(a)

# What will happen?
# Prediction: It will print only an error because Osman does not have height attribute. 
a = Human("Osman")
print(a.height)

# What will happen?
# Prediction: It will create Osman instance, update its age, but it will only print an error when it tries to print the height of a as the height attribute does not exist. 
a = Human("Osman")
a.increment_age()
print(a.height)

# What will happen?
# Prediction: It will intialize "a", and run into an error when trying to access the attribute "salary" which does not exist. It will never even get to printing dummy. 
a = Human("Osman")
a.salary = 10000
a.dummy()

# What will happen?
# Prediction: It will intialize an instace called a, with the name "Leyla" and default age of 0. The program will produce an error when "dummy" is called because the instance does not have an intialized salary attribute. 
a = Human("Leyla")
a.dummy()

# Question (increment_age)
# Complete increment_age method
class Human:
    def __init__(self, name, age=0):
        self._internal_name = name
        self.age = age

    def increment_age_n(self, increase_by: int):
        self.age += increase_by
    
    def increment_age(self):
        """Increases the age by 1"""
        #TODO we know that if i can call increment_age_n(1), the age will be increased by 1.
        # That is what the function description says this function do. How would i call increment_age_n(1)
        # inside this function to increase the age by 1.
        self.age += 1

    def __str__(self):
        return f"{self._internal_name} is {self.age} y.o."
        
# Question (No class method)
# Answer all what will happens based on the following Book class definiton
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def from_string(self, string: str) -> "Book":
        """Creates a book from a string"""
        print(self.title)
        title, author = string.split(",") 
        new_book = Book(title, author)
        print(new_book.title)
        return new_book
    
    def __str__(self):
        return f"{self.title} is written by {self.author}"

# What will happen
# Prediction: A new instance "a" will be intialized with War and Peace for the name and Leo for the author. The variable below new_book_str will be created. When from_string() is called, War and Peace will be printed. A new book instance will be created with the details from new_book_str as "b". The title will also be printed of the new book. 
a = Book("War and peace", "Leo")
new_book_str = "1984, George Orwell"
b = a.from_string(new_book_str)

# What will happen
# Prediction: A new instance "a" will be intialized with War and Peace for the name and Leo for the author. The variable below new_book_str will be created. When from_string() is called, War and Peace will be printed. A new book instance will be created with the details from new_book_str as "b". The title will also be printed of the new book. Afterwards, the string representation of "b" will print, "1984 is written by George Orwell."
a = Book("War and peace", "Leo")
new_book_str = "1984, George Orwell"
b = a.from_string(new_book_str)
print(b)

# What will happen
# Prediction: A new instance "a" will be intialized with War and Peace for the name and Leo for the author. The variable below new_book_str will be created. When from_string() is called as a class method with "a" as self, War and Peace will be printed. A new book instance will be created with the details from new_book_str as "b". The title will also be printed of the new book. 
a = Book("War and peace", "Leo")
new_book_str = "1984, George Orwell"
b = Book.from_string(a, new_book_str)

# What will happen
# Prediction: A new book class instance will be intialized as 'a'. When the from_string() method is called, there will be an error because it is an instance method and not a class method. Thus, there will be an error due to the lack of instance in the parameter of the method. 
a = Book("War and peace", "Leo")
new_book_str = "1984, George Orwell"
b = Book.from_string(new_book_str)

# Question (classmethod)
# Given the string below and a class Book, create a book object in 2 ways:
# 1. Use from_string method
# 2. Use the __init__ method.
my_str = "War and peace, Leo"

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    @classmethod
    def from_string(cls, string: str) -> "Book":
        """Creates a book from a string"""
        title, author = string.split(",") 
        new_book = Book(title, author)
        return new_book
    
first_book = Book('War and Leace', "Leo Tolstoy")
second_book = Book.from_string('War and Leace', 'Leo Tolstoy')
    

        

        