class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = len(nums)+1

        for idx in range(len(nums)):
            if int(nums[idx])>0 and int(nums[idx])<len(nums)+1:
                nums[int(nums[idx])-1]=str(nums[int(nums[idx])-1])
            elif isinstance(nums[idx],int):
                nums[idx]=idx+1



        for idx in range(len(nums)):
            if isinstance(nums[idx],int):
                ans = idx+1
                break
        return ans