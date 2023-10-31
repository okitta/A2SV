class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # Step 1: Initialize a 2D boolean array dp
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Step 2: Initialization
        dp[0][0] = True
        
        # Initialize the first row based on patterns with '*'
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Step 3: Fill in the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Case 1: We use the wildcard
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j]
                    # Case 2: We don't use the wildcard
                    dp[i][j] = dp[i][j] or dp[i][j - 2]
        
        # Step 4: Final Answer
        return dp[m][n]