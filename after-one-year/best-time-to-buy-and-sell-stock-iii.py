class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(prices,idx,can_buy,transaction,dp):
            if idx >= len(prices) or transaction <= 0:
                return 0
            if dp[idx][can_buy][transaction] != -1:
                return dp[idx][can_buy][transaction]
            if can_buy:
                dp[idx][can_buy][transaction] = max(-prices[idx] + helper(prices,idx + 1, not can_buy, transaction , dp),helper(prices,idx+1,can_buy, transaction ,dp))
            else:
                dp[idx][can_buy][transaction] = max(prices[idx] + helper(prices,idx + 1, not can_buy, transaction-1 , dp),helper(prices,idx+1,can_buy, transaction ,dp))
            
            return dp[idx][can_buy][transaction]
        dp = [[[ -1 for _ in range(3)] for _ in range(3)] for _ in range(len(prices)+1)]

        return helper(prices,0,True,2,dp)