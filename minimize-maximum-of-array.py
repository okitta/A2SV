class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max(ceil(x / i) for i, x in enumerate(accumulate(nums), 1))