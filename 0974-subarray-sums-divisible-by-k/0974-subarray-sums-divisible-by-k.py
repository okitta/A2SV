class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefix = {0:1}
        for num in nums:
            curSum += num
            diff = curSum % k
            res += prefix.get(diff,0)
            prefix[diff] = prefix.get(diff,0)+1
        return res
        