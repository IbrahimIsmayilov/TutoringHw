# Question
# In class 32 we have implemented a dictionary class with normal list.
# However, we examined the time complexities of our dictionary methods and they do not work same as
# regular Python dictionary. We agreed that to match Python dictionary time complexity we need to use Hash Tables instead.
# Implement dictionary class using hash table.


# Main dictionary operations: adding, removing, updating
class Dictionary():

    # Time complexity O(1), constant time complexity
    def __init__(self):
        self.hash_table = [[]] * 1000

    # Time complexity O(1), constant time complexity
    @classmethod
    def __hash__(cls, unhashed_key):
        return hash(unhashed_key) % 1000
    
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def find_kv_idx(self, hashed_idx, key_target):
        for kv_idx in range(len(self.hash_table[hashed_idx])):
            if self.hash_table[hashed_idx][kv_idx][0] == key_target:
                return kv_idx
        return -1
    
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def check_key_existence(self, key):
        hashed_idx = Dictionary.__hash__(key)
        kv_idx = self.find_kv_idx(hashed_idx, key)
        if kv_idx == -1:
            raise KeyError
        else:
            return hashed_idx, kv_idx

    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def add(self, key, value):
        try:
            self.check_key_existence(key)
        except KeyError:
            hashed_idx = Dictionary.__hash__(key)
            self.hash_table[hashed_idx].append((key, value))

    
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def remove(self, key):
        hashed_idx, kv_idx = self.check_key_existence(key)
        self.hash_table[hashed_idx][kv_idx], self.hash_table[hashed_idx][-1] = self.hash_table[hashed_idx][-1], self.hash_table[hashed_idx][kv_idx]
        self.hash_table[hashed_idx].pop()

        
    # Time complexity O(N), where N is the length of the inner list, that is located at hash_table[hashed_idx]. Linear time complexity
    def update_key(self, key, value):
        hashed_idx, kv_idx = self.check_key_existence(key)
        self.hash_table[hashed_idx][kv_idx] = (key, value)

    def print_kv_pair(self, key):
        hashed_idx, kv_idx = self.check_key_existence(key)
        print(self.hash_table[hashed_idx][kv_idx])

    # Time complexity O(1), constant time complexity
    def __str__(self):
        return f'{self.hash_table}'
        
        
    
            

        

    

    
test_dictionary = Dictionary()
print(test_dictionary)  # empty list with 1000 inner sub lists
print(test_dictionary.__hash__(0))  # 0
print(test_dictionary.__hash__(1000))  # 0
test_dictionary.add(0, '1')  
test_dictionary.print_kv_pair(0)  # (0, '1')
test_dictionary.add(1000, '2')
test_dictionary.print_kv_pair(1000)   # (1000, '2')
print(test_dictionary.find_kv_idx(0, 1000))  # 1
test_dictionary.remove(1000)
print(test_dictionary.hash_table[0])   # [(0, '1')]
test_dictionary.update_key(0, '5')
print(test_dictionary.hash_table[0])   # [(0, '5')]
# test_dictionary.print_kv_pair(9000)   # KeyError


# Question
# You are given a string of paranthesis, you need to decide if that is a valid set of paranthesis.

# Steps:
# 1. We need to find the first opening paranthesis and add it to our stack of opening parantheses.
# 2. While iterating through the string, we are looking for a closing paranthesis that will be paired with the opening paranthesis found in step 1 and label them as a a couple of parantheses by popping the opening paranthesis from the end of the stack. If on our search for a closing paranthesis, we find another opening paranthesis, we append it to our stack and it becomes the opening that takes priority when a closing paranthesis is found to couple them together. 
# 3. Once done iterating though all parantheses, return true if there are no opening parantheses left that have yet to find a closing paranthesis to couple together. Else, if there are any left, it is invalid and return False. If in any case, before encountering an open paranthesis while the stack is empty we encounter a closing paranthesis first, the parantheses are labeled invalid and an IndexError is captured. In a valid set of parantheses, a closing paranthesis can never come before an opening paranthesis. 

# Time complexity O(N), where N is the length of the string parantheses
def is_valid(parantheses: str) -> bool:
    opening_parantheses_stack  = []
    try:
        for paranthesis in parantheses:
            if paranthesis == "(":
                opening_parantheses_stack.append(paranthesis)
            else:
                opening_parantheses_stack.pop()
        return not opening_parantheses_stack
    
    except IndexError:
        return False



# You need to use stack here.
# You need to use python list to solve this problem.


# Examples:
print(is_valid("()"))  # True
print(is_valid("()()"))  # True

print(is_valid("(()())"))   # True
print(is_valid("(()())()")) # True

print(is_valid("(()(")) # False
print(is_valid(")())")) # False
print(is_valid("(()))")) # False

# Question
# For number n count the number of ordered sums till n.
def ordered_sums(n: int) -> int:
    pass

# Ex: 
ordered_sums(4) # -> 7
#1+1+1+1
#1+1+2
#1+2+1
#2+1+1
#2+2
#1+3
#3+1