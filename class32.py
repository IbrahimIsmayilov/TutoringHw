# TODO Git
# TODO Hash table design

a = {}

# Things we can do with python dicitonayr
# 1. We can provide key to get the value.
# 2. We can remove key value pairs.
# 3. We can update the value of the key.
# 4. We can add key-value pair.

# We need to develop our own dictionary without using python dictionary data type. Do it.

# Maybe we should make a class dictionary.
# 0 for keys 1 for values: 
z = {}

#my_dict = dicitionary()
#my2 = dicitionary()
# list, tuple, int, float, bool, str, None

# keys must be unique!!!
# Constant: 1
# logarithmic: log(n)
# Linear: n
# polynomial: quadratic (n**2), cubid (n**3)
class dicitionary:
    def __init__(self):
        """ elements attribut contains key-value pairs as tuples """
        self.elements = []

    # Linear (O(n))
    def add(self, key, value):
        """ all keys will be unique """
        # 1. Go through the list and make sure the key does not exist
        # 2. Use get_value function.
            # How do we check if the function raises an error!
        try:
            self.get_value(key)
            # Maybe we want to update the value
            print("Key already exists")
        except KeyError:
            self.elements.append((key, value))
    
    # O(n)
    def get_value(self, key):
        if self._get_kv_idx(key) != -1:
            return self.elements[self._get_kv_idx(key)][1]
        raise KeyError

    # What is the time complexity? 
    # O(n), where n is len(self.elements)
    def _get_kv_idx(self, key):
        """ Returns the key-val pair's idx if it exists, otherwise returns -1 """
        for idx in range(len(self.elements)):
            if self.elements[idx][0] == key:
                return idx
        return -1
    
    # O(n)
    # 3 * n
    # n, 7n
    def remove(self, key):
        # 1. Use _get_pair to check if the key exists
        # 2. If the key exists, we want to remove key-value pair (tuple) from the list.
        idx = self._get_kv_idx(key)
        if  idx != -1:
            self.elements[-1], self.elements[idx] =  self.elements[idx], self.elements[-1]
            self.elements.pop()
        else:
            raise KeyError
    
    # Linear time: O(n)
    def update(self, key, new_value):
        # If the pair does not exist, nothing to update.
        # steps
        # 1. check if key value exists in our dictionary
        # 2. if the pair exists, then change the first index of the tuple
        idx = self._get_kv_idx(key)
        if  idx != -1:
            self.elements[idx] = (key, new_value)
        else:
            raise KeyError
        
# Python dictionaries, use hash tables which makes their time complexities constant.
# You cannot update the tuple

lst = [10, 20, 30]
lst = [10, 20, 30]
#
lst.remove(10)


my_dictionary = dicitionary()
my_dictionary.add(38, "Osman")
my_dictionary.add(38, "Murad")
print(my_dictionary.elements)
my_dictionary.update(38, "Ibrahim")
my_dictionary.add(40, "Leyla")
print(my_dictionary.elements)
print(my_dictionary.get_value(38))
print(my_dictionary.get_value(46))

# What attributes will the dictionary have?
# key-values

# First agree on what you want to do with the class (methods) then decide for those methods what attributes u will need.

# What should we put inside the dicitionary?
    # your keys can only be integers but you values can be anything.

# 1. First agree on what you want to do with the class (methods) then decide for those methods what attributes u will need.
# 2. As you implement each method, make sure to test it.

# TODO Command line
# TODO Computer architecture