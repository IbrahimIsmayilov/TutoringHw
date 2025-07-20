def longest_prefix(lst: list) -> str:
    if len(lst) == 0:
        return ""
    current_index = 0    
    
    while True:
        for index in range(0, len(lst)):
            if current_index < len(lst[index]):
                if lst[index][current_index] != lst[0][current_index]:
                    return lst[0][:current_index]
            else:
                return lst[0][:current_index]
        current_index += 1
        
        

print(longest_prefix(["flower","flow","flight"]))
print(longest_prefix(["flower","","flight"]))
# Steps
# 1. Go over the first letter and see if that letter is same for each word
# 2. if that is same, continue to the next letter
# 3. when we reach an index such that, letters are not equal for all words, we return up until that index from the first word of the list
# 4. check if the length of the word is greater than current index before incrementing current index

True
# "fl"
class Oaerguiaeg:
    def __init__():
        pass