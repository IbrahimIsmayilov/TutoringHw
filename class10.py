# Question
# Given a string, write a function that finds  how many words are in the string.
def find_word_cnt(sentence: str) -> int:
    pass

"Hi there. My name is Osman" # 6 words

# Question
# Given a string write a function that finds how many words are in the string
# def find_word_cnt(sentence: str) -> int:
#     if len(sentence) >= 1:
#         count = 1
#         for char in sentence:
#             if char == " ":
#                 count += 1
                
#         return count

#     print("    adjfhglauifdhgiula there. My name is Osman")
#     return 0

def find_word_cnt(sentence: str) -> int:
    count = 0
    is_inside_the_word = False
    for char in sentence:
        # If we are not in the white space, we are inside the word
        # if we are inside the white space, we are not inside the word
        if char == " ":
            is_inside_the_word = False
        elif not is_inside_the_word:
            count += 1
            is_inside_the_word = True
    return count



print(find_word_cnt("          Osman          says hi"))

# print("Working with files")
lst = [1,2,45]

# Reading data from the file
# If the file does not exist, opening it to read will result in error
# file = open("dummy2.txt","r")
# file_content = file.read()
# print(file_content + "by there ")

# Write a data to the file
# If the file does not exist, opening it to write will result in creation of the file
# print("Working with files")
# file = open("tutorial.txt", "w")
# file.write("Osman\n5")


# file.write("123456")
# file.read() <= cannot do this, cause we opened it for writing
# file = open("tutorial.txt", "a")
# file.write("9")

# file = open("tutorial.txt", "r")
# content = file.read()
# print(content)
# s = file.readline()
# print(s)

# s = file.readline()
# print(s)
# while True:
#     s = file.readline()
#     if s == "":
#         break
#     print(s)

# Print the content of the file
# f = open("tutorial.txt", "r")
# content = f.read()
# print(find_word_cnt(content))
# f.close()

# Find how many words are inside the file.
alphabet = "abcdefghijklmnopqrstuvxyz"
print(alphabet[5:2:1])

