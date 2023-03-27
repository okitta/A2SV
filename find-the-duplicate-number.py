class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stack = [0]*max(nums)
        ans = 0
        for num in nums:
            stack[num-1] += 1
        for idx in range(len(stack)):
            if stack[idx] > 1:
                ans = idx + 1
        return ans