class Human:
    POPULATION = 0
    
    def __init__(self, name):
        # Everything that is used by self. are attributes of instances
        self.name = name
        
    def __str__(self):
        return f"This person's name is {self.name}"
print(dir(Human))

# h1.name = "Murad"

# h1 = Human("Osman")
# WHat are the names that i can do like so h1.name
# print(dir(h1))


# h2 = Human("Leyla")

# print(h1.name)
# print(h2.name)

# print(Human.POPULATION)
# Human.POPULATION += 1

# print(Human.POPULATION)
# print(h1.POPULATION)
# print(h2.POPULATION)

# def foo():
#     a = 10
#     return 20
# print(a)

print(dir(Human))
print(dir())
a = "Osman"
print(dir())

class Human:
    # Is an attribute of a class that represent the current population
    # It makes sense to increase the population, each time a human object is created.
    POPULATION = 5
    
    def __init__(self, name):
        # Everything that is used by self. are attributes of instances
        self.name = name
        Human.POPULATION += 1
        # self.age = 23
        # print(self.POPULATION)
        
        # self.POPULATION = self.POPULATION + 1
        # print(dir())
        
        
    def __str__(self):
        return f"This person's name is {self.name}"


# Precedence of name resolution
# Instance names are resolved first
# if not matching instance name exists, we will try to find that variable in a class attributes.
# If the variable does not exist in class attributes, then we get an error that variable does not exist.
# h1 = Human("Osman")
# print(h1.name)
# print(h1.age)

# print(h1.POPULATION)
# # Human.POPULATION += 1
# print(h1.POPULATION)
# print(Human.POPULATION)

# h1 = Human("Leyla")
# print(Human.POPULATION)

# h2 = Human("Leyla")
# Human.POPULATION += 1

# a += 1

class Human:
    # Is an attribute of a class that represent the current population
    # It makes sense to increase the population, each time a human object is created.
    POPULATION = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.POPULATION += 1
        self.POPULATION = 0

    # Builtin methods
    # __str__
    # __lt__
    # __eq__
    # __iter__
    # __next__
    # __init__

    def __lt__(self, other):
        # It should return boolean expressoin
        # Ideally True or False
        return [10, 52]
    
    
    def __str__(self):
        return f"This person's name is {self.name}"
    
    def increment_age(self, add: int):
        self.age += add




# print(Human.POPULATION)
h1 = Human("Os", 24)
my_str = h1.__str__()
print(my_str)

# print(h1.age)
# h1.increment_age(5)
# print(h1.age)
# h2 = Human("Leyla", 27)
# print(h1)
# h1.age
# h2.age
# print(10 > 24)
# print(h1 > h2)

# print(Human.POPULATION)
# print(h1.POPULATION)

# h1 = Human("Os", 24)
# for elem in [10, 20, 30]:
#     # Python is going to invoke the following call: 
#     # my_iterable_obj = iter([10, 20, 30])
#     # elem = next(my_iterable_obj)
#     print(elem)

# print(type([10, 20, 30]))
# print(type(iter([10, 20, 30])))
# list_iterator = iter([10, 20, 30])
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))


class CountUpTo:
    
    def __init__(self, num):
        self.count_up_to = num
        self.current = 1
       
    # This is what really gets executed when you call iter() 
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.count_up_to:
            # self.current += 1
            return "Osman"
        else:
            raise StopIteration
        
# c = CountUpTo(4)
# for num in c:
#     # Python does this num = next(c), until it hits the StopIteration exception/error which indicates that we reached the end of the for loop.
#     print(num)

# print(next(c)) # next magically calls __next__
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))