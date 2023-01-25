# Sorting using selection sort algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_index=i
            for j in range(min_index+1, len(nums)):
                if nums[j]<nums[min_index]:
                    min_index=j
            if i != min_index:
                nums[i],nums[min_index]=nums[min_index],nums[i]
        