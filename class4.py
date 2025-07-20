# list
# looping over list
# passing by reference vs passing by value
# do ex

# bool, str, int, float

# list
name = "osman"
# for l in name:
#     print(l)

lst1 = [19, 27, 38, 47]
print(len(name))
print("Learning lists")
print(len(lst1))

empty_str = ""
empty_lst = []
print(len(empty_lst))

bool_lst = [True, False]

# print(str_lst[2])
# print(str_lst[-1])

# mix_lst = ["Osman", 24]
str_lst = ["Osman", "Dilara", "Ibrahim", "Habil"]
new_student_lst = str_lst + ["Huseyn"]
print(new_student_lst)

new_student_lst = new_student_lst + ["Nigar"]
print(new_student_lst)

name = "Osman"
for l in name:
    print(l)

for student_name in new_student_lst:
    print(len(student_name))


lst = [20, 28, 17]

def find_max(lst):
    if len(lst) == 0:
        print("Cannot find a biggest value in an empty list")
        return None

    max = lst[0]
    for num in lst:
        if num > max:
            max = num

    return max

my_max = find_max([13])

# range(start_idx, end_idx, step)
# end_idx no included

my_range = range(0, 12)
print(my_range)
for num in my_range:
    print(num)
    
for idx in range(0, 4):
    print(idx)
    
for idx in range(6):
    print(idx)
    
junk = "awuioerhgwlkejfngvwef"
for letter in junk:
    if letter == "o":
        print("yes letter exists")

# junk_len = len(junk)
for idx in range(len(junk)):
    if junk[idx] == "o":
        print(idx)
        
str_lst = ["Osman", "Dilara", "Ibrahim", "Habil"]
for idx in range(len(str_lst)):
    print(str_lst[idx])