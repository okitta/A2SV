class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])/k
        tot = sum(nums[:k])
        l = 0
        r = k
        while r < len(nums):
            tot -= nums[l]
            tot += nums[r]
            avg = tot / k
            l += 1
            r += 1
            if avg > ans:
                ans = avg
        return ans
            
        