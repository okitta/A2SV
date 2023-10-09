class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for j in range(len(s)+1)] for i in range(len(s)+1)]
        reverse = s[::-1]
        # print(dp,reverse)
        for idx in range(len(s)-1,-1,-1):
            for jdx in range(len(s)-1,-1,-1):
                if s[idx] == reverse[jdx]:
                    dp[idx][jdx] = 1 + dp[idx+1][jdx+1]
                else:
                    dp[idx][jdx] = max(dp[idx+1][jdx],dp[idx][jdx+1])
        return dp[0][0]