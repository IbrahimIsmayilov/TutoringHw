# Hash table collision resolution
arr = [[],[],[]]
# k = "a", v = 10
arr = [[("a", 10)],[],[]]
# arr[hash("z")].append(("z", 99))

# k = "z", v = 99
arr = [[("a", 10), ("z", 99)],[],[]]

def hash(sentence: str) -> int:
    return len(sentence) % 2

# Getting the value of the
# key in a dicitonary is constanct time

# There are 3 operations when it comes to dictionaries
# 1. Insertion: Constant time
#    # Assumption: let's say computing the hash takes constant time
#    1. Find the hash of the key which becomes our index
#    2. We insert the key value pair as a tuple to an array at that index

# Why does python dictionary gives us a lookup time that is constant.
# It does not.
# THe worst case is not constant for a lookup in a dictionary.
# The worst case time complexity for a dicitonary is equal of to the size of dictionary.

# Average lookup time is constant in dcitionary

# 2. Lookup: Worst case time complexity is also a constant time
#    1. Find the hash of the key which becomes our index
#    2. Search for the key value in the array at that index
#    3. Go through each tuple of that array at that index, compare the keys of the tuples to the key that
#       we are interesed in. If that key is equal to the one that we want, we can return the value of that tuple.
# 3. Deletion 
#    1. Find the has of the key which becomes our index
#    2. Find the tuple that matches the key for the array at the hashed index.
#    3. We remove the tuple itself from the list


# TODO
# Git remote
# Git branching
# Process lifecycle

lst = []
s = set()
s.add("abc")
# lst.append("abc")


# we can only remove from the end of the list
lst = [10, 20, 30, 50, 60, 70]
lst.pop()
lst.remove(20)
lst = [10, 70, 30, 50, 60]


# We will be submitting our homework through Github form now on.
# Why do we use git?
# We use git as a version control tool.
# Git is actually also used in collabration.


# 1. Ibrahim
# 2. Dilara
# 3. Ali


# All 3 parts must be working