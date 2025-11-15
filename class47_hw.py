# Leetcode
# 1. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=array

#  1. Define the minimum and maximum variables such that they are out of the range of any integer in the sample. Also define the difference to be 0.
#  2. Iterate through all numbers and choose a new minimum or maximum number. When a new minimum is chosen, the maximum is reset as it has to be to the right of the minimum.
#  3. If a difference exists, then the value of new difference, a variable created to store the current max-min value is greater than 0. If it greater than the already known difference, then the difference variable is updated.
#  4. Return the difference.

#  Time Complexity: O(N), where N reperesents the size of the list. 

"""
Finds the greatest difference between two integers in a list in which the greater value's index is to the right of the lesser value's index. Returns that difference.
"""
def maxProfit(self, prices: list[int]) -> int:
        min_num = 100001
        max_num = -1
        difference = 0
        for index in range(len(prices)):
            if prices[index] < min_num:
                min_num = prices[index]
                max_num = -1

            if prices[index] > max_num:
                max_num = prices[index]
    
            new_difference = max_num - min_num
            if new_difference > 0 and new_difference > difference:
                difference = new_difference

        return difference
    


# 2. https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=array

#  1. Create a dictionary
#  2. Iterate through every element while iterating if any dictionary index is greater than 1, return True. Else return True.

#  Time Complexity: O(N), where N represents the size of the list. 
def containsDuplicate(self, nums: list[int]) -> bool:
    """
    Returns true if there are any duplicate elements (same integer values) in a list, false otherwise.
    """
    elem_dict = {}
    for num in nums:
        occurences = elem_dict.get(num, 0)
        if occurences > 0:
            return True
        else:
            elem_dict[num] = occurences + 1
            
    return False

# 3. https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=array

#  1. Make a new empty list and save the size of the list in the parameter.
#  2. Start iterating the list in the parameter and removing from the end like a stack. Whenever a non-zero value is encountered, add it to the new list. 
#  3. Once the list given in the parameter is empty, append all the elements in the new list + 0's to match the size of the previous list

#  Time Complexity: O(N), where N represents the length of the list. 
def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, and point to a list where all the 0's are the end. 
        """
        list_size = len(nums)
        non_zero_list = []

        for index in range(list_size) :
            checked_elem = nums.pop()
            if checked_elem != 0:
                non_zero_list.append(checked_elem)
        
        
        index = 0
        while len(nums) != list_size:
            if len(non_zero_list) > 0:
                nums.append(non_zero_list.pop())
            else:
                nums.append(0)
            

                 

           
                      
                
        

# Doubly Linked List
# During the class we have talked about DoublyLinkedList data structure.
# Implement DoublyLinkedList that also has size attribute.
# You implementation must support the following functions:
# - add
# - remove
# - remove_first

# There are some resources to study 2 graph algorithms:
# BFS (Breadth First Search): https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/
# DFS (Depth FIrst Search): https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/
# Please study above material. If something is not clear use Chatgpt to clarify things.
# Important thing is to understand the primary objective of each and their difference in the patterns of how they search.

# Once you understand BFS and DFS, use the following class to create an example binary search tree.
# You goal is then to implement print function. You will implement 2 print funcitons:
# print_BFS
# print_DFS
# Both functions should take root node as a parameter and print all the nodes of the tree in BFS and DFS manner.
class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right