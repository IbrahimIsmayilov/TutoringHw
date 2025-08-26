# TODO Briefly review assignment
# TODO Architecutre
count = 0
for i in range(10):
    count += i
print(count)


next_non_occupied_idx = 0
lst = 15000 * []

lst[next_non_occupied_idx] = 50
next_non_occupied_idx += 1

lst[next_non_occupied_idx] = 100
next_non_occupied_idx += 1

# What happens in our big RAM Array when we try to store a character?
a = 'p'
b = 20
z = 2.0
b = True


#lst = [10, 20, 30]
lst2 = [50, 60, 70, 80]

name = "Osman"
lst3 = ["ab", "cd"]


# Memory fragmentation


# 1 byte occupies 8 bits (each bit is either 0 or 1)

# 
# 0001100 <= 1 byte
# 2 bytes is 16 0s and 1s


# A language that only computers understand
# They represent True or False
# 1 is True
# 0 is False

# Binary code: binary numbers

# Decimal number vs binary number
# 255 => 11111111
# 0 => 11111111

# If you look how data is stored in compute, it is stored in hw called flip-flops
# Flip flop can store either True or False (aka. 1 bit of data)
# 1, 0


# If you combine 2 flip flops
# 00: 0
# 01: 1
# 10: 2
# 11: 3

# 000
# 001
# 010

# How much information can we store with n bits
# 2 ** n => where n is the number of bits
#
# X: 2

# 0 1 2 3
# XX


# "a"
# "b"
# "c"
# 26 English Alphabet character, 26 for Capital
# 10 for digits
# "102" => 001100010011000000110010
#49 48 50

# How many bits do we need to store an boolean?
# X
# How many bits do we need to store a character?
# 8 bits, 2 ** 8 = 256, 1 byte

# How many bits do we need to store an integer?
# 4 bytes
# 2 ** 32

# Why 1 bytes is not enough to represent an integer?
# 1 bytes -> 8 bits -> 256.
a = 10
a = 200
a = 13245243

# double: double of int

# 111010001

# How many bits do we need to store an float?