#TODO
# These are excellent resources on time complexity and Python classes and I want you to spend time and read each of them:
# NOTE: Read them in order

# Class
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/10-abstraction/01-introduction.html
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/10-abstraction/02-classes.html
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/10-abstraction/03-methods.html

# Time complexity
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/09-runtime/01-introduction.html
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/09-runtime/07-data-types-runtime.html
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/09-runtime/09-testing-functions-4.html

# TODO:
# These are the instructions on how to activate WSL if you are using Windows:
# https://ardupilot.org/dev/docs/building-setup-windows10_new.html


# WARNING: Before this make sure Git is intalled and is available on command line!!!
# For the exercise below you will need to use the following Git commands
# git status
# git commit -m "<commit message>"
# git add
# git log
# git checkout <commit id>
# TODO Command line practice
# 1. Create a directory
# 2. Go to the created and run following command: git init
# 3. Create a file named foo.txt
# 4. Add something to the content of the file
# 5. Add the file to the staging area
# 6. Commit the file
# 7. Check the git log
# 8. Create another file named foo2.txt and add something to the new file as well.
# 9. Add some more things to foo.txt
# 10. Add both files to the staging area.
# 11. Commit both files
# 12. Check git log
# 13. Return back to the first commit. What do you see in the directory?
# It tells me that in the detached head state and I can experiment there. 
# 14. Check git log
# 15. Go back to the master commit. What do you see in the directory?
# It says the head is now at the second commit's id. 

# Question (Two sum simple)
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#
#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#Example 2:
#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#
#Example 3:
#Input: nums = [3,3], target = 6
#Output: [0,1]


def two_sum(lst: list, target: int) -> list:
    result = []
    s = {}
    for i in range(len(lst)):
        if target-lst[i] in s and (target-lst[i]) * 2 != target:
            result.append((i, s[target-lst[i]]))
        else:
            s[lst[i]] = i

    return result

print(two_sum([3, 0, 2, 4], 6))  # [3, 2]

print(two_sum([3, 3, 2, 4], 6))  # [3, 2]

# Question (Longest common prefix)
#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
# 
#
#Example 1:
#
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input

def longest_prefix(lst: list) -> str:
    
    if len(lst) == 0:
        return longest_prefix
    current_index = 0
    
    
    while True:

        for index in range(1, len(lst)):
            if current_index < len(lst[index]):
                if lst[index][current_index] != lst[0][current_index]:
                    return lst[0][:current_index]
            else:
                return lst[0][:current_index]
        current_index += 1


print(longest_prefix(["flower","flow","flight"]))
    
    

# Question (Student class)
# Student is someone with a name and a CGPA. At the beginning of the university journey all students have CGPA of 0.
# At the end of each semester students will get bunch of grades and based on that their CGPA will get updated.
# CGPA is calculated as total of grades of ALL courses taken divided by the number of TOTAL courses taken by a student.
# Ex. At the end of the first semester student get [30, 20]. Their CGPA is calculated as (30 + 20) / 2 = 25
# In the next semester, student gets another course grade of 100. Their new CGPA IS NOT (25 + 100) / 2.
# Instead their new CGPA is (30 + 20 + 100) / 3
# Design the student class with 2 methods:
# __init__
# def grades_released(self, grades: list[float]) -> None


class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.CGPA = 0

    def grades_released(self, grades: list[float]) -> None:
        self.CGPA = round(sum(grades) / len(grades))

person1 = Student('Ibrahim Ismayilov')
person1.grades_released([86, 98, 87]) 
print(person1.CGPA) # 90




            

def my_decode(encoded_string: str) -> str:
    result = ""
    for i in range(0, len(encoded_string), 2):
        result += encoded_string[i]
    
    return result