def helper(self, r, c, grid):
        res = all(1<=grid[i][j]<=9 for i in range(r,r+3) for j in range(c,c+3))
        res &= len({grid[i][j] for i in range(r,r+3) for j in range(c,c+3)})==9
        for i in range(r,r+3):
            res &= sum(grid[i][j] for j in range(c,c+3))==15
        for j in range(c,c+3):
            res &= sum(grid[i][j] for i in range(r,r+3))==15
        res &= sum(grid[i][j] for i,j in zip(range(r,r+3),range(c,c+3)))==15
        res &= sum(grid[i][j] for i,j in zip(range(r,r+3),range(c+2,c-1,-1)))==15
        return res
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return sum(self.helper(r,c,grid) for r in range(m-2) for c in range(n-2))