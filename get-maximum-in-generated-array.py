class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = defaultdict(int)
        memo[0],memo[1] = 0,1
        def dp(target):
            if 2*target > n or ((2*target)+1) > n:
                return 
            if 2*target not in memo:
                memo[target*2] = memo[target]
                memo[(target*2)+1] = memo[target] + memo[target+1]
            dp(target+1)
            return memo[target]
        val = dp(1)
        return max(memo.values()) if n > 0 else 0