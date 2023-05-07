class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        area = 0

        def check(row,col):
            return True if row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0 else False
        def dfs(r,c):
            if check(r,c) and (r,c) not in visited and grid[r][c]==1:
                visited.add((r,c))
                return (1 + dfs(r+1,c)+
                            dfs(r-1,c)+
                            dfs(r,c+1)+
                            dfs(r,c-1))
            return 0
        for row in range(rows):
            for col in range(cols):
                area = max(area,dfs(row,col))
        return area