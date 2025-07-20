# TODO

# staticmethod
# classmethods

# Inheritance

# The main challenge is having multiple ways of creating a book
# Subchallenge is to call from_string function, we need to already have
# an instance of this class.

# There are 2 ways of calling from_string funciton
# 1. Book.from_string(b1, usr_in)
# 2. b1.from_string(usr_in)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    # @classmethod
    def from_string(cls, string: str) -> "Book":
        """Creates a book from a string"""
        title, author = string.split(",") 
        new_book = Book(title, author)
        return new_book

    def print_book_title(self):
        print(self.title)

# 2 types of methods in the class 
# 1. regular instance methods. That need an instance to be called!
# 2. classmethod

usr_in = "War and peace, Leo ibn Tolstoy"
b1 = Book("War and peace", "Tolstoy")
b1.print_book_title()

# Book.from_string(usr_in)
Book.from_string(b1, usr_in)

# b1 = Book("War and peace", "Tolstoy")

# b2 = Book.from_string(b1, usr_in)

# Book.from_string(b1, usr_in)

# I want to create an instance of class book give a string.
# usr_in = input("Enter: ")

# b1 = Book("War and peace", "Tolstoy")

# Right now, to create a new book from a string, we need to have an old book.
# What do we do?

# b2.from_string(usr_in)


# def new_from_string(self, string):
#     pass

# new_from_string(b1, usr_in)
# b1.from_string(usr_in)
# Book.from_string(b1, usr_in)




# def foo(a):
#     return a

# foo(5)
# foo(9)

# Re-review class iterators the next class