# Question
# In class 32 we have implemented a dictionary class with normal list.
# However, we examined the time complexities of our dictionary methods and they do not work same as
# regular Python dictionary. We agreed that to match Python dictionary time complexity we need to use Hash Tables instead.
# Implement dictionary class using hash table.

class Dictionary():

    def __init__(self):
        self.hash_table = [[]] * 1000

    @classmethod
    def __hash__(cls, unhashed_key):
        return hash(unhashed_key) % 1000
    
    def find_kv_idx(self, hashed_idx, key_target):
        for kv_idx in range(len(self.hash_table[hashed_idx])):
            if self.hash_table[hashed_idx][kv_idx][0] == key_target:
                return kv_idx
        return - 1
    
    def add(self, key, value):
        hashed_idx = Dictionary.__hash__(key)
        self.hash_table[hashed_idx].append((key, value))
    
    # def remove(self, key):
    #     hashed_idx = Dictionary.__hash__(key)
    #     kv_idx = self.find_kv_idx(self, hashed_idx, key)
    #     if kv_idx != - 1:
    #         self.hash_table[hashed_idx][kv_idx], self.hash_table[hashed_idx][-1]
            

        

    

    
test_dictionary = Dictionary()
print(test_dictionary.hash_table)
print(test_dictionary.__hash__(10004353453))
test_dictionary.add(1000435345, 1)
print(test_dictionary.hash_table[453])

# Question
# You are given a string of paranthesis, you need to decide if that is a valid set of paranthesis.

def is_valid(paranthesis: str) -> bool:
    pass

# You need to use stack here.
# You need to use python list to solve this problem.

# Examples:
#print(is_valid("()"))
#print(is_valid("()()"))
#
#print(is_valid("(()())"))   # yes
#print(is_valid("(()())()")) # yes
#
#print(is_valid("(()(")) # no
#print(is_valid(")())")) # no

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