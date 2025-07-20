name = "Osman"
surname  = 'Afandiyev'

# full_name = ''''Os\'man'''

# print(full_name)

full_name = """Osm"an"""

full_name = ''''''


age = "24"
# print(age)
# print(age + 10)

print(int(age) + 10)
# print(int(name))

print(int(3.5))
print("Converting int to string")
print(type(str(4)))

amount_in_usd = 100
conversion_rate = 1.42

#  and the conversion rate is . Final result is
print("Initial amount was " + str(amount_in_usd) + "and the conversion rate is " + str(conversion_rate) + "final result is: " + str(amount_in_usd * conversion_rate))

print(f"Initial amount was {amount_in_usd} and the conversion rate is {conversion_rate}. Fina result is {amount_in_usd * conversion_rate}")

#           0123456789
alphabet = "abcdefghij"
print(alphabet[0])

# [start_idx: end_idx : step]

print("String slciing")
print(alphabet[0:3])
print(alphabet[4:2])
print(alphabet[-3:-1])

print(alphabet[0:4:2])
# print(alphabet[0:4:0]) steo size cannot be zero

print(alphabet[:4])
print(alphabet[4:])


#           0123456789
alphabet = "abcdefghij"
print("Negative step count")
print(alphabet[4:0:-1])
print(alphabet[4:0:-2])

# [start_idx: end_idx : step]
print(alphabet[1:3:-1])

length = len(alphabet[1:3:-1])
empty_string = ""
print(length)

print("Boolean opeartions")

true_d = True
false_d = False
print(true_d + false_d)

# and, or, not
print(True and True)
print(True and False)

print(True or False)
print(False or False)
print(not True)

print(True and False or True)
print(False and True or False)

# 3 + 5 * 12
# non-empty string is true
print(True and "1234")
print(False or "1234")

# and operation evaluates until the first false and return that
# if there is not false, it returns last true
print("" and True)
print(False and True)
print(True and True)

# when the statement is true, or operation will return the first true 
print(False or "abc" or "def")
print(True or "abc" or "def")



age = int(input("Enter age"))
if age < 20 and age > 12:
    print("Teen")
elif age < 20:
    print("Kid")
else:
    print("Adult")
    
# print("Will i reach here?")