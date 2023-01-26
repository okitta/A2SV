class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for items in  range(len(nums)):
            nums[items] = str(nums[items])
        for items in range(len(nums)):
            nums.append(nums[items][::-1])
        for items in range(len(nums)):
            nums[items] = int(nums[items])
        return len(set(nums))
