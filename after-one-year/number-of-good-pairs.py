class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for idx in range(len(nums)):
            for i in range(idx+1,len(nums)):
                if nums[idx] == nums[i]:
                    count += 1
        return count
        