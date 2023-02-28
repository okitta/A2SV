class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [0]*len(nums)
        suffix[-1] =nums[-1] 
        ans = []
        for idx in range(1,len(nums)):
            prefix.append(nums[idx]*prefix[-1])
        for idx in range(len(nums)-2,-1,-1):
            suffix[idx] = nums[idx]*suffix[idx+1]
        for idx in range(len(nums)):
            if idx == 0:
                ans.append(suffix[idx+1])
            elif idx == len(nums) -1:
                ans.append(prefix[idx-1])
            else:
                ans.append(prefix[idx-1]*suffix[idx+1])
        return ans
            
        