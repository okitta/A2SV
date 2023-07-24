class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = math.inf
        if n<=4:
            return 0
        nums.sort()
        for i in range(4):
            for j in range(1,4-i+1):
                ans = min(ans,abs(nums[i]-nums[n-j]))
        return ans