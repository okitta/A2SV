class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo ={}

        def dp(row,col):
            if row == m-1 and col == n - 1:
                return 1
            row_ret,col_ret = 0,0
            if (row,col) in memo:
                return memo[(row,col)]
            if row < m-1:
                row_ret = dp(row+1,col)
            if col < n-1:
                col_ret = dp(row,col+1)
            memo[(row,col)] = col_ret + row_ret
            return memo[(row,col)]
        val = dp(0,0)
        return val