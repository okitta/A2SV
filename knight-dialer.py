class Solution:
    def knightDialer(self, n: int) -> int:
        possiblities = [[4,6],[8,6],[7,9],[8,4],[0,3,9],[],[0,7,1],[2,6],[1,3],[2,4]]
        dp = [1 for i in range(10)]
        for i in range(1,n):
            new_dp = [0 for _ in range(10)]
            for j in range(10):
                for possible in possiblities[j]:
                    new_dp[j] += dp[possible]
            dp = new_dp
                # print(dp[i][j])
        
        
        return sum(dp)%1000000007