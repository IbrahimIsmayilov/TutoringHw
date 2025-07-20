name = "Osman"
# print(name[20])
print(name[len(name) - 1])

surname = "Afandiyev"
print(name + " " + surname)
# print(name * surname) <= cannot do

print("abc" * 3)
# print("abc" * 3. 0)

alphabet = "abcdefghijklmnopqrst"
print(alphabet[0]) # <= alphabet[index]
print(alphabet[3]) # [] <= square brackets


# Max string index is the length of the string -1
#           0123456789
alphabet = "abcdefghijklmnopqrst"
print(alphabet[-1])
print(alphabet[len(alphabet) - 1])

# string slicing
# str_variable[start_idx : end_idx] 
# start_idx <= included
# end_idx <= not included

print(alphabet[0:2])
print(alphabet[2:5])

print(alphabet[4:2])
print(alphabet[-4:-1])

print(alphabet[-1:-2])
print(alphabet[4:2])

#           0123456789
alphabet = "abcdefghijklmnopqrst"
print(alphabet[:3])
print(alphabet[5:])

print("Advanced slicing")
# str_variable[start_idx : end_idx : step_size] 
#           0123456789
alphabet = "abcdefghijklmnopqrst"
print(alphabet[0::2])

print(alphabet[5:2:-1])

print("Weird case")
print(alphabet[3:6:-1])



# user-den USD input gotursen
# exchange rateden istifade ederk bu fromatda user-e neticeni versin

# USD amount was _initial_amount. We used exchange rate _exchange_rate. Result: final_amount
# exchange_rate_usd_to_cad = 1.42
# initial_amount = int(input("Enter initial amount"))

# final_amount = initial_amount * exchange_rate_usd_to_cad

# # salam osman necesen
# print("salam osman necesen")
# print(f"USD amount was {initial_amount}. We used exchange rate {exchange_rate_usd_to_cad}. Result: {final_amount}")

# alphabet = "abcdefghijklmnopqrst"
# letter_number = int(input("Enter which letter to pring: "))
# print(alphabet[letter_number - 1])


print("Boolean data type")
a = True  # <= True is 1
b = False # <= False is 0 

print("Boolean operations")

# and, or, not
c = True and True
print(c)

c = True and False
print(c)

# or
c = True or False
print(c)

c = False or True
print(c)

c = False or False
print(c)

# not
c = not True
c = not False

print(5 + 19 * 7)

print(True and True or False or False)
print(False or True and True  or False)

print(False or True and False  or False)
print(False or False or False)

print(False or False)

# 1. not
# 2. and
# 3. or

print(False or True and not False  or False)
print(False or True and True  or False)
print(False or True  or False)
print(True or False)

print("Weird cases")
print(True and "abc")
print(True and 5)
print(5 and True)

print(False and "abc")

print("" and False)

# non-empty string is True
# any number but 0 are true
# and returns the last true if all the operands are true
# returns the first false

# or operation returns the first true
print("abc" or False)
print(True or "abc")

print(1 or True or "abc")

print(False or "abc" or 19)