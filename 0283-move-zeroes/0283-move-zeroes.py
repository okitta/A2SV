class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in nums:
            if x == 0:
                nums.remove(0)
                nums.append(0)
        
        return nums
            
                
                
        
        