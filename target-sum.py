class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # non recurrsion method
        # n = len(nums)
        # total = sum(nums)
        
        # if (total + target) % 2 != 0: return 0 
        # total = abs(total + target) // 2
        # dp = [0] * (total + 1)
        # dp[0] = 1

        # for i in range(n):
        #     for j in range(total, nums[i] - 1, -1): 
        #         dp[j] = dp[j] + dp[j - nums[i]]
        # # print(dp)
        # return dp[total]

        # recurrsion method
        memory = {}
        
        def dp(i, total):
            if i == len(nums):
                return int(total == target)
            if (i,total) in memory:
                return memory[(i, total)]
            memory[(i, total)] = (dp(i+1, total + nums[i]) + dp(i+1, total-nums[i]))
            return memory[(i, total)]

        return dp(0,0)