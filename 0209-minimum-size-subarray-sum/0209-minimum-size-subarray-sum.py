class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size=len(nums)
        left=right=0
        window_sum=nums[0]
        window_size=9999999
        while right<size and left<=right:
            if window_sum >=target:   
                window_size=min(window_size,right-left+1)
                window_sum-=nums[left]
                left+=1
            else:
                right+=1
                if right<size:
                    window_sum +=nums[right]
        if window_size!=9999999:
            return window_size
        return 0