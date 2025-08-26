# TODO Talk about assignment
# Why do we need Git?
# To create different versions of out project throughout the development cycle.
 
# TODO
# Git directory
# adding commits

# TODO
# Aboslute path
# Relative path

# Git commands
# git init
# git add
# git status: shows the files that have been changed since the last commit
# git commit
# git log: use to look at the history of versions of your project


# Git workflow
# 1. git init: git init does not create a version. it initializes a directory to be a git directory (aka. creates .git folder) enabling us to run git commands
# 2. git status
# 3. git add
#    - turns red files into green files in git status
#    - What is the difference between green files and red files?
#    - Green files are files in a staging area.
#    - When we perform git commit, only the files in a staging area will be added to the new commit.
# 4. git status
# 5. git commit
# 6. git log

# Commit and version are the same things.

# When i do git commit, which files will be added to the new version/commit?




# git push
# git pull

# TODO Go over homework
# Option 1
# 1. How many times does target occur in the rest of the list after the first element?
# 2. Add 1 if the first element matches the target, otherwise 0, to the answer from the smaller question.
# 3. When the list is empty, return 0

def count_occurece(lst,target):
    # These are base cases
    if len(lst) == 0:
        return 0

    elif len(lst) == 1:
        if lst[0] == target:
            return 1
        else: 
            return 0


    middle = len(lst) // 2
    first_part = count_occurece(lst[:middle], target)
    second_part = count_occurece(lst [middle:], target)
        
    return first_part + second_part


print(count_occurece([1,2,5,3,2,4,8,2,7],2))

# Option 2
# 1. How many times does target occur in the rest of the list after the first element?
# 2. Add 1 if the first element matches the target, otherwise 0, to the answer from the smaller question.
# 3. When the list is empty, return 0

def count_occurence(lst: list[int], target: int) -> int:
   
    if len(lst) == 0:
        return 0
    
    smaller_list = count_occurence(lst[1:],target)

    if lst[0] == target:
        first_count = 1
    else:
        first_count = 0

    return first_count + smaller_list

print(count_occurence([1,2,5,2,2],2))

def calPoints(operations):
        """
        :type operations: List[str]
        :rtype: int
        """
    
        records = []
       
        for elem in range(len(operations)):
            if operations[elem].lstrip("-").isdigit():  
                records.append(int(operations[elem]))
       
            elif operations[elem] == "C":
                records.pop()
              
            elif operations[elem] == "D":
                
                records.append(records[-1]*2)
        
            elif operations[elem] == "+":
                records.append(records[-1] + records[-2])
             
            else:
                print("this operator not found")

        return sum(records)

# TODO Design sets without using sets & dictionaries
# DO we need to make our own set class? Yes.
# Properties of python sets
#   - no element can be repeated. Each element can occure only once.

# Operation
# - add elment to a set
# - remove an element
# - get the length of the set
# - Check if an element is in the set

#s = {1, 2}
# 
class my_set:
    def __init__(self):
        self.elements = []
    
    def add(self, *args):
        pass
    
    def remove(self, elem):
        pass
    
    def get_len(self):
        return len(self.elements)
    
    def contains(self, elem):
        return elem in self.elements

s = my_set()
s.get_len()
    

# Next class
# TODO Talk about process execution model