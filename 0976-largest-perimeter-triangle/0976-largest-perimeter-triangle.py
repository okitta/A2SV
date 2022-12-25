class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        list_length = len(nums)
        nums.sort()
        pointer_left = list_length-3
        pointer_right = list_length-1
        while (pointer_left >= 0):
            if nums[pointer_left]+nums[pointer_left+1] > nums[pointer_right]:
                return nums[pointer_left]+nums[pointer_left+1] + nums[pointer_right]
            pointer_left-=1
            pointer_right-=1
        return 0
                            
        
        