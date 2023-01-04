from collections import Counter 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counted_dict = Counter(nums) #counting elements in the given list
        values = counted_dict.values() # taking the values of the counter dictionary
        good_pairs = 0 #assigning the minimum good pair that can exist is 0
        
        for item in values:
            good_pairs+= (item*(item-1)//2)
        
        return good_pairs
            