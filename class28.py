# Hashing
# Takes original file (text, image, audio, video) and concverts it into some different format.
# * Whatever you hashing funciton is, hashed value will always have the same size, regardless
# how big your input is.
# * Encoding function compes in pairs, hash function does not.


# Each encoding function should have its matching decoding function by using which we can restore
# the original text from an encoded text.

def my_hash(param: str) -> str:
    """ Conversts input parameter into a 3 character hashed value """
    return param[:3]

hash("absdufihweiorgbwoieur")

# Ecoding
# You take original file (text, image, audio, video) and convert it into 
# some different format though which original content cannot be seen.

# We usually use encoding technique to hide the original content from malicious actors.
def my_encode(param: str) -> str:
    result = ""
    for letter in param:
        result += letter * 2
    return result

def my_decode(encoded_string: str) -> str:
    decoded_str = ""
    for elem in encoded_string[::2]:
        decoded_str += elem
    return decoded_str

# Ceasar's cipher
# TODO HW: write ceaser encode and decode functions
def ceaser_encode(original: str) -> str:
    pass

def ceaser_decode(encoded_txt: str) -> str:
    pass

# Take every letter and replace it with a letter in alphabet 
# that is 3 letters later than original letter
original_text = "osman"
# ceaser_encode(original_txt) => "rvpdq"

encoded = my_encode("osman") # => "oossmmaann"
print(encoded)
decoded = my_decode(encoded) # => "osman"
print(decoded)

# TODO HW: Why this code does not work:
#def my_decode(param):
#    my_decode=""
#    for i in range(len(param)):
#        if param[i]==param[i+1]:
#            my_decode += i
#
#    return my_decode
#
#print(my_decode("oossmmaann"))

# Decoding

# Dictionaries and sets in python are implemented using "hash tables"
lst = [""] * 10

# Given a string add that string to a certain index in the lst. The same string
# must always be added to the same index if it is added again.
def hash_dummy(text: str) -> int:
    return 0

def good_hash(text: str) -> int:
    return len(text) % 10

def add_str(new_str):
    global lst
    #indx = hash_dummy(new_str)
    indx = good_hash(new_str)
    lst[indx] = new_str

add_str("Osman")
add_str("Osman")
add_str("Leyla") # => 3
print(lst)