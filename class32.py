class Dictionary():
    def __init__(self):
        self.hash_table = [[]] * 10000

    def hash(self, key):
        return  # waiting for constraints regarding types

    def add_kv(self, key, value):
        hashed_idx = self.hash(key)
        self.hash_table[hashed_idx].append((key, value))




random_dict = Dictionary()
print(random_dict.hash_table)

random_dict.add_kv('Joseph', 24)

        
    