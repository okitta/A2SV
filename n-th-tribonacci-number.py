class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        
        def helper(val):
            if val == 0 or val == 1:
                memo[val] = val
                return val
            if val == 2:
                memo[val] = 1
                return 1
            if val not in memo:
                memo[val] = helper(val-1) + helper(val - 2)+helper(val-3)
            return memo[val]
        helper(n)
        return memo[n]