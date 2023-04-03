class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        if max_val % min_val == 0:
            return min_val
        idx = 1
        ans = 0
        while idx < min_val and idx < max_val:
            if min_val % idx == 0 and max_val % idx == 0:
                ans = idx
            idx += 1
        return ans