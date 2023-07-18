class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # def dp(n):
        #     if n < 2: 
        #         return cost[n] 
        #     return cost[n] + min(dp(n-1), dp(n-2)) 
        # length = len(cost) 
        # return min(dp(length-1), dp(length-2))

        # Non recurssive method

        size = len(cost)
        left = cost[0]
        right = cost[1]
        # current = 0

        if size <= 2:
            return min(left,right)

        for i in range(2,size):
            current = 0
            current += (cost[i] + min(left,right))
            left = right
            right = current
        
        return min(left,right)