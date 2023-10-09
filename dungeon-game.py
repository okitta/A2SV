class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[float("-inf") for i in range(len(dungeon[0]))]for j in range(len(dungeon))]
        dp[len(dungeon)-1][len(dungeon[0])-1] = dungeon[-1][-1]
        for row in range(len(dungeon)-1,-1,-1):
            for col in range(len(dungeon[0])-1,-1,-1):
                if row == len(dungeon)-1 and col == len(dungeon[0])-1:
                    dp[row][col] = min(0,dungeon[-1][-1])
                elif row == len(dungeon)-1:
                    dp[row][col] = min(0,dp[row][col+1]+dungeon[row][col])
                elif col == len(dungeon[0]) -1:
                    dp[row][col] = min(0,dp[row+1][col]+dungeon[row][col])
                else:
                    dp[row][col] = min(0,dungeon[row][col] + max(dp[row+1][col],dp[row][col+1]))
        # print(dp)
        return abs(dp[0][0])+1