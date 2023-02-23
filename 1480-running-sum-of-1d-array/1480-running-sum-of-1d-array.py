class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        for index in range(len(nums)):
            if not prefix:
                prefix.append(nums[index])
            else:
                prefix.append(prefix[-1]+nums[index])
        return prefix